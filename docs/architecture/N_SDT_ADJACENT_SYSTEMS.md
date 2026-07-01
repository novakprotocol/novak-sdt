# N-SDT Adjacent Systems

## Decision

Use **N-SDT** as the Novak display name for this implementation of Software
Digital Thread.

Keep the technical names stable:

- repository: `novakprotocol/novak-sdt`
- package: `novak-sdt`
- CLI: `sdt`

Do not rename this repo, package, or CLI in the cleanup pass.

## Active System Map

| Name | Role | Keep active? |
|---|---|---|
| N-SDT / `novak-sdt` | Product truth, operator continuity, repo birth, repo baseline, report-only, doctor. | Yes |
| RepoOps | Repository operating standard, agent rules, quality gates, repo checks. | Yes |
| W.R.A.P.I.T. | Command receipts, run logs, artifacts, integrity evidence, latest/summary/verify. | Yes |
| S.I.G.I.L. | Product repo for governed script and instruction execution. | Yes |

## W.R.A.P.I.T. Naming

Keep W.R.A.P.I.T. as W.R.A.P.I.T.

Do not rename it to `N-SURE`, `N-Sure`, or another `N-*` name right now. The
existing name already points at the job: wrapping consequential commands and
leaving receipts.

If a plainer label is needed in docs, use:

```text
W.R.A.P.I.T. (Novak command receipts)
```

That gives humans the plain-English meaning without breaking the existing repo,
package, CLI, docs, or release surface.

## Boundaries

N-SDT owns truth and continuity.

RepoOps owns repo operating discipline.

W.R.A.P.I.T. owns evidence that a command ran.

S.I.G.I.L. owns its product behavior and should stay a product under SDT, not
become the name of SDT.

## Rule

Build one operator workflow, not one giant repo:

```text
N-SDT establishes truth
RepoOps establishes repo discipline
W.R.A.P.I.T. proves important runs
product repos stay product repos
```
