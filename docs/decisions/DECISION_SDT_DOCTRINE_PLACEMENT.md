# Decision — SDT doctrine placement

## Decision
The full SDT doctrine lives in the SDT control-plane repo, not in every born repo by default.

## Born floor rule
Born repos receive operational truth, product truth, handoff truth, and status truth.
They do not automatically receive the full doctrine packet until that is directly justified.

## Why
- internal v0.1 is already cut without doctrine auto-birth
- prior auto-birth attempts were not clean enough
- control-plane doctrine is the safer immediate truth

## Revisit trigger
Revisit only after:
- doctrine wording is stable
- validator rules are defined
- born-floor cost is justified
