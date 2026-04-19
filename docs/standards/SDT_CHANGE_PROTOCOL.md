# SDT Change Protocol

## Rule

Every meaningful change should preserve:

- what changed
- why it changed
- what old truth was replaced
- what proof was rerun
- what a future human or AI should conclude
- whether the actual change stayed aligned with stated intent

## Minimum owner-grade bundle

1. change branch
2. pre-state capture
3. intent statement
4. code/doc updates
5. explicit change record
6. post-state proof
7. alignment check
8. single coherent commit

## Minimum artifacts

- docs/changes/<date>-<slug>.md
- docs/status/<CHANGE>_PRESTATE.md
- docs/status/<CHANGE>_POSTSTATE.md
- docs/templates/SDT_CHANGE_INTENT_TEMPLATE.md

## Intent standard

Use a minimal intent block:

### Intent Statement
- actor: who is making or editing the change
- intended change: what should change
- intended non-change: what must not drift
- why: reason for the change
- proof expected: what should be rerun or checked

### Alignment Check
- observed change summary
- in-intent: PASS | PARTIAL | FAIL | UNVERIFIED
- notes

## Native CLI

Scaffold only:
sdt change-bundle --repo /path/to/repo --title "Rename Hello World to Hello Worlds" --type "wording-change" --why "Demonstrate structured SDT change scaffolding."

Scaffold plus proof capture:
sdt change-bundle --repo /path/to/repo --title "Rename Hello World to Hello Worlds" --type "wording-change" --why "Demonstrate proof capture." --apply-proof --command "python3 -m pytest -q tests" --command "bash bin/run-hello-world.sh" --proof-ref "docs/status/HELLO_WORLD_CHANGE_POSTSTATE.md"

## Goal

Git preserves the diff.
SDT must preserve the reasoning, verification context, and alignment-to-intent.
