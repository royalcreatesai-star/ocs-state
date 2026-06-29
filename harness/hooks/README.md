# Claude Code Harness Hooks — versioned archive

**Authoritative live copy:** `~/.claude/hooks/bash-path-guard.py` (NOT git-tracked — that dir is outside any repo). The files here are a point-in-time **mirror for institutional memory**. If you edit the live hook, re-copy it here.

## `bash-path-guard.py` — Bash scope TRIPWIRE

A PreToolUse hook that denies Bash commands referencing a *literal* `/Users/iglobalian/` path outside an allowlist (the /ME/Ai iCloud tree, `~/.claude`, the Claude app-support dirs, this `ocs-state` repo, and the Google Drive mirror mount).

**It is a tripwire, not a security boundary.** It matches the command *string*, so it cannot see paths built dynamically, relative paths after `cd`, symlinks reached via a relative path, command-substitution/base64, paths inside a script file, or interpreter invocations (`python3 -c`). For a real boundary, sandbox the process (sandbox-exec profile / container with explicit mounts). Full analysis: `…/ME/Ai/wallyb/SECURITY-POSTURE-MEMO_2026-06-28_path-guard.md`.

## Lineage

| Version | File | Date | Change |
|---|---|---|---|
| v0 | `archive/bash-path-guard.py.v0-original-20260628` | pre-2026-06-28 | Original literal-only matcher. Bypassable via `~/` and `$HOME` forms. |
| v1 | `archive/bash-path-guard.py.v1-normalize-20260628` | 2026-06-28 | Normalize `~/` and `$HOME/${HOME}` to the literal home dir; whitelist the Google Drive mount. |
| v2 | `bash-path-guard.py` (current) | 2026-06-28 | **realpath** resolution of every extracted path (closes absolute-literal symlink + `../` traversal); allowed roots realpath'd; path-**segment** boundary match (fixes a `.claude` vs `.claude-evil` prefix-collision); docstring relabeled TRIPWIRE with bypass classes enumerated. |

## Note on a corrected claim

Earlier notes (incl. OCS §11) described the residual bypass as `D=~/x; cp "$D"`. That is **wrong** — the `~/x` literal is still in the command string and is caught. The real residual is *dynamically constructed* paths (e.g. `D=$(echo <b64> | base64 -d); cp "$D"`), where the path never appears literally. v2's docstring lists the accurate residual classes.
