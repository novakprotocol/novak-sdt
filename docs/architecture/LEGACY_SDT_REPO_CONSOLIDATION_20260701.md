# Legacy SDT Repo Consolidation - 2026-07-01

## Purpose

This document records the cleanup decision for older SDT support repos so the
active mental model is simple.

The active implementation is N-SDT in `novakprotocol/novak-sdt`.

## Disposition

| Repository | Final disposition | Why |
|---|---|---|
| `novakprotocol/novak-sdt` | Keep active. | Current N-SDT implementation with `sdt` CLI. |
| `novakprotocol/Archived20260701-novak-sdt-born-proof` | Archived historical proof. | One-time proof repo, not active infrastructure. |
| `novakprotocol/Archived20260701-novak-control-plane` | Archived legacy doctrine after extraction. | Portfolio/control-plane ideas are captured here instead of maintained as a separate active repo. |
| `novakprotocol/Archived20260701-novak-repo-template` | Archived legacy template after extraction. | Current repo birth path is `sdt new`; template parity is recorded in N-SDT. |
| `novakprotocol/W.R.A.P.I.T.` | Keep active. | Separate command receipt/evidence wrapper. |
| `novakprotocol/S.I.G.I.L.` | Keep active. | Product repo under SDT, not SDT itself. |

## What Was Preserved From `novak-control-plane`

The old control-plane repo carried useful doctrine:

- repo/project register thinking
- repo index thinking
- birth versus adoption lanes
- product-versus-system naming boundaries
- minimum repo-floor ideas
- portfolio-level "what exists and why" mapping

N-SDT preserves those ideas as current docs, not as a separate active control
plane repo.

The current rule is:

```text
N-SDT can document portfolio/control-plane doctrine.
N-SDT should not become a heavy portfolio database by default.
```

## What Was Preserved From `novak-repo-template`

The old template repo carried useful birth-floor ideas:

- README, project state, and current truth surfaces
- product truth files
- operator handoff files
- decision/history/status lanes
- "remove lanes that are not justified" rule

N-SDT preserves the active birth path through:

- `sdt new`
- `sdt baseline`
- `sdt baseline --report-only`
- `sdt doctor`
- generated product truth files
- generated operator continuity files
- generated report/status/history surfaces

Template parity details live in
`docs/architecture/SDT_BIRTH_TEMPLATE_PARITY.md`.

## What Was Preserved From `novak-sdt-born-proof`

The born-proof repo proved a historical path: a repo could be born from the old
SDT-aligned template.

That evidence is preserved by archiving the repo. It no longer needs to appear
as active infrastructure.

## Cleanup Rule

Archive old support repos only after their useful idea has a home in active
N-SDT docs or behavior.

Do not archive active products or tools just because they use SDT.
