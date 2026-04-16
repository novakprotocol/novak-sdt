from __future__ import annotations

def extended_required_floor_files() -> list[str]:
    return [
        "mkdocs.yml",
        "docs/index.md",
        "docs/ABOUT.md",
        "docs/INSTALLATION.md",
        "docs/SYSTEM_AND_COMPONENT_STATUS.md",
    ]

def mkdocs_templates() -> dict[str, str]:
    return {
        "mkdocs.yml": """site_name: {{PUBLIC_TITLE}}
site_description: {{REPO_SUMMARY}}
repo_name: repo

theme:
  name: material
  features:
    - navigation.sections
    - navigation.tabs
    - navigation.top

plugins:
  - search

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences

nav:
  - Home: index.md
  - About: ABOUT.md
  - Installation: INSTALLATION.md
  - System and Component Status: SYSTEM_AND_COMPONENT_STATUS.md
""",
        "docs/index.md": """# {{PUBLIC_TITLE}}

## What this documentation is

This is the human-readable front door for {{PRODUCT_NAME}}.

It should explain:

- what this project is
- who owns it
- what version state it is in
- what it does
- how to install it
- how to rebuild it
- what the latest verified state is
""",
        "docs/ABOUT.md": """# About

## Name

**{{PUBLIC_TITLE}}**

## What it is

{{PRODUCT_STATEMENT}}
""",
        "docs/INSTALLATION.md": """# Installation

## Purpose

This page is the step-by-step installation and bootstrap path for this repo.

## Step 1 - Install SDT

Create a Python virtual environment and install `novak-sdt` editable.

## Step 2 - Create or baseline the repo

Use `sdt new` for a new repo or `sdt baseline` for an existing repo.

## Step 3 - Build docs

If MkDocs is installed in the repo, run `mkdocs build`.
""",
        "docs/SYSTEM_AND_COMPONENT_STATUS.md": """# System and Component Status

This page is the truthful current component view for this repo.

| Component | Current status | Primary purpose | Used with | Date installed or first verified | Last updated | How to install or verify |
|---|---|---|---|---|---|---|
| SDT repo floor | Confirmed at birth or baseline | continuity and truth floor | repo docs | unknown | unknown | run `sdt doctor --path <repo>` |
| MkDocs floor | Confirmed if these files exist | human-readable docs surface | local docs build or Pages later | unknown | unknown | check for `mkdocs.yml` and docs pages |
""",
    }
