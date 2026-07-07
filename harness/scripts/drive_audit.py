#!/usr/bin/env python3
"""
drive_audit.py — ROC-OS PRUNE_QUEUE audit harness (Drive-only scope).

Rebuilt 2026-07-03 (Thread 2, Resolution C). Supersedes the 2026-07-01 version:
  - REMOVED: LOCAL_LEGACY_PATHS, local file walk, scan-queue handling, --scan-only.
  - Legacy-tree scanning (PQ-003 class entries: disposition=null / legacy_risk=yes)
    is OUT OF SCOPE — owned by the dual-location cleanup session (Thread 5).

Master of record: Drive /ROC-OS/00_Registry/PRUNE_QUEUE.md
Execution surface: Claude Code (this script). Chat/Cowork never in-place edit
Drive masters; this harness is the sanctioned writer.

Disposition behavior (enum is canonical in the PRUNE_QUEUE.md header):
  archive → move file to /ROC-OS/00_Registry/archive/, rename with
            _ARCHIVED_{date} suffix, audit_status → completed
  trash   → NEVER auto-trash. Flag for human confirmation (audit_status →
            flagged). Execute later with --confirm-trash PQ-NNN.
  review  → report only, no action.
  null    → skipped (out of scope — Thread 5).

Safety: dry-run is the DEFAULT. Nothing touches Drive without --execute.

Setup (Thread 3 — Google Cloud Console):
  1. Enable Drive API, create OAuth 2.0 Client ID (Desktop app).
  2. Place credentials.json next to this script. token.json is created on
     first auth.
  3. .gitignore MUST include: credentials.json, token.json
  4. pip install google-api-python-client google-auth-oauthlib

Usage:
  python drive_audit.py                          # dry-run report (default)
  python drive_audit.py --execute                # perform archive moves, flag trash
  python drive_audit.py --execute --confirm-trash PQ-016   # trash a flagged entry
"""

import argparse
import re
import sys
from datetime import date, datetime

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaInMemoryUpload
except ImportError:
    sys.exit("Missing deps: pip install google-api-python-client google-auth-oauthlib")

# ── Config (canonical Drive IDs) ─────────────────────────────────────────────
PRUNE_QUEUE_FILE_ID = "1hlt-RlbihpfonnNHepPgCAFaj0T1etXx"   # /ROC-OS/00_Registry/PRUNE_QUEUE.md
ARCHIVE_FOLDER_ID   = "1X-uEOiIfeCgolDjDFP0WFffINuGxva1B"   # /ROC-OS/00_Registry/archive/
SCOPES = ["https://www.googleapis.com/auth/drive"]
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"

ENTRY_RE = re.compile(r"^\[PQ-(\d{3})\]\s*$")
FIELD_RE = re.compile(r"^([a-z_]+):\s*(.*)$")


# ── Auth ─────────────────────────────────────────────────────────────────────
def get_service():
    creds = None
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    except FileNotFoundError:
        pass
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return build("drive", "v3", credentials=creds)


# ── Queue parse / serialize ──────────────────────────────────────────────────
def fetch_queue(service):
    return service.files().get_media(fileId=PRUNE_QUEUE_FILE_ID).execute().decode("utf-8")


def parse_entries(text):
    """Return list of dicts: {id, fields (ordered), line_start, line_end}."""
    lines = text.split("\n")
    entries, current = [], None
    for i, line in enumerate(lines):
        m = ENTRY_RE.match(line.strip())
        if m:
            if current:
                current["line_end"] = i - 1
                entries.append(current)
            current = {"id": f"PQ-{m.group(1)}", "fields": {}, "line_start": i}
            continue
        if current is not None:
            fm = FIELD_RE.match(line.strip())
            if fm:
                current["fields"][fm.group(1)] = fm.group(2).strip()
            elif line.strip().startswith("# ───") and current["fields"]:
                current["line_end"] = i - 1
                entries.append(current)
                current = None
    if current:
        current["line_end"] = len(lines) - 1
        entries.append(current)
    return entries


def set_field(text, entry, key, value):
    """Rewrite one field line within an entry's block. Returns new text."""
    lines = text.split("\n")
    for i in range(entry["line_start"], entry["line_end"] + 1):
        fm = FIELD_RE.match(lines[i].strip())
        if fm and fm.group(1) == key:
            lines[i] = f"{key}: {value}"
            return "\n".join(lines)
    # field absent → append at end of block
    lines.insert(entry["line_end"] + 1, f"{key}: {value}")
    return "\n".join(lines)


def update_header(text, pending_count):
    text = re.sub(r"^# Last audit run: .*$",
                  f"# Last audit run: {date.today().isoformat()}",
                  text, count=1, flags=re.M)
    text = re.sub(r"^# Pending entries: .*$",
                  f"# Pending entries: {pending_count}",
                  text, count=1, flags=re.M)
    return text


def append_run_log(text, stats, notes):
    block = (
        f"\nrun_date: {date.today().isoformat()}\n"
        f"surface: Claude Code\n"
        f"entries_processed: {stats['processed']}\n"
        f"entries_archived: {stats['archived']}\n"
        f"entries_trashed: {stats['trashed']}\n"
        f"entries_flagged: {stats['flagged']}\n"
        f"entries_skipped: {stats['skipped']}\n"
        f"run_notes: {notes}\n"
    )
    return text.rstrip() + "\n" + block


