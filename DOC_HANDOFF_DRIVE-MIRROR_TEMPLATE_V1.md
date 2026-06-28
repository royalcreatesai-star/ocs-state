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

## CANDIDATE HAND-OFFS / CROSS-RUNTIME METHODS TO EVALUATE (added 06-28)
A future pass should inventory recurring cross-runtime work and decide which to templatize (like this Drive mirror) vs leave as one-offs. Known candidates + where each currently lives:
| Candidate | Recurs? | Currently recorded | Action to weigh |
|---|---|---|---|
| Repo→Drive mirror | every canonical change | **this doc (DONE)** | ✅ templatized |
| Stray-file / dup cleanup in Drive | occasional | canonical §12 (F12/F13) | templatize the "find dups + remove" CoWork step? |
| Advisory Drive access (oconnoradvisory.ai) | when touching client funnel | memory `project_ocs_runtime_access_map` | stand up dedicated `/mcp` connector vs share-to-royalcreates workaround |
| Google Form read via connector (export zip→html+csv) | each Risk Scan check | memory `project_ocs_runtime_access_map` | promote method-note → reusable procedure |
| Binary Office edit (native app, not connector) | each .docx/.xlsx deliverable | canonical §8 F14ext | re-test now that direct-mount `cp` may make this byte-faithful |

*Note: some of these are "methods" buried in memory rather than discoverable procedures — the value of the pass is surfacing them into one place a cold session can find.*

---
*DOC_HANDOFF_DRIVE-MIRROR_TEMPLATE_V1.md | OCS | repo→Drive mirror procedure + log + hand-off candidates | 2026-06-28 | /ROC-OS/00_Registry/*
