# S.D.T. (Software Digital Thread)

**Bootstrap or baseline repos with the SDT operator floor and product-truth floor.**

This repo also includes an optional GitHub Pages front door under `site/` for public docs, proofs, and report publishing.

SDT is not a coding assistant replacement. It is a repo continuity and truth layer that helps humans, Copilot, and future AI work against the same repo with less hidden context.

## What this repo does

This repo gives you a simple CLI called `sdt` that can:

- create a new repo with the SDT operator floor and product-truth floor
- baseline an existing repo with missing SDT floor files
- generate a report-only baseline view without writing files
- run a doctor check to show what is missing
- generate Markdown and HTML repo reports

## What it does not do

It does not magically invent missing product truth.

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
Baseline an existing repo
sdt baseline \
  --path /path/to/existing-repo \
  --product-name "Existing Product" \
  --product-statement "Existing Product is a product for X."
Report only
sdt baseline \
  --path /path/to/existing-repo \
  --product-name "Existing Product" \
  --product-statement "Existing Product is a product for X." \
  --report-only
Check a repo
sdt doctor --path /path/to/repo
Generate a repo report
python3 tools/sdt_repo_report.py --path /path/to/repo
How people actually use novak-sdt
Do I download it?

Yes.

You either:

clone the repo, or
download the source zip from GitHub.
Then what?

Install it locally and run one of these:

sdt new
sdt baseline
sdt doctor
python3 tools/sdt_repo_report.py --path ...
Brand new repo flow
git clone https://github.com/novakprotocol/novak-sdt.git
cd novak-sdt
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .

sdt new \
  --path /tmp/my-product \
  --product-name "My Product" \
  --product-statement "My Product is a product for X."

That creates a new repo folder with:

operator floor files
product truth floor files
a baseline gap report
Existing repo flow
git clone https://github.com/novakprotocol/novak-sdt.git
cd novak-sdt
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .

sdt baseline \
  --path /path/to/existing-repo \
  --product-name "Existing Product" \
  --product-statement "Existing Product is a product for X."

That adds the SDT floor files to an existing repo.

Inspect first without writing files
sdt baseline \
  --path /path/to/existing-repo \
  --product-name "Existing Product" \
  --product-statement "Existing Product is a product for X." \
  --report-only

That only shows the gap report.

Generate a Markdown and HTML report
python3 tools/sdt_repo_report.py --path /path/to/repo

That generates:

docs/status/SDT_REPO_REPORT.md
docs/status/SDT_REPO_REPORT.html
Optional GitHub Pages site

This repo includes a simple static GitHub Pages front door under site/ plus a Pages workflow under .github/workflows/pages.yml.

What you get by default

If you clone or fork this repo, you get:

the site files
the Pages workflow
the proof/docs/report pages
What does not happen automatically

A live hosted Pages site is not enabled automatically on your GitHub repo just because these files exist.

If you want your own live Pages site

After pushing the repo to GitHub:

Go to Settings
Go to Pages
Under Build and deployment
Set Source to GitHub Actions

Then wait for the Deploy Pages workflow to complete.

Default project-site URL pattern

Your site URL will usually be:

https://YOUR-GITHUB-NAME.github.io/YOUR-REPO-NAME/

Local preview
cd site
python3 -m http.server 8000

Then open:

http://localhost:8000/

Notes
the Pages site is optional
it is intended as a public front door, docs surface, and proof/report surface
do not publish sensitive information in the Pages site
Learn fast
docs/SDT_101.md
docs/EXAMPLE_BASELINE_BEFORE_AFTER.md
docs/DIAGRAM_01_OPERATIONAL_FLOW.md
docs/DIAGRAM_02_FILES_ADDED.md
docs/DIAGRAM_03_FRESHMAN_EXPLANATION.md
docs/PUBLIC_VS_PRIVATE.md
Rights

This repository is public for visibility and limited evaluation use.
It is not open source and it does not grant production, redistribution, managed-service, or commercial rights.

See:

LICENSE.txt
NOTICE.md

## Plain-English explanation

SDT is a small repo setup and cleanup tool. It gives a repo the minimum structure needed so a human or AI can quickly understand what the repo is, what is real now, and what to do next.

In plain terms:
- it helps new repos start cleaner
- it helps messy repos become easier to understand
- it helps teams stop losing project truth in chats, heads, and scattered files

## Advanced ops

For serious server or infra repos, SDT now also supports:

- serious-mode execution receipts via `bash bin/sdt-serious-run.sh ...`
- runtime inventory snapshots via `bash bin/sdt-inventory-snapshot.sh <repo_path> <label>`

Use inventory mode for before/after server truth.

## Documentation Doctrine

Documentation is part of the product, not an afterthought.

**Principle**

Every meaningful coding action should leave behind enough structured truth that a new human or AI can understand what was built, why it changed, what failed, what is currently real, and what should happen next — without exposing secrets or burying signal in noise.

Every meaningful coding action should leave behind enough structured truth that a new human or AI can understand:

- what was built
- why it changed
- what failed
- what is currently real
- what should happen next

Our standard is not maximum volume. Our standard is documentation that is:

- accurate
- structured
- current
- task-oriented
- security-aware

We separate documentation into clear lanes:

- **Human docs** — purpose, architecture, setup, operation, recovery, and current truth
- **Operational evidence** — runs, changes, failures, trends, signals, and priority
- **Security-aware records** — controls, boundaries, approvals, and process, never secrets

Documentation must reduce mystery, preserve continuity, support recovery, and improve safe reuse by both humans and AI.

Do not bury signal in noise.  
Do not present assumptions as facts.  
Do not expose secrets, credentials, or unnecessary internal risk.

If it matters, it should be documented clearly enough that work can continue without the original author.

