# Security-Posture Memo — Claude Code Path-Guard

**Date:** 2026-06-28
**Author:** Claude Code (security-hardening pass, commissioned by Royal O'Connor)
**Scope:** `~/.claude/hooks/bash-path-guard.py` + the permission surface around it
**Status:** ANALYSIS ONLY — no changes made to live config. Recommendations below await Royal's approval.
**Refs:** OCS_STATE_CANONICAL.md §11 + §8 F15; memory `project-ocs-runtime-access-map`

---

## TL;DR (the one thing that matters)

The Bash path-guard is **not a security boundary and cannot be made into one** — it is a command-string matcher, so anything that doesn't present a literal path string evades it. That was the known framing. What this pass found that changes the picture:

1. **The permission allowlist (`wallyb/.claude/settings.local.json`) contains three wildcard entries that nullify the guard *and* human-in-the-loop:** `Bash(python3 -)`, `Bash(python3 -c ' *)`, `Bash(pip3 install *)`. Any of these runs **auto-approved** and can read/write/delete anywhere the macOS user can. **Confirmed empirically.** This is the highest-priority finding — higher than any hook gap.
2. **The Read tool is auto-approved across the entire home directory** (`Read(//Users/iglobalian/**)`). No hook touches Read. The guard restricts Bash to /ME/Ai while Read can see *all* of `$HOME` unprompted — including `.ssh`, `.env`, browser profiles, Bitwarden vault, client files.
3. **Write/Edit and the filesystem-MCP `create_file` are not gated by anything OCS-specific.** A Write to `~/Desktop` (fully out of scope) succeeded in this session with **no prompt** — confirmed empirically.

Net: the hook gives the *appearance* of containment over one tool (Bash) while three other write/read paths are wide open. For an Engine-2 AI-governance practice, the honest posture statement is: **"accident tripwire on typed Bash paths," not "scope sandbox."**

---

## Deliverable 1 — Bypass-class enumeration (tested, not assumed)

Method: every probe targeted a **nonexistent** path under an out-of-scope dir (`~/Desktop/__guardprobe…`) so only *reachability* was proven — no real out-of-scope content was read. "Executed" = hook allowed the command (real bypass). "Blocked" = hook denied.

| # | Class | Probe | Result | Real? |
|---|-------|-------|--------|-------|
| C0 | Literal path (control) | `ls /Users/iglobalian/Desktop/x` | **BLOCKED** | — |
| C0 | `~/` form (fixed 06-28) | `ls ~/Desktop/x` | **BLOCKED** | — |
| C0 | `$HOME` form (fixed 06-28) | `ls $HOME/Desktop/x` | **BLOCKED** | — |
| 1 | Var indirection *as documented* | `D=~/x; ls "$D"` | **BLOCKED** | **NO** — cold-start note was wrong |
| 1b | Var built *dynamically* | `D=$(echo <b64>\|base64 -d); ls "$D"` | **EXECUTED** | **YES** |
| 2 | Relative path after `cd` | `cd ~ && ls Desktop/x` | **EXECUTED** | **YES** |
| 3 | Symlink at allowed path → outside | `ln` (dynamic target) then `ls ./link/x` | **EXECUTED** | **YES** |
| 4a | base64 → command substitution | `ls "$(echo <b64>\|base64 -d)/x"` | **EXECUTED** | **YES** |
| 4b | Script file (`bash script.sh`) | script body holds literal `/Users/.../Desktop` | **EXECUTED** | **YES** |
| 5 | Interpreter stdin/`-c` (NEW) | `python3 -c '…os.path…'` | **EXECUTED + AUTO-APPROVED** | **YES — worst** |

**Correction to the cold-start threat list:** Bypass class 1 as written (`D=~/x; cp "$D"`) is **caught** — the literal `~/x` is still in the command string and the 06-28 normalization now matches it. The real hole is *dynamic* construction (1b), where the path value never appears literally. Worth fixing in the source-of-truth notes.

**Root cause (single sentence):** the hook inspects the *command string*; classes 1b/2/3/4a/4b/5 all arrange for the out-of-scope path to **not exist as a literal in that string** (dynamic value, relative path, symlink indirection, encoded, inside a file, or constructed inside an interpreter). No amount of regex closes that — it is the structural ceiling of a string matcher.

---

## Deliverable 3 — What governs the NON-Bash tools (confirmed)

The Bash hook (`matcher: "Bash"`) gates **only** Bash. Everything else is governed by the Claude Code **permission system** (allow/ask/deny lists in settings + the active permission mode), with **no path scoping**:

| Tool | Gated by hook? | Actual control | Effective scope today |
|------|----------------|----------------|-----------------------|
| **Bash** | Yes (porously) | hook + permission allowlist | /ME/Ai *for literal paths only* |
| **Read** | **No** | permission allowlist | **All of `$HOME`** — `Read(//Users/iglobalian/**)` is auto-allowed (line 31), plus `/Applications`, `/Volumes`, `/private/tmp` |
| **Write / Edit** | **No** | permission mode default | No OCS limit; **wrote to `~/Desktop` unprompted** this session (mode is auto-accepting) |
| **Filesystem MCP** (`mcp__19d8…`) | **No** | permission allowlist | `create_file`, `read_file_content`, `download_file_content`, `search_files` all auto-allowed — a write primitive entirely outside the guard |
| **Other MCP** (Notion, Gmail, Chrome, wallyb-workspace) | **No** | permission allowlist | Several read/write ops auto-allowed |

**Conclusion:** the guard protects one of at least four write/read avenues. Read is *broader* than Bash by design. This is the core asymmetry to fix or to document honestly.

---

## Deliverable 4 — settings + other-hooks review

- **`~/.claude/settings.json` (global):** one PreToolUse hook (Bash → this guard). **No `permissions` block at all** — so global defaults apply and the project allowlist below is the operative permission surface. No other hooks. No Stop/PostToolUse/PreCompact hooks.
- **`~/.claude/settings.local.json`:** does not exist.
- **`wallyb/.claude/settings.local.json` (operative):** large `allow` list. Gaps, by severity:
  - 🔴 **`Bash(python3 -)`** — runs an arbitrary script from stdin, auto-approved. Total bypass of guard + review.
  - 🔴 **`Bash(python3 -c ' *)`** — arbitrary Python one-liner, wildcard, auto-approved. **Confirmed reaching `~/Desktop` via base64-built path.**
  - 🔴 **`pip3 install *`** — arbitrary package install (arbitrary code execution / supply-chain), auto-approved.
  - 🟠 **`Read(//Users/iglobalian/**)`** — whole-home read, auto-approved. Likely broader than intended.
  - 🟠 **`NODE_PATH=$(npm root -g) node build_*.js`** + **filesystem-MCP `create_file`/`download_file_content`** — write/exec primitives outside the guard.
  - 🟡 Many one-off `cp`/`sed` entries referencing `~/Downloads`, `/tmp`, `~/blueprint` — out-of-scope paths already permanently allowlisted from past sessions; allowlist is accreting and should be pruned.
- **No project-level hooks anywhere** (only `launch.json` + this settings file under `wallyb/.claude/`).

---

## Deliverable 2 — Threat model + recommendation

**Who is the adversary?** Not a remote attacker with shell access (this is a single-user Mac, not a multi-tenant host). The realistic threats are:
1. **Prompt-injection / tool-misuse** — the agent reads a poisoned source (a doc, email, web page, NotebookLM source, MCP payload) that instructs it to read/exfiltrate/modify/delete outside scope. This is the live risk for a practice that ingests client and third-party content.
2. **Accidents** — a fat-fingered or over-eager command touching the wrong tree.

**What the hook actually buys against those:** it stops *accidents that take the form of a typed literal Bash path*, and naive agent behavior. It does **nothing** against an injected instruction that says "run `python3 -c …`" (auto-approved), "read `~/.ssh/id_rsa`" (Read is allowed home-wide), or "use the filesystem MCP to write here." Against threat #1 it is close to cosmetic.

**Options weighed:**

- **(A) Keep as accident-preventer, add realpath resolution.** Resolving tokens/symlinks via `os.path.realpath` before checking closes the *symlink-via-literal* and `..`-traversal accident cases. It **cannot** close 1b/2/4a/4b/5 (no path string to resolve) and touches nothing outside Bash. Low cost, low ceiling.
- **(B) macOS `sandbox-exec` (seatbelt) profile wrapping the launch.** Kernel-enforced file allowlist over the whole `claude` process tree — works regardless of how a path is built (python, scripts, MCP subprocesses). Fits the **iCloud-resident data layout** (the /ME/Ai tree lives in *this* user's `~/Library/Mobile Documents`). Caveats: the seatbelt API is Apple-deprecated (still functional), profiles are fiddly, and you must whitelist the harness's real needs (node, caches, tmp, app-support, the MCP servers) or things break.
- **(C) Restricted second macOS user.** Strong and durable, but the /ME/Ai data lives in the **primary** user's iCloud Library, which a second user cannot natively see. Poor fit for this data layout.
- **(D) Container with explicit mounts.** Cleanest *airtight* boundary — bind-mount only /ME/Ai, the repo, and the Drive mirror; everything else unreachable by construction. Cost: breaks the native-macOS MCP workflow (Chrome control, computer-use, iCloud sync, native-app round-trips). A re-architecture, not a patch.

**Recommendation (pick-one, with the trade stated honestly):**

> **Do not invest in turning the Python hook into a boundary — it structurally cannot be one.** Instead, in priority order:
>
> 1. **NOW, zero-cost, highest leverage:** close the permission-allowlist holes (remove the three 🔴 wildcards; narrow Read). This removes the auto-approved total-bypass paths and is worth more than any hook change.
> 2. **NOW, cheap:** realpath-harden the hook (Option A) and **explicitly re-label it a "tripwire," not a sandbox**, in the docstring + OCS §11. Honesty is itself a governance deliverable.
> 3. **WHEN client-confidential data enters the workflow:** stand up a real OS boundary. Given the iCloud data locality, **prototype the `sandbox-exec` profile (Option B)** as the lowest-friction enforced boundary; fall back to the **container (Option D)** only if seatbelt's deprecation is judged unacceptable. Treat this as a deliberate Horizon-Two decision Royal makes with eyes open — not an auto-adopted patch.

The Engine-2 angle: this same tiered reasoning (tripwire → permission hygiene → enforced boundary, sized to the data's sensitivity) **is** a sellable AI-governance artifact. The honest "what the control does and doesn't do" table is the deliverable clients actually need.

---

## Deliverable 5 — `.bak-20260628` housekeeping

The pre-hardening original sits at `~/.claude/hooks/bash-path-guard.py.bak-20260628`. `~/.claude/hooks/` is **not** under git, so this `.bak` is the only versioned copy of the pre-06-28 logic. Per OCS rule (never hard-delete state):

> **Recommended (await approval):** commit *both* the current `bash-path-guard.py` and the `.bak` into the `ocs-state` repo under e.g. `harness/hooks/` (institutional memory, properly versioned), **then** remove the loose `.bak` from the live `~/.claude/hooks/` dir so it can't be confused with the active hook. Net: nothing lost, history preserved in git, live dir clean.

---

## Recommended config diff (for approval — NOT yet applied)

### 1. `wallyb/.claude/settings.local.json` — remove the 🔴 total-bypass entries
```diff
-      "Bash(python3 -)",
-      "Bash(python3 -c ' *)",
-      "Bash(pip3 install *)",
```
…and replace with the *specific* commands actually needed (e.g. the exact `python3 scripts/run.py …` invocations already enumerated, plus a pinned `pip3 install -r requirements.txt` if a known requirements file exists).

### 2. (Optional, recommend) narrow whole-home Read
```diff
-      "Read(//Users/iglobalian/**)",
+      "Read(//Users/iglobalian/Library/Mobile Documents/com~apple~CloudDocs/ME/Ai/**)",
+      "Read(//Users/iglobalian/Documents/ME/Ai/ocs-state/**)",
+      "Read(//Users/iglobalian/.claude/**)",
```
(Keep the specific `/Applications`, `/Volumes`, `/private/tmp` Read entries the workflow already relies on.)

### 3. `bash-path-guard.py` — realpath hardening (marginal; tripwire-grade only)
Resolve each extracted path (and symlinks) to a real absolute path before the allowlist check, and realpath the allowed roots once. Closes symlink-via-literal and `..` traversal for the *accident* case. **Does not** close dynamic/relative/interpreter classes — pair with a docstring change re-labeling the hook a tripwire. Full patch to follow on approval.

---

## Approval checklist for Royal

- [x] **#1 — remove the 3 wildcard Bash allows** (DONE 2026-06-28: `python3 -`, `python3 -c ' *`, `pip3 install *` removed from `wallyb/.claude/settings.local.json`; JSON re-validated. Takes full effect next session.)
- [x] #2 — narrow `Read(//Users/iglobalian/**)` to the OCS trees (DONE 2026-06-28: replaced with 5 scoped entries — /ME/Ai, ocs-state, .claude, Application Support/Claude, Google Drive mount. Out-of-scope reads now prompt instead of auto-approving.)
- [x] #3 — realpath-harden the hook + re-label it "tripwire" (DONE 2026-06-28: realpath on extracted paths + realpath'd roots + path-segment boundary match fixing a `.claude` vs `.claude-evil` prefix-collision; docstring relabeled TRIPWIRE with bypass classes enumerated. 8/8 test battery PASS; old hook proven to allow the `../`-traversal + prefix-collision escapes the new one blocks. Snapshot: `bash-path-guard.py.bak-20260628-prerealpath`. OCS §11 updated 2026-06-28 in commit 1baaecc.)
- [x] #5 — archive `.bak` into the `ocs-state` git repo, remove the loose copy (DONE 2026-06-28: `harness/hooks/` added — live hook v2 + v0/v1 archive + README lineage; both loose `.bak`s removed from `~/.claude/hooks/`; §11 updated + inaccurate residual-claim corrected; committed + pushed `origin/main` 1baaecc.)
- [ ] (Decision) — whether/when to pilot a `sandbox-exec` profile for client-confidential work
```