# ── Drive actions ────────────────────────────────────────────────────────────
def archive_file(service, file_id):
    meta = service.files().get(fileId=file_id, fields="name, parents").execute()
    stem, dot, ext = meta["name"].rpartition(".")
    new_name = (f"{stem}_ARCHIVED_{date.today().isoformat()}.{ext}"
                if dot else f"{meta['name']}_ARCHIVED_{date.today().isoformat()}")
    service.files().update(
        fileId=file_id,
        addParents=ARCHIVE_FOLDER_ID,
        removeParents=",".join(meta.get("parents", [])),
        body={"name": new_name},
    ).execute()
    return new_name


def trash_file(service, file_id):
    service.files().update(fileId=file_id, body={"trashed": True}).execute()


def write_back(service, text):
    media = MediaInMemoryUpload(text.encode("utf-8"), mimetype="text/markdown")
    service.files().update(fileId=PRUNE_QUEUE_FILE_ID, media_body=media).execute()


# ── Routing ──────────────────────────────────────────────────────────────────
def route_entries(service, text, entries, execute, confirm_trash):
    stats = dict(processed=0, archived=0, trashed=0, flagged=0, skipped=0)
    report = []
    for e in entries:
        f = e["fields"]
        pq, disp = e["id"], f.get("disposition", "").lower()
        status = f.get("audit_status", "").lower()
        if status == "completed":
            continue
        stats["processed"] += 1

        # Resolution C: legacy scans are Thread 5's job
        if disp == "null" or f.get("legacy_risk", "").lower() == "yes":
            stats["skipped"] += 1
            report.append(f"  {pq}  SKIPPED — legacy/null scope, owned by Thread 5 cleanup session")
            if execute and status != "skipped":
                text = set_field(text, parse_one(text, pq), "audit_status", "skipped")
            continue

        fid = f.get("superseded_id", "null")
        if disp == "archive":
            if execute:
                new_name = archive_file(service, fid)
                text = set_field(text, parse_one(text, pq), "audit_status",
                                 f"completed ({date.today().isoformat()})")
                report.append(f"  {pq}  ARCHIVED → archive/{new_name}")
            else:
                report.append(f"  {pq}  would ARCHIVE {f.get('superseded_file')} (id {fid})")
            stats["archived"] += 1
        elif disp == "trash":
            if execute and pq in confirm_trash:
                trash_file(service, fid)
                text = set_field(text, parse_one(text, pq), "audit_status",
                                 f"completed ({date.today().isoformat()})")
                report.append(f"  {pq}  TRASHED (human-confirmed) — recoverable 30 days")
                stats["trashed"] += 1
            else:
                if execute:
                    text = set_field(text, parse_one(text, pq), "audit_status", "flagged")
                report.append(f"  {pq}  FLAGGED for trash — confirm with --confirm-trash {pq}")
                stats["flagged"] += 1
        elif disp == "review":
            report.append(f"  {pq}  REVIEW required — {f.get('notes', '(no notes)')[:80]}")
            stats["flagged"] += 1
            if execute and status != "flagged":
                text = set_field(text, parse_one(text, pq), "audit_status", "flagged")
        else:
            stats["skipped"] += 1
            report.append(f"  {pq}  SKIPPED — unknown disposition '{disp}'")
    return text, stats, report


def parse_one(text, pq_id):
    for e in parse_entries(text):
        if e["id"] == pq_id:
            return e
    raise KeyError(pq_id)


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description="ROC-OS PRUNE_QUEUE audit (Drive-only)")
    ap.add_argument("--execute", action="store_true",
                    help="perform actions (default: dry-run report only)")
    ap.add_argument("--confirm-trash", nargs="*", default=[], metavar="PQ-NNN",
                    help="entry IDs whose trash disposition is human-confirmed")
    args = ap.parse_args()

    service = get_service()
    text = fetch_queue(service)
    entries = parse_entries(text)
    mode = "EXECUTE" if args.execute else "DRY-RUN"
    print(f"drive_audit.py — {mode} — {datetime.now().isoformat(timespec='seconds')}")
    print(f"Queue entries found: {len(entries)}\n")

    text, stats, report = route_entries(service, text, entries,
                                        args.execute, set(args.confirm_trash))
    print("\n".join(report) if report else "  (nothing to process)")
    print(f"\nprocessed={stats['processed']} archived={stats['archived']} "
          f"trashed={stats['trashed']} flagged={stats['flagged']} skipped={stats['skipped']}")

    if args.execute:
        pending = sum(1 for e in parse_entries(text)
                      if e["fields"].get("audit_status", "").startswith("pending"))
        text = update_header(text, pending)
        text = append_run_log(text, stats, f"{mode} run via drive_audit.py (Resolution C build)")
        write_back(service, text)
        print("\nPRUNE_QUEUE.md updated on Drive (header, statuses, run log).")
    else:
        print("\nDry-run: no Drive writes. Re-run with --execute to act.")


if __name__ == "__main__":
    main()
