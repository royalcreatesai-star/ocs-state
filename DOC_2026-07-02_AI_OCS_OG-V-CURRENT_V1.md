# The Royal O'Connor Operating System — V-Current (Canonical)

**Status:** OG **V1.1** (published 2026-07-03) | Base: OG V1.0, frozen 2026-05-31 (see `DOC_2026-07-02_AI_OCS_OG-V1.0-FREEZE-RECORD_V1.md`)
**Location:** /ROC-OS/00_Registry/ — this is the canonical, editable OG going forward
**Change control:** Amendments only via the SPEC_DELTA protocol at `/wrap` — `[SD-NNN] description | disposition (ratify/revert/review) | session`. Ratified deltas batch at gate closures or quarterly review, never per-session (SD-018).
**Next publish target:** OG V1.2, at the next gate closure or quarterly review.

---

## The OG and ROC-OS (SD-006)

The OG is the **meta-layer** — the operating philosophy above ROC-OS. Where ROC-OS is the technical operating system (Data / Ops Visibility / Automation / Intelligence, per SD-004), the OG governs it. Every system decision runs against the OG first, ROC-OS mechanics second.

The **canonical OG artifact** is this Design Spec, not the infographic. The infographic is an illustration; this document is the specification.

---

## Northstar Filter *(Constitutional — V1.0 phrasing canonical, per SD-021)*

> "Building a five-engine income architecture — W2 transition, consulting, real estate, AI-native products, and AI-augmented investing — that makes the W2 optional, grows generational wealth, funds my family's future, and creates something my kids can watch being built and learn from in real time."

Every idea, session, and decision runs through one question:
**Does this make the W2 optional faster — or not?**

*Downstream paraphrases (working-memory files, session artifacts) are shorthand only; V1.0 phrasing above is the canonical filter (SD-021).*

---

## The Four Layers *(Living article — additive reframe per SD-004)*

Two views, both canonical. V1.0's Four Layers describe **where things live**; the ROC-OS operational stack describes **what each tool does**.

### View A — V1.0 Four Layers (where)

**Layer 1 — Northstar (Claude.ai Blueprint Project).** Strategic thinking, vision refinement. This is where you *think*. No execution happens here.

**Layer 2 — Identity + Principles (`~/.claude/CLAUDE.md`).** Who you are, how you work, filters — loaded into every Claude Code session. Global scope. Subject to the 600-token authoring constraint (SD-014).

**Layer 3 — Execution System (`~/blueprint/` living files).** Where ideas land, get triaged, decided, tracked. Files: `ideas.md`, `decisions.md`, `processes.md`, `projects.md`, `northstar.md`.

**Layer 4 — Operational Layer (Notion).** Where humans read and act. Notion Command Center + Session Log + project pages. Not client-facing.

### View B — ROC-OS Operational Stack (what)

| Layer | Tool | Role |
|-------|------|------|
| Data | Google Drive (royalcreates.ai@gmail.com) — the "Hallway" | Canonical file storage |
| Ops Visibility | Notion (royalcreates.ai workspace) | Where humans see state and act |
| Automation | n8n (Docker, local) | Automation backbone — "workflows are controls, agents are staff" (SD-005) |
| Intelligence | Claude (Chat + Cowork + Code) | Reasoning, build, analysis |

Both views coexist. View A describes the OG's conceptual layering; View B describes the running system.

---

## Filing Root (SD-007)

Canonical Drive taxonomy, mirrored in the git state repo:

```
/ROC-OS/
  00_Registry/       — canonical state, OG, PRUNE_QUEUE, freeze records
  01_Intelligence/   — GPT docs, intelligence assets
  02_Automation/     — n8n workflow exports
  03_Data/           — REI and data assets
  04_Domain/         — domain protocols, prompts, skills, controls
  05_Projects/       — project folders
  99_Archive/        — archived artifacts
```

---

## Naming Conventions (SD-008, SD-009)

**Files:** `{TYPE}_{DATE}_{DOMAIN}_{CATEGORY}_{DESCRIPTION}_{VERSION}`
- TYPE: DOC, IMG, VOICE, PDF, WORKPAPER, RECEIPT, TEMPLATE
- DATE: YYYY-MM-DD
- DOMAIN: HOME, BUSINESS, HEALTH, EDUCATION, AI, PROJECTS, ADVISORY, OCS, PROTOCOL

