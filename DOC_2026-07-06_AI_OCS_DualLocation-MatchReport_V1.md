# DOC_2026-07-06_AI_OCS — Dual-Location Match Report (Thread 5)

**Filed:** 2026-07-06 | **Session:** Thread 5 — Dual-Location Cleanup (Code harness) | **Route:** /ROC-OS/00_Registry/
**Deliverable for:** PQ-003 (legacy `/ME/Ai/` tree scan). **Status: report + Royal-approved cleanup executed 2026-07-06.**

**ACTIONS TAKEN 2026-07-06 (all Royal-approved; fully reversible / non-destructive):**
1. **Backup:** the 19 Schwab investing-theme files (§D substantive gap) **copied** to Drive `/05_Projects/PROJ_AI_AUTOTRADING/` — all verified byte-identical; iCloud originals untouched.
2. **Junk quarantined:** stale `lu41p4cs0.tmp` + `.~lock.Steuben...#` **moved** to `/ME/Ai/_LEGACY_ARCHIVE_2026-07-06/` (LibreOffice confirmed not running). Not hard-deleted.
3. **Reference/source dupes pruned:** the **190** non-`PROJ_*` exact-duplicates — **each content-hash verified byte-identical to a Drive twin (0 surprises)** — **moved** to `/ME/Ai/_LEGACY_ARCHIVE_2026-07-06/` (preserving structure) + 55 emptied dirs removed. Reversible: nothing deleted; the content also lives in Drive canonical. The 54 `PROJ_*` duplicates were KEPT (iCloud is their canonical home).
4. **WORKPAPER.xlsx reconciled:** both 9-sheet; Drive copy (56 KB, saved 14:11) is newer + fuller than iCloud (24 KB, 13:31) → **Drive is authoritative**; the iCloud copy is a stale earlier save (a `PROJ_*` deliverable — left for Royal to overwrite-from-Drive or prune).

