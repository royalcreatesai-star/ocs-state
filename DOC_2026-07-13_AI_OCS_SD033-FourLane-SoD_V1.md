# SD-033 — Four-Lane AI Segregation of Duties [LD-#16] (amends SD-019)

**Status:** RATIFIED — adjudicated 2026-07-12 by Royal O'Connor; landed by the Maker (Code) lane; batches into **OG V1.3** per SD-018.
**Location:** git repo `ocs-state` — **source of truth (SD-039)**; Drive `/ROC-OS/00_Registry/` is the mirror.
**Lineage:** ratification candidate (Fable 5 one-shot, 2026-07-12, `DOC_2026-07-12_AI_PROJECTS_OCS_SD033-RatificationPackage_V1.md`) → Final Adjudicated (Orchestrator draft, propose-only, `DOC_2026-07-12_AI_PROJECTS_OCS_SD033-Final-Adjudicated_V1.md`) → this canonical artifact (Maker-verified and landed).
**Relation to the OG:** the SD-033 seed published in OG V1.2 (2026-07-11); this artifact is the completed `[PENDING Fable 5 Approach 2]` detail. The OG Session Routing section carries the summary; this document carries the full rights matrix and escalation paths.

---

## 0. ADJUDICATION RECORD — the eight rulings

| # | Open item | Ruling | Change applied |
|---|---|---|---|
| 1 | Batching (reframe) | Carry completed detail to **V1.3**, honor SD-018 strictly | Completion of the pending seed; batches into OG V1.3, not a post-publish edit to V1.2 |
| 2 | FM-4 SD-039 mis-cite (blocking) | **Reground on State §11**; SD-039 was a fabricated cross-ref | SD-039 removed from cross-cites, FM-4 row, and dependency register; FM-4 ground = State §11 + 06-28 hardening pass; 07-07 `settings.local.json` = illustrative incident |
| 3 | FM-1 "07-07 cleanup" ground | Unsubstantiated as a phantom-close event; **reground on SD-011/VBS** | FM-1 ground = SD-011 / Verify-Before-Status; illustrative incident = 07-03 V7.6 fork (real) |
| 4 | Handoff carve-out (B.1 ¹) | **Option (b)** — reroute; Chat drafts, Code lands | Orchestrator Drive-text/create rights = — (unconditional); OG `/wrap close` process text corrected (§F) |
| 5 | Session Log append (B.1 ²) | Confirm as written | Every lane **except Checker** appends its own row; Checker logged by commissioning Orchestrator |
| 6 | FM-4 enforcement follow-on | **Park** to 2026-10-12 as a checkpoint | Cross-linked to existing §12 Harness Security Gate + R2 Review Sprint; no duplicate charter — real trigger is client data |
| 7 | Two parked mode candidates | Confirm parked → **confirm-and-close** at 10-12 | Notion-as-datastore already remediated 06-28; attribution gap handled by §D Last-Run discipline; FM set stays capped at 5 |
| 8 | Assumptions B.3 / C.1 | Both **confirmed** | B.3 upgraded assumption→canonical (F15 06-28 update); C.1 confirmed — both Decision #8 axes resolve to Royal today |

---

## A. SD-033 CANONICAL TEXT

### A.1 Amendment Log entry (as it reads in the OG V1.3 Amendment Log)

