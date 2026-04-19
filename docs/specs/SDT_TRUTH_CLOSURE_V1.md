# SDT Truth Closure V1

## Goal

Close the gap between a good born floor and a self-refreshing truth system.

## Proven floor from latest fresh-specimen proof

- SDT main can birth a fresh specimen.
- Truth surfaces are created on birth.
- Fresh specimen app and test can run.
- Core truth surfaces exist.

## Gaps to close

1. Post-change truth refresh is not automatically closed out after meaningful repo mutation.
2. Project intelligence overweights shell wrappers and underweights application files and tests.
3. Placeholder-like text still leaks into core docs.
4. Trusted floor is not explicitly frozen or tagged.

## Deliverables

- `tools/install_truth_refresh_hooks.sh`
- `tools/run_truth_refresh_and_stage.sh`
- `tools/freeze_trusted_floor.sh`
- `tools/patch_project_intel_weights.py`
- `tools/clean_placeholder_docs.py`
- `tests/test_truth_closure_smoke.py`

## Execution order

1. Install local post-commit and post-merge hooks.
2. Make truth refresh/stage callable as one deterministic helper.
3. Patch project intelligence weighting.
4. Clean placeholder-like docs.
5. Freeze trusted floor explicitly with a tag.
6. Re-run fresh specimen proof.
