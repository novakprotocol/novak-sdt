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
        "bin/history-import.sh",
        "tools/archive_history_log.py",
        "tools/render_project_docs_status.py",
        "tools/render_freshness_gauge.py",
        ".github/workflows/pages.yml",
    ]

def mkdocs_and_history_templates() -> dict[str, str]:
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
  - History:
      - History Index: history/HISTORY_INDEX.md
      - Failure Patterns: history/FAILURE_PATTERNS.md
      - Missed Opportunities: history/MISSED_OPPORTUNITIES.md
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

## Install SDT

Create a Python virtual environment and install novak-sdt editable.

## Create a new repo

Run sdt new with product name, product statement, public title, and repo summary.

## Baseline an existing repo

Run sdt baseline against the existing repo path.

## Render docs

Run python3 tools/render_project_docs_status.py and python3 tools/render_freshness_gauge.py.
""",
        "docs/SYSTEM_AND_COMPONENT_STATUS.md": """# System and Component Status

This page is the truthful current component view for this repo.

| Component | Current status | Primary purpose | Used with | Date installed or first verified | Last updated | How to install or verify |
|---|---|---|---|---|---|---|
| SDT repo floor | Confirmed at birth or baseline | continuity and truth floor | repo docs | unknown | unknown | run sdt doctor --path <repo> |
| MkDocs floor | Confirmed if these files exist | human-readable docs surface | Pages or local docs build | unknown | unknown | check mkdocs.yml and docs pages |
| History lane | Confirmed if history files exist | attempt tracking and later analysis | raw logs and docs | unknown | unknown | check docs/history and bin/history-import.sh |
""",
        "docs/LATEST_RUN.md": """# Latest Run

No run receipt found yet.
""",
        "docs/LATEST_INVENTORY.md": """# Latest Inventory

No inventory snapshot found yet.
""",
        "docs/FRESHNESS_GAUGE.md": """# Freshness Gauge

No freshness render has been generated yet.
""",
        "docs/history/ATTEMPTS.ndjson": "",
        "docs/history/HISTORY_INDEX.md": """# History Index

This page summarizes archived run attempts, outcomes, and next steps.
""",
        "docs/history/FAILURE_PATTERNS.md": """# Failure Patterns

This page summarizes recurring failure modes discovered from archived run logs.
""",
        "docs/history/MISSED_OPPORTUNITIES.md": """# Missed Opportunities

This page is the review surface for repeated avoidable failures and hardening gaps.
""",
        "bin/history-import.sh": """#!/usr/bin/env bash
set -Eeuo pipefail
set +H

