# N-SDT RepoOps Adoption Guide

## Status

Accepted as the current narrow adoption path for N-SDT and RepoOps.

This guide intentionally covers only two layers:

- N-SDT
- RepoOps

It does not add another control-plane repo, split RepoOps, merge RepoOps into
N-SDT, rename either system, or bring adjacent product/evidence systems into
the current adoption path.

## Plain-English Rule

N-SDT explains the repo.

RepoOps governs the repo.

Use N-SDT first to establish truth and continuity. Use RepoOps second to apply
repo operating discipline.

```text
N-SDT = what is true and how to continue
RepoOps = how the repo is operated and checked
```

## Layer Contract

| Layer | Owns | Does not own |
|---|---|---|
| N-SDT | Product truth, current state, operator continuity, repo birth, repo baseline, doctor output. | Repo standard profiles, AI-agent policy, PR discipline, quality-gate policy. |
| RepoOps | Repo standards, agent instructions, command map, quality gates, public/private safety checks, profile exceptions. | Product truth, current product state, operator continuity files. |
| Local repo owner | Product naming, release posture, privacy posture, accepted exceptions, final approval. | Silent replacement by either layer. |

## N-SDT Provides

N-SDT should be the first pass because it gives the repo a current truth floor:

- `sdt baseline --report-only`
- `sdt baseline`
- `sdt doctor`
- `WHAT_IS_REAL_NOW.md`
- `PROJECT_STATE.md`
- `docs/product/`
- `docs/operator/`
- SDT reports under `docs/status/`

The important output is not just files. The important output is a clearer
answer to:

```text
What is this repo?
What is real now?
What is missing?
What does the next operator need?
```

## RepoOps Consumes

RepoOps should treat N-SDT outputs as read-only context unless the owner
explicitly approves a change.

RepoOps can use that context to decide whether the repo has:

- a declared standard/profile
- clear AI-agent instructions
- a command map
- local checks
- quality gates
- public/private safety checks when needed
- generated-output freshness checks when needed
- documented exceptions

The important output is a clearer answer to:

```text
Can this repo be operated safely and repeatedly?
```

## Required Adoption Sequence

1. Run N-SDT report-only.
2. Review the missing truth and continuity files.
3. Apply N-SDT baseline only after approval.
4. Run `sdt doctor`.
5. Run RepoOps in dry-run or report mode.
6. Choose the smallest RepoOps profile that fits.
7. Review suggested merges for existing important files.
8. Record accepted exceptions.
9. Apply RepoOps changes or open a pull request.
10. Run local checks.

## Done Means

A repo is not adopted just because files exist.

Done means:

- N-SDT truth files exist or gaps are intentionally recorded.
- `sdt doctor` has been run and the result is known.
- RepoOps profile choice is recorded.
- RepoOps checks have been run or the blocker is recorded.
- Existing important files were not silently overwritten.
- A human can tell what changed and why.

## Hard Boundaries

- Do not make N-SDT write RepoOps governance files by default.
- Do not make RepoOps rewrite N-SDT truth files by default.
- Do not treat RepoOps as the source of product truth.
- Do not treat N-SDT as the source of repo policy.
- Do not introduce a new acronym or repository to solve this boundary.

## Future Small Adapters

The next implementation work should stay small:

- N-SDT can print a final recommendation after baseline:

  ```text
  Next: run RepoOps dry-run, choose a profile, and review suggested merges.
  ```

- RepoOps can detect N-SDT context files:

  ```text
  SDT context present: WHAT_IS_REAL_NOW.md, PROJECT_STATE.md, docs/product/
  ```

- RepoOps can include N-SDT status as context in its report without editing
  N-SDT-owned files.

That is enough integration for now. The two layers should feel like one
operator path while remaining separate systems.
