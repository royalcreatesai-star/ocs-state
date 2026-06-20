# OAIS_STATE.md — O'Connor AI System State

**Program:** O'Connor Configured System (OCS) | 60-Day Initiative
**Version:** V7.1 — Gate 4 CLOSED / Gate 5 OPEN / Migration Sprint V2 ACTIVE — **Workstream B BUILT**
**Last Updated:** 2026-06-19
**Updated By:** Royal O'Connor + Claude (Opus 4.8, Claude Code) — 2026-06-18 build session
**Route:** /ROC-OS/00_Registry/
**Supersedes & reconciles:** the TWO divergent V6 files — the 06-15 "foundation" branch (git repo, 15 locked decisions, harness registry, Gate 4 detail) AND the 06-17 "Migration Sprint" branch (W7 decisions). The 06-17 branch had dropped foundation content; V7 re-merged everything and added the 2026-06-18 decisions. **V7.1 = V7 imported into the git repo (which had been stale at V6) + the 2026-06-18 build-session outputs (Migration Sprint Components 1–3 built, Workstream A Phases 0–1 drafted). Repo is canonical again and now ahead of the Drive mirror until re-mirrored.**
**Canonical:** git repo `~/Documents/ME/Ai/ocs-state` → github.com/royalcreatesai-star/ocs-state. This Drive copy is the MIRROR. ⚠ Edit `.md` as TEXT only — opening in Google Docs spawns duplicate files.
**Cross-platform bridge:** Load in any Claude or ChatGPT session before work. Read in full. Check §12 for active tasks.

---

## 1. PROGRAM IDENTITY
| Field | Value |
|-------|-------|
| Program | O'Connor Configured System (OCS) / codename ROC-OS |
| Owner | Royal O'Connor |
| Window | 2026-06-15 → 2026-08-14 (60 days, 9 gates) |
| Mission | Consolidate all AI assets into a single documented, sellable system |
| Canonical Home | git repo (SoT) + Google Drive mirror — royalcreates.ai@gmail.com |
| Filing Root | /ROC-OS/{00_Registry, 01_Intelligence, 02_Automation, 03_Data, 04_Domain, 05_Projects} |
| Maturity | 2.5 of 4 (Level 3 target by close) |

## 2. FIVE ENGINES
| # | Engine | Status |
|---|--------|--------|
| 1 | W2 — Audit Firm (Sr Audit Manager) | Active |
| 2 | O'Connor Advisory — AI Governance, Risk & Migration Advisory | Active; **Migration Sprint V2 — delivery product built** |
| 3 | Real Estate — Oxford, Neckar, Steuben | Active; phased data mgmt |
| 4 | AI Product — OCS, WallyB, MovieWatch | Active; OCS primary |
| 5 | Investing — options, equities, Schwab | Active; auto-trading on hold |

## 3. GATE STATUS
| Gate | Focus | Status |
|------|-------|--------|
| 1 | Filing room + asset registry | CLOSED ~06-12 |
| 2 | State standardization | CLOSED ~06-12 |
| 3 | Skills / Commands / Refinery | CLOSED ~06-13 |
| 4 | OpenAI export audit + GPT configs | ✅ CLOSED 06-14 |
| 5 | Claude Projects audit **+ ChatGPT memory/connector audit (added 06-18)** | OPEN |
| 6 | n8n workflow export + docs | PENDING |
| 7 | Binder V1 | PENDING |
| 8 | Demo engineering + Migration Rescue | PENDING |
| 9 | Final packaging + sellable system | PENDING ~08-14 |

