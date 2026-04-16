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
        "docs/history/HISTORY_SUMMARY.md",
        "docs/history/FAILURE_PATTERNS.md",
        "docs/history/MISSED_OPPORTUNITIES.md",
        "docs/SDT_HISTORY_LANE.md",
        "tools/render_project_docs_status.py",
        "tools/render_freshness_gauge.py",
        "tools/archive_history_log.py",
        "bin/history-import.sh",
        ".github/workflows/pages.yml",
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
  - History Lane: SDT_HISTORY_LANE.md
  - History:
      - History Index: history/HISTORY_INDEX.md
      - History Summary: history/HISTORY_SUMMARY.md
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

## Step 1 - Install SDT

Create a Python virtual environment and install `novak-sdt` editable.

## Step 2 - Create or baseline the repo

Use `sdt new` for a new repo or `sdt baseline` for an existing repo.

## Step 3 - Build docs

If MkDocs is installed in the repo, run `mkdocs build`.

## Step 4 - Import history when needed

Use `bin/history-import.sh <logfile>` to archive a pasted operator log into the repo history lane.
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
| Render helper scripts | Confirmed if file exists | status and freshness rendering | docs/status JSON inputs | unknown | unknown | run the helper scripts in `tools/` |
| Pages workflow | Confirmed if workflow file exists | publish docs automatically | GitHub Pages | unknown | unknown | check `.github/workflows/pages.yml` |
| History import tooling | Confirmed if script exists | archive pasted operator history | docs/history lane | unknown | unknown | run `bin/history-import.sh <logfile>` |
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
        "docs/SDT_HISTORY_LANE.md": """# SDT History Lane

## Purpose

This repo can archive pasted operator logs into a structured history lane.

## What it should capture

- source log name
- archive stamp
- attempt summary
- failure patterns
- missed opportunities
- raw archived log copy reference

## Entry point

Use:

```bash
bin/history-import.sh /path/to/log.txt

""",
"docs/history/ATTEMPTS.ndjson": "",
"docs/history/HISTORY_INDEX.md": """# History Index

No attempt history has been recorded yet.
""",
        "docs/history/HISTORY_SUMMARY.md": """# History Summary

No history summary has been recorded yet.
""",
"docs/history/FAILURE_PATTERNS.md": """# Failure Patterns

No failure patterns have been recorded yet.
""",
"docs/history/MISSED_OPPORTUNITIES.md": """# Missed Opportunities

No missed opportunities have been recorded yet.
""",
"tools/render_project_docs_status.py": """#!/usr/bin/env python3
from future import annotations

import json
from pathlib import Path

repo = Path(file).resolve().parent.parent
docs = repo / "docs"
status = docs / "status"

docs.mkdir(parents=True, exist_ok=True)
status.mkdir(parents=True, exist_ok=True)

run_json = status / "LATEST_RUN.json"
inv_json = status / "LATEST_INVENTORY.json"

run_md = ["# Latest Run", "", "No run receipt has been recorded yet."]
inv_md = ["# Latest Inventory", "", "No inventory snapshot has been recorded yet."]

if run_json.exists():
try:
data = json.loads(run_json.read_text(encoding="utf-8"))
timing = data.get("timing", {})
notes_value = data.get("notes", "")

    if isinstance(notes_value, list):
        notes_lines = [f"- {x}" for x in notes_value] if notes_value else ["- none"]
    else:
        notes_text = str(notes_value).strip()
        notes_lines = [notes_text] if notes_text else ["- none"]

    run_md = [
        "# Latest Run",
        "",
        f"- run_label: `{data.get('run_label', 'UNSET')}`",
        f"- status: `{data.get('status', 'UNSET')}`",
        f"- generated_utc: `{data.get('generated_utc', 'UNSET')}`",
        f"- start_time: `{timing.get('start_local', 'UNSET')}`",
        f"- finish_time: `{timing.get('end_local', 'UNSET')}`",
        f"- elapsed_seconds: `{timing.get('run_elapsed_sec', 'UNSET')}`",
        f"- next_step: `{data.get('next_step', 'UNSET') or 'UNSET'}`",
        "",
        "## Notes",
        *notes_lines,
    ]
except Exception as exc:
    run_md = [
        "# Latest Run",
        "",
        f"Failed to render run status: `{exc}`",
    ]

if inv_json.exists():
try:
data = json.loads(inv_json.read_text(encoding="utf-8"))
host = data.get("host", {})
inv_md = [
"# Latest Inventory",
"",
f"- label: {data.get('label', 'UNSET')}",
f"- generated_utc: {data.get('generated_utc', 'UNSET')}",
f"- host: {host.get('hostname', 'UNSET')}",
f"- fqdn: {host.get('fqdn', 'UNSET')}",
f"- platform: {host.get('platform', 'UNSET')}",
f"- python: {host.get('python', 'UNSET')}",
]
except Exception as exc:
inv_md = [
"# Latest Inventory",
"",
f"Failed to render inventory status: {exc}",
]

(docs / "LATEST_RUN.md").write_text("\n".join(run_md) + "\n", encoding="utf-8")
(docs / "LATEST_INVENTORY.md").write_text("\n".join(inv_md) + "\n", encoding="utf-8")

print("WROTE docs/LATEST_RUN.md")
print("WROTE docs/LATEST_INVENTORY.md")
""",
"tools/render_freshness_gauge.py": """#!/usr/bin/env python3
from future import annotations

from datetime import UTC, datetime
from pathlib import Path

repo = Path(file).resolve().parent.parent
docs = repo / "docs"
status = docs / "status"

docs.mkdir(parents=True, exist_ok=True)
status.mkdir(parents=True, exist_ok=True)

run_json = status / "LATEST_RUN.json"
inv_json = status / "LATEST_INVENTORY.json"
now = datetime.now(UTC)

def age_days(path: Path) -> int | None:
if not path.exists():
return None
m return None
mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=UTC)
return (now - mtime).days

def classify(age: int | None) -> str:
if age is None:
return "unknown"
if age <= 7:
return "fresh"
if age <= 30:
return "aging"
return "stale"

run_age = age_days(run_json)
inv_age = age_days(inv_json)

lines = [
"# Freshness Gauge",
"",
f"- generated_utc: {now.strftime('%Y-%m-%d %H:%M:%S UTC')}",
f"- latest_run_json_age_days: {run_age if run_age is not None else 'missing'}",
f"- latest_inventory_json_age_days: {inv_age if inv_age is not None else 'missing'}",
f"- run_status: {classify(run_age)}",
f"- inventory_status: {classify(inv_age)}",
]

(docs / "FRESHNESS_GAUGE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("WROTE docs/FRESHNESS_GAUGE.md")
""",
        "tools/archive_history_log.py": """#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
import sys
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path


def classify_failure(line: str) -> str:
    lowered = line.lower()
    if "permission denied" in lowered:
        return "permission"
    if "command not found" in lowered:
        return "missing-command"
    if "traceback" in lowered:
        return "python-traceback"
    if "syntaxerror" in lowered:
        return "python-syntax"
    if "indentationerror" in lowered:
        return "python-indentation"
    if "mkdocs" in lowered:
        return "mkdocs"
    if "error" in lowered or "fail" in lowered:
        return "generic-error"
    return "other"


def is_failure_line(line: str) -> bool:
    lowered = line.lower()
    return any(token in lowered for token in ("fail", "error", "traceback", "mkdocs"))


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: archive_history_log.py <logfile>", file=sys.stderr)
        return 2

    source = Path(sys.argv[1]).resolve()
    if not source.is_file():
        print(f"ERROR: log file not found: {source}", file=sys.stderr)
        return 1

    repo = Path(__file__).resolve().parent.parent
    docs = repo / "docs"
    history = docs / "history"
    raw_dir = history / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    target = raw_dir / f"{stamp}-{source.name}"
    shutil.copy2(source, target)

    text = source.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    failure_lines = [line for line in lines if is_failure_line(line)]
    missed_lines = [
        line for line in lines
        if "Permission denied" in line or "command not found" in line
    ]
    failure_classes = Counter(classify_failure(line) for line in failure_lines)

    attempt_record = {
        "archived_utc": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "source_name": source.name,
        "archived_copy": str(target.relative_to(repo)),
        "line_count": len(lines),
        "failure_line_count": len(failure_lines),
        "missed_opportunity_count": len(missed_lines),
        "failure_classes": dict(sorted(failure_classes.items())),
    }

    attempts_path = history / "ATTEMPTS.ndjson"
    with attempts_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(attempt_record, sort_keys=True) + "\\n")

    records: list[dict] = []
    for raw_line in attempts_path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip():
            continue
        try:
            records.append(json.loads(raw_line))
        except json.JSONDecodeError:
            continue

    latest_record = records[-1] if records else attempt_record
    attempt_count = len(records)
    total_failure_lines = sum(int(record.get("failure_line_count", 0)) for record in records)
    total_missed_lines = sum(int(record.get("missed_opportunity_count", 0)) for record in records)

    aggregate_failure_classes = Counter()
    for record in records:
        classes = record.get("failure_classes", {}) or {}
        for key, value in classes.items():
            try:
                aggregate_failure_classes[str(key)] += int(value)
            except (TypeError, ValueError):
                continue

    history_index = history / "HISTORY_INDEX.md"
    history_summary = history / "HISTORY_SUMMARY.md"
    failure_patterns = history / "FAILURE_PATTERNS.md"
    missed_opportunities = history / "MISSED_OPPORTUNITIES.md"

    history_index.write_text(
        "# History Index\\n\\n"
        f"- latest_archive: `{latest_record.get(\"archived_utc\", \"unknown\")}`\\n"
        f"- source_name: `{latest_record.get(\"source_name\", \"unknown\")}`\\n"
        f"- archived_copy: `{latest_record.get(\"archived_copy\", \"unknown\")}`\\n"
        f"- line_count: `{latest_record.get(\"line_count\", 0)}`\\n",
        encoding="utf-8",
    )

    history_summary.write_text(
        "# History Summary\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- latest_source_name: `{latest_record.get(\"source_name\", \"unknown\")}`\\n"
        f"- total_failure_lines_across_all_imports: `{total_failure_lines}`\\n"
        f"- total_missed_opportunity_lines_across_all_imports: `{total_missed_lines}`\\n"
        f"- total_failure_lines_in_latest_import: `{latest_record.get(\"failure_line_count\", 0)}`\\n"
        f"- total_missed_opportunity_lines_in_latest_import: `{latest_record.get(\"missed_opportunity_count\", 0)}`\\n"
        "\\n## Failure Classes In Latest Import\\n"
        + (
            "\\n".join(
                f"- {key}: {value}"
                for key, value in sorted((latest_record.get(\"failure_classes\", {}) or {}).items())
            )
            if (latest_record.get(\"failure_classes\", {}) or {})
            else "- none"
        )
        + "\\n\\n## Failure Classes Across All Imports\\n"
        + (
            "\\n".join(
                f"- {key}: {value}"
                for key, value in sorted(aggregate_failure_classes.items())
            )
            if aggregate_failure_classes
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    failure_patterns.write_text(
        "# Failure Patterns\\n\\n"
        + (
            "\\n".join(
                f"- {re.sub(r'`', "\'", line[:200])}"
                for line in failure_lines[:25]
            )
            if failure_lines
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    missed_opportunities.write_text(
        "# Missed Opportunities\\n\\n"
        + (
            "\\n".join(
                f"- {re.sub(r'`', "\'", line[:200])}"
                for line in missed_lines[:25]
            )
            if missed_lines
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    print(f"ARCHIVED {source} -> {target}")
    print(f"UPDATED {attempts_path}")
    print(f"UPDATED {history_index}")
    print(f"UPDATED {history_summary}")
    print(f"UPDATED {failure_patterns}")
    print(f"UPDATED {missed_opportunities}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
        "bin/history-import.sh": """#!/usr/bin/env bash
set -Eeuo pipefail
set +H

if [[ $# -ne 1 ]]; then
echo "usage: bin/history-import.sh <logfile>" >&2
exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

python3 "${REPO_ROOT}/tools/archive_history_log.py" "$1"
""",
".github/workflows/pages.yml": """name: Pages

on:
push:
branches:
- main
workflow_dispatch:

permissions:
contents: read
pages: write
id-token: write

jobs:
build:
runs-on: ubuntu-latest

steps:
  - name: Checkout
    uses: actions/checkout@v4

  - name: Setup Python
    uses: actions/setup-python@v5
    with:
      python-version: '3.12'

  - name: Install MkDocs
    run: |
      python -m pip install --upgrade pip
      python -m pip install mkdocs mkdocs-material pymdown-extensions

  - name: Build site
    run: mkdocs build

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
