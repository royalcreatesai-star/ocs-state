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
"""

import pathlib
import unittest

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

    def test_dry_run_is_default(self):
        # --execute must be an opt-in store_true flag, not default-on.
        self.assertIn('"--execute", action="store_true"', self.src)


if __name__ == "__main__":
    unittest.main()
