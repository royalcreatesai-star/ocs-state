# DOC_HANDOFF_DRIVE-MIRROR_TEMPLATE_V1.md — Repo → Drive Mirror (procedure + log)

**Route (logical):** /ROC-OS/00_Registry/ — physically in git repo SoT `~/Documents/ME/Ai/ocs-state`.
**Created:** 2026-06-28 by Royal O'Connor + Claude (Opus 4.8, Claude Code).
**Purpose:** reusable procedure + execution log for keeping the Google Drive mirror in sync with the git repo (SoT). Preserves each mirror as an audit-trail artifact. Supersedes the ad-hoc CoWork starter-prompt regenerated per session.

**Rule:** git repo is the source of truth. **Direction is always repo → Drive.** Drive is the mirror — never the other way. Edit `.md` as **text**; never open the mirror in Google Docs (spawns duplicates — F13).

---

## Method A — DIRECT (default, from the Claude Code harness) — *enabled 2026-06-28*
The Google Drive mount is local and whitelisted in the path-guard (canonical §11). The harness `cp`s repo files into the mounted Drive folder; Drive-for-Desktop uploads to cloud. A local `cp` is byte-faithful, so this is clean for **text and binary** (sidesteps the connector's F14ext corruption).

**Paths:**
- Repo: `~/Documents/ME/Ai/ocs-state/`
- Drive mount: `~/Library/CloudStorage/GoogleDrive-royalcreates.ai@gmail.com/My Drive/ROC-OS/`

**Destination map:**
| Repo file (by category) | Drive subfolder |
|---|---|
| `OCS_STATE_CANONICAL.md`, `DOC_HANDOFF_*`, registry docs | `00_Registry/` |
| `..._AI_INTELLIGENCE_*`, GPT registry | `01_Intelligence/` |
| `..._AI_PROJECTS_*`, session logs, Gate docs | `05_Projects/` |

**Steps:**
1. Confirm repo is committed + pushed (`git status` clean).
2. `cp` each changed file to its mapped Drive subfolder.
3. **Verify (verify-before-status):** `diff` repo file vs Drive-mount file — must be byte-identical. Only then log it done.
4. Note: the `diff` proves the *local mount* copy. Cloud upload is Drive-for-Desktop's async job (usually seconds); confirm in the web UI if a downstream reader needs it immediately.

## Method B — FALLBACK (CoWork connector)
Use when the Drive mount is unavailable (e.g. Drive-for-Desktop not running) or from a runtime without the mount. CoWork's Drive connector writes the mirror. Limitations: connector corrupts binary Office downloads (F14ext) — text `.md` only; can't reliably delete/rename. Verify the Drive copy reads the expected version before marking done.

---

## EXECUTION LOG
| Date | Repo HEAD | Version | Files mirrored | Method | Verified |
|---|---|---|---|---|---|
| 2026-06-28 | (this commit) | V7.4 | OCS_STATE_CANONICAL + 3 Gate 5 docs + GATE5-CLOSE-SESSION + this template | A (direct) | ✅ diff byte-identical |

---
*DOC_HANDOFF_DRIVE-MIRROR_TEMPLATE_V1.md | OCS | repo→Drive mirror procedure + log | 2026-06-28 | /ROC-OS/00_Registry/*
