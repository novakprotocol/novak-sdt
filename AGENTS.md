# AGENTS.md

This repository is the current N-SDT implementation.

## First Steps

1. Read `README.md`.
2. Read `docs/architecture/N_SDT_REPOOPS_ADOPTION_GUIDE.md`.
3. Read `docs/architecture/N_SDT_ADJACENT_SYSTEMS.md` before changing adjacent-system language.
4. Inspect `src/novak_sdt/cli.py` before changing CLI behavior.

## N-SDT And RepoOps Brief

Use this brief when a task mentions SDT, N-SDT, RepoOps, repo standards, agent
instructions, or adoption.

Current architecture:

- N-SDT is the truth and continuity layer.
- RepoOps is the repository operations layer.
- WhyPy currently contains the active RepoOps source and proving ground.
- N-SDT and RepoOps are separate systems that lightly integrate through adapters.

Ownership:

- N-SDT owns product truth, current state, continuity, repo birth, repo baseline,
  operator handoff, truth-floor docs, and `sdt doctor` output.
- RepoOps owns repo standards, quality gates, AI-agent governance, repo
  profiles, drop-ins, repo checks, and operational discipline.
- Local repo owners decide product naming, release posture, privacy posture,
  accepted exceptions, and final approval.

Hard rules:

- Do not merge RepoOps into N-SDT.
- Do not split RepoOps into a standalone repo yet.
- Do not rename `novak-sdt`, the package, or the `sdt` CLI.
- Use `N-SDT` as display naming only.
- Do not make N-SDT write RepoOps governance files by default.
- Do not use N-SDT to decide repo policy.
- Do not pick random target repos for adoption.
- Ignore W.R.A.P.I.T. and S.I.G.I.L. unless the owner opens a separate task.

Already completed:

- N-SDT PR #50 added RepoOps follow-up guidance after `sdt baseline` and
  `sdt baseline --report-only`.
- WhyPy PR #32 made RepoOps detect N-SDT context files as informational
  read-only context.
- WhyPy PR #34 refreshed the N-SDT/RepoOps next-action recommendation.
- Legacy repos were archived and renamed:
  - `Archived20260701-novak-sdt-born-proof`
  - `Archived20260701-novak-control-plane`
  - `Archived20260701-novak-repo-template`

Correct adoption sequence:

1. Owner names an explicit target repo.
2. Run `sdt baseline --report-only`.
3. Review missing N-SDT truth and continuity files.
4. Apply `sdt baseline` only after owner approval.
5. Run `sdt doctor`.
6. Run RepoOps report or dry-run mode.
7. Choose the smallest RepoOps profile that fits.
8. Record exceptions or suggested merges in a PR.
9. Merge only after checks pass.

Plain-English boundary:

```text
N-SDT explains what is true and how to continue.
RepoOps governs how the repo is operated and checked.
They should cooperate, not collapse into each other.
```

## Validation

For N-SDT changes, run the narrow relevant tests first. Before a PR, run:

```bash
python -m pytest
python -m mkdocs build --strict --site-dir .mkdocs-site-tmp
```

Remove temporary docs/test output before committing unless project policy changes.
