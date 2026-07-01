# Migration From Old Operator Kit

## Decision

`novakprotocol/novak-sdt-operator-kit` was a lightweight starter-kit repo.

The useful handoff material has been consolidated into `novakprotocol/novak-sdt` under:

- `kits/operator-kit/`
- `docs/operator-kit/`

## Why

N-SDT is now the authoritative implementation for product truth, current state, operator continuity, repo birth, repo baseline, and doctor output.

The old operator-kit repo overlapped with that lane but did not include the current N-SDT CLI, baseline, doctor, report, or N-SDT/RepoOps boundary guidance.

## What moved conceptually

- Zero-context handoff checklist
- Cold-start recovery guide
- Next-operator packet template

## What was added during consolidation

- `WHAT_IS_REAL_NOW` template
- `PROJECT_STATE` template or example
- operator handoff template
- minimal repo-floor example
- archive/delete command documentation

## What did not happen

- The old repo was not deleted.
- The old repo was not archived.
- RepoOps was not merged into N-SDT.
- N-SDT was not made responsible for RepoOps policy.

## Next step

After this PR is merged and reviewed, the owner can archive or delete `novakprotocol/novak-sdt-operator-kit`.