**Sessions:** `{STATUS}_{DATE}_{DOMAIN}_{CATEGORY}_{DESCRIPTION}`
- STATUS: `IN_PROGRESS` or `CLOSE`
- Underscore-delimited, no pipes or special characters.
- Claude proposes name and status when shape is clear; Royal confirms.

**Codename:** OCS / ROC-OS (SD-016). The prior "OAIS / O'Connor AI System" was retired 2026-06-19.

---

## The Idea Flow

Every idea — regardless of source — moves through the same sequence:

```
CAPTURE
 Source: voice note / written / chat / old laptop / random thought
 Action: Land in ideas.md with date and source tag
 ↓
TRIAGE (Northstar Lens — 3 questions)
 1. Which engine does this serve? (1–5, or none)
 2. What's the unlock? (revenue / friction removed / capability built)
 3. Flush or build?
 ↓
 ├── FLUSH   → noted, archived, done — no further energy
 ├── ITERATE → explore before deciding — no build commitment yet
 └── BUILD   → moves to projects.md
                  ↓
              SCOPE GATE
              "Does this need to be a product?"
              "To what degree?"
                  ↓
        ┌─────────────────────────┐
        │ Full product            │
        │ Lightweight tool        │
        │ Internal process        │
        │ One-time task           │
        └─────────────────────────┘
```

**Key principle:** Nothing moves to BUILD without passing through ITERATE first.
Flushing is not failure — it is discipline.

---

## The Process Library

Proven methods available on demand. Pull the right process for the situation.
New processes get added as discovered. The library compounds over time.

### PROCESS: Session Open (`/start`)
**When:** Beginning of any meaningful work session
**Steps:**
1. Load identity and Northstar from `~/.claude/CLAUDE.md`
2. Check `projects.md` — what is active, what is the priority
3. Check `ideas.md` — anything pending triage
4. Read OG V-Current at `/ROC-OS/00_Registry/`; check session's approach against the Process Library and Stability Gradient
5. Set session intent — what are we actually doing today?
6. Confirm which engine this session serves

### PROCESS: Session Close (`/wrap`) *(supersedes V1.0's `/update`, per SD-010)*
**When:** End of any meaningful work session
**Variants:**
- `/wrap checkpoint` — mid-session pause; appends timestamped entry to Notion ROC Session Log; keeps Status Open
- `/wrap close` — terminal exit; finalizes row; writes Next Starter to Drive `/04_Domain/{project}/PROMPTS.md`
**Steps:**
1. Log any decisions made → `decisions.md`
2. Capture any new ideas → `ideas.md`
3. Update project status → `projects.md`
4. Log any SPEC_DELTAs into Amendment Log candidate list (batching per SD-018)
5. Log any PRUNE_QUEUE entries (see PRUNE_QUEUE process)
6. Answer the closing question: *"What do I know now that I didn't before — and how does it change what I build next?"*

### PROCESS: Idea Triage
**When:** Any new idea surfaces — structured or unstructured
**Trigger:** `ideas.md` has uncategorized entries
**Output:** Each idea marked: FLUSH / ITERATE / BUILD + engine tag

### PROCESS: Northstar Check
**When:** Any time a decision feels hard or priorities conflict
**One question:** "Does this make the W2 optional faster — or not?"
**If unclear:** Run it against the architecture rules before deciding