if [[ $# -lt 1 ]]; then
  echo "Usage: bash bin/history-import.sh /path/to/log1.txt [/path/to/log2.txt ...]"
  exit 1
fi

ARGS=()
for f in "$@"; do
  ARGS+=(--log-file "$f")
done

python3 tools/archive_history_log.py "${ARGS[@]}"
python3 tools/render_project_docs_status.py
python3 tools/render_freshness_gauge.py
""",
        "tools/archive_history_log.py": """#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, re, shutil
from datetime import UTC, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HISTORY = REPO / "docs" / "history"
RAW = HISTORY / "raw"
LEDGER = HISTORY / "ATTEMPTS.ndjson"
INDEX_MD = HISTORY / "HISTORY_INDEX.md"
FAIL_MD = HISTORY / "FAILURE_PATTERNS.md"
MISSED_MD = HISTORY / "MISSED_OPPORTUNITIES.md"
RUN_BLOCK = re.compile(r"RUN_LABEL:\\s+(?P<label>.+?)\\n.*?START_UTC:\\s+(?P<start>.+?)\\n.*?STATUS:\\s+(?P<status>PASS|FAIL).*?END_UTC:\\s+(?P<end>.+?)\\nRUN_ELAPSED_SEC:\\s+(?P<elapsed>\\d+)", re.S)

def now_utc() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def load_rows() -> list[dict]:
    if not LEDGER.exists():
        return []
    out = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except Exception:
            pass
    return out

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--log-file", action="append", required=True)
    args = p.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    HISTORY.mkdir(parents=True, exist_ok=True)
    rows = load_rows()
    for name in args.log_file:
        src = Path(name).expanduser().resolve()
        if not src.exists():
            print(f"SKIP missing log file: {src}")
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        dst = RAW / f"{now_utc()}__{src.name}"
        shutil.copy2(src, dst)
        matches = list(RUN_BLOCK.finditer(text))
        if not matches:
            rows.append({"record_type":"log_only","source_name":src.name,"raw_log":f"raw/{dst.name}","status":"UNKNOWN","run_label":src.name,"start_utc":"","end_utc":"","elapsed_sec":None,"source_sha256":sha256_text(text)})
        else:
            for m in matches:
                rows.append({"record_type":"run_attempt","source_name":src.name,"raw_log":f"raw/{dst.name}","status":m.group("status").strip(),"run_label":m.group("label").strip(),"start_utc":m.group("start").strip(),"end_utc":m.group("end").strip(),"elapsed_sec":int(m.group("elapsed")),"source_sha256":sha256_text(text)})
    with LEDGER.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True) + "\\n")
    attempts = [r for r in rows if r.get("record_type") == "run_attempt"]
    INDEX_MD.write_text("# History Index\\n\\n- generated_utc: `" + now_utc() + "`\\n- total_attempts: `" + str(len(attempts)) + "`\\n", encoding="utf-8")
    FAIL_MD.write_text("# Failure Patterns\\n\\n- generated_utc: `" + now_utc() + "`\\n", encoding="utf-8")
    MISSED_MD.write_text("# Missed Opportunities\\n\\nUse this page to review repeated failures, retries, and avoidable confusion.\\n", encoding="utf-8")
    print(f"WROTE {LEDGER}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
""",
        "tools/render_project_docs_status.py": """#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
docs = repo / "docs"
status = docs / "status"
run_json = status / "LATEST_RUN.json"
inv_json = status / "LATEST_INVENTORY.json"
run_md = ["# Latest Run", "", "No run receipt found yet."]
inv_md = ["# Latest Inventory", "", "No inventory snapshot found yet."]
if run_json.exists():
    try:
        d = json.loads(run_json.read_text(encoding="utf-8"))
        run_md = ["# Latest Run", "", f"- status: `{d.get('status', 'UNSET')}`", f"- run_label: `{d.get('run_label', 'UNSET')}`", f"- next_step: `{d.get('next_step', 'UNSET')}`"]
    except Exception:
        pass
if inv_json.exists():
    try:
        d = json.loads(inv_json.read_text(encoding="utf-8"))
        h = d.get("host", {})
        inv_md = ["# Latest Inventory", "", f"- label: `{d.get('label', 'UNSET')}`", f"- host: `{h.get('hostname', 'UNSET')}`", f"- platform: `{h.get('platform', 'UNSET')}`"]
    except Exception:
        pass
(docs / "LATEST_RUN.md").write_text("\\n".join(run_md) + "\\n", encoding="utf-8")
(docs / "LATEST_INVENTORY.md").write_text("\\n".join(inv_md) + "\\n", encoding="utf-8")
print("WROTE docs/LATEST_RUN.md")
print("WROTE docs/LATEST_INVENTORY.md")
""",
        "tools/render_freshness_gauge.py": """#!/usr/bin/env python3
from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
docs = repo / "docs"
status = docs / "status"
now = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
content = f"""# Freshness Gauge

- generated_utc: `{now}`
- latest_run_present: `{(status / "LATEST_RUN.json").exists()}`
- latest_inventory_present: `{(status / "LATEST_INVENTORY.json").exists()}`
- history_ledger_present: `{(docs / "history" / "ATTEMPTS.ndjson").exists()}`
"""
(docs / "FRESHNESS_GAUGE.md").write_text(content, encoding="utf-8")
print(f"WROTE {docs / 'FRESHNESS_GAUGE.md'}")
""",
        ".github/workflows/pages.yml": """name: Deploy MkDocs site

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install docs dependencies
        run: |
          python -m pip install --upgrade pip
          pip install mkdocs-material

      - name: Render docs status
        run: |
          python tools/render_project_docs_status.py
          python tools/render_freshness_gauge.py

      - name: Build site
        run: |
          mkdocs build --site-dir site

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
""",
    }
