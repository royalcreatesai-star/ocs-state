# The Royal O'Connor Operating System — V-Current (Canonical)

**Status:** OG **V1.2** (published 2026-07-11) | Base: OG V1.1 (2026-07-03) → V1.0, frozen 2026-05-31 (see `DOC_2026-07-02_AI_OCS_OG-V1.0-FREEZE-RECORD_V1.md`)
**Location:** git repo `ocs-state` — **source of truth (SD-039)**; Drive `/ROC-OS/00_Registry/` is the mirror. Git history is the OG's version lineage (V1.1 → V1.2 → …).
**Change control:** Amendments only via the SPEC_DELTA protocol at `/wrap` — `[SD-NNN] description | disposition (ratify/revert/review) | session`. Ratified deltas batch at gate closures or quarterly review, never per-session (SD-018). Disposition is two-state (SD-038): *proposed-at-capture* (author's intent when logged) vs *current-batch-disposition* (authoritative, assigned at the batch).
**Next publish target:** OG V1.3, at the next gate closure or quarterly review.

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

**Layer 3 — Execution System (`~/blueprint/` living files).** Files: `ideas.md`, `decisions.md`, `processes.md`, `projects.md`, `northstar.md`. *Retained-but-demoted (SD-036): `ideas.md` / `projects.md` are Code-surface working context loaded per session, NOT canonical destinations — canonical capture = Gmail `ROC-OS Intake` label (SD-025), canonical build state = Notion Initiative Registry (SD-026). `northstar.md` + `decisions.md` remain canonical.*

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
  00_Inbox/          — intake staging (Drive-side; parallel to the ROC-OS Intake Gmail label per SD-025) — SD-037
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

## The Idea Flow *(V3 — rewritten per SD-025–029; replaces the V1.1 flow and PROCESS: Idea Triage)*

Every item — regardless of source — moves through the same seven-step sequence:

```
CAPTURE SWEEP  → read Gmail "ROC-OS Intake" AND NOT "ROC-OS Intake/Processed"; inventory only
RESOLVE        → get each item to discussable text (fetch / transcribe-flag / paste-flag)
CLASSIFY       → TYPE (Reference→bucket+score, bypasses Flush/Iterate/Build | Idea→Northstar Lens)
                 BUCKET (topic, not engine) · RELEVANCE (anchor = 6 active initiatives)
TRIAGE         → Northstar Lens (engine? / unlock? / Flush-Iterate-Build?) — idea-candidates only
ROUTE          → FLUSH (log, done) | ITERATE (hold, note the one open question) | BUILD (→ Scope Gate)
SCOPE GATE     → Full product / Lightweight tool / Internal process / One-time task
LAND           → BUILD→Notion Initiative Registry · REFERENCE→Notion Reference Library DB
                 (authoritative→NotebookLM) · ALL→add "ROC-OS Intake/Processed" (keep Intake for provenance)
```

**Key principle:** Nothing reaches BUILD without passing ITERATE first. Flushing is discipline, not failure.
**Guardrail:** LAND is the flow's only side-effect gate — nothing writes before it; NotebookLM adds are a manual human-curation gate (no consumer API).
**Flow-step tagging (SD-029):** each step carries `[provenance · action-class]`; the action-class pre-marks automation gates before any trigger is wired.

**Surfaces (target-state where noted):** CAPTURE = Gmail `ROC-OS Intake` label; mark-done = `ROC-OS Intake/Processed` (`Label_4981583307976649244`), Intake = `Label_448698645156134993` (SD-025). BUILD → Notion Initiative Registry (SD-026). REFERENCE → Notion Reference Library DB — *target-state, not yet built* (SD-027). Authoritative sources → NotebookLM — *target-state* (SD-028). Ingestion rule (SD-023): third-party/marketing content is parsed for substance, hype discarded; video requires a local file for `transcribe.sh`.

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
2. Capture any new ideas → `ideas.md` *(working-context write; canonical capture = Gmail `ROC-OS Intake` label per SD-025)*
3. Update project status → `projects.md` *(working-context write; canonical build state = Notion Initiative Registry per SD-026)*
4. Log any SPEC_DELTAs into Amendment Log candidate list (batching per SD-018)
5. Log any PRUNE_QUEUE entries (see PRUNE_QUEUE process)
6. Answer the closing question: *"What do I know now that I didn't before — and how does it change what I build next?"*

### PROCESS: Idea Triage *(folded into The Idea Flow V3, per SD-025–029)*
**Superseded:** the standalone triage step is now the CLASSIFY → TRIAGE → ROUTE stages of the Idea Flow V3 (see above). Retained as a named pointer; no separate procedure.

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

### Four-Lane AI Segregation of Duties *(SD-033 — amends SD-019; three surfaces → four lanes, write-authority made explicit)*

The operating reality is a **four-lane authority model** — the **ChatGPT Checker** lane exists in operation but appeared nowhere in V1.1 canon. Write-authority is now explicit per lane.

| Lane | Surface / model | Role | In-place Drive master edit | Repo commit | New-file create/copy | External-system writes |
|---|---|---|---|---|---|---|
| **Maker** | Claude **Code** | Sole writer; harness runs, execution | ✅ yes (sole) | ✅ yes (sole) | ✅ | scoped, path-guarded |
| **Orchestrator** | Claude **Chat** | Session open, reasoning, /wrap authoring, drafts, digests | ❌ read-only | ❌ | ❌ (drafts to outputs, routes to Code) | Notion Session Log writes only (SD-012) |
| **Checker** | **ChatGPT** | Specialist / second-opinion review | ❌ read-only | ❌ | ❌ | none (no write path) |
| **Background** | **CoWork** | Multi-step background tasks; mirror fallback | ❌ no in-place master edits | ❌ | ✅ create/copy only | fallback Drive mirror when mount unavailable |

**Cross-cites:** **SD-019** (superseded-and-extended — three surfaces → four lanes, ChatGPT named; V1.0 Session Routing remains the routing table of record) · **Decision #8 / State §5b** (the *human* SoD — Royal owns Domain + controls, engineer owns Automation + Data — a distinct axis; the two segregation models cross-reference, they do not collapse) · **SD-030** (the Notion-lane visibility-only discipline is a corollary of this model).

**`[PENDING Fable 5 Approach 2 — seed committed; do NOT fabricate]`** the full §F positive/negative rights-matrix reconciliation, the **five failure modes + escalation paths**, and the SD-019 amendment mechanics are the Approach-2 deliverable and fold in as a follow-up (stays within V1.2). This SD-033 (the four lanes + cross-cites above) is the ratification-candidate seed and ratifies the already-operating model.

---

## The Five Engines (Decision Filter) *(two-axis per SD-022)*

**Character axis (Constitutional, from V1.0):** Active / Passive / Scalable / Capital Growth — intrinsic to the engine, does not change.

**Status axis (Living, operational):** Not Started / In-Progress / Active / Closed — reflects operational state; synced to State V7.8 (2026-07-06) and updated as engines transition (SD-035).

| Engine | Character | Status *(synced to State V7.8, 2026-07-11 per SD-035)* | Role in decisions |
|---|---|---|---|
| 1 — W2 Income | Active | Active | Funds everything. Protect the runway. |
| 2 — O'Connor Advisory | Active | Active | First priority for new work and tools. *Status = Active = operationally delivering-capable; a separate first-revenue-closed milestone flag (still open, gated on F11 E&O) tracks the revenue event.* |
| 3 — Real Estate | Passive | Active | Data-driven decisions only. Run numbers first. |
| 4 — AI-Native Product | Scalable | Active | Only after consulting proves itself |
| 5 — Trading & Investing | Capital Growth | Active | Capital from Engines 2+3 only |

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

Canonical location: OCS-local Maturity Model artifact in `/ROC-OS/00_Registry/` (SD-015′). The Audit Group Framework HTML (June 24 deliverable) is a *derived instance*, not canon — this removes OCS governance canon from an employer-adjacent artifact. Scoring uses a single A–E scale with a stated **A–E ↔ numeric** mapping (resolves the "2.5 of 4" vs "3.2/5" vs A–E fragmentation); State §1 is fixed in the same V7.9 pass. Applies universally (audit group, OCS/personal, firm-scale).

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
- Session Routing (V1.0 table + four-lane AI SoD, SD-033)
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

**OCS vocabulary reference-tags (SD-031):** §-references, gate IDs, and PQ IDs carry their canonical reference tag so opaque references stay legible across surfaces. Companion to SD-014.

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
| SD-023 | 2026-07-11 (batch) | Ingestion standing rule: parse third-party content for substance; video → local file for `transcribe.sh` | Fold running-system intake rule into canon | V1.2 batch |
| SD-024 | 2026-07-11 (batch) | Automation-cost principle (scheduling for unattended jobs only) ratified | Cost discipline on automation; cadence on-demand until volume warrants | V1.2 batch |
| SD-025 | 2026-07-11 (batch) | Idea Flow CAPTURE surface = Gmail label `ROC-OS Intake`; mark-done `ROC-OS Intake/Processed` (`Label_4981583307976649244`) | Replaces `ideas.md` capture with the live Gmail intake | V1.2 batch |
| SD-026 | 2026-07-11 (batch) | Idea Flow BUILD routes to Notion Initiative Registry (not `projects.md`) | Registry is the live build destination; Layer-3 demoted (SD-036) | V1.2 batch |
| SD-027 | 2026-07-11 (batch) | CLASSIFY layer; reference bypasses Flush/Iterate/Build → Reference Library DB (target-state) | Reference assets need a destination distinct from builds | V1.2 batch |
| SD-028 | 2026-07-11 (batch) | NotebookLM authoritative-source tier; three-tier destination model (target-state) | Grounded per-initiative corpus for authoritative sources | V1.2 batch |
| SD-029 | 2026-07-11 (batch) | Flow-step tagging `[provenance · action-class]` | Pre-marks automation gates before triggers are wired | V1.2 batch |
| SD-030 | 2026-07-11 (batch) | Notion Plus posture: Drive-first / Notion-eyeball; no query-tool reach | Notion is visibility-only; Business-plan upgrade declined | V1.2 batch |
| SD-031 | 2026-07-11 (batch) | OCS vocabulary reference-tag convention (§/gates/PQ IDs) → Authoring Constraints | Companion to SD-014; keeps opaque refs legible | V1.2 batch |
| SD-032 | — | **REDIRECTED to State** (Thread 5 cleanup status — not an OG amendment) | Project-status records live in State §5d, not the OG | V1.2 batch (redirect logged) |
| SD-033 | 2026-07-11 (batch) | Four-lane AI SoD (Maker/Orchestrator/Checker/Background); amends SD-019; cross-cites Decision #8 | Load-bearing write-authority model was operating without canon; ChatGPT lane absent from SD-019 | V1.2 batch |
| SD-034 | 2026-07-11 (batch) | Agentic sequencing constraint: no G-gap hard-gated on Gate 7; G7 Aug-26-anchored via Migration Sprint | Constraint contradicted by executed G3/G8 | V1.2 batch |
| SD-035 | 2026-07-11 (batch) | Five Engines Status axis synced to State V7.8 (E2/E4/E5 → Active); E2 two-axis note + first-revenue milestone flag | OG body table stale vs confirmed Status | V1.2 batch |
| SD-036 | 2026-07-11 (batch) | Layer 3 retained-but-demoted (Code-surface context, not canonical); /wrap steps 1–3 updated | Consequence of SD-025/026 rerouting | V1.2 batch |
| SD-037 | 2026-07-11 (batch) | Filing root adds `00_Inbox` (Drive-side intake, parallel to Gmail label) | Live folder was absent from SD-007 taxonomy | V1.2 batch |
| SD-038 | 2026-07-11 (batch) | SPEC_DELTA disposition semantics: proposed-at-capture vs current-batch-disposition | Resolves Session-Log/pending-table disposition mismatch | V1.2 batch |
| SD-015′ | 2026-07-11 (batch) | Maturity Model canonical location → `/00_Registry` (OCS-local); Audit HTML becomes derived | Removes OCS canon from employer-adjacent artifact | V1.2 batch |
| SD-039 | 2026-07-11 (batch) | OG governance doc enters `ocs-state` git repo as SoT; Drive mount = mirror | Closes F15 cross-runtime boundary; "git = SoT" now holds for governance, not just State | V1.2 batch |

*OG V1.1 → V1.2 published 2026-07-11 (SD-018 quarterly-review batch, Q3; session `CLOSE_2026-07-11_AI_PROJECTS_OCS_CoherenceReview-Adjudication`). Applied to the git repo by the Maker (Code) lane per SD-039. Next amendment batch targets OG V1.3 at the next gate closure or quarterly review (per SD-018).*
*Note (SD-033): the four-lane SoD is committed as the ratification-candidate seed; the full positive/negative rights matrix + five failure-mode escalation paths are `[PENDING Fable 5 Approach 2]` and fold in as a follow-up within V1.2.*
