#!/usr/bin/env python3
"""
Unit tests for drive_audit.py (Thread 2, Resolution C).

Covers the PQ-001 (archive) / PQ-002 (review) / PQ-003 (null+legacy_risk,
skip → Thread 5) routing scenarios referenced in OCS_STATE_CANONICAL.md,
plus a structural check that the Drive-only scope patch stayed applied
(no LOCAL_LEGACY_PATHS, no local file-walk, no --scan-only).

route_entries() only touches the `service` argument when execute=True and
the disposition is archive/trash, so a dry-run (execute=False) can pass
service=None without mocking the Google API.

Auth coverage (added 2026-07-28) exercises load_credentials() with the
Google objects mocked out — no network, no browser, no real token.json.
"""

import pathlib
import tempfile
import unittest
from unittest import mock

from google.auth.exceptions import RefreshError, TransportError

import drive_audit

SAMPLE_QUEUE = """# Last audit run: never
# Pending entries: 3

[PQ-001]
disposition: archive
audit_status: pending
superseded_file: old_notes.md
superseded_id: fileid001
path: /ROC-OS/00_Registry/old_notes.md
logged: 2026-06-01

[PQ-002]
disposition: review
audit_status: pending
superseded_file: ambiguous.md
notes: needs human judgment

[PQ-003]
disposition: null
legacy_risk: yes
legacy_path: /ME/Ai/legacy_tree/
notes: dual-location cleanup candidate, owned by Thread 5
"""


class ParseEntriesTests(unittest.TestCase):
    def test_parses_three_entries(self):
        entries = drive_audit.parse_entries(SAMPLE_QUEUE)
        self.assertEqual([e["id"] for e in entries], ["PQ-001", "PQ-002", "PQ-003"])

    def test_fields_captured(self):
        entries = drive_audit.parse_entries(SAMPLE_QUEUE)
        pq1 = entries[0]["fields"]
        self.assertEqual(pq1["disposition"], "archive")
        self.assertEqual(pq1["superseded_id"], "fileid001")


class RouteEntriesDryRunTests(unittest.TestCase):
    def setUp(self):
        self.entries = drive_audit.parse_entries(SAMPLE_QUEUE)

    def test_pq001_archive_dry_run(self):
        _, stats, report = drive_audit.route_entries(
            None, SAMPLE_QUEUE, self.entries, execute=False, confirm_trash=set()
        )
        self.assertEqual(stats["archived"], 1)
        self.assertTrue(any("PQ-001" in line and "would ARCHIVE" in line for line in report))

    def test_pq002_review_dry_run(self):
        _, stats, report = drive_audit.route_entries(
            None, SAMPLE_QUEUE, self.entries, execute=False, confirm_trash=set()
        )
        self.assertEqual(stats["flagged"], 1)
        self.assertTrue(any("PQ-002" in line and "REVIEW required" in line for line in report))

    def test_pq003_null_legacy_risk_skipped_to_thread5(self):
        _, stats, report = drive_audit.route_entries(
            None, SAMPLE_QUEUE, self.entries, execute=False, confirm_trash=set()
        )
        self.assertEqual(stats["skipped"], 1)
        self.assertTrue(
            any("PQ-003" in line and "Thread 5" in line for line in report)
        )

    def test_full_stats_tuple(self):
        _, stats, _ = drive_audit.route_entries(
            None, SAMPLE_QUEUE, self.entries, execute=False, confirm_trash=set()
        )
        self.assertEqual(
            stats,
            {"processed": 3, "archived": 1, "trashed": 0, "flagged": 1, "skipped": 1},
        )


