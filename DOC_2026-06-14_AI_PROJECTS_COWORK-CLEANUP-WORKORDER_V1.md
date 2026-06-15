# CoWork Work Order — OCS File Cleanup (Gate 5 handoff)
**Doc Ref:** DOC_2026-06-14_AI_PROJECTS_COWORK-CLEANUP-WORKORDER_V1
**Date:** 2026-06-14
**Source of truth:** DOC_2026-06-14_AI_PROJECTS_GATE5-RECONCILIATION_V1.md (Drive 00_Registry)
**For:** CoWork session — Drive + iCloud cleanup

---

## NAMING CONVENTION (apply everywhere)
Format: `{TYPE}_{DATE}_{DOMAIN}_{CATEGORY}_{DESCRIPTION}_{VERSION}`
- TYPE: DOC / PROJ / WF / PDF / IMG  •  DATE: YYYY-MM-DD  •  VERSION: V1, V2…
- Reference tools: `/ME/Ai/DOC_AI_NAMING_BUNDLE/` (cheat sheet, shell script, PowerShell, iOS shortcut)
- **EXCEPTION:** `OAIS_STATE` keeps its stable memorable name (canonical bridge) — confirm with Royal before renaming.

---

## PHASE 3 — BULK FILE RENAMING (current)
Files that do NOT follow the convention — rename:
- [ ] Drive `PROJECT_STATE_*.md` exports (folder `1t0_…`) — 10 files
- [ ] Drive blueprint mirror (folder `1CVa…`) — 12 `.md` files
- [ ] iCloud `/ME/Ai/blueprint/projects/*.md` — 12 files
- [ ] iCloud loose files: `project_state_Company Description Translator.md`, `text.txt`, `unknown.png`
- [ ] Decide on `OAIS_STATE_V5.md` (now superseded by V6)

**RULE:** rename in BOTH Drive and iCloud so mirrors stay matched. One code per initiative (e.g. choose ONE of `PROJ_AI_REI` / `REI Technical Expert` / `RE_PROPDATA` — don't keep three).

---

## PHASE 4 — iCloud ↔ DRIVE DEDUP
- [ ] iCloud is origin; Drive is canonical "hallway." Keep ONE source per file.
- [ ] `blueprint/projects` exists in both iCloud and Drive (folder `1CVa`) — consolidate.
- [ ] WallyB sprawl: own repo + Drive state-history folder + multiple PROJECT_STATE copies — collapse to one current + one history folder.

---

## PHASE 5 — SPECIFIC FIXES
- [ ] Create `Steuben_2025_Final.xlsx` in Drive `/TAX FILES/2025 TAX/` (only `.numbers` exists in iCloud; Oxford + Neckar already have `.xlsx`)
- [ ] Archive `OCS_Program_State_V1–V5.md` → new `/ROC-OS/00_Registry/_archive/` subfolder (lineage retired; content folded into `OAIS_STATE_V6`)
- [ ] Delete stray Google Doc `Project MD files (Various Sources)` in Drive root (confirmed discardable)
- [ ] Resolve duplicate Blueprint files (multiple `royal-oconnor-blueprint` / `PROJECT_STATE_Blueprint` copies)

---

## DO NOT TOUCH
- `n8n-docker/` — RULE: never syncs to Drive
- `ocs-state/.git/` — version control
- `OAIS_STATE_V6.md` — current canonical state file
- `wallyb/` working code — active project

---

## DEFINITION OF DONE
- Every file follows the naming convention (or is the OAIS_STATE exception)
- One code per initiative, matched across iCloud + Drive
- No orphaned duplicates; OCS_Program_State archived; stray doc deleted
- Steuben `.xlsx` present in Drive

---
*DOC_2026-06-14_AI_PROJECTS_COWORK-CLEANUP-WORKORDER_V1 — OCS | Gate 5 handoff | 2026-06-14*
