from __future__ import annotations

def extended_required_floor_files() -> list[str]:
    return [
        "mkdocs.yml",
        "docs/index.md",
        "docs/ABOUT.md",
        "docs/INSTALLATION.md",
        "docs/SYSTEM_AND_COMPONENT_STATUS.md",
        "docs/LATEST_RUN.md",
        "docs/LATEST_INVENTORY.md",
        "docs/FRESHNESS_GAUGE.md",
        "docs/history/ATTEMPTS.ndjson",
        "docs/history/HISTORY_INDEX.md",
        "docs/history/FAILURE_PATTERNS.md",
        "docs/history/MISSED_OPPORTUNITIES.md",
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
  - Latest Run: LATEST_RUN.md
  - Latest Inventory: LATEST_INVENTORY.md
  - Freshness Gauge: FRESHNESS_GAUGE.md
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
| Latest run placeholder | Confirmed if file exists | future execution truth surface | docs review | unknown | unknown | check `docs/LATEST_RUN.md` |
| Latest inventory placeholder | Confirmed if file exists | future runtime truth surface | docs review | unknown | unknown | check `docs/LATEST_INVENTORY.md` |
| Freshness gauge placeholder | Confirmed if file exists | future freshness surface | docs review | unknown | unknown | check `docs/FRESHNESS_GAUGE.md` |
""",
        "docs/LATEST_RUN.md": """# Latest Run

No run receipt has been recorded yet.
""",
        "docs/LATEST_INVENTORY.md": """# Latest Inventory

No inventory snapshot has been recorded yet.
""",
        "docs/FRESHNESS_GAUGE.md": """# Freshness Gauge

No freshness render has been recorded yet.
""",
        "docs/history/ATTEMPTS.ndjson": "",
        "docs/history/HISTORY_INDEX.md": """# History Index

No attempt history has been recorded yet.
""",
        "docs/history/FAILURE_PATTERNS.md": """# Failure Patterns

No failure patterns have been recorded yet.
""",
        "docs/history/MISSED_OPPORTUNITIES.md": """# Missed Opportunities

No missed opportunities have been recorded yet.
""",
    }