> **SD-033 (detail completed 2026-07-12; carries to V1.3 batch) — Four-Lane AI Segregation of Duties [LD-#16]. Amends SD-019.** Completes the `[PENDING Fable 5 Approach 2]` detail on the SD-033 seed published in OG V1.2 (2026-07-11): the four-lane authority model (Maker / Orchestrator / Checker / Background), the positive/negative rights matrix (§B), the five failure-mode escalation paths **FM-1…FM-5** (capped at five; quarterly review 2026-10-12), and the SD-019 amendment mechanics (§A.3). Governing principle: technical capability and granted right have come apart — connectors on Chat and ChatGPT can both write Drive and Notion; the SoD withholds rights the tools technically hold. Cross-cites: **SD-019** (extended, not replaced), **SD-030** (Notion visibility-only corollary), **State §5b Decision #8** (human work-split — a distinct segregation axis, mapped not merged), **F15** (CoWork sandbox off the repo; grounds B.3), **F23** (Checker read-only posture). Living-article change per the Stability Gradient; batched into OG V1.3 per SD-018.

### A.2 The Four-Lane table (extends the SD-019 three-surface table; SD-019's log entry stands)

**Four Lanes (authority model of record):**

| Lane | Surface | Role | Authority summary |
|---|---|---|---|
| **Maker** | Claude Code | Execution — sole canonical writer | Sole in-place Drive master edits and git commits; harness runs; PRUNE_QUEUE merge/execute; the only lane whose output *closes* status |
| **Orchestrator** | Claude Chat | Digest cockpit — session open, reasoning, /wrap authoring, triage | Propose-only on canon and governance; Notion writes limited to ops visibility + own Session Log row; Drive-text write right withheld despite connector capability |
| **Checker** | ChatGPT | Specialist / second-opinion review | Read-only on Drive and Notion; no write path anywhere; findings enter as Proposals only, via the Orchestrator |
| **Background** | CoWork | Staging / multi-step build | Drive create/copy only; no in-place master edits; no repo reach (F15); stages, never commits |

**Governing principle:** *The rights matrix (§B) records rights, not capabilities. A cell marked "(cap. withheld)" means the lane's connector can perform the write and the SoD forbids it. The failure modes (§C) are what happens when capability leaks back into right.*

**Cross-cite block:** SD-019 (amended) · SD-030 (Notion visibility corollary — bounds Orchestrator Notion-W) · State §5b Decision #8 (human SoD, distinct axis) · F15 (CoWork sandbox; grounds B.3) · F23 (Checker read-only). **[SD-039 removed — it denotes "git repo = SoT / closes F15," unrelated to the harness-settings ground it was attached to.]**

### A.3 SD-019 amendment mechanics — before / after *(verified accurate against OG V1.2 SD-019; carried unchanged)*

**What SD-019 said:** three surfaces named alongside V1.0 Session Routing, additive, not superseding — Chat = digest cockpit, Cowork = multi-step build, Code = execution.

**What it now says (as amended by SD-033):** four lanes; the three SD-019 surfaces preserved with roles intact but re-expressed as rights-bearing lanes (Maker / Orchestrator / Background); a fourth lane — **ChatGPT Checker, read-only Specialist** — added, which existed nowhere in canonical governance before this amendment.

**Why extension, not replacement:** the Stability Gradient classes surface definitions as Living articles (standard SPEC_DELTA), so this is not Constitutional. It is a *superseding* amendment (adds a lane, converts description to authority), so it carries a full before/after rather than a footnote. Replacement would sever the chain of record — SD-019's descriptive claim remains true and its log entry stays immutable history. Chain: V1.0 routing → SD-019 (additive) → SD-033 (superseding-in-part, normative).

---

## B. FORMAL AUTHORITY TABLE — positive / negative rights per lane

Legend: **W** write/commit · **P** propose only (drafts → Maker) · **R** read · **—** no access. *(cap. withheld)* = connector can perform the write; the SoD forbids it.

### B.1 Consolidated rights matrix (final — all candidate footnotes resolved)

| Governed object | Maker (Code) | Orchestrator (Chat) | Checker (ChatGPT) | Background (CoWork) |
|---|---|---|---|---|
| Canonical state (`OCS_STATE_CANONICAL.md`) | **W** | P | R | — (stage only; no repo reach — F15) |
| Governance (OG / SD / LD) | **W** | P | R | — |
| Git commits (repo = SoT) | **W** (sole) | P (may draft diffs/messages) | — | — |
| Drive mirror — text `.md` | **W** (mirror after commit) | — *(cap. withheld)* | R | W (fallback only, mount down — B.3) |
| Drive mirror — binary `.docx/.xlsx` | **W** (local `cp`) | — | R | W (native-app path) |
| Drive create/copy (new files, staging) | W | **—** *(carve-out (b): Chat drafts to session outputs; Code lands)* | — | **W** (primary staging lane) |
| Notion ops DBs (Tracker, Registry, Agent Registry) | W | **W** (ops visibility only — SD-030) | R | R |
| Notion Session Log (append-only rows) | W | W (/wrap) | **—** (logged by commissioning Orchestrator) | W (append own row only) |
| n8n workflows (local) | **W** | P | — | — |
| Harness config (`settings.local.json`, path-guard) | **W** (governed = SD-numbered — FM-4) | P | — | — |
| `PRUNE_QUEUE.md` | **W** (in-place merge + `--execute`) | P (log candidates at /wrap) | R | P |
| External-system writes (email, calendar, web, any connector not named above) | — | — | — | — |
| Read scope | Full: repo + mounted Drive + Notion | Drive + Notion (read) + full conversation context | Drive + Notion (read-only connectors — F23) | CoWork sandbox + Drive + Notion (read) |

**Resolved cells:**

- **¹ Orchestrator handoff carve-out → RULED (b): reroute.** The Orchestrator does **not** receive a Drive-text write right. Chat drafts the Next Starter in-chat / to session outputs; **Royal or the Maker lands it** to `/04_Domain/{project}/PROMPTS.md`. The crux cell (Orchestrator Drive-text = —) stays **absolute**. This required the OG `/wrap close` process-text correction (§F) — it removed the live contradiction where `/wrap close` claimed a Chat Drive write.
- **² Session Log append right → CONFIRMED.** Every lane **except Checker** may append its **own** row (never edit others'). Checker stays at — ; its sessions are logged by the commissioning Orchestrator, preserving zero-write posture. Required for FM-5 / HG-3 closure.
- **³ External-writes default-deny (unchanged).** No lane holds any external-system write right. Any future grant is a per-system, per-lane SD amendment — never an inferred extension (closes the matrix against an ungoverned column; ties to FM-4).

### B.3 CoWork mirror-fallback — **canonical, not assumed** *(assumption resolved)*

The Background lane's `W` on Drive-mirror text is **conditional**: it activates only when the Code→Drive mount is down. **Grounded in F15 (06-28 update):** the CoWork mirror is the designated fallback for mount-unavailable — this is canonical, no longer an [ASSUMPTION]. Every fallback write must (i) be flagged as fallback in the file or Session Log row, and (ii) be reconciled by Maker against git HEAD at next session. An unflagged fallback write is indistinguishable from FM-2 and is treated as one.

### B.4 Crux cells

- **Orchestrator: Notion W / Drive-text —.** Same connector capability, opposite rights, because the objects differ in blast radius: Notion is downstream visibility (SD-030), Drive text is canon-adjacent. Ruling (b) keeps this cell absolute.
- **Checker: R everywhere, W nowhere.** F23 recharacterized — value is "read-only connectors under withheld rights," not "zero connectors." FM-3 keeps it true.
- **Background: create-W / edit-—.** Creation is additive and reconcilable; in-place master edits are canonical acts reserved to Maker.

---

## C. FAILURE-MODE ESCALATION PATHS — FM-1…FM-5

Set **capped at five** (quarterly review 2026-10-12). No sixth mode. Two parked candidates below.

### C.1 Decision #8 cross-map — **confirmed** *(assumption resolved)*

**Axis 1 — human SoD (State §5b Decision #8):** Royal owns **Domain + Controls**; the engineer owns **Automation + Data**.
**Axis 2 — AI SoD (SD-033):** Maker / Orchestrator / Checker / Background.
**The map:** every FM escalation lands on a *human role* by which Decision #8 axis the failure touches — governance/rights/verification failures = **Controls → Royal**; sync/pipeline/permission-surface *implementation* = **Automation/Data → engineer**.
**Confirmed by Royal (2026-07-12):** no second human currently holds the Automation/Data role in personal ROC-OS, so both axes resolve to Royal wearing distinct control hats today; they split into distinct humans only in engagement contexts (Migration Sprint executor→reviewer). The two axes do not contradict — Decision #8 splits humans by *work type*; SD-033 splits AI lanes by *write authority*; they intersect only at escalation ownership and at the ratification checklist.

### C.2 The five modes

| # | Mode | Detection signal | Ground | Owning human (Dec #8) | Resolution / escalation | Closes |
|---|---|---|---|---|---|---|
| **FM-1** | Phantom close | Closed/verified status with no commit hash or Code confirmation | **SD-011 / Verify-Before-Status** *(illustrative incident: 07-03 V7.6 fork reconcile)* | Royal — Controls | (1) status → *reported, unverified*; (2) Maker re-runs tree/hash; (3) only Maker evidence re-closes (VBS); (4) Session Log incident row | **HG-1** — Chat→Code handoff carries a mandatory verification hook: no close recorded until Code returns a commit hash / tree output |
| **FM-2** | Mirror fork | Drive mirror ≠ repo HEAD; `(1).md` duplicates | 07-03 fork → V7.7 reconcile | Engineer — Automation/Data (mirror sync = plumbing); Royal — Controls countersigns | (1) git HEAD wins, unconditionally; (2) mirror overwritten from repo; (3) forked file → PRUNE_QUEUE `review`; (4) incident row, identify writing lane (§D attribution) | **HG-4** — single-writer lock: exactly one lane (Maker) holds W on any canonical file; non-Maker canonical write is *void on detection*. Interim = the negative right + a `drive_audit.py` divergence sweep (mirror-hash vs HEAD) per harness run |
| **FM-3** | Checker drift | ChatGPT connector shows read-write; or Checker text verbatim in canon | F23 posture | Royal — Controls | (1) re-scope RO immediately; (2) quarantine canon text sourced from Checker pending Maker re-derivation; (3) incident row; connector-scope attestation next quarterly review | **HG-2** — Checker findings carry an **as-of stamp** (state version / commit hash read); Orchestrator rejects-or-refreshes any finding older than HEAD before proposing |
| **FM-4** | Ungoverned capability grant | `settings.local.json` / hook / path-guard diff with no matching SD | **State §11** (path-guard = tripwire-not-sandbox; 06-28 security-hardening pass) *(illustrative incident: 07-07 `settings.local.json` creation for R1 — a `deny` could silently break the Code→Drive mirror)* | Royal — Controls decides the grant; engineer — Automation implements/reverts | (1) revert config to last SD-numbered state; (2) a wanted change enters as an SD candidate through normal adjudication — never lands first; (3) incident row linking the diff to its (missing) SD | **HG-5** — detection sweep: config diffed against the SD registry per harness run. Enforcement gap (nothing *structurally* prevents an out-of-authority op) is formally named as open. **Enforcement follow-on PARKED to 2026-10-12 as a checkpoint, cross-linked to the existing §12 Harness Security Gate + R2 Review Sprint — no duplicate charter; the real trigger is first client-data routing, not a review date.** |
| **FM-5** | Background overreach | Canon change attributed to CoWork; `/blueprint/` export treated as SoT | F15 | Royal — Controls (boundary is a governance line); engineer consulted if the sandbox reach itself changed | (1) revert from git HEAD; (2) CoWork artifact re-staged, landed through Maker; (3) `/blueprint/` export re-labeled non-authoritative; (4) incident row | **HG-3** — CoWork appends its own Session Log row on completion (right granted at B.1 ²), so Orchestrator and Royal see mid-session that background work landed |

**Escalation invariant (all five):** every resolution terminates in (a) a Maker-verified state, (b) a Session Log incident row naming the FM, and (c) — where a right or scope was at issue — a Controls-axis decision by Royal. No path resolves inside the lane that failed.

### C.3 Parked mode candidates — **confirm-and-close at 2026-10-12** (not open risk)

- **Notion-as-datastore** — already **remediated 06-28** (Session Log reshaped to a Drive-pointing index; SD-030 visibility-only). Confirm-and-close at review; not a mode.
- **Attribution / telemetry gap** (Agent Registry "Last Run" blank) — handled by the §D discipline (every lane updates its own Last Run). Confirm-and-close; not a mode.

Neither is promoted to a sixth FM. Set stays capped at five.

---

## D. AUDIT-TRAIL REQUIREMENTS — per lane

Existing rails reused (no new logging systems): git history (repo = SoT), /wrap → Notion Session Log, PRUNE_QUEUE.

- **Maker (Code):** git history is the primary evidence rail — every canonical change carries a commit; the hash is the unit of "verified." Mirror `cp` ops noted in the commit message or Log row. Harness-config changes cite the governing SD number in the commit message (FM-4 detection depends on this being machine-checkable). PRUNE_QUEUE `--execute` runs logged with the disposition set acted on.
- **Orchestrator (Chat):** /wrap Session Log row per session (proposals made; PQ candidates `[PQ-NNN] filename | disposition | legacy-risk-flag`; handoff prompts authored — noting Code lands them per carve-out (b)). Every draft explicitly labeled *proposal / ratification candidate*; an unlabeled Chat draft found in canon is FM-1/FM-2 evidence.
- **Checker (ChatGPT):** findings stamped **as-of state version + commit hash + date read** (feeds HG-2). **Inverted audit:** quarterly attestation (2026-10-12) that connector scope remains read-only — screenshot / settings export attached to the review row. Checker sessions logged by the commissioning Orchestrator (no Session Log write — B.1 ²).
- **Background (CoWork):** Session Log row per completed task (closes HG-3). Created files carry the naming standard + explicit *staged* status until Maker lands them. Any mirror-fallback write (B.3) flagged as such — unflagged fallback = treated as FM-2.

**Cross-lane precondition — attribution.** Every lane's session updates its Agent Registry "Last Run" entry (Maker writes its own; Orchestrator writes its own + the Checker's; Background writes its own). This closes the attribution gap as **logging discipline**, without promoting it to a sixth FM.

---

## F. OG PROCESS-TEXT EDIT (carve-out (b) — landed with this artifact's commit)

The OG Process Library `/wrap close` variant previously read: *"/wrap close — terminal exit; finalizes row; writes Next Starter to Drive `/04_Domain/{project}/PROMPTS.md`."* That claimed a Chat Drive-text write and **contradicted** the SD-033 Orchestrator cell (Drive-text = —). Corrected in the OG V-Current to:

> **`/wrap close`** — terminal exit; finalizes the Session Log row; **authors** the Next Starter prompt, which the **Maker (Code) lane lands** to Drive `/04_Domain/{project}/PROMPTS.md`. *(Orchestrator holds no Drive-text write — SD-033 carve-out (b).)*

This removed the last live contradiction between the process text and the authority table.

---

**SD dependency register (SD-039 removed):** SD-018 (amendment batching — rides OG V1.3) · SD-019 (amended) · SD-030 (Notion visibility corollary) · SD-011 (VBS — FM-1 ground) · **State §11** (path-guard / hardening pass — FM-4 ground) · State §5b Decision #8 (cross-cited axis) · F15 (CoWork sandbox — B.3 / FM-5) · F23 (Checker read-only — FM-3).

**Failure state of the ratification itself:** if any step is reported complete without the landing commit hash existing, that is **FM-1 by definition** — the ratification of the SoD is itself governed by the SoD.

---

*File: `DOC_2026-07-13_AI_OCS_SD033-FourLane-SoD_V1.md` · Standalone SD-033 governance artifact (ratification checklist §E step 6) · Landed by Maker (Code); repo copy is SoT, Drive `/ROC-OS/00_Registry/` is the mirror.*