### PROCESS: Explore → Plan → Approve → Code → Commit *(renamed per SD-020)*
**When:** Any build session with meaningful scope
**Steps:**
1. **Explore** codebase / context
2. **Plan** the change
3. **Approve** the plan (decision-commit; V1.0's original approval gate) — no code before this
4. **Code** the change
5. **Commit** to source control
**Rule:** Never code before the plan is approved.

### PROCESS: Brainstorm → Spec → Plan → Build
**When:** New feature or product idea with real uncertainty
**Steps:** `/brainstorm` → design doc → `/writing-plans` → implementation
**Rule:** Hard gate between spec and build — no building unspecced work

### PROCESS: Iterate Before Build
**When:** New idea in ITERATE status
**Steps:** Define the question → explore approaches → assess necessity → scope if needed
**Rule:** "Do we actually need to build this?" must be answered before scope

### PROCESS: Verify-Before-Status (VBS) *(new, per SD-011)*
**When:** Any status change on a deliverable or engagement artifact
**Steps:** Compare the artifact to its evidence; confirm the status claim matches; record verification; only then update status.
**Rule:** No status claim without evidence check. Applies especially at the Assessment self-review gate and Build reviewer step in Migration Sprint delivery.
**Reference:** `/04_Domain/DOC_AI_HARNESS_Controls/DOC_2026-06-19_AI_HARNESS_VERIFY-BEFORE-STATUS-CONTROL_V1.md`

### PROCESS: PRUNE_QUEUE *(new, per SD-012)*
**When:** Any session identifies a file that is superseded, duplicated, misfiled, or needs review
**Surface routing:** Chat writes to Notion ROC Session Log "Prune Queue" field (intermediate buffer). Code executes against Drive (master of record).
**Disposition enum:**
- `archive` — move to `/ROC-OS/00_Registry/archive/`, rename with `_ARCHIVED_{date}` suffix
- `trash` — Drive trash (recoverable 30 days). Script flags; human confirms. Never auto-trash on first run.
- `review` — human decision required
- `null` — no prior file to act on; entry exists for legacy scan
**Audit status enum:** pending / flagged / completed / skipped
**Reference:** `/ROC-OS/00_Registry/PRUNE_QUEUE.md`

---

## Session Routing Rules

### V1.0 Session Routing *(canonical, retained)*

| Session type | Start here |
|---|---|
| Pure strategic thinking, vision, big picture | Claude.ai — Blueprint project |
| Any idea that might become something real | Claude Code — `/start` |
| Building, executing, integrating tools | Claude Code — project directory |
| Querying saved knowledge / research | Claude Code — NotebookLM skill |
| Quick capture with no immediate intent | Voice note or written → lands in `ideas.md` next session |

**Default rule:** When in doubt, start in Claude Code.
Ideas are not scarce. Execution context is.

### Three Surfaces *(additive per SD-019 — operational reality on top of V1.0)*

| Surface | Role |
|---|---|
| **Chat** (Claude.ai) | Digest cockpit — session open, quick reasoning, /wrap authoring, conversational triage |
| **Cowork** | Multi-step build surface — file work, artifact creation, connector-heavy sessions |
| **Code** (Claude Code) | Execution — direct file writes to the repo, harness runs, commit-level work |

The three-surface view names how work actually flows today; the V1.0 routing above remains the routing table of record.

---

## The Five Engines (Decision Filter) *(two-axis per SD-022)*

**Character axis (Constitutional, from V1.0):** Active / Passive / Scalable / Capital Growth — intrinsic to the engine, does not change.

**Status axis (Living, operational):** Not Started / In-Progress / Active / Closed — reflects operational state; maintained in State V7.5 and updated as engines transition.

| Engine | Character | Status *(proposed 2026-07-03; Royal to confirm/adjust in State V7.5)* | Role in decisions |
|---|---|---|---|
| 1 — W2 Income | Active | Active | Funds everything. Protect the runway. |
| 2 — O'Connor Advisory | Active | In-Progress | First priority for new work and tools; transitions to Active on first paid engagement |
| 3 — Real Estate | Passive | Active | Data-driven decisions only. Run numbers first. |
| 4 — AI-Native Product | Scalable | In-Progress | Only after consulting proves itself |
| 5 — Trading & Investing | Capital Growth | In-Progress | Capital from Engines 2+3 only |

**Architecture rules (non-negotiable, Constitutional):**
- Consulting proves itself before product gets priority
- Real estate capital decisions require data — run the analysis first
- Trading capital comes only from Engine 2 and 3 cash flow
- Every decision gets measured against the Northstar
- The W2 is a runway, not a destination

**Scope clarification (SD-013):** Personal / Family work (children's projects, family game concept, family sports coordination) is **NOT** an Engine. Engine set is exactly the Five above. Family agents in the Agent Registry are Engine-unset by design.

---

## The Edge Discipline

> "The tools are available to everyone. The moat is built from judgment compounding, trusted relationships, proprietary systems refined through real client work, and an integrated five-engine vision that no single-problem solver can replicate. We sharpen this edge deliberately in every session. We never confuse access to tools with ownership of capability."

**Sharpening practice:** End every Blueprint session with:
*"What do I know now that I didn't know before — and how does it change what I build next?"*

---

## The Agentic Maturity Model *(SD-015)*

Universal governance scorecard for OCS growth. Levels A–E:

- **A** — General LLM chat
- **B** — Structured prompting
- **C** — Persistent context
- **D** — Agentic integration
- **E** — Autonomous governance

**Living record.** The Model carries a Growth Ledger — dated advances that materially advanced OCS maturity. Update the Ledger every meaningful session that adds governance, foundation, or agentic capability. This is the honest counter-signal to the "mirage of stagnation" that governance work can create.

Canonical location: Audit Group Framework build (June 24 HTML deliverable). Applies universally (audit group, OCS/personal, firm-scale).

---

## Stability Gradient *(SD-002 mechanism, SD-017 formal designation)*

The OG has two tiers with different bars for change:

### Constitutional core — near-prohibitive bar to change
- **Northstar Filter** (SD-021: V1.0 phrasing canonical)
- **Five Engines — Character** (Active / Passive / Scalable / Capital Growth per SD-022)
- **Five Engines — Architecture rules** (four non-negotiables above)
- **Tony Wray five-sources foundation** (dedication + philosophical grounding)

### Living articles — standard change control via V-Current + SPEC_DELTA
- Four Layers implementation (Views A + B)
- Filing root taxonomy
- Naming conventions (file + session)
- Process Library
- Session Routing (V1.0 table + three-surface addition)
- Five Engines — Status axis
- Edge Discipline mechanics
- Authoring constraints (600-token rule)
- Codename
- Agentic Maturity Model implementation
- Amendment batching rule

### Amendment Batching Rule *(SD-018)*
Ratified deltas batch at **gate closures or quarterly review**, never per-session. This prevents amendment thrash and enforces the OG as a slow-moving governing document.

---

## Authoring Constraints

**600-token rule (SD-014):** `CLAUDE.md` and skill files stay under 600 tokens each. Applies at Layer 2. Rationale: quadratic token tax on context load; loose files silently degrade every session.

---

## What Gets Built (Implementation Sequence)

1. `~/.claude/CLAUDE.md` — personal identity file, globally scoped
2. `~/blueprint/northstar.md` — authoritative Blueprint living copy
3. `~/blueprint/ideas.md` — idea capture and triage log
4. `~/blueprint/decisions.md` — decision log
5. `~/blueprint/processes.md` — process library reference
6. `~/blueprint/projects.md` — active project registry
7. Visual infographic — system flow diagram for reference

---

## Success Criteria

- Every Claude Code session loads Royal's context before a word is typed
- No idea gets lost — everything lands somewhere and gets triaged
- No project starts without passing through the scope gate
- Process library is consulted deliberately, not rediscovered each session
- Blueprint project in Chat and Claude Code execution layer stay in sync
- Six months from now: sessions feel like continuing a conversation, not rebooting one

---
*Dedicated to Mr. Anthony "Tony" Wray — "Tru Word"*
*"Five sources of income." Every engine in this Blueprint is a Tru Word kept.*

---

## Amendment Log

| # | Date | Change | Reason | Session |
|---|------|--------|--------|---------|
| SD-001 | 2026-07-02 | SPEC_DELTA capture adopted into /wrap | Gives the OG a formal, low-overhead change-control mechanism instead of ad hoc edits | 2026-07-02 Chat (Thread 0) |
| SD-002 | 2026-07-02 | OG versioning model: V1.0 freeze + living V-current | Separates the immutable founding charter from ongoing evolution so the charter can't silently drift | 2026-07-02 Chat (Thread 0) |
| SD-003 | 2026-07-02 | Reconciliation folded into Thread 0 closing phase | Keeps OG canonicalization and post-May-31 convention reconciliation in one motion instead of a separate thread | 2026-07-02 Chat (Thread 0) |
| SD-004 | 2026-07-03 | Four-layer stack reframed as Data (Drive) / Ops Visibility (Notion) / Automation (n8n) / Intelligence (Claude), presented additively alongside V1.0's Four Layers | Both views are useful; the operational stack names what the system runs on today | 2026-07-03 Cowork (Thread 0 Phase 4) |
| SD-005 | 2026-07-03 | n8n named as automation backbone ("workflows are controls, agents are staff") | V1.0 was silent on automation; the system depends on a workflow layer | 2026-07-03 Cowork |
| SD-006 | 2026-07-03 | OG designated meta-layer above ROC-OS; Design Spec = canonical OG artifact (not infographic) | Prevents future confusion between visual rendering and the governing document | 2026-07-03 Cowork |
| SD-007 | 2026-07-03 | Filing root taxonomy `/ROC-OS/{00_Registry, 01_Intelligence, 02_Automation, 03_Data, 04_Domain, 05_Projects}` | Locks the proven taxonomy into the OG; closes "where does this go" at write time | 2026-07-03 Cowork |
| SD-008 | 2026-07-03 | File naming convention `{TYPE}_{DATE}_{DOMAIN}_{CATEGORY}_{DESCRIPTION}_{VERSION}` | Ratifies the universal pattern rather than leaving it as informal habit | 2026-07-03 Cowork |
| SD-009 | 2026-07-03 | Session naming convention `{STATUS}_{DATE}_{DOMAIN}_{CATEGORY}_{DESCRIPTION}` (STATUS = IN_PROGRESS or CLOSE) | Ratifies the 2026-06-28 standard for session artifacts | 2026-07-03 Cowork |
| SD-010 | 2026-07-03 | `/wrap` (checkpoint + close variants) supersedes `/update` as session-close trigger | `/wrap` is surface-agnostic; `/update` was Chat-specific in V1.0 | 2026-07-03 Cowork |
| SD-011 | 2026-07-03 | Verify-Before-Status (VBS) added to Process Library | Load-bearing for the Assessment self-review gate; belongs in the OG process library | 2026-07-03 Cowork |
| SD-012 | 2026-07-03 | PRUNE_QUEUE governance protocol added to Process Library (disposition enum archive/trash/review/null; audit_status enum) | Formalizes file hygiene and prevents legacy-tree drift; Chat writes to Notion buffer, Code executes | 2026-07-03 Cowork |
| SD-013 | 2026-07-03 | Personal/Family scope clarified as NOT-an-Engine (does not alter the Five Engines) | Prevents scope creep; Family agents in Agent Registry are Engine-unset by design | 2026-07-03 Cowork |
| SD-014 | 2026-07-03 | 600-token rule for CLAUDE.md and skill files | Quadratic token tax rule; live since foundation lock; belongs in OG as authoring constraint on Layer 2 | 2026-07-03 Cowork |
| SD-015 | 2026-07-03 | Agentic Maturity Model (Levels A–E) elevated to universal OCS growth scorecard, with Growth Ledger updated per material advance | Governance work is real progress; counter-signal to "mirage of stagnation" | 2026-07-03 Cowork |
| SD-016 | 2026-07-03 | Codename standard: OCS / ROC-OS (OAIS retired 2026-06-19) | Aligns OG vocabulary with the rest of the system | 2026-07-03 Cowork |
| SD-017 | 2026-07-03 | Stability gradient formally adopted: Constitutional core (near-prohibitive bar) vs Living articles (standard SPEC_DELTA) | Companion to SD-002 — SD-002 said *how*, SD-017 names *what* is protected at which tier | 2026-07-03 Cowork |
| SD-018 | 2026-07-03 | Amendment batching rule: ratified deltas batch at gate closures or quarterly review, never per-session | Prevents amendment thrash; enforces the OG as a slow-moving governing document | 2026-07-03 Cowork |
| SD-019 | 2026-07-03 | Three surfaces named alongside V1.0 Session Routing (additive, not superseding): Chat = digest cockpit, Cowork = multi-step build, Code = execution. V1.0's Claude.ai / Claude Code routing remains canonical. | Names the operational reality without retiring V1.0 constructs | 2026-07-03 Cowork |
| SD-020 | 2026-07-03 | Process Library method renamed: Explore → Plan → Approve → Code → Commit (5 phases). "Approve" = decision-commit (V1.0's plan-approval gate); "Commit" = git commit. | Resolves terminology overload in V1.0 phrasing without changing intent | 2026-07-03 Cowork |
| SD-021 | 2026-07-03 | Clarifying note: OG V1.0 Northstar Filter phrasing remains canonical. Downstream paraphrases are working-memory shorthand, not redefinitions. | Prevents paraphrase-drift on Constitutional core without substantively amending it | 2026-07-03 Cowork |
| SD-022 | 2026-07-03 | Five Engines table split into two axes. Character (intrinsic; Constitutional): Active / Passive / Scalable / Capital Growth. Status (operational; Living): Not Started / In-Progress / Active / Closed. | Restores V1.0's phasing signal that had been flattened, without editing the Constitutional Five Engines | 2026-07-03 Cowork |

*OG V1.0 → V1.1 published 2026-07-03 via Thread 0 Phase 4 (Reconcile) closure. Next amendment batch targets OG V1.2 at the next gate closure or quarterly review (per SD-018).*
