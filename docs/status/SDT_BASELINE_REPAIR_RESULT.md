# SDT baseline repair result

## Stamp
2026-04-17 21:18:12 UTC

## Bug repaired
baseline with --git-commit now auto-initializes git when the target path is not already a git repository.

## Proven
- cli.py imports cleanly
- fresh repo birth still works
- baseline now succeeds on a messy non-git existing directory
- doctor passes on the adopted existing proof repo
- git commit is created for the adopted existing proof repo

## Next
- fold this into the internal release gate