class CredentialRefreshTests(unittest.TestCase):
    """Regression cover for the 2026-07-28 incident.

    The OAuth consent screen is in "Testing" publishing status, whose refresh
    tokens die after 7 days. The token minted 2026-07-06 was already revoked,
    so creds.refresh() raised RefreshError(invalid_grant) and the script died
    with an unhandled traceback instead of re-authenticating. A failed refresh
    must fall through to the InstalledAppFlow browser path.
    """

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.token_path = pathlib.Path(tmp.name) / "token.json"
        patcher = mock.patch.object(drive_audit, "TOKEN_FILE", str(self.token_path))
        patcher.start()
        self.addCleanup(patcher.stop)

    @staticmethod
    def _stub_creds(*, valid, expired=False, refresh_token=None, refresh_raises=None):
        creds = mock.Mock()
        creds.valid = valid
        creds.expired = expired
        creds.refresh_token = refresh_token
        creds.to_json.return_value = '{"stub": "written"}'
        if refresh_raises is not None:
            creds.refresh.side_effect = refresh_raises
        return creds

    def _run(self, stored, *, fresh=None):
        """Call load_credentials() with Credentials/Request/InstalledAppFlow mocked.

        `stored` is what token.json deserializes to (or an exception to raise);
        `fresh` is what the browser flow hands back. Returns (creds, flow_cls).
        """
        fresh = fresh or self._stub_creds(valid=True)
        loader = mock.patch.object(
            drive_audit.Credentials, "from_authorized_user_file",
            side_effect=stored if isinstance(stored, Exception) else None,
            return_value=None if isinstance(stored, Exception) else stored,
        )
        with loader, \
                mock.patch.object(drive_audit, "InstalledAppFlow") as flow_cls, \
                mock.patch.object(drive_audit, "Request"):
            flow_cls.from_client_secrets_file.return_value.run_local_server.return_value = fresh
            creds = drive_audit.load_credentials()
        return creds, flow_cls

    def test_revoked_refresh_token_falls_back_to_browser_flow(self):
        stale = self._stub_creds(valid=False, expired=True, refresh_token="revoked",
                                 refresh_raises=RefreshError("invalid_grant"))
        fresh = self._stub_creds(valid=True)
        creds, flow_cls = self._run(stale, fresh=fresh)

        stale.refresh.assert_called_once()          # it did try the cheap path first
        self.assertIs(creds, fresh)                 # ...then re-authed instead of raising
        flow_cls.from_client_secrets_file.assert_called_once_with(
            drive_audit.CREDENTIALS_FILE, drive_audit.SCOPES
        )
        self.assertEqual(self.token_path.read_text(), '{"stub": "written"}')

    def test_transport_error_on_refresh_also_falls_back(self):
        stale = self._stub_creds(valid=False, expired=True, refresh_token="whatever",
                                 refresh_raises=TransportError("connection reset"))
        creds, flow_cls = self._run(stale)
        self.assertIsNot(creds, stale)
        flow_cls.from_client_secrets_file.assert_called_once()

    def test_successful_refresh_skips_browser_flow(self):
        stale = self._stub_creds(valid=False, expired=True, refresh_token="still-good")
        creds, flow_cls = self._run(stale)

        stale.refresh.assert_called_once()
        flow_cls.from_client_secrets_file.assert_not_called()
        self.assertIs(creds, stale)
        self.assertEqual(self.token_path.read_text(), '{"stub": "written"}')

    def test_missing_token_file_runs_browser_flow(self):
        fresh = self._stub_creds(valid=True)
        creds, flow_cls = self._run(FileNotFoundError(drive_audit.TOKEN_FILE), fresh=fresh)
        self.assertIs(creds, fresh)
        flow_cls.from_client_secrets_file.assert_called_once()

    def test_valid_token_touches_neither_refresh_nor_flow(self):
        good = self._stub_creds(valid=True)
        creds, flow_cls = self._run(good)

        good.refresh.assert_not_called()
        flow_cls.from_client_secrets_file.assert_not_called()
        self.assertIs(creds, good)
        self.assertFalse(self.token_path.exists())  # nothing changed → nothing rewritten


class DriveOnlyScopeStructuralTests(unittest.TestCase):
    """Confirms the Resolution C patch (Drive-only scope) is actually in the file on disk."""

    def setUp(self):
        self.src = pathlib.Path(drive_audit.__file__).read_text()

    def test_no_local_legacy_paths_constant(self):
        # Changelog note in the docstring is allowed to mention the removed
        # name; only an actual assignment/usage would mean the patch regressed.
        self.assertNotIn("LOCAL_LEGACY_PATHS =", self.src)
        self.assertNotIn("LOCAL_LEGACY_PATHS=", self.src)

    def test_no_scan_only_flag(self):
        # Docstring/comments may reference "--scan-only" historically; the
        # patch regressed only if argparse actually wires the flag back up.
        self.assertNotIn('add_argument("--scan-only"', self.src)
        self.assertNotIn("args.scan_only", self.src)

    def test_no_local_file_walk(self):
        self.assertNotIn("os.walk", self.src)

    def test_no_scan_queue_in_route_entries(self):
        self.assertNotIn('queues["scan"]', self.src)
        self.assertNotIn("execute_scan", self.src)

    def test_refresh_call_is_exception_guarded(self):
        # The 2026-07-28 crash was a bare creds.refresh(Request()). Keep it wrapped.
        block = self.src.split("def load_credentials")[1].split("\ndef ")[0]
        self.assertIn("creds.refresh(", block)
        self.assertIn("except", block)

    def test_dry_run_is_default(self):
        # --execute must be an opt-in store_true flag, not default-on.
        self.assertIn('"--execute", action="store_true"', self.src)


if __name__ == "__main__":
    unittest.main()
