# SDT notification rebuild spec

## Rule
Do not revive the old broad notification burst as one giant PR.

## Slice N1
- helper syntax clean
- notification status renders
- outbox ledger writes deterministically
- repro harness passes

## Slice N2
- routing and secret handling
- explicit policy docs
- no hidden assumptions

## Slice N3
- optional fanout or multi-channel work
- only after N1 and N2 are green

## Must not be claimed
- complete notification subsystem
- production-safe fanout
- final routing policy
