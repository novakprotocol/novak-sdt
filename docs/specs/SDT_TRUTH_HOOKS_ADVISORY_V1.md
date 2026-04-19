# SDT Truth Hooks Advisory V1

## Goal

Change SDT local git hooks from tracked-file mutation behavior to advisory behavior.

## Why

The truth-closure v1 pack is real and tagged, but the local post-commit and post-merge hooks were aggressive enough to dirty tracked truth files after otherwise good commits.

## Rule

Hooks may:

- detect meaningful repo mutations
- print clear operator guidance
- point to exact follow-up commands

Hooks must not:

- auto-stage tracked truth files
- auto-modify tracked repo truth on post-commit or post-merge
- leave a clean repo dirty just because a hook ran

## Explicit mutation stays here

- `bash tools/run_truth_refresh_and_stage.sh /root/novak-sdt`
- `bash tools/freeze_trusted_floor.sh /root/novak-sdt <tag>`

## Success criteria

- local hooks install cleanly
- post-commit and post-merge no longer mutate tracked truth
- hooks only print advisory output when the last commit changed non-truth files
