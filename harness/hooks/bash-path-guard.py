#!/usr/bin/env python3
"""
PreToolUse hook — Bash scope TRIPWIRE for the /ME/Ai working tree.

⚠ THIS IS NOT A SECURITY BOUNDARY. It is a command-string matcher that trips on
*literal* out-of-scope paths typed into Bash — an accident-catcher and a speed
bump, nothing more. It gates Bash ONLY; Read / Write / Edit / MCP are governed by
the Claude Code permission allowlist, not by this hook.

Known, unclosable bypass classes (a string matcher cannot see these):
  - dynamically-built paths         D=$(...); ls "$D"
  - relative paths after cd         cd ~ && ls Desktop/x
  - symlink reached via a relative path
  - command substitution / base64   ls "$(echo <b64> | base64 -d)/x"
  - path inside a script file        bash script.sh
  - interpreters                     python3 -c '...'
For a real boundary, sandbox the process (sandbox-exec profile, or a container
with explicit mounts). See SECURITY-POSTURE-MEMO_2026-06-28_path-guard.md and
OCS_STATE_CANONICAL.md §11.

Hardening present (tripwire-grade):
  - ~/ and $HOME/${HOME} are normalized to the literal home dir.
  - Every extracted path is resolved with os.path.realpath before the check, so
    an *absolute literal* path that is a symlink, or that uses ../ traversal, is
    evaluated by its REAL target. (Marginal — only helps the literal-path case;
    relative paths and the classes above are never extracted, so realpath can't
    see them.)
  - Allowed roots are realpath'd too (apples-to-apples), and matched on a path
    SEGMENT boundary so '/x/.claude' does not also allow '/x/.claude-evil'.
"""
import sys
import json
import re
import os

HOME = "/Users/iglobalian"

ALLOWED_USER_PATHS = [
    "/Users/iglobalian/Library/Mobile Documents/com~apple~CloudDocs/ME/Ai",
    "/Users/iglobalian/.claude",
    "/Users/iglobalian/Library/Application Support/Claude",
    "/Users/iglobalian/Library/Application Support/claude",
    "/Users/iglobalian/Documents/ME/Ai/ocs-state",  # OCS state repo (git; iCloud blocks .git)
    "/Users/iglobalian/Library/CloudStorage/GoogleDrive-royalcreates.ai@gmail.com",  # Google Drive mirror mount — direct repo->Drive sync (enabled 2026-06-28)
]

# Resolve allowed roots once so a symlinked root compares apples-to-apples.
ALLOWED_REAL = [os.path.realpath(a) for a in ALLOWED_USER_PATHS]


def _normalize(p: str) -> str:
    # Collapse ~ and $HOME/${HOME} prefixes to the literal home dir.
    if p.startswith("~/"):
        return HOME + p[1:]
    if p.startswith("${HOME}"):
        return HOME + p[len("${HOME}"):]
    if p.startswith("$HOME"):
        return HOME + p[len("$HOME"):]
    return p


def _real(p: str) -> str:
    # realpath resolves symlinks + ../ traversal; safe on nonexistent paths
    # (it resolves the existing prefix and keeps the rest lexically).
    try:
        return os.path.realpath(p)
    except Exception:
        return p


def _allowed(real_path: str) -> bool:
    # Exact root, or a child below it on a path-segment boundary.
    return any(real_path == a or real_path.startswith(a + os.sep) for a in ALLOWED_REAL)


def extract_paths(cmd: str):
    paths = []
    # Literal /Users/iglobalian paths (quoted handles spaces like "Mobile Documents")
    paths += re.findall(r'"(/Users/iglobalian/[^"]+)"', cmd)
    paths += re.findall(r"'(/Users/iglobalian/[^']+)'", cmd)
    paths += re.findall(r'(?<!["\'])(/Users/iglobalian/[^\s\'";&|>)\\]+)', cmd)
    # Unquoted ~/ paths (quoted tilde does NOT expand in bash, so we skip those)
    paths += re.findall(r'(?<!["\'])(~/[^\s\'";&|>)\\]+)', cmd)
    # $HOME / ${HOME} paths — both unquoted and double-quoted expand in bash
    paths += re.findall(r'"((?:\$HOME|\$\{HOME\})/[^"]+)"', cmd)
    paths += re.findall(r'(?<!["\'])((?:\$HOME|\$\{HOME\})/[^\s\'";&|>)\\]+)', cmd)
    return [_normalize(p) for p in paths]


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    cmd = data.get("tool_input", {}).get("command", "")
    blocked = []
    for path in extract_paths(cmd):
        path = path.rstrip(")'\"\\ ")
        if not _allowed(_real(path)):
            blocked.append(path)

    if blocked:
        out = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f"Blocked: path outside /ME/Ai — {', '.join(blocked[:3])}"
                ),
            }
        }
        print(json.dumps(out))


if __name__ == "__main__":
    main()
