# S.D.T. (Software Digital Thread)

**Bootstrap or baseline repos with the SDT operator floor and product-truth floor.**

This repo also includes an optional GitHub Pages front door under `site/` for public docs, proofs, and report publishing.

## What this repo does

This repo gives you a simple CLI called `sdt` that can:

- create a new repo with the SDT operator floor and product-truth floor
- baseline an existing repo with missing SDT floor files
- generate a report-only baseline view without writing files
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
How people actually use novak-sdt

This is the plain-English answer you should give people.

If they ask “do I download it?”

Yes.

They either:

clone the repo, or
download the source zip from GitHub.
If they ask “then what?”

They install it locally and run one of three commands:

sdt new
sdt baseline
sdt doctor
The actual flow is this
For a brand new repo
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
For an existing repo
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

If they only want to inspect first
sdt baseline \
  --path /path/to/existing-repo \
  --product-name "Existing Product" \
  --product-statement "Existing Product is a product for X." \
  --report-only

That does not write files.
It only shows the gap report.

If they want to check whether a repo already has the floor
sdt doctor --path /path/to/repo

That tells them whether the required SDT floor files are present.

The simplest explanation to give people

Use this:

novak-sdt is a small tool that creates or adds the minimum survival structure a repo needs so the next human or AI can understand what the project is, what is real now, and what to do next.

Learn fast
docs/SDT_101.md
docs/EXAMPLE_BASELINE_BEFORE_AFTER.md
docs/DIAGRAM_01_OPERATIONAL_FLOW.md
docs/DIAGRAM_02_FILES_ADDED.md
docs/DIAGRAM_03_FRESHMAN_EXPLANATION.md
Rights

This repository is public for visibility and limited evaluation use.
It is not open source and it does not grant production, redistribution, managed-service, or commercial rights.

See:

LICENSE.txt
NOTICE.md\n- `docs/PUBLIC_VS_PRIVATE.md`\n
## Optional GitHub Pages site

This repo includes a simple static GitHub Pages front door under `site/` plus a Pages workflow under `.github/workflows/pages.yml`.

### What you get by default
If you clone or fork this repo, you get:
- the site files
- the Pages workflow
- the proof/docs/report pages

### What does not happen automatically
A live hosted Pages site is **not** enabled automatically on your GitHub repo just because these files exist.

### If you want your own live Pages site
After pushing the repo to GitHub:

1. Go to **Settings**
2. Go to **Pages**
3. Under **Build and deployment**
4. Set **Source** to **GitHub Actions**

Then wait for the **Deploy Pages** workflow to complete.

### Default project-site URL pattern
Your site URL will usually be:

`https://YOUR-GITHUB-NAME.github.io/YOUR-REPO-NAME/`

### Local preview
You can preview the static site locally:

```bash
cd site
python3 -m http.server 8000
```

Then open:

`http://localhost:8000/`

### Notes
- the Pages site is optional
- it is intended as a public front door, docs surface, and proof/report surface
- do not publish sensitive information in the Pages site
