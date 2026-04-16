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
        "docs/history/HISTORY_TRENDS.md",
        "docs/history/HISTORY_SIGNALS.md",
        "docs/history/HISTORY_OPERATOR_PAIN.md",
        "docs/history/HISTORY_PRIORITY_QUEUE.md",
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
      - History Trends: history/HISTORY_TRENDS.md
      - History Signals: history/HISTORY_SIGNALS.md
      - History Operator Pain: history/HISTORY_OPERATOR_PAIN.md
      - History Priority Queue: history/HISTORY_PRIORITY_QUEUE.md
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
        "docs/history/HISTORY_TRENDS.md": """# History Trends

No history trends have been recorded yet.
""",
        "docs/history/HISTORY_SIGNALS.md": """# History Signals

No history signals have been recorded yet.
""",
        "docs/history/HISTORY_OPERATOR_PAIN.md": """# History Operator Pain

No operator pain summary has been recorded yet.
""",
        "docs/history/HISTORY_PRIORITY_QUEUE.md": """# History Priority Queue

No history priority queue has been recorded yet.
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
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path


SEVERITY_WEIGHTS = {
    "other": 1,
    "generic-error": 2,
    "mkdocs": 3,
    "python-traceback": 4,
    "permission": 5,
    "missing-command": 5,
    "python-syntax": 6,
    "python-indentation": 6,
}


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


def compare_signal(latest: int, previous: int | None) -> str:
    if previous is None:
        return "no-prior"
    if latest > previous:
        return "worse"
    if latest < previous:
        return "better"
    return "flat"


def rolling_average(values: list[int | float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def compare_to_average(latest: int | float, average: float | None) -> str:
    if average is None:
        return "no-prior"
    if latest >= max(average * 1.5, average + 1.0):
        return "spike"
    if latest > average:
        return "worse"
    if latest < average:
        return "improving"
    return "stable"


def fmt_avg(value: float | None) -> str:
    if value is None:
        return "none"
    return f"{value:.2f}"


def severity_weight_for_class(name: str) -> int:
    return int(SEVERITY_WEIGHTS.get(name, 1))


def decayed_priority_score(name: str, records: list[dict]) -> float:
    score = 0.0
    for age, record in enumerate(reversed(records)):
        classes = record.get("failure_classes", {}) or {}
        count = int(classes.get(name, 0) or 0)
        if count <= 0:
            continue
        score += float(count * severity_weight_for_class(name)) * (0.85 ** age)
    return score


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

    weighted_severity_total = sum(
        severity_weight_for_class(key) * int(value)
        for key, value in failure_classes.items()
    )

    attempt_record = {
        "archived_utc": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "source_name": source.name,
        "archived_copy": str(target.relative_to(repo)),
        "line_count": len(lines),
        "failure_line_count": len(failure_lines),
        "missed_opportunity_count": len(missed_lines),
        "failure_classes": dict(sorted(failure_classes.items())),
        "weighted_severity_total": weighted_severity_total,
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
    previous_record = records[-2] if len(records) >= 2 else None
    prior_window = records[-6:-1] if len(records) >= 2 else []
    current_window_3 = records[-3:] if records else []
    previous_window_3 = records[-6:-3] if len(records) >= 6 else []
    attempt_count = len(records)

    total_failure_lines = sum(int(record.get("failure_line_count", 0)) for record in records)
    total_missed_lines = sum(int(record.get("missed_opportunity_count", 0)) for record in records)

    aggregate_failure_classes = Counter()
    trend_map: dict[str, dict[str, object]] = defaultdict(
        lambda: {
            "imports_seen": 0,
            "total_lines": 0,
            "first_seen": None,
            "latest_seen": None,
        }
    )

    for record in records:
        classes = record.get("failure_classes", {}) or {}
        archived_utc = str(record.get("archived_utc", "unknown"))
        for key, value in classes.items():
            try:
                count = int(value)
            except (TypeError, ValueError):
                continue
            cls = str(key)
            aggregate_failure_classes[cls] += count
            trend = trend_map[cls]
            trend["imports_seen"] = int(trend["imports_seen"]) + 1
            trend["total_lines"] = int(trend["total_lines"]) + count
            if trend["first_seen"] is None:
                trend["first_seen"] = archived_utc
            trend["latest_seen"] = archived_utc

    recurring_classes = {
        key: value for key, value in trend_map.items()
        if int(value["imports_seen"]) >= 2
    }
    one_off_classes = {
        key: value for key, value in trend_map.items()
        if int(value["imports_seen"]) == 1
    }

    history_index = history / "HISTORY_INDEX.md"
    history_summary = history / "HISTORY_SUMMARY.md"
    history_trends = history / "HISTORY_TRENDS.md"
    history_signals = history / "HISTORY_SIGNALS.md"
    history_operator_pain = history / "HISTORY_OPERATOR_PAIN.md"
    history_priority_queue = history / "HISTORY_PRIORITY_QUEUE.md"
    failure_patterns = history / "FAILURE_PATTERNS.md"
    missed_opportunities = history / "MISSED_OPPORTUNITIES.md"

    history_index.write_text(
        "# History Index\\n\\n"
        f"- latest_archive: `{latest_record.get('archived_utc', 'unknown')}`\\n"
        f"- source_name: `{latest_record.get('source_name', 'unknown')}`\\n"
        f"- archived_copy: `{latest_record.get('archived_copy', 'unknown')}`\\n"
        f"- line_count: `{latest_record.get('line_count', 0)}`\\n",
        encoding="utf-8",
    )

    history_summary.write_text(
        "# History Summary\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- latest_source_name: `{latest_record.get('source_name', 'unknown')}`\\n"
        f"- total_failure_lines_across_all_imports: `{total_failure_lines}`\\n"
        f"- total_missed_opportunity_lines_across_all_imports: `{total_missed_lines}`\\n"
        f"- total_failure_lines_in_latest_import: `{latest_record.get('failure_line_count', 0)}`\\n"
        f"- total_missed_opportunity_lines_in_latest_import: `{latest_record.get('missed_opportunity_count', 0)}`\\n"
        f"- weighted_severity_total_in_latest_import: `{latest_record.get('weighted_severity_total', 0)}`\\n"
        "\\n## Failure Classes In Latest Import\\n"
        + (
            "\\n".join(
                f"- {key}: {value}"
                for key, value in sorted((latest_record.get('failure_classes', {}) or {}).items())
            )
            if (latest_record.get('failure_classes', {}) or {})
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

    history_trends.write_text(
        "# History Trends\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- recurring_failure_class_count: `{len(recurring_classes)}`\\n"
        f"- one_off_failure_class_count: `{len(one_off_classes)}`\\n"
        "\\n## Recurring Failure Classes\\n"
        + (
            "\\n".join(
                f"- {key}: imports_seen={int(value['imports_seen'])}, total_lines={int(value['total_lines'])}, first_seen={value['first_seen']}, latest_seen={value['latest_seen']}"
                for key, value in sorted(recurring_classes.items())
            )
            if recurring_classes
            else "- none"
        )
        + "\\n\\n## One-Off Failure Classes\\n"
        + (
            "\\n".join(
                f"- {key}: imports_seen={int(value['imports_seen'])}, total_lines={int(value['total_lines'])}, first_seen={value['first_seen']}, latest_seen={value['latest_seen']}"
                for key, value in sorted(one_off_classes.items())
            )
            if one_off_classes
            else "- none"
        )
        + "\\n\\n## Latest 5 Imports\\n"
        + (
            "\\n".join(
                f"- {record.get('archived_utc', 'unknown')} | {record.get('source_name', 'unknown')} | failure_lines={record.get('failure_line_count', 0)} | missed_opportunities={record.get('missed_opportunity_count', 0)} | weighted_severity={record.get('weighted_severity_total', 0)}"
                for record in records[-5:]
            )
            if records
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    latest_classes = latest_record.get("failure_classes", {}) or {}
    previous_classes = previous_record.get("failure_classes", {}) or {} if previous_record else {}
    latest_failure_lines_count = int(latest_record.get("failure_line_count", 0))
    previous_failure_lines_count = int(previous_record.get("failure_line_count", 0)) if previous_record else None
    latest_missed_count = int(latest_record.get("missed_opportunity_count", 0))
    previous_missed_count = int(previous_record.get("missed_opportunity_count", 0)) if previous_record else None
    latest_weighted_severity = int(latest_record.get("weighted_severity_total", 0))
    previous_weighted_severity = int(previous_record.get("weighted_severity_total", 0)) if previous_record else None

    prior_failure_values = [int(record.get("failure_line_count", 0)) for record in prior_window]
    prior_missed_values = [int(record.get("missed_opportunity_count", 0)) for record in prior_window]
    prior_severity_values = [int(record.get("weighted_severity_total", 0)) for record in prior_window]
    recent_failure_avg = rolling_average(prior_failure_values)
    recent_missed_avg = rolling_average(prior_missed_values)
    recent_severity_avg = rolling_average(prior_severity_values)

    current_window_failure_avg = rolling_average([int(record.get("failure_line_count", 0)) for record in current_window_3])
    previous_window_failure_avg = rolling_average([int(record.get("failure_line_count", 0)) for record in previous_window_3])
    current_window_missed_avg = rolling_average([int(record.get("missed_opportunity_count", 0)) for record in current_window_3])
    previous_window_missed_avg = rolling_average([int(record.get("missed_opportunity_count", 0)) for record in previous_window_3])
    current_window_severity_avg = rolling_average([int(record.get("weighted_severity_total", 0)) for record in current_window_3])
    previous_window_severity_avg = rolling_average([int(record.get("weighted_severity_total", 0)) for record in previous_window_3])

    class_keys = sorted(
        set(latest_classes)
        | set(previous_classes)
        | {str(key) for record in prior_window for key in (record.get("failure_classes", {}) or {}).keys()}
        | {str(key) for record in current_window_3 for key in (record.get("failure_classes", {}) or {}).keys()}
        | {str(key) for record in previous_window_3 for key in (record.get("failure_classes", {}) or {}).keys()}
    )

    class_signal_lines: list[str] = []
    pain_rows: list[tuple[float, int, int, str, str]] = []
    priority_rows: list[tuple[float, int, str, str]] = []

    for key in class_keys:
        latest_value = int(latest_classes.get(key, 0) or 0)
        previous_value = int(previous_classes.get(key, 0) or 0) if previous_record else None
        delta_value = latest_value - previous_value if previous_value is not None else None
        previous_signal = compare_signal(latest_value, previous_value)

        prior_class_values = [
            int((record.get("failure_classes", {}) or {}).get(key, 0) or 0)
            for record in prior_window
        ]
        recent_avg = rolling_average(prior_class_values)
        rolling_signal = compare_to_average(latest_value, recent_avg)

        current_window_class_avg = rolling_average([
            int((record.get("failure_classes", {}) or {}).get(key, 0) or 0)
            for record in current_window_3
        ])
        previous_window_class_avg = rolling_average([
            int((record.get("failure_classes", {}) or {}).get(key, 0) or 0)
            for record in previous_window_3
        ])
        window_signal = compare_to_average(
            current_window_class_avg if current_window_class_avg is not None else 0.0,
            previous_window_class_avg,
        )

        class_signal_lines.append(
            f"- {key}: latest={latest_value}, previous={previous_value if previous_value is not None else 'none'}, delta={delta_value if delta_value is not None else 'n/a'}, previous_signal={previous_signal}, recent_average={fmt_avg(recent_avg)}, rolling_signal={rolling_signal}, current_window_avg={fmt_avg(current_window_class_avg)}, previous_window_avg={fmt_avg(previous_window_class_avg)}, window_signal={window_signal}"
        )

        imports_seen = int(trend_map[key]["imports_seen"]) if key in trend_map else 0
        total_lines_for_key = int(trend_map[key]["total_lines"]) if key in trend_map else 0
        weight = severity_weight_for_class(key)
        decay_score = decayed_priority_score(key, records)

        pain_line = (
            f"- {key}: total_lines={total_lines_for_key}, imports_seen={imports_seen}, severity_weight={weight}, latest_count={latest_value}, previous_count={previous_value if previous_value is not None else 'none'}, recent_average={fmt_avg(recent_avg)}, rolling_signal={rolling_signal}, decay_priority_score={decay_score:.2f}"
        )
        pain_rows.append((decay_score, total_lines_for_key, imports_seen, key, pain_line))

        priority_line = (
            f"- {key}: decay_priority_score={decay_score:.2f}, severity_weight={weight}, total_lines={total_lines_for_key}, imports_seen={imports_seen}, current_window_avg={fmt_avg(current_window_class_avg)}, previous_window_avg={fmt_avg(previous_window_class_avg)}, window_signal={window_signal}"
        )
        priority_rows.append((decay_score, weight, key, priority_line))

    history_signals.write_text(
        "# History Signals\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- latest_source_name: `{latest_record.get('source_name', 'unknown')}`\\n"
        f"- previous_source_name: `{previous_record.get('source_name', 'none') if previous_record else 'none'}`\\n"
        f"- failure_line_signal_vs_previous: `{compare_signal(latest_failure_lines_count, previous_failure_lines_count)}`\\n"
        f"- failure_line_signal_vs_recent_average: `{compare_to_average(latest_failure_lines_count, recent_failure_avg)}`\\n"
        f"- failure_line_window_signal_last3_vs_previous3: `{compare_to_average(current_window_failure_avg if current_window_failure_avg is not None else 0.0, previous_window_failure_avg)}`\\n"
        f"- missed_opportunity_signal_vs_previous: `{compare_signal(latest_missed_count, previous_missed_count)}`\\n"
        f"- missed_opportunity_signal_vs_recent_average: `{compare_to_average(latest_missed_count, recent_missed_avg)}`\\n"
        f"- missed_opportunity_window_signal_last3_vs_previous3: `{compare_to_average(current_window_missed_avg if current_window_missed_avg is not None else 0.0, previous_window_missed_avg)}`\\n"
        f"- weighted_severity_signal_vs_previous: `{compare_signal(latest_weighted_severity, previous_weighted_severity)}`\\n"
        f"- weighted_severity_signal_vs_recent_average: `{compare_to_average(latest_weighted_severity, recent_severity_avg)}`\\n"
        f"- weighted_severity_window_signal_last3_vs_previous3: `{compare_to_average(current_window_severity_avg if current_window_severity_avg is not None else 0.0, previous_window_severity_avg)}`\\n"
        f"- latest_failure_lines: `{latest_failure_lines_count}`\\n"
        f"- previous_failure_lines: `{previous_failure_lines_count if previous_failure_lines_count is not None else 'none'}`\\n"
        f"- recent_average_failure_lines: `{fmt_avg(recent_failure_avg)}`\\n"
        f"- current_window_3_average_failure_lines: `{fmt_avg(current_window_failure_avg)}`\\n"
        f"- previous_window_3_average_failure_lines: `{fmt_avg(previous_window_failure_avg)}`\\n"
        f"- latest_missed_opportunities: `{latest_missed_count}`\\n"
        f"- previous_missed_opportunities: `{previous_missed_count if previous_missed_count is not None else 'none'}`\\n"
        f"- recent_average_missed_opportunities: `{fmt_avg(recent_missed_avg)}`\\n"
        f"- current_window_3_average_missed_opportunities: `{fmt_avg(current_window_missed_avg)}`\\n"
        f"- previous_window_3_average_missed_opportunities: `{fmt_avg(previous_window_missed_avg)}`\\n"
        f"- latest_weighted_severity: `{latest_weighted_severity}`\\n"
        f"- previous_weighted_severity: `{previous_weighted_severity if previous_weighted_severity is not None else 'none'}`\\n"
        f"- recent_average_weighted_severity: `{fmt_avg(recent_severity_avg)}`\\n"
        f"- current_window_3_average_weighted_severity: `{fmt_avg(current_window_severity_avg)}`\\n"
        f"- previous_window_3_average_weighted_severity: `{fmt_avg(previous_window_severity_avg)}`\\n"
        "\\n## Failure Class Signals\\n"
        + (
            "\\n".join(class_signal_lines)
            if class_signal_lines
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    sorted_pain_lines = [
        line for _, _, _, _, line in sorted(
            pain_rows,
            key=lambda item: (-item[0], -item[1], -item[2], item[3]),
        )
    ]

    history_operator_pain.write_text(
        "# History Operator Pain\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- ranked_class_count: `{len(sorted_pain_lines)}`\\n"
        "\\n## Top Operator Pain Classes\\n"
        + (
            "\\n".join(sorted_pain_lines[:10])
            if sorted_pain_lines
            else "- none"
        )
        + "\\n\\n## Classes Seen In Latest Import\\n"
        + (
            "\\n".join(
                f"- {key}: {value}"
                for key, value in sorted(latest_classes.items())
            )
            if latest_classes
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    sorted_priority_lines = [
        line for _, _, _, line in sorted(
            priority_rows,
            key=lambda item: (-item[0], -item[1], item[2]),
        )
    ]

    history_priority_queue.write_text(
        "# History Priority Queue\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- ranked_class_count: `{len(sorted_priority_lines)}`\\n"
        "\\n## Priority Queue\\n"
        + (
            "\\n".join(sorted_priority_lines[:10])
            if sorted_priority_lines
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    failure_patterns.write_text(
        "# Failure Patterns\\n\\n"
        + (
            "\\n".join(
                f"- {re.sub(r'`', \"'\", line[:200])}"
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
                f"- {re.sub(r'`', \"'\", line[:200])}"
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
    print(f"UPDATED {history_trends}")
    print(f"UPDATED {history_signals}")
    print(f"UPDATED {history_operator_pain}")
    print(f"UPDATED {history_priority_queue}")
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
