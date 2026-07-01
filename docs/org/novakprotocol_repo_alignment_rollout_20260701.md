# Novakprotocol Repo Alignment Rollout - 2026-07-01

## Purpose

This document records the classification-first N-SDT + RepoOps rollout for the selected `novakprotocol` repositories.

The goal is not to make every repo look the same. The goal is to make every repo immediately understandable, honestly classified, and safely operable.

## Operating rule

```text
N-SDT = repo truth, current state, product/system boundary, and operator continuity.
RepoOps = repo operating profile, checks, AI/human handoff discipline, exceptions, and repeatable operation.
```

Use N-SDT first. Use RepoOps second. Do not apply one heavyweight structure to every repo.

## Master tracking

Master issue:

- https://github.com/novakprotocol/novak-sdt/issues/52

## Deletion candidates

The following repos were verified through GitHub repository metadata as `size: 0`. They appear empty and should be treated as delete candidates unless there is a reason outside the repo to preserve the name.

| Repository | GitHub size | Current recommendation | Reason |
|---|---:|---|---|
| `C.O.R.E.---OLD` | 0 | Delete candidate | Empty legacy/old repo; active `C.O.R.E.` exists. |
| `H.A.L.T.` | 0 | Delete candidate | Empty reserved placeholder; no repo content. |
| `M.E.S.H.` | 0 | Delete candidate | Empty reserved placeholder; no repo content. |
| `N.E.X.S.` | 0 | Delete candidate | Empty reserved placeholder; no repo content. |
| `P.A.S.S.` | 0 | Delete candidate | Empty reserved placeholder; no repo content. |
| `P.R.O.V.E.` | 0 | Delete candidate unless intentionally reserved | Empty placeholder; `novare` appears to carry actual recovery/proof implementation. |
| `S.E.A.L.` | 0 | Delete candidate | Empty reserved placeholder; no repo content. |
| `S.E.C.S.N.E.T.` | 0 | Delete candidate | Empty reserved placeholder; no repo content. |
| `T.R.A.C.E.` | 0 | Delete candidate unless intentionally reserved | Empty placeholder; ProofPlane Access appears to carry actual access/evidence implementation. |
| `V.O.I.D.` | 0 | Delete candidate | Empty reserved placeholder; no repo content. |

### Why they probably exist

The pattern suggests these were created as acronym placeholders for future NOVAK control-plane lanes or old naming experiments. Empty placeholder repos are not useful long-term because they create false inventory, confuse scans, and make it harder to tell what is real.

### Delete limitation

The GitHub connector exposed in this chat does not provide a repository-delete action. It only exposes file deletion, issue creation, comments, and related repository operations. Therefore repository deletion must be done manually through GitHub UI or a local authenticated GitHub CLI.

Manual deletion commands if confirmed locally:

```bash
gh repo delete novakprotocol/C.O.R.E.---OLD --yes
gh repo delete novakprotocol/H.A.L.T. --yes
gh repo delete novakprotocol/M.E.S.H. --yes
gh repo delete novakprotocol/N.E.X.S. --yes
gh repo delete novakprotocol/P.A.S.S. --yes
gh repo delete novakprotocol/P.R.O.V.E. --yes
gh repo delete novakprotocol/S.E.A.L. --yes
gh repo delete novakprotocol/S.E.C.S.N.E.T. --yes
gh repo delete novakprotocol/T.R.A.C.E. --yes
gh repo delete novakprotocol/V.O.I.D. --yes
```

Recommended safety check before deletion:

```bash
for repo in \
  C.O.R.E.---OLD H.A.L.T. M.E.S.H. N.E.X.S. P.A.S.S. \
  P.R.O.V.E. S.E.A.L. S.E.C.S.N.E.T. T.R.A.C.E. V.O.I.D.; do
  gh repo view "novakprotocol/$repo" --json name,isEmpty,visibility,updatedAt,pushedAt
done
```

If any repo shows non-empty content, stop and inspect before deletion.

## Active/documented repos queued for alignment

These repos have enough documented purpose to receive classification-first N-SDT + RepoOps assessment.