## 4. GATE 4 RECORD — OpenAI Export Audit (CLOSED)
290 conversations (Aug 2023–Jun 2026), 157 .dat assets (100% resolved), **deprecation risk CLEAN** (zero Assistants API / Agent Builder objects). Account royaloconnor@gmail.com, training_allowed: false.
**6 of 6 Custom GPTs confirmed** (Financial Strategist, Home Renovation Advisor, 4× Cold Case). Full registry: DOC_2026-06-14_AI_GPT-GIZMO-REGISTRY_V3.md (01_Intelligence).
**CORRECTION (locked):** Audit Trainer, NYC CRE Broker, Financial Aid Consultant, Technical Expert are **Claude Projects** (Gate 5), NOT GPTs.

## 5. GATE 3 — 16 HARNESS ASSETS (04_Domain/)
Skills: method-select, coc-underwrite, risk-score, comp-score, content-curation, billing-conventions. Rules: pii-sanitize, derive-never-store, security-hygiene, session-close. Template: persona-spec. Commands: status, wrap, gpt-revise, property-rollup, trade-log. (600-token rule; detail in Refinery MD on demand.)
**Document Refinery** (02_Automation/refinery/): 5-stage n8n pipeline, build pending (W3). **NotebookLM MCP** installed/authenticated (royalcreates.ai), 25 tools, zero-token retrieval.

## 5b. LOCKED KEY DECISIONS (foundation)
1. Hallway = Google Drive (royalcreates.ai). 2. Hamilton = SMB two-track (Configured Business demo + Migration Rescue); Audit Trainer = internal/firm-eval only. 3. OpenAI path = Responses API / Agents SDK only. 4. n8n = core rails ("workflows are controls, agents are staff"). 5. wrap = session-close trigger; fresh session opens with state file only. 6. MovieWatch Phase 1 ready. 7. n8n-docker NEVER syncs to Drive. 8. Work split: Royal owns Domain+controls; engineer owns Automation+Data. 9. Tax worksheets → 03_Data/rei/. 10. Dashboards open in Chrome. 11. Intake: /ROC-OS/00_Inbox/ + "ROC-OS Intake" Gmail label. 12. royalcreates.ai domain NOT yet registered. 13. Session hygiene is a RULE (quadratic token tax). 14. CLAUDE.md/skill 600-token rule. 15. NotebookLM + Drive MCP both on royalcreates.ai, working.

## 6. MIGRATION SPRINT V2 — DECISIONS LOCKED (Engine 2)
Full plan: **DOC_2026-06-18_AI_ADVISORY_MIGRATION-SPRINT-PLAN_V2.md** (/ROC-OS/05_Projects/).
- **Positioning:** AI Governance, Risk & Migration Advisory (NOT AI Development Services).
- **Naming ladder:** AI Dependency Risk **Scan** (free lead magnet) → AI Dependency Risk **Assessment** ($1,500, replaces "Exposure Assessment") → **Migration Build** (tiered). Scan flags / Assessment quantifies / Build fixes.
- **Build pricing TIERED (supersedes flat $5–10K):** T1 Simple $3.5–6K (8–15h) · T2 Moderate $8–15K (20–40h) · T3 Complex $20–40K, custom above (60+h). T3 = exception (mid-market). Tier set by Asset Register signals.
- **Workpaper:** Section 1 = AI Asset Register (spine; +Owner, Business Function, Migration Complexity S/M/L, Data-Loss Exposure, WP-numbered Evidence). SOC-1 Type II structural reference.
- **SOC ports:** Continuity Confirmation (bridge letter), Carve-Out dependencies (S3), Complementary Client Actions (CUEC — homes the Aug-26 data-wipe finding), WP cross-referencing. Derived from Reid CPAs ADP SOC-1 / ADP GETS carve-out memos + AuditMiner Service Org Review Tool.
- **Risk Scan:** 5 questions, Low/Mod/High bands, manual-first (Google Form → Sheet w/ formula scoring → Claude prompt-template reply → send → status log). Q5 "No idea" bumps band up one ONLY when Q1/Q2 ≠ confident No. Automate ~month 3 if volume.
- **Dual-deadline:** Wave 1 Aug 26 (Assistants API) + Wave 2 Nov 30 (Agent Builder) in all outreach + scan.
- **Delivery (TIERED by blast radius — refined 06-19):** direct account access (primary). **Scan + Assessment = single operator (Royal)** with a Verify-Before-Status self-review gate — read-only, low blast radius; a second body on a $1,500 / ~2hr engagement erodes the "Main Street economics" margin. **Migration Build = explicit executor→reviewer split** — engineer executes, Royal reviews the *changed* artifact against evidence before go-live (high blast radius + peak E&O, F11). Assessment read-only; Build separate engagement; clean outcome = $1,500 Clearance Report. VBS control: `/04_Domain/DOC_AI_HARNESS_Controls/DOC_2026-06-19_AI_HARNESS_VERIFY-BEFORE-STATUS-CONTROL_V1.md`. *(Refines the prior flat "engineer = execution, Royal = reviewer" — at the Assessment Royal IS the executor, so the gate is self-review; the engineer enters at the Build.)*

