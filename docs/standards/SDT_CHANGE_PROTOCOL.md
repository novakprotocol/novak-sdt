# SDT Change Protocol

## Rule

Every meaningful change should preserve:

- what changed
- why it changed
- what old truth was replaced
- what proof was rerun
- what a future human or AI should conclude

## Minimum owner-grade bundle

1. change branch
2. pre-state capture
3. code/doc updates
4. explicit change record
5. post-state proof
6. single coherent commit

## Minimum artifacts

- docs/changes/<date>-<slug>.md
- docs/status/<CHANGE>_PRESTATE.md
- docs/status/<CHANGE>_POSTSTATE.md

## Native CLI

Scaffold only:
sdt change-bundle --repo /path/to/repo --title "Rename Hello World to Hello Worlds" --type "wording-change" --why "Demonstrate structured SDT change scaffolding."

Scaffold plus proof capture:
sdt change-bundle --repo /path/to/repo --title "Rename Hello World to Hello Worlds" --type "wording-change" --why "Demonstrate proof capture." --apply-proof --command "python3 -m pytest -q tests" --command "bash bin/run-hello-world.sh" --proof-ref "docs/status/HELLO_WORLD_CHANGE_POSTSTATE.md"

## Goal

Git preserves the diff.
SDT must preserve the reasoning and verification context.