Remaining (report-only, Royal's call): preserve SOC `.docx` + `OConnorServiceMenu.html` native formats; back up 3 OCS artifacts (`DailyDigest.tsx`, `CoworkStarterPrompt`, `InitiativeMap`); triage the loose iCloud-only files (`Ai Implementation.m4a`, `IMG_8182.jpeg`, `text.txt`, `unknown.png`); empty the `.DS_Store`-only folders left after the prune. **Recovery: to undo any prune, move files back from `_LEGACY_ARCHIVE_2026-07-06/`.**
**Method:** Read-only cross-reference of the legacy iCloud tree against the canonical Drive tree, by filename + byte-size. Scan script: `scratchpad/thread5_scan.py` (this session).

- **Legacy tree:** `/Users/iglobalian/Library/Mobile Documents/com~apple~CloudDocs/ME/Ai/`
- **Canonical tree:** `/Users/iglobalian/Library/CloudStorage/GoogleDrive-royalcreates.ai@gmail.com/My Drive/ROC-OS/`
- **Scope (Royal's 07-06 call — "strays + duplicates only"):** EXCLUDED the canonical-in-iCloud trees: `blueprint/`, `memory/`, `n8n-docker/` (locked decision #7 — never syncs to Drive), `wallyb/`, `CLAUDE.md`, `TASKS.md`, `.git/`.

---

## 1. Executive Summary

Scanned **270 in-scope** iCloud files against **435** Drive `/ROC-OS/` files:

| Category | Count | Meaning |
|---|---:|---|
| **A. Exact duplicate** (same name + byte-size in Drive) | 226 | iCloud copy is byte-identical to a Drive copy |
| **B. Name match, different size** | 5 | Same filename, different content — variant or stale |
| **C. Junk / temp / lock** | 4 | Editor temp + lock + loose files |
| **D. iCloud-only** (no Drive match) | 35 | Present in iCloud, **not** in Drive |

**The dual-location problem has TWO sides — this is the key finding:**
1. **Redundancy (226):** ~84% of the in-scope legacy tree is byte-identical to Drive. BUT "duplicate" ≠ "delete from iCloud" — disposition depends on which side is *canonical* (see §2).
2. **Unbacked-up unique assets (35):** iCloud holds real assets **missing from the Drive canonical**, including the **Steuben property workbook** (Engine 3), **20 Schwab investing-theme PDFs** (Engine 5 research), and **two SOC memos** (Engine 2). These are a backup-gap risk — they need **migration to Drive, not deletion**.

---

## 2. Canonical-ownership lens (why "duplicate" ≠ "prune iCloud")

Per the File-Sync Protocol (decisions.md, 2026-06-21), canonical home differs by artifact type:

| Artifact type | Canonical home | Prune direction if duplicated |
|---|---|---|
| OCS state docs | git repo → Drive mirror | (out of scope here) |
| Blueprint living files | iCloud | (excluded from scan) |
| **Project deliverables (`PROJ_*`)** | **iCloud** (Drive = mirror) | A byte-identical Drive copy = *healthy mirror*. **Do NOT delete the iCloud copy.** |
| Reference/source material, OCS artifacts | Drive `/ROC-OS/` | iCloud copy is the stray → prune-from-iCloud candidate |

So the 226 exact-duplicates split into two dispositions (§3.A).

---

## 3. Findings by category

### A. Exact duplicates (226) — by top-level group

| Group | # | Canonical owner | Recommended disposition |
|---|---:|---|---|
| `DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/` | 146 | Reference (a cloned plugin repo; also installed at `~/.claude`) | **Prune from iCloud** — pure downloaded source, fully in Drive; not a working file |
| `WF_AI_N8N_TEMPLATES/` | 16 | Reference | Prune from iCloud (mirrored in Drive) |
| `PROJ_AI_CASHFLOWMASTER/` | 14 | **iCloud (deliverable)** | KEEP iCloud — Drive dupe = healthy mirror |
| `PROJ_AI_BAYSTREET/` | 10 | **iCloud (deliverable)** | KEEP iCloud — healthy mirror |
| `DOC_AI_TOOLS_AND_GUIDES/` | 7 | Reference | Prune from iCloud |
| `DOC_AI_EDUCATION/` | 7 | Reference | Prune from iCloud |
| `PROJ_AI_FAMILYSPORTS/` | 4 | **iCloud (deliverable)** | KEEP iCloud |
| `PROJ_ADVISORY_MIGRATION-SPRINT/` | 4 | **iCloud (deliverable)** | KEEP iCloud |
| `PROJ_AI_REI/` | 3 | **iCloud (deliverable)** | KEEP iCloud |
| `IMG_AI_SCREENSHOTS/`, `DOC_AI_NAMING_BUNDLE/`, `Ai Bootcamp/`, `DOC_AI_BIZ_ADMIN/`, `MD Files/`, loose root `DOC_*.html`, `dashboard.html`, `project_state_*.md`, `SOC 1 Review - Clean.numbers`, `PROJ_AI_AUTOTRADING/` (1) | 15 | Mixed | Review per-item (§ appendix) — mostly reference → prune-from-iCloud |

**Net:** ~190 of the 226 are reference/source/OCS-artifact duplicates that are candidates to remove from the iCloud legacy tree; ~36 are `PROJ_*` deliverables where **iCloud is canonical** and the Drive dupe simply confirms a working mirror (keep both).

⚠️ Caveat: byte-size match is strong but not proof of identical content. Before any bulk removal, spot-check a sample with a checksum (`shasum`) — cheap insurance.

### B. Name match, different size (5) — REVIEW each

| iCloud file | iCloud size | Drive size | Read |
|---|---:|---:|---|
| `DOC_2026-06-28_AI_OCS_CLAUDE-MD_V2.md` | 14100 | 14099 | 1-byte delta (trailing newline) — effectively identical; treat as dup |
| `DOC_2026-06-28_AI_OCS_TASKS-MD_V2.md` | 9392 | 9391 | 1-byte delta — effectively identical |
| `DOC_2026-06-30_AI_REFERENCE_ROC-OS-ProtocolCheatSheet_V1.html` | 9142 | 9463 | 321-byte delta — a real variant; confirm which is current before pruning |
| `PROJ_ADVISORY_.../TEMPLATE_...RISK-ASSESSMENT-CLIENT-REPORT_V1.docx` | 12835 | 12678 | 157-byte delta (docx metadata likely); deliverable — iCloud canonical, keep |
| `PROJ_ADVISORY_.../TEMPLATE_...RISK-ASSESSMENT-WORKPAPER_V1.xlsx` | 24033 | **56733** | **Big delta.** Drive copy is 2.4× larger — likely the built 9-tab version; the iCloud copy may be stale/partial. **Do not treat as dup — reconcile which is authoritative.** |

### C. Junk / temp / lock (4 + 1 from §D)

| File | Note |
|---|---|
| `lu41p4cs0.tmp` (11980b) | LibreOffice temp — same size as `Steuben_2025_Final.xlsx`; a temp copy from an open Steuben edit. Safe to delete. |
| `.~lock.Steuben_2025_Final.xlsx#` (110b) | LibreOffice lock file (Steuben was/is open) — delete once the workbook is closed. |
| `text.txt` (8954b) | Generic name — **peek before deleting** (may be notes). |
| `unknown.png` (23401b) | Unidentified image — peek before deleting. |
| `Ai Implementation.m4a` (3.5 MB) | Audio recording — **NOT auto-junk**; confirm it's not a voice note worth keeping/migrating. |

### D. iCloud-only — CORRECTED 2026-07-06 by content-hash re-check

> ⚠️ **CORRECTION.** The original Category D below was matched by exact filename only, which **over-counted the gap** — it missed files renamed on upload and Office→Google-Doc conversions. A content-hash + basename re-check (`scratchpad/thread5_hashcheck.py`) resolves the 35+ name-misses to:
> - **7 already in Drive, identical content under a different name** — incl. the **Steuben `.numbers`** (byte-identical to `/03_Data/TAX FILES/.../DOC_2026-06-14_PROJECTS_Steuben_2025_FINAL.numbers`) and the whole `DOC_AI_NAMING_BUNDLE/` (renamed to the `DOC_2026-06-14_*` convention in `/04_Domain/DOC_AI_SYSTEM_Tools/`). **No gap — no action.**
> - **3 present in Drive as Google Docs** (basename match): `SOC 1 Memo.docx`, `SubService Organization Memo.docx`, `OConnorServiceMenu_V1.html`. Content backed up; only the **native `.docx`/`.html` format** is iCloud-only (preserve only if the Word/HTML format itself matters).
> - **29 TRUE backup gap** — genuinely absent from Drive:
>   - **SUBSTANTIVE:** the **20 Schwab investing-theme PDFs** (`PROJ_AI_AUTOTRADING/`, Engine 5, ~9 MB) + 3 OCS artifacts (`DailyDigest.tsx`, `CoworkStarterPrompt_V1.md`, `InitiativeMap_V1.html`).
>   - **LOW/JUNK:** `Steuben_2025_Final.xlsx` (regenerable export of the backed-up `.numbers`), `Ai Implementation.m4a`, `IMG_8182.jpeg`, `text.txt`, `unknown.png`, `lu41p4cs0.tmp`, `.~lock.Steuben...#`.
> **Net: the only substantive backup gap is the 20 Schwab PDFs + 3 OCS artifacts.** Steuben and the SOC memos are already backed up. This same content-hash caveat also applies to Category A — filename+size match is strong but a `shasum` pass is the definitive check.

_Original (filename-only) Category D, retained for trail:_

These exist ONLY in iCloud (backup gap). Grouped:

- **Engine 3 — Real Estate (HIGH VALUE, back up):** `Steuben_2025_Final.numbers` (720 KB) + `Steuben_2025_Final.xlsx` — the Steuben property workbook. Per locked decision #9, REI workbooks belong in Drive `/03_Data/rei/`. **Migrate.**
- **Engine 5 — Trading research:** 20 × `Schwab Investing Themes _ Charles Schwab_*.pdf` (~9 MB total) under `PROJ_AI_AUTOTRADING/`. Reference set; migrate to Drive (`03_Data` or `01_Intelligence`) or confirm intentionally local.
- **Engine 2 — Advisory work products:** `SOC 1 Memo.docx`, `SubService Organization Memo.docx`, `DOC_2026-06-26_BUSINESS_ADVISORY_OConnorServiceMenu_V1.html`. Migrate to Drive.
- **OCS artifacts:** `DOC_2026-06-28_AI_OCS_CoworkStarterPrompt_V1.md`, `DOC_2026-06-28_AI_PROJECTS_OCS_InitiativeMap_V1.html`, `DIGEST 2026-06-30 AI OCS DailyDigest V1.tsx`. Consider migrating to `/00_Registry/` or `/05_Projects/`.
- **Naming bundle:** `DOC_AI_NAMING_BUNDLE/` (cheat sheet .docx, .pdf, .ps1 script, shortcut .json, automator .txt) — the file-naming toolkit; migrate to `/04_Domain/` or keep local.
- **Source tree remnant:** `DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/AGENTS.md` — part of the cloned repo (the rest matched); goes wherever that tree goes.
- **Misc images:** `IMG_8182.jpeg` (800 KB) — identify.
- **Lock file:** `.~lock.Steuben_2025_Final.xlsx#` — junk (see §C).

---

## 4. Recommended next steps (proposals — for Royal's review, nothing executed)

1. **Confirm the disposition split** in §3.A (reference/source → prune-from-iCloud; `PROJ_*` → keep as mirror).
2. **Migrate the §D unique assets to Drive** (esp. Steuben workbook + Schwab PDFs + SOC memos) — closes the backup gap BEFORE any iCloud pruning.
3. **Reconcile §B item 5** (the WORKPAPER .xlsx size mismatch) — determine which copy is authoritative.
4. **Checksum-verify a sample** of the 226 before bulk removal.
5. **Then** log the confirmed prune/migrate set into `PRUNE_QUEUE.md` and run `drive_audit.py` — report-first, human-confirm trash, as usual. (Note: the current `drive_audit.py` acts on *Drive* file-ids; removing *iCloud-local* copies is a separate step — likely a local move-to-archive, since these files may not have Drive-side ids of their own.)

**No files were moved, deleted, or trashed in producing this report.**

---

## Appendix — full list of the 226 exact duplicates (iCloud relative paths)

```
Ai Bootcamp/untitled folder/AI Bootcamp Hub.png
Ai Bootcamp/untitled folder/IMG_9571.jpg
dashboard.html
DOC_2026-06-24_AI_AUDIT_FRAMEWORK_Agentic_Maturity_Model_V1.html
DOC_2026-06-24_AI_AUDIT_FRAMEWORK_Architect_Lifecycle_V1.html
DOC_2026-06-30_AI_TIMELINE_ActiveInitiativesGantt_V1.html
DOC_AI_BIZ_ADMIN/PDF_2026-05-31_AI_BIZ_Namecheap_Order_203271955.pdf
DOC_AI_EDUCATION/DOC_2026-05-31_AI_EDUCATION_AI_Playlist_Beginner_Tutorial_Extract.txt
DOC_AI_EDUCATION/DOC_2026-05-31_AI_EDUCATION_Bootcamp_Session1.html
DOC_AI_EDUCATION/IMG_2026-05-31_AI_EDUCATION_Anthropic_Academy_Certificate.png
DOC_AI_EDUCATION/IMG_2026-05-31_AI_EDUCATION_Claude_Academy_101.png
DOC_AI_EDUCATION/IMG_2026-05-31_AI_EDUCATION_Claude_Code_101.png
DOC_AI_EDUCATION/PDF_2026-05-31_AI_EDUCATION_AI_Bootcamp_Curation_Transcript.pdf
DOC_AI_EDUCATION/PDF_2026-05-31_AI_EDUCATION_AI_Productivity_Stack.pdf
DOC_AI_NAMING_BUNDLE/DOC_2026-05-31_AI_PROJECTS_Automator_Workflow_Setup_Notes_V1.txt
DOC_AI_NAMING_BUNDLE/DOC_2026-05-31_AI_PROJECTS_File_Naming_Automator_Shell_Script_V1.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.claude-plugin/marketplace.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.claude-plugin/plugin.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.codex-plugin/plugin.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.cursor-plugin/plugin.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.gitattributes
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.github/FUNDING.yml
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.github/ISSUE_TEMPLATE/bug_report.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.github/ISSUE_TEMPLATE/config.yml
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.github/ISSUE_TEMPLATE/feature_request.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.github/ISSUE_TEMPLATE/platform_support.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.github/PULL_REQUEST_TEMPLATE.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.gitignore
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.opencode/INSTALL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.opencode/plugins/superpowers.js
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/.version-bump.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/assets/app-icon.png
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/assets/superpowers-small.svg
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/CLAUDE.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/CODE_OF_CONDUCT.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/plans/2025-11-22-opencode-support-design.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/plans/2025-11-22-opencode-support-implementation.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/plans/2025-11-28-skills-improvements-from-user-feedback.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/plans/2026-01-17-visual-brainstorming.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/README.opencode.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/plans/2026-01-22-document-review-system.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/plans/2026-02-19-visual-brainstorming-refactor.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/plans/2026-03-11-zero-dep-brainstorm-server.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/plans/2026-03-23-codex-app-compatibility.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/plans/2026-04-06-worktree-rototill.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/specs/2026-01-22-document-review-system-design.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/specs/2026-02-19-visual-brainstorming-refactor-design.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/specs/2026-03-11-zero-dep-brainstorm-server-design.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/specs/2026-03-23-codex-app-compatibility-design.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/superpowers/specs/2026-04-06-worktree-rototill-design.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/testing.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/docs/windows/polyglot-hooks.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/gemini-extension.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/GEMINI.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/hooks/hooks-cursor.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/hooks/hooks.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/hooks/run-hook.cmd
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/hooks/session-start
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/LICENSE
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/package.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/README.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/RELEASE-NOTES.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/scripts/bump-version.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/scripts/sync-to-codex-plugin.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/brainstorming/scripts/frame-template.html
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/brainstorming/scripts/helper.js
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/brainstorming/scripts/server.cjs
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/brainstorming/scripts/start-server.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/brainstorming/scripts/stop-server.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/brainstorming/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/brainstorming/spec-document-reviewer-prompt.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/brainstorming/visual-companion.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/dispatching-parallel-agents/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/executing-plans/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/finishing-a-development-branch/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/receiving-code-review/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/requesting-code-review/code-reviewer.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/requesting-code-review/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/subagent-driven-development/code-quality-reviewer-prompt.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/subagent-driven-development/implementer-prompt.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/subagent-driven-development/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/subagent-driven-development/spec-reviewer-prompt.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/condition-based-waiting-example.ts
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/condition-based-waiting.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/CREATION-LOG.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/defense-in-depth.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/find-polluter.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/root-cause-tracing.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/test-academic.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/test-pressure-1.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/test-pressure-2.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/systematic-debugging/test-pressure-3.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/test-driven-development/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/test-driven-development/testing-anti-patterns.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/using-git-worktrees/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/using-superpowers/references/codex-tools.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/using-superpowers/references/copilot-tools.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/using-superpowers/references/gemini-tools.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/using-superpowers/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/verification-before-completion/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/writing-plans/plan-document-reviewer-prompt.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/writing-plans/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/writing-skills/anthropic-best-practices.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/writing-skills/examples/CLAUDE_MD_TESTING.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/writing-skills/graphviz-conventions.dot
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/writing-skills/persuasion-principles.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/writing-skills/render-graphs.js
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/writing-skills/SKILL.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/skills/writing-skills/testing-skills-with-subagents.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/brainstorm-server/package-lock.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/brainstorm-server/package.json
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/brainstorm-server/server.test.js
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/brainstorm-server/windows-lifecycle.test.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/brainstorm-server/ws-protocol.test.js
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/claude-code/analyze-token-usage.py
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/claude-code/README.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/claude-code/run-skill-tests.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/claude-code/test-document-review-system.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/claude-code/test-helpers.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/claude-code/test-requesting-code-review.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/claude-code/test-subagent-driven-development-integration.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/claude-code/test-subagent-driven-development.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/claude-code/test-worktree-native-preference.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/codex-plugin-sync/test-sync-to-codex-plugin.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/prompts/action-oriented.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/prompts/after-planning-flow.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/prompts/claude-suggested-it.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/prompts/i-know-what-sdd-means.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/prompts/mid-conversation-execute-plan.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/prompts/please-use-brainstorming.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/prompts/skip-formalities.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/prompts/subagent-driven-development-please.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/prompts/use-systematic-debugging.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/run-all.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/run-claude-describes-sdd.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/run-extended-multiturn-test.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/run-haiku-test.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/run-multiturn-test.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/explicit-skill-requests/run-test.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/opencode/run-tests.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/opencode/setup.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/opencode/test-bootstrap-caching.mjs
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/opencode/test-bootstrap-caching.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/opencode/test-plugin-loading.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/opencode/test-priority.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/opencode/test-tools.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/skill-triggering/prompts/dispatching-parallel-agents.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/skill-triggering/prompts/executing-plans.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/skill-triggering/prompts/requesting-code-review.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/skill-triggering/prompts/systematic-debugging.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/skill-triggering/prompts/test-driven-development.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/skill-triggering/prompts/writing-plans.txt
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/skill-triggering/run-all.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/skill-triggering/run-test.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/subagent-driven-dev/go-fractals/design.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/subagent-driven-dev/go-fractals/plan.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/subagent-driven-dev/go-fractals/scaffold.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/subagent-driven-dev/run-test.sh
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/subagent-driven-dev/svelte-todo/design.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/subagent-driven-dev/svelte-todo/plan.md
DOC_AI_SUPERPOWERS_SOURCE/superpowers-main/tests/subagent-driven-dev/svelte-todo/scaffold.sh
DOC_AI_TOOLS_AND_GUIDES/DOC_2026-05-31_AI_TOOLS_Claude_Superpowers.md
DOC_AI_TOOLS_AND_GUIDES/IMG_2026-05-31_AI_TOOLS_Business_Consultant_Prompts.png
DOC_AI_TOOLS_AND_GUIDES/IMG_2026-05-31_AI_TOOLS_TAG_RISE_Prompt_Frameworks.png
DOC_AI_TOOLS_AND_GUIDES/PDF_2026-05-31_AI_TOOLS_AI_Assisted.pdf
DOC_AI_TOOLS_AND_GUIDES/PDF_2026-05-31_AI_TOOLS_Claude_Plugins_And_Skills_2026.pdf
DOC_AI_TOOLS_AND_GUIDES/PDF_2026-05-31_AI_TOOLS_Complete_Guide_Building_Skills_for_Claude.pdf
DOC_AI_TOOLS_AND_GUIDES/PDF_2026-05-31_AI_TOOLS_GenAI_Divide_2025.pdf
IMG_AI_SCREENSHOTS/IMG_2026-05-31_AI_SCREENSHOTS_Ai_UI_Nov14_2025_V1.png
IMG_AI_SCREENSHOTS/IMG_2026-05-31_AI_SCREENSHOTS_Ai_UI_Nov14_2025_V2.png
MD Files/CLAUDE.md
PROJ_ADVISORY_MIGRATION-SPRINT/DOC_2026-06-18_AI_ADVISORY_OUTREACH-KIT_V1.md
PROJ_ADVISORY_MIGRATION-SPRINT/DOC_2026-06-21_AI_ADVISORY_PHASE2-OUTREACH-PLAN_V1.md
PROJ_ADVISORY_MIGRATION-SPRINT/DOC_2026-06-21_AI_ADVISORY_PHASE2-OUTREACH-SPEC_V1.md
PROJ_ADVISORY_MIGRATION-SPRINT/TEMPLATE_2026-06-18_AI_ADVISORY_ENGAGEMENT-PACK_V1.docx
PROJ_AI_AUTOTRADING/DOC_2026-05-31_AI_AUTOTRADING_Thought_Leader_Discussion_Migration.txt
PROJ_AI_BAYSTREET/DOC_2026-05-31_AI_BAYSTREET_Cash_on_Cash_Analysis.md
PROJ_AI_BAYSTREET/DOC_2026-05-31_AI_BAYSTREET_Comprehensive_Summary.md
PROJ_AI_BAYSTREET/DOC_AI_BAYSTREET_Admin/DOC_2026-05-31_AI_BAYSTREET_Oxford_Portfolio_Analysis_Design.md
PROJ_AI_BAYSTREET/DOC_AI_BAYSTREET_Admin/DOC_2026-05-31_AI_BAYSTREET_Stapleton_Research_Project.md
PROJ_AI_BAYSTREET/OConnor_Capital_Access.xlsx
PROJ_AI_BAYSTREET/PDF_2026-05-31_AI_BAYSTREET_Cash_on_Cash_Return_Analysis_NYC.pdf
PROJ_AI_BAYSTREET/PDF_2026-05-31_AI_BAYSTREET_Current_State_And_Next_Steps.pdf
PROJ_AI_BAYSTREET/PDF_2026-05-31_AI_BAYSTREET_Knowledge_Base_Decisions_Log.pdf
PROJ_AI_BAYSTREET/PDF_2026-05-31_AI_BAYSTREET_Quick_Start_Guide.pdf
PROJ_AI_BAYSTREET/PDF_2026-05-31_AI_BAYSTREET_Real_Estate_Automation_System.pdf
PROJ_AI_CASHFLOWMASTER/DOC_2026-05-31_AI_CFM_Notes.txt
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Admin/DOC_2026-05-31_AI_CFM_Import_Test_Guide.md
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Admin/IMG_2026-05-31_AI_CFM_Citibank_Sample_Statement.jpeg
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Project_Files/cfm_manual_log_2026-06.csv
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Project_Files/DOC_2026-05-31_AI_CFM_Manual_Log_Guide.md
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Project_Files/DOC_2026-05-31_AI_CFM_Phase3_ADR.md
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Project_Files/DOC_2026-05-31_AI_CFM_Phase3_Schema.md
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Test_Environment/DOC_2026-05-31_AI_CFM_App_V2.html
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Test_Environment/DOC_2026-05-31_AI_CFM_Status_2026.md
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Test_Environment/files_2/cfm_import_test_guide.md
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Test_Environment/files_2/test_import_citibank.csv
PROJ_AI_CASHFLOWMASTER/DOC_AI_CFM_Test_Environment/files_3/PDF_2026-05-31_AI_CFM_Test_Citibank_Statement.pdf
PROJ_AI_CASHFLOWMASTER/PDF_2026-05-31_AI_CFM_Fallback.pdf
PROJ_AI_CASHFLOWMASTER/PDF_2026-05-31_AI_CFM_Results.pdf
PROJ_AI_FAMILYSPORTS/DOC_2026-05-31_AI_FAMILYSPORTS_Design_Summary_V2.md
PROJ_AI_FAMILYSPORTS/DOC_2026-05-31_AI_FAMILYSPORTS_Spouse_Summary_V1.docx
PROJ_AI_FAMILYSPORTS/PDF_2026-05-31_AI_FAMILYSPORTS_Command_Center.pdf
PROJ_AI_FAMILYSPORTS/PDF_2026-05-31_AI_FAMILYSPORTS_Spouse_Summary_Google_Docs.pdf
PROJ_AI_REI/phase1-opendata.json.txt
PROJ_AI_REI/property-workbooks/Neckar_2025_Final.xlsx
PROJ_AI_REI/WF_2026-05-31_AI_REI_Phase1_Single_Property_Clean.json
project_state_Company Description Translator.md
SOC 1 Review - Clean.numbers
WF_AI_N8N_TEMPLATES/DOC_2026-05-31_AI_N8N_Scrape_Summarize_Webpages_Guide.rtf
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_AI_Agent_Google_Calendar_OpenAI.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_AI_Agent_Scrape_Webpages.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_AI_Chat_Any_Data_Source.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_AI_Chatbot_Web_Search.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_AI_Web_Researcher_Sales.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_Auto_Generate_Workflow_Docs.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_Automated_HR_CV_Analysis.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_Autonomous_AI_Crawler.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_Fetch_Dynamic_Prompts_GitHub.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_Organise_Local_File_Directories.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_Personal_Shopper_WooCommerce_RAG.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_RAG_Stock_Earnings_Analysis.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_Stock_Analysis_QA_Workflow.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_Web_Scraping_Jina_Google_Sheets.json
WF_AI_N8N_TEMPLATES/WF_2026-05-31_AI_N8N_YouTube_Summarization_Analysis.json
```