### 6a. BUILD STATUS — 2026-06-18 session (all in /ROC-OS/05_Projects/)
- **Workstream B — Delivery Infrastructure COMPLETE:**
  - **C1 Workpaper** — `TEMPLATE_2026-06-18_AI_ADVISORY_RISK-ASSESSMENT-WORKPAPER_V1.xlsx`. 9-tab Excel: AI Asset Register spine + Sections 2–5 + Carve-Outs + CUEC + Continuity Confirmation + WP-Index/Evidence Log + Reference; cross-sheet links, conditional formatting, deterministic tier rollup. Verified (309 cross-refs resolve, 0 errors).
  - **C2 Client Report** — `TEMPLATE_..._RISK-ASSESSMENT-CLIENT-REPORT_V1.docx`. Branded one-page; Exec Summary + Finding Detail + Remediation Estimate + Next Steps + Clearance Report variant.
  - **C3 Engagement Pack** — `TEMPLATE_..._ENGAGEMENT-PACK_V1.docx`. Intake Questionnaire + **non-attest** Engagement Letter (adapted AICPA ASB-CL-1.1 spine, dropped via 00_Inbox; explicitly not an audit/review/attestation, no opinion) + Credential-Handling Protocol + Post-Engagement Checklist.
  - C4 = tiered pricing framework (wired into the workpaper's rollup; no separate doc).
- **Workstream A — Phases 0–1 DRAFTED:** `DOC_2026-06-18_AI_ADVISORY_OUTREACH-KIT_V1.md` — Risk Scan form + scoring logic + all 3 reply variants (HIGH/MODERATE/LOW-Clearance) + hook/pitch/FAQ. Remaining: stand up live Google Form + Sheet scoring; Phase 2 (3-touch); Phase 3 (leave-behind PDF); Phase 4 (target list).
- **Intake channels LIVE (06-18):** Drive connector reads /ROC-OS/00_Inbox; Gmail connector wired, "ROC-OS Intake" label = Label_448698645156134993 (0 threads tagged yet).

## 7. PROJECT REGISTRY
PROJ_AI_OCS (Gate 5 next) · PROJ_AI_WALLYB (nodes 8/8a/12 passing) · PROJ_AI_MOVIEWATCH (Phase 1) · PROJ_AI_FAMILYSPORTS · PROJ_AI_AUTOTRADING (hold) · PROJ_AI_CDT · PROJ_AI_BOOTCAMP · PROJ_AI_COLDCASE · PROJ_AI_DIGITALLITERACY · PROJ_RE_PROPDATA · PROJ_EDU_SHSAT · PROJ_AI_FOOTBALL · **PROJ_AI_MIGRATION (Engine 2 — ACTIVE SPRINT; Workstream B delivery product BUILT 06-18; Workstream A outreach next)**.
Full universe: 24 unique initiatives across 6 sources — DOC_2026-06-14_AI_PROJECTS_GATE5-RECONCILIATION_V1.md.

## 8. OPEN FINDINGS
F1 Oxford rent discrepancy ($50,700 vs $45,000) · F2 Bay Street file anomaly · F3 Advisory domain undercounted · F4 GPT capability toggles · F5 CLOSED · F6 CFM Phase 2 + Neckar 2025 · F7 WAV transcription (low) · F8 PNG spot-check (low) · F9 RESOLVED · F10 state lineage — folded/retired (residual: CoWork archive old files) · **F11 E&O / professional liability — confirm CPA licensure extends to tech consulting or obtain advisory E&O (placeholder left in C3 engagement letter — resolve before first paid engagement)** · F12 CoWork dedup (naming + iCloud↔Drive). **F13: two divergent V6 files — V7 reconciled them; the git repo was stale at V6 and is now updated to V7.1 (this commit). Residual: CoWork to remove the 2 stray Google Docs (IDs in §12) + update the Drive .md mirror to V7.1.** **F14 (NEW): no LibreOffice/pandoc on the Mac — can't render PDFs, recalc xlsx, or run the docx/xlsx skill validators locally; deliverables verified structurally only. `brew install --cask libreoffice` unlocks PDF export + recalc.** **F14 ext (06-19): the Drive connector corrupts binary Office downloads — `download_file_content` on a .docx returns bad-CRC/garbled bytes (though `read_file_content` text is clean); no `defusedxml` either, so the docx-skill unpack scripts fail. Binary Office edits must go through the native app (Google Docs/Word) or a clean local filesystem, NOT connector download→edit→reupload.** **F15 (NEW 06-19): cross-runtime access map — no single runtime can both edit a Drive Office doc AND commit to the git repo. This Code harness is path-guarded to /ME/Ai + the ocs-state repo (can't reach the local Drive mount); CoWork's sandbox can't reach the repo and can't unpack binary .docx; Chrome needs a per-domain site-access grant. Split file-edit work (CoWork/Chrome → Drive) from repo commits (Code harness). Detail in memory `project-ocs-runtime-access-map`; control in `feedback-verify-before-status`.**

