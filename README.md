# OCS State Repo — Quick Reference

This repo holds the canonical OCS / ROC-OS state. Plain Markdown files, version-controlled, backed up on GitHub.

## What's here
| File | What it is |
|------|-----------|
| `OAIS_STATE.md` | **The canonical state file.** Drop this first in any session. |
| `DOC_..._GATE5-RECONCILIATION_V1.md` | The 24-initiative project reconciliation (the bridge map) |
| `DOC_..._COWORK-CLEANUP-WORKORDER_V1.md` | Cleanup task list for CoWork |

## Mental model (Git is NOT an editor)
- **Repo folder** (`~/Documents/ME/Ai/ocs-state`) = the desk where the real files live.
- **Git** = camera + courier: snapshots the folder (`commit`) and mails it to GitHub (`push`).
- **GitHub** = off-site vault: https://github.com/royalcreatesai-star/ocs-state
- **Drive `00_Registry`** = a separate mirror copy. It does NOT auto-sync with this repo.

## How to edit (two ways)
**A — Let Claude Code do it (default):** say what to change in plain English → Claude edits + commits + pushes. You type nothing.

**B — By hand:** open the `.md` in a text editor → save → then:
```bash
cd ~/Documents/ME/Ai/ocs-state
git add -A
git commit -m "what changed"
git push
```

## ⚠ The one rule
**Edit in the repo, then mirror to Drive.** Never edit the Drive copy directly for canonical state — the two copies will drift.

## Auth
GitHub login uses a fine-grained PAT (saved in macOS keychain + Bitwarden). Pushes are silent now. If ever re-prompted: username `royalcreatesai-star`, password = the `github_pat_…` token.
