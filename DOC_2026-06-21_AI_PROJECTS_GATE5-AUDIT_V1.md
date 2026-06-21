# DOC_2026-06-21_AI_PROJECTS_GATE5-AUDIT_V1.md — Gate 5 Audit

**Gate:** 5 (OPEN) — Claude Projects audit **+ ChatGPT memory/connector audit (added 06-18)**
**Program:** O'Connor Configured System (OCS) | Engine 4 (program) / governance artifact
**Route (logical):** /ROC-OS/05_Projects/ — physically committed to git repo SoT `~/Documents/ME/Ai/ocs-state` (flat layout, alongside the Gate 5 reconciliation doc). **Mirror to Drive /ROC-OS/05_Projects/ pending.**
**Created:** 2026-06-21 by Royal O'Connor + Claude (Opus 4.8, Claude Code).
**Status:** ⏳ V1 SCAFFOLD — awaiting Royal's paste of (a) each Claude Project's instructions + knowledge list, (b) ChatGPT memory list, (c) ChatGPT connector list. Sections marked **⏳ AWAITING PASTE** are placeholders.
**Source-of-truth inputs:** OCS_STATE_CANONICAL.md V7.1 §3/§4/§11/§12; DOC_2026-06-14_AI_PROJECTS_GATE5-RECONCILIATION_V1.md.
**Constraint this session:** Parallel session is editing OCS_STATE_CANONICAL.md (Migration Sprint setup). **This doc does NOT edit the state file.** §C below proposes state edits only — Royal merges them.

---

## §A — CLAUDE PROJECTS AUDIT