| Repository | Current classification | N-SDT treatment | RepoOps treatment | Better/stronger signal found | Repo-local issue |
|---|---|---|---|---|---|
| `ACLForge` | Active product/tool | Product truth + operator continuity | Active product/tool profile | Strong governed ACL execution/evidence lane; not just visibility. | https://github.com/novakprotocol/ACLForge/issues/1 |
| `B.A.S.E.L.I.N.E.-DAY-` | Support/governance workflow lane | Truth/drift lane boundary | Support/governance profile | Clear approved-state and drift plane. | https://github.com/novakprotocol/B.A.S.E.L.I.N.E.-DAY-/issues/1 |
| `B.I.N.A.T.E.-DAY` | Active language/spec repo | B2 Language truth boundary | Language/spec profile | README already retires B.I.N.A.T.E. as alias and points to NOVAK B2 Language. | https://github.com/novakprotocol/B.I.N.A.T.E.-DAY/issues/1 |
| `B.I.N.A.T.E.-RDY` | Readiness/handoff lane | Transition truth only | Support/readiness profile | Looks like promotion/handoff lane, not main product. | https://github.com/novakprotocol/B.I.N.A.T.E.-RDY/issues/1 |
| `B.U.I.L.D.-DAY-` | Support/governance workflow lane | Lineage/build/rebuild truth | Support/governance profile | Clear lineage, deployment, rebuild, proof-of-change plane. | https://github.com/novakprotocol/B.U.I.L.D.-DAY-/issues/1 |
| `C.H.A.N.G.E.-DAY` | Support/governance workflow lane | Change/governed mutation truth | Support/governance profile | Clear request/review/closeout/rollback lane. | https://github.com/novakprotocol/C.H.A.N.G.E.-DAY/issues/1 |
| `C.O.R.E.` | Active product/tool or overlap candidate | NIA Foundry truth plus acronym-overlap exception | Active product or overlap profile | README is strong: governed AI-assisted engineering control room. | https://github.com/novakprotocol/C.O.R.E./issues/12 |
| `niat` | Active infrastructure truth/data product | Infrastructure-as-truth boundary | Data-spine or active product profile | Strong separation of reviewed truth from live discovery. | https://github.com/novakprotocol/niat/issues/1 |
| `novare` | Active recovery/proof product | Recovery-proof truth | Active product profile | Appears to be real implementation for recovery/proof lane; may supersede empty `P.R.O.V.E.`. | https://github.com/novakprotocol/novare/issues/1 |
| `nsip` | Active execution-evidence product | Proof-before-action truth | Active product/evidence profile | Strong receipt, replay, proof-guard, bundle evidence lane. | https://github.com/novakprotocol/nsip/issues/1 |
| `S.I.G.I.L.` | Active governed-instruction product | Script/instruction governance truth | Active product profile | Clear script/instruction approval control-plane direction. | https://github.com/novakprotocol/S.I.G.I.L./issues/1 |
| `speech-protocol-lab` | Research/lab side repo | Lab truth only | Lightweight lab profile | Should not be merged wholesale into N-TRFACE; useful as reference only. | https://github.com/novakprotocol/speech-protocol-lab/issues/1 |
| `SSHIT` | Active access/evidence product | Access broker truth | Active product profile | README indicates product-facing name should be ProofPlane Access; issue creation blocked by connector. | Covered by master issue |
| `TouchDeck` | Historical/source-accounting and migration reference | Predecessor truth and migration residue | Historical/source-accounting profile | Valuable source-accounting repo for N-CTRL; do not port wholesale. | https://github.com/novakprotocol/TouchDeck/issues/265 |
| `V.I.S.O.R.` | Active visibility/glass product | Visibility layer truth | Active product profile | Strong rule: displays upstream truth, is not truth source. | https://github.com/novakprotocol/V.I.S.O.R./issues/1 |
| `va-location-reference-catalog` | Data/reference repo | Public-data truth boundary | Data/reference profile | Correctly separate from N-X; public-source only. | https://github.com/novakprotocol/va-location-reference-catalog/issues/15 |
| `W.R.A.P.I.T.` | Active CLI/evidence tool | Thin wrapper truth | CLI/tool profile | Strong focused lane; do not inflate into policy engine/orchestrator. | https://github.com/novakprotocol/W.R.A.P.I.T./issues/2 |
| `N-TRFACE` | Active command-interface backend | Command backend truth + N-App bridge status | Python/product profile | Should use `speech-protocol-lab` only as selective research input, not migration source. | https://github.com/novakprotocol/N-TRFACE/issues/4 |

## Alignment implementation sequence

For each active/documented repo:

1. Read repo current truth.
2. Run N-SDT report-only.
3. Decide whether N-SDT baseline is needed.
4. Run N-SDT baseline only if it fills real truth gaps and does not overwrite important docs.
5. Run `sdt doctor`.
6. Run RepoOps dry-run/report mode.
7. Choose the smallest fitting profile.
8. Record profile and exceptions.
9. Open a PR for changes.
10. Run local checks and record evidence.

## RepoOps profile guidance

| Repo class | Suggested profile |
|---|---|
| Python product/tool | `python-human-ai` or equivalent active tool profile |
| Browser/app UI product | `app-ui` |
| Data/reference repo | `data-spine` |
| Course/training repo | `course-repo` |
| Historical/source-accounting repo | lightweight historical/reference profile |
| Research/lab repo | `experimental-private` or lab profile |
| Empty placeholder | delete; do not align |

## What should happen next

### Immediate next actions

1. Delete the ten empty repositories manually if no external reason exists to preserve the slugs.
2. Start with `novare`, `nsip`, `W.R.A.P.I.T.`, `niat`, and `N-TRFACE` because they have the clearest active implementation signal.
3. For each, run N-SDT report-only and RepoOps dry-run.
4. Create PRs only for real gaps.
5. Do not modify `TouchDeck` beyond source-accounting and migration-residue documentation.
6. Review `SSHIT` naming/description separately; product appears to be ProofPlane Access.
7. Decide whether `P.R.O.V.E.` and `T.R.A.C.E.` should remain names at all after comparing with `novare` and ProofPlane Access.

### Stronger ideas found while reading

- `novare` appears to be the real recovery/proof implementation. Empty `P.R.O.V.E.` may be redundant.
- `SSHIT` appears to have a stronger product name already in README: ProofPlane Access. The slug should be reviewed later.
- `S.I.G.I.L.` has a clear product lane: governed script/instruction control plane. It should not be collapsed into generic proof tooling.
- `V.I.S.O.R.` has the right boundary: human glass over upstream truth, not a second truth source.
- `speech-protocol-lab` should remain a small lab, not a migration source for N-TRFACE.
- `TouchDeck` remains useful as predecessor/source-accounting for N-CTRL, but should not be treated as the current product.
- The DAY repos are not random junk; they look like workflow planes: baseline, build, change, and B2 transition lanes.

## Hard no-go items

- Do not align empty repos. Delete them or park them with one sentence only.
- Do not rename repos during this pass.
- Do not claim release readiness.
- Do not claim hosted CI passed without evidence.
- Do not force every repo into the same template.
- Do not let RepoOps decide product truth.
- Do not let N-SDT decide repo policy.
- Do not overwrite existing docs silently.
