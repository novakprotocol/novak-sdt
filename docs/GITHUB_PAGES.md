# GitHub Pages

## What this repo includes

This repo includes a GitHub Pages publishing workflow and a public docs surface.

## What happens automatically

If the repo is configured for Pages with GitHub Actions, pushes to `main` can publish the docs site.

## What does not happen automatically for someone else

If another person clones or forks this repo, they get the workflow and docs files, but they do not automatically get a live hosted site on their own GitHub account.
They still need to enable Pages in their own repository settings.

## Local preview

Run:

    mkdocs serve -a 0.0.0.0:8001

Then open the local docs site in a browser.
