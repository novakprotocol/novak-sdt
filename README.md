# S.D.T. (Software Digital Thread)

**Bootstrap or baseline repos with the SDT operator floor and product-truth floor.**

## What this repo does

This repo gives you a simple CLI called `sdt` that can:

- create a new repo with the SDT operator floor and product-truth floor
- baseline an existing repo with missing SDT floor files
- run a doctor check to show what is missing

## What it does not do

It does not magically invent your missing product truth.

If your repo does not clearly state:
- what the product is
- what is real now
- what is planned
- where product ends and supporting system begins

then `sdt` will scaffold those files and make the gap obvious, but a human still has to fill them in.

## Commands

### Create a new repo
```bash
sdt new \
  --path /tmp/my-product \
  --product-name "My Product" \
  --product-statement "My Product is a product for X." \
  --public-title "My Product" \
  --repo-summary "My Product under SDT."
```

### Baseline an existing repo
```bash
sdt baseline \
  --path /path/to/existing-repo \
  --product-name "Existing Product" \
  --product-statement "Existing Product is a product for X."
```

### Check a repo
```bash
sdt doctor --path /path/to/repo
```

## Rights

This repository is public for visibility and limited evaluation use.
It is **not** open source and it does **not** grant production, redistribution, managed-service, or commercial rights.

See:
- `LICENSE.txt`
- `NOTICE.md`

## Learn fast

- `docs/SDT_101.md`
- `docs/EXAMPLE_BASELINE_BEFORE_AFTER.md`
- `docs/DIAGRAM_01_OPERATIONAL_FLOW.md`
- `docs/DIAGRAM_02_FILES_ADDED.md`
- `docs/DIAGRAM_03_FRESHMAN_EXPLANATION.md`
