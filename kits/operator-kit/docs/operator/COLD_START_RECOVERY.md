# Cold Start Recovery

## Purpose

Help a new operator enter a repo cold and move safely.

## First 10 minutes

1. Identify repo, branch, and head commit.
2. Read `WHAT_IS_REAL_NOW.md`.
3. Read `PROJECT_STATE.md`.
4. Read latest operator docs.
5. Read latest decision docs.
6. Inspect git status.
7. Inspect last 10 commits.
8. Find the exact next command block.
9. Identify rollback point.
10. Only then mutate anything.

## Required terminal checks

```bash
pwd
git status --short
git log --oneline --decorate -10
find docs -maxdepth 2 -type f | sort
```

On Windows PowerShell, use:

```powershell
Get-Location
git status --short
git log --oneline --decorate -10
Get-ChildItem docs -Recurse -File | Select-Object -ExpandProperty FullName
```

## Stop conditions

Do not proceed until you know:

- what is proved
- what is assumed
- what is next
- what would be dangerous
- which files are source-of-truth files
- which files are generated or disposable

## Rule

If the repo does not expose a clear next action, create a handoff/update before doing new work.