## 9. DEPRECATION TIMELINE
Assistants API 2026-08-26 (~10wk) · Agent Builder 2026-11-30 (~24wk) · OCS Gate 9 2026-08-14. Royal's account exposure: ZERO (the positioning advantage).

## 10. ARCHITECTURE / STACK
Claude (Sonnet 4.6) orchestration · OpenAI (GPT-5-5-thinking) specialist advisory (6 GPTs + 2 Projects, ===SECTION=== format) · n8n 2.0 (Docker, M4, LOCAL only) · Google Drive mirror. Naming: {TYPE}_{DATE}_{DOMAIN}_{CATEGORY}_{DESCRIPTION}_{VERSION}.

## 11. GIT REPO (✅ LIVE)
Local `~/Documents/ME/Ai/ocs-state` (outside iCloud — iCloud blocks .git). Remote github.com/royalcreatesai-star/ocs-state (main). Canonical file OAIS_STATE.md; Drive 00_Registry = mirror. Fine-grained PAT (Contents r/w). Push: `cd ~/Documents/ME/Ai/ocs-state && git push -u origin main`.
**06-18:** repo path whitelisted in `~/.claude/hooks/bash-path-guard.py` so Claude Code (this harness) can `git add/commit/push` the repo directly without the /ME/Ai path-guard blocking it.

## 12. OPEN ACTIONS
**Gate 5 (Claude Projects audit):**
- [ ] Map Claude Projects (Audit Trainer, NYC CRE Broker, Financial Aid Consultant, Technical Expert) — name, instructions, files, knowledge, purpose
- [ ] Cross-reference Claude Projects vs OpenAI GPTs — overlaps, gaps, consolidation
- [ ] **ChatGPT memory + connector audit (NEW 06-18):** check ChatGPT Memory + "Reference chat history"; ChatGPT connectors; Google Account → third-party apps (myaccount.google.com/connections) for OpenAI↔Drive scope. Document as a governance/credibility artifact. (Likely "O'Connor Advisory" surfaced via state-file paste or ChatGPT memory, NOT a Drive connection.)
- [ ] Enable GPT capability toggles (F4)