### A.0 Scope confirmation
Per **§4 locked correction**, these four are **Claude Projects (Anthropic), NOT OpenAI GPTs** → **no Gizmo ID exists** for any of them. Do not look for one. Claude Projects expose two configurable surfaces to capture:
1. **Custom instructions** (the project's "instructions" / set-context box)
2. **Project knowledge** (attached files + pasted knowledge)

### A.1 Summary table

| # | Claude Project | Intended Engine | Reconciliation cross-ref | Type confirmed | Instructions captured | Knowledge list captured |
|---|----------------|:--:|---|:--:|:--:|:--:|
| 1 | **Audit Trainer** | 1 (W2 / firm-internal) | Locked decision #2: *"Audit Trainer = internal/firm-eval only"*; ≠ The Binder | ✅ Claude Project (not GPT) | ⏳ | ⏳ |
| 2 | **NYC CRE Broker** | 3 (Real Estate) | #13 "NYC CRE Commercial Broker — **Claude only, confirmed not a GPT**" | ✅ Claude Project (not GPT) | ⏳ | ⏳ |
| 3 | **Financial Aid Consultant** | ❓ (likely Family/Personal — verify) | ⚠ **Not present under this name** in reconciliation cross-ref — possible undocumented project | ✅ Claude Project (not GPT) | ⏳ | ⏳ |
| 4 | **Technical Expert** | 3 (Real Estate) | #14 "REI Technical Expert" → PROJ_AI_REI / Bay St | ✅ Claude Project (not GPT) | ⏳ | ⏳ |

> ⚠ **Flag A-1 (gap):** *Financial Aid Consultant* is not in the Gate 5 reconciliation cross-reference (S1–S6, 24 initiatives). Either it is newer than the 06-14 reconciliation, or it was missed in the source sweep. Capture it fully and assign an engine + PROJ_ code in §C.
> ⚠ **Flag A-2 (naming):** Project #4 is labeled **"Technical Expert"** in the Gate 4 correction but **"REI Technical Expert"** in reconciliation #14 and Drive state S6. Confirm the live claude.ai name and homogenize (D7 naming rule).

### A.2 Per-project detail

#### Project 1 — Audit Trainer
- **Purpose / role:** ⏳ AWAITING PASTE. *(Working assumption from state: internal audit-skills training / firm-evaluation aid. Explicitly NOT a client deliverable and NOT The Binder.)*
- **Intended engine:** 1 (W2 / firm-internal). *Confirm it should not be re-pointed at Engine 2 advisory.*
- **Custom instructions:** ⏳ AWAITING PASTE (full text).
- **Knowledge files:** ⏳ AWAITING PASTE (list every attached file + 1-line description each).
- **Overlap / consolidation notes:** Compare against Engine 2 advisory assets and the Migration Sprint workpapers — confirm no client-facing leakage. Cross-ref Gate 4 GPTs: no audit-training GPT exists (the 6 GPTs are Financial Strategist, Home Renovation Advisor, 4× Cold Case) → **no GPT overlap.**

#### Project 2 — NYC CRE Broker
- **Purpose / role:** ⏳ AWAITING PASTE. *(Working assumption: NYC commercial real-estate brokerage analysis / deal support — Abby/Engine 3 adjacent.)*
- **Intended engine:** 3 (Real Estate).
- **Custom instructions:** ⏳ AWAITING PASTE.
- **Knowledge files:** ⏳ AWAITING PASTE.
- **Overlap / consolidation notes:** Reconciliation confirms **Claude-only, no GPT twin** → no cross-platform dedup needed. Check overlap with Project 4 (Technical Expert / REI) — both Engine 3; confirm they are distinct (brokerage vs. REI technical underwriting) and not redundant.

#### Project 3 — Financial Aid Consultant
- **Purpose / role:** ⏳ AWAITING PASTE. *(Working assumption: college/school financial-aid guidance — possibly Family engine, tied to McKayla HS/college track. VERIFY.)*
- **Intended engine:** ❓ — assign on paste (candidate: Family/Personal; or Engine 2 if client-facing).
- **Custom instructions:** ⏳ AWAITING PASTE.
- **Knowledge files:** ⏳ AWAITING PASTE.
- **Overlap / consolidation notes:** New to the registry (Flag A-1). Decide whether it gets a PROJ_ code or is folded into an existing family/education initiative (e.g., PROJ_EDU_SHSAT family cluster).

#### Project 4 — Technical Expert (a.k.a. REI Technical Expert)
- **Purpose / role:** ⏳ AWAITING PASTE. *(Working assumption: REI technical/underwriting expert — Bay Street / Staten Island analysis support.)*
- **Intended engine:** 3 (Real Estate) → PROJ_AI_REI / Bay St.
- **Custom instructions:** ⏳ AWAITING PASTE.
- **Knowledge files:** ⏳ AWAITING PASTE.
- **Overlap / consolidation notes:** Present in iCloud (S4/S5) + Drive state (S6) but **Claude-only, no GPT twin.** Confirm distinct from Project 2 (CRE Broker).

### A.3 Cross-reference — Claude Projects vs OpenAI GPTs (Gate 4)
- **Gate 4 confirmed 6 GPTs:** Financial Strategist, Home Renovation Advisor, 4× Cold Case.
- **Overlap:** ZERO of the 4 Gate 5 Claude Projects has a same-purpose GPT twin. (Cross-platform *pairs* identified in reconciliation — Translator/"The Bridge", Travel/World Tour — are **not** in this Gate 5 set.)
- **Consolidation finding (preliminary):** No Claude↔GPT dedup action required for these four. Internal overlap to resolve is Project 2 vs Project 4 (both Engine 3). Confirm on paste.

### A.4 ⬇ EXACT COPY-PASTE GUIDE FOR ROYAL (claude.ai — I cannot reach it)
For **each** of the 4 projects, in claude.ai:
1. Open **Projects** (left sidebar) → click the project.
2. **Custom instructions:** open the project's **instructions / "Set project instructions"** panel (gear or "Edit" near the project title). **Select-all → copy the entire text** and paste it here labeled `### <Project> — INSTRUCTIONS`.
3. **Knowledge files:** open the **Project knowledge** panel (right side). For each item, paste: **filename + type** (PDF/MD/pasted-text) and, if quick, a 1-line "what it is." Label it `### <Project> — KNOWLEDGE`.
4. **Name + description:** paste the exact project **name** as shown and the short description if set (resolves Flag A-2).
> Do all four in one message if easy; I'll slot each into A.2 and finalize engines/PROJ codes.

---

## §B — CHATGPT MEMORY / CONNECTOR AUDIT (added 06-18)

Account in scope: **royaloconnor@gmail.com** (the Gate 4 export account). Purpose: governance/credibility artifact — show the advisory practitioner runs a clean, documented AI footprint.

### B.1 Saved "memory" entries — ⏳ AWAITING PASTE
Scaffold (one row per memory entry Royal pastes):

| # | Memory entry (verbatim) | Category (business / personal / stale) | Privacy flag | Action (keep / edit / delete) |
|---|---|---|:--:|:--:|
| _ | ⏳ | ⏳ | ⏳ | ⏳ |

> Hypothesis from §12: any "O'Connor Advisory" awareness in ChatGPT most likely came from a **state-file paste or a saved memory**, **NOT** a Drive connection. The memory list confirms or refutes this.

### B.2 Connected connectors / apps — ⏳ AWAITING PASTE
Scaffold (one row per connector):

| # | Connector / app | Scope / permissions | Data exposure | Action |
|---|---|---|:--:|:--:|
| _ | ⏳ | ⏳ | ⏳ | ⏳ |

Also inventory at the **Google Account** layer: myaccount.google.com → Security → **Your connections to third-party apps** → look for any **OpenAI/ChatGPT ↔ Google Drive** grant. Record present/absent + scope.

### B.3 Data-control settings — re-verify Gate 4 finding
| Setting | Gate 4 (06-14) | Now (06-21) | Status |
|---|---|---|:--:|
| `training_allowed` ("Improve the model for everyone" / data-controls) | **false** (export) | ⏳ verify | 🔄 |
| "Reference saved memories" | n/a | ⏳ | 🔄 |
| "Reference chat history" | n/a | ⏳ | 🔄 |

### B.4 Flags
- **Deprecation exposure:** Gate 4 found **ZERO** Assistants API / Agent Builder objects (the positioning advantage, §9). **Re-confirm** no such objects/connectors have appeared since 06-14. Timeline still live: Assistants API 2026-08-26, Agent Builder 2026-11-30.
- **Privacy:** any connector with Drive/Gmail write scope, or memory entries containing client/family PII, gets flagged for removal/redaction (ties to harness rule `pii-sanitize`).

### B.5 ⬇ EXACT COPY-PASTE GUIDE FOR ROYAL (ChatGPT settings — I cannot reach it)
In ChatGPT (royaloconnor@gmail.com):
1. **Memory:** Settings → **Personalization** → **Memory** → **Manage memories**. Copy the full list of saved entries → paste under `### B.1 PASTE`.
2. **Connectors:** Settings → **Connectors** (or **Connected apps**). List each connector + on/off + scope → paste under `### B.2 PASTE`.
3. **Data controls:** Settings → **Data controls** → report the "Improve the model for everyone" toggle (on/off) + "Reference chat history" + "Reference saved memories" states → paste under `### B.3 PASTE`.
4. **Google side:** myaccount.google.com/connections → screenshot/list any OpenAI/ChatGPT entry + its scope.

---

## §C — PROPOSED STATE UPDATES (do NOT apply — Royal merges)

> Provided as diffs for the parallel editor to merge into OCS_STATE_CANONICAL.md after this audit's data is in.

**§3 — Gate 5 status line (proposed change):**
- Current: `| 5 | Claude Projects audit + ChatGPT memory/connector audit (added 06-18) | OPEN |`
- Proposed (interim, this session): **`| 5 | Claude Projects audit + ChatGPT memory/connector audit | OPEN — audit doc V1 scaffolded (DOC_2026-06-21...GATE5-AUDIT_V1); awaiting Royal's claude.ai + ChatGPT paste |`**
- On completion: flip to **`CLOSED`** once A.2 (all 4 projects) and B.1–B.4 are filled and verified.

**§12 — Gate 5 open actions (proposed edits):**
- `[ ] Map Claude Projects …` → **mark in-progress**; add sub-note: *scaffold built, 4/4 awaiting instructions+knowledge paste; Financial Aid Consultant is a NEW project not in 06-14 reconciliation (Flag A-1).*
- `[ ] Cross-reference Claude Projects vs OpenAI GPTs` → **partially done**: no Claude↔GPT overlap among the 4; open item = Project 2 (CRE Broker) vs Project 4 (Technical Expert/REI) internal-overlap check.
- `[ ] ChatGPT memory + connector audit` → **scaffold built (§B)**; awaiting paste of memory list + connector list + data-control re-verify.

**§7 — Project registry (proposed, pending Financial Aid Consultant resolution):**
- Add a PROJ_ code for **Financial Aid Consultant** once engine is assigned (candidate: PROJ_FAM_FINAID or fold into PROJ_EDU_SHSAT cluster).

**§8 — Findings (proposed new):**
- **F16 (proposed):** *Financial Aid Consultant Claude Project undocumented in Gate 5 reconciliation — capture + classify (Flag A-1).*
- Optionally close/keep **F4** (GPT capability toggles) — unrelated to this audit; leave as-is.

---

## WHAT I NEED FROM YOU (to finish Gate 5)

**From claude.ai (one message, all four projects):**
1. **Audit Trainer** — full custom instructions + knowledge file list + exact name/description.
2. **NYC CRE Broker** — same.
3. **Financial Aid Consultant** — same **+ tell me its intended engine** (Family? Engine 2 client-facing? other).
4. **Technical Expert** — same + confirm exact live name (is it "Technical Expert" or "REI Technical Expert"?).

**From ChatGPT settings (royaloconnor@gmail.com):**
5. **Memory list** (Personalization → Memory → Manage memories) — verbatim.
6. **Connector list** (Connectors / Connected apps) — each + scope.
7. **Data controls** — "Improve the model for everyone" on/off (re-verify `training_allowed`), plus "Reference chat history" + "Reference saved memories".
8. **Google connections** — myaccount.google.com/connections — any OpenAI/ChatGPT↔Drive grant (present/absent + scope).

**Decisions I need from you:**
9. Engine + PROJ_ code for **Financial Aid Consultant** (Flag A-1).
10. Confirm **CRE Broker vs Technical Expert** are distinct (no consolidation) once I see both instruction sets.

---

### PROPOSED ONE-LINE GATE 5 STATUS CHANGE FOR §3
> `| 5 | Claude Projects audit + ChatGPT memory/connector audit | OPEN — audit doc V1 scaffolded (DOC_2026-06-21..._GATE5-AUDIT_V1); awaiting claude.ai + ChatGPT paste |`

---
*DOC_2026-06-21_AI_PROJECTS_GATE5-AUDIT_V1.md | OCS Gate 5 | V1 scaffold | does not edit canonical state | mirror to Drive /ROC-OS/05_Projects/ pending | 2026-06-21*