**Migration Sprint V2 (parallel — not gated):**
- [x] **Component 1 — Risk Assessment workpaper BUILT 06-18** (Asset Register + S2–5 + Carve-Outs + CUEC + Continuity Confirmation + WP numbering) — .xlsx in /05_Projects/
- [x] **Component 2 — client report template BUILT 06-18** — .docx
- [x] **Component 3 — Engagement Pack BUILT 06-18** (intake + non-attest engagement letter + credential protocol + post-engagement checklist) — .docx
- [x] **Risk Scan reply templates + messaging foundation DRAFTED 06-18** (Outreach Kit V1: 5-Q form + scoring + HIGH/MOD/LOW replies + hook/pitch/FAQ)
- [ ] Stand up the LIVE Risk Scan (Google Form + Sheet formula scoring); optional SKILL_risk-scan-respond_V1
- [ ] Outreach Phase 2 (3-touch sequence) + Phase 3 (leave-behind one-pager PDF) + Phase 4 (target list)
- [ ] **Tier cost-and-margin model (xlsx):** bottom-up cost build-up + elasticity by buyer profile — validates tier prices
- [ ] **Bridge-letter (Continuity Confirmation) pricing:** research + set
- [ ] **Replicate this work into the OpenAI environment where appropriate** (cross-platform parity)
- [ ] Engineer readiness gate (Responses API/Agents SDK familiarity) (F10 partner)
- [ ] Confirm E&O coverage (F11)
- [ ] Test run on Royal's own (CLEAN) account — sample deliverable, validate ≤2-hr target

**File hygiene (CoWork — F12/F13):**
- [x] **Commit V7.1 to git repo (SoT) — done this session** (repo had been stale at V6; now reconciled + current)
- [ ] Update the Drive `.md` mirror in 00_Registry to V7.1 (so mirror = repo)
- [ ] Remove 2 stray Google Docs V6 (IDs: 1vFnP5NHBlT66pSJZefwnsvWozU0WRMXGtYolmR3kv7k, 1QUdVtWKKKYP1Y2RRXcUiFKyL6gmkIYKciyIDZw_ibQU)
- [x] Courtesy: fix Salesforce→ADP slip in SubService memo — DONE 06-19; verified in Drive (memo reads "ADP Workforce / ADP GETS" throughout, zero "Salesforce")

## 13. SHORTHAND DECODE
OCS / ROC-OS · The Binder (8-ch client Playbook) · The Blueprint (5-engine strategy) · Hallway (Google Drive) · Gates (pass/fail) · Harness (tools/workflows/protocols) · Hamilton (NJ Anthropic SMB Workshop) · **Migration Rescue = Risk Scan → Risk Assessment → Migration Build** · Deprecation (software shutdown, NOT accounting) · Gizmo ID (OpenAI GPT id) · ===SECTION=== (GPT delimiter) · Claude Projects (Anthropic GPT-equivalent) · Execution Gap (the moat) · Carve-Out (third-party dependency documented not tested) · CUEC → Complementary Client Actions · Band (Low/Mod/High risk) vs Tier (T1/T2/T3 price).

## 14. SESSION BRIDGE
1. Read in full. 2. Check §12 (open actions). 3. Check §8 (findings). 4. Check §3 (gates). 5. Confirm orientation. 6. Close: /wrap (Chat) or /update (Code) → update state, mirror to Drive, commit to repo.

---
*OAIS_STATE.md | OCS | V7.1 | Gate 4 CLOSED / Gate 5 OPEN / Migration Sprint V2 ACTIVE — Workstream B built | reconciles both V6 branches + 06-18 build session | 2026-06-18 | /ROC-OS/00_Registry/*
