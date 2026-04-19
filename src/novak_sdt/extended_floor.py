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
        "docs/history/HISTORY_REMEDIATION.md",
        "docs/history/HISTORY_ACTION_QUEUE.md",
        "docs/estate/ESTATE_HISTORY_SUMMARY.md",
        "docs/estate/ESTATE_PRIORITY_QUEUE.md",
        "docs/estate/ESTATE_ACTION_QUEUE.md",
        "docs/estate/ESTATE_INGEST_SUMMARY.md",
        "docs/estate/ESTATE_CATALOG.md",
        "docs/estate/ESTATE_REFRESH_STATUS.md",
        "docs/estate/ESTATE_ARCHIVE_INDEX.md",
        "docs/estate/ESTATE_DELTA.md",
        "docs/estate/ESTATE_TRENDS.md",
        "docs/estate/ESTATE_CADENCE.md",
        "docs/estate/ESTATE_RUNNER_STATUS.md",
        "estate/estate_sources.json",
        "estate/archive/estate_refresh_history.ndjson",
        "estate/notification_config.json",
        "estate/outbox/notifications.ndjson",
        "ops/systemd/estate-refresh.service",
        "ops/systemd/estate-refresh.timer",
        "bin/estate-refresh-runner.sh",
        "bin/install-estate-refresh-timer.sh",
        "docs/estate/ESTATE_FAILURE_POLICY.md",
        "docs/estate/ESTATE_NOTIFICATIONS.md",
        "docs/estate/ESTATE_NOTIFICATION_STATUS.md",
        "docs/history/FAILURE_PATTERNS.md",
        "docs/templates/SDT_CHANGE_INTENT_TEMPLATE.md",
        "docs/changes/CHANGE_INDEX.md",
        "docs/history/MISSED_OPPORTUNITIES.md",
        "docs/SDT_HISTORY_LANE.md",
        "tools/install_novak_shell_shortcuts.sh",
        "tools/sdt_shell_activate.sh",
        "tools/render_project_docs_status.py",
        "tools/render_freshness_gauge.py",
        "tools/archive_history_log.py",
        "tools/build_estate_history_report.py",
        "bin/estate-notify.sh",
        "bin/history-import.sh",
        "bin/estate-aggregate.sh",
        "bin/estate-refresh.sh",
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
      - History Remediation: history/HISTORY_REMEDIATION.md
      - History Action Queue: history/HISTORY_ACTION_QUEUE.md
      - Estate History Summary: estate/ESTATE_HISTORY_SUMMARY.md
      - Estate Priority Queue: estate/ESTATE_PRIORITY_QUEUE.md
      - Estate Action Queue: estate/ESTATE_ACTION_QUEUE.md
      - Estate Ingest Summary: estate/ESTATE_INGEST_SUMMARY.md
      - Estate Catalog: estate/ESTATE_CATALOG.md
      - Estate Refresh Status: estate/ESTATE_REFRESH_STATUS.md
      - Estate Archive Index: estate/ESTATE_ARCHIVE_INDEX.md
      - Estate Delta: estate/ESTATE_DELTA.md
      - Estate Trends: estate/ESTATE_TRENDS.md
      - Estate Cadence: estate/ESTATE_CADENCE.md
      - Estate Runner Status: estate/ESTATE_RUNNER_STATUS.md
      - Estate Failure Policy: estate/ESTATE_FAILURE_POLICY.md
      - Estate Notifications: estate/ESTATE_NOTIFICATIONS.md
      - Estate Notification Status: estate/ESTATE_NOTIFICATION_STATUS.md
      - Failure Patterns: history/FAILURE_PATTERNS.md
      - Missed Opportunities: history/MISSED_OPPORTUNITIES.md
      - Change Index: changes/CHANGE_INDEX.md
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
        "docs/history/HISTORY_REMEDIATION.md": """# History Remediation

No history remediation guidance has been recorded yet.
""",
        "docs/history/HISTORY_ACTION_QUEUE.md": """# History Action Queue

No history action queue has been recorded yet.
""",
        "docs/estate/ESTATE_HISTORY_SUMMARY.md": """# Estate History Summary

No estate history summary has been recorded yet.
""",
        "docs/estate/ESTATE_PRIORITY_QUEUE.md": """# Estate Priority Queue

No estate priority queue has been recorded yet.
""",
        "docs/estate/ESTATE_ACTION_QUEUE.md": """# Estate Action Queue

No estate action queue has been recorded yet.
""",
        "docs/estate/ESTATE_INGEST_SUMMARY.md": """# Estate Ingest Summary

No estate ingest summary has been recorded yet.
""",
        "docs/estate/ESTATE_CATALOG.md": """# Estate Catalog

No estate catalog has been recorded yet.
""",
        "docs/estate/ESTATE_REFRESH_STATUS.md": """# Estate Refresh Status

No estate refresh status has been recorded yet.
""",
        "estate/estate_sources.json": """[]
""",
                "estate/notification_config.json": """{
  "enabled": true,
  "profile": "notify-n1",
  "channels": []
}
""",
        "estate/outbox/notifications.ndjson": "",
"docs/estate/ESTATE_ARCHIVE_INDEX.md": """# Estate Archive Index

No estate archive index has been recorded yet.
""",
        "docs/estate/ESTATE_DELTA.md": """# Estate Delta

No estate delta has been recorded yet.
""",
        "docs/estate/ESTATE_TRENDS.md": """# Estate Trends

No estate trends have been recorded yet.
""",
        "estate/archive/estate_refresh_history.ndjson": """
""",
        "docs/estate/ESTATE_CADENCE.md": """# Estate Cadence

## Default operating guidance

- manual refresh for one-off review or proof runs
- daily timer for stable estates
- hourly timer only for fast-changing lab or incident windows
- run an extra refresh before and after high-risk changes

## Runner path

- `bash bin/estate-refresh-runner.sh`
- `bash bin/install-estate-refresh-timer.sh --output-dir /tmp/estate-systemd`
- review `docs/estate/ESTATE_REFRESH_STATUS.md` after each run
""",
        "docs/estate/ESTATE_RUNNER_STATUS.md": """# Estate Runner Status

No estate runner status has been recorded yet.
""",
        "docs/estate/ESTATE_FAILURE_POLICY.md": """# Estate Failure Policy

## Notify N1 return codes
- lock-busy -> `75`
- failure -> `2`
- success -> `0`

## Rule
Notify N1 records event, status, and return code deterministically before exiting.
""",
        "docs/estate/ESTATE_NOTIFICATIONS.md": """# Estate Notifications

## Scope
Notify N1 is the minimum notification lane.

## Included
- deterministic outbox writes
- notification status rendering
- reproducible helper return codes

## Not included
- routing policy
- secrets handling
- fanout
- multi-channel delivery
""",
        "docs/estate/ESTATE_NOTIFICATION_STATUS.md": """# Estate Notification Status

- total_events: `0`
- last_event: `none`
- last_status: `none`
- last_run_label: `none`

## Counts
- lock-busy: `0`
- failure: `0`
- success: `0`

## Latest 5 events
- none yet
""",
"docs/history/FAILURE_PATTERNS.md": """# Failure Patterns

No failure patterns have been recorded yet.
""",
        "docs/changes/CHANGE_INDEX.md": """# Change Index

- Add change records here in chronological order.
""",
"docs/templates/SDT_CHANGE_INTENT_TEMPLATE.md": """# SDT Change Intent

## Intent Statement
- actor: <creator/editor/operator>
- intended change: <one sentence>
- intended non-change: <one sentence>
- why: <one sentence>
- proof expected: <tests / run / docs / review>

## Alignment Check
- observed change summary: <one sentence>
- in-intent: PASS | PARTIAL | FAIL | UNVERIFIED
- notes: <short note>
""",
        "docs/history/MISSED_OPPORTUNITIES.md": """# Missed Opportunities

No missed opportunities have been recorded yet.
""",
"tools/install_novak_shell_shortcuts.sh": """#!/usr/bin/env bash
set -Eeuo pipefail
set +H

SHORTCUTS_FILE="${HOME}/.novak_sdt_shell_shortcuts.sh"
BASHRC_FILE="${HOME}/.bashrc"
SOURCE_LINE='[[ -f "${HOME}/.novak_sdt_shell_shortcuts.sh" ]] && source "${HOME}/.novak_sdt_shell_shortcuts.sh"'

cat > "${SHORTCUTS_FILE}" <<'EOS'
novak() {
  local target
  target="${1:-$PWD}"

  if [[ -d "${target}" ]]; then
    cd "${target}" || return 1
  fi

  if [[ -f "./tools/sdt_shell_activate.sh" ]]; then
    source ./tools/sdt_shell_activate.sh
  else
    echo "No SDT shell helper found in: $(pwd)"
    return 1
  fi
}

nsdt() {
  novak "$@"
}
EOS

chmod 0644 "${SHORTCUTS_FILE}"
touch "${BASHRC_FILE}"

if ! grep -Fqx "${SOURCE_LINE}" "${BASHRC_FILE}"; then
  printf '\n%s\n' "${SOURCE_LINE}" >> "${BASHRC_FILE}"
fi

echo "WROTE ${SHORTCUTS_FILE}"
echo "UPDATED ${BASHRC_FILE}"
echo "For immediate use in the current shell:"
echo "  source ${SHORTCUTS_FILE}"
""",
        "tools/sdt_shell_activate.sh": r"""#!/usr/bin/env bash
set -Eeuo pipefail
set +H

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "ERROR: source this file instead of executing it"
  echo "USE: source ./tools/sdt_shell_activate.sh"
  exit 1
fi

if [[ -z "${SDT_OLD_PS1+x}" ]]; then
  export SDT_OLD_PS1="${PS1-}"
fi

if [[ -z "${SDT_OLD_PROMPT_COMMAND+x}" ]]; then
  export SDT_OLD_PROMPT_COMMAND="${PROMPT_COMMAND-__SDT_EMPTY__}"
fi

export SDT_SHELL_ACTIVE=1
export VIRTUAL_ENV_DISABLE_PROMPT=1

sdt_refresh_context() {
  local repo_label
  local branch_label
  local branch_color
  local novak_color
  local repo_color
  local reset_color
  local warn_color
  local clean_color
  local dirty_color

  novak_color='\[\e[1;35m\]'
  repo_color='\[\e[0;37m\]'
  clean_color='\[\e[1;32m\]'
  dirty_color='\[\e[1;31m\]'
  warn_color='\[\e[1;33m\]'
  reset_color='\[\e[0m\]'

  if git rev-parse --show-toplevel >/dev/null 2>&1; then
    repo_label="$(basename "$(git rev-parse --show-toplevel)")"
  else
    repo_label="NO-REPO"
  fi

  if git rev-parse --abbrev-ref HEAD >/dev/null 2>&1; then
    branch_label="$(git rev-parse --abbrev-ref HEAD)"
  else
    branch_label="NO-BRANCH"
  fi

  if [[ "${repo_label}" == "NO-REPO" ]]; then
    branch_color="${warn_color}"
  elif [[ "${branch_label}" == "HEAD" || "${branch_label}" == "NO-BRANCH" ]]; then
    branch_color="${warn_color}"
  else
    if ! git diff --no-ext-diff --quiet --ignore-submodules HEAD -- 2>/dev/null || \
       ! git diff --cached --no-ext-diff --quiet --ignore-submodules -- 2>/dev/null || \
       [[ -n "$(git ls-files --others --exclude-standard 2>/dev/null)" ]]; then
      branch_color="${dirty_color}"
    else
      branch_color="${clean_color}"
    fi
  fi

  PS1="(${novak_color}NOVΛK™${reset_color}-SDT:${repo_color}${repo_label}${reset_color}@${branch_color}${branch_label}${reset_color}) \u@\h:\w# "
}

sdt_deactivate() {
  if [[ -n "${SDT_OLD_PS1-}" ]]; then
    PS1="${SDT_OLD_PS1}"
  fi

  if [[ "${SDT_OLD_PROMPT_COMMAND-__SDT_EMPTY__}" == "__SDT_EMPTY__" ]]; then
    unset PROMPT_COMMAND
  else
    PROMPT_COMMAND="${SDT_OLD_PROMPT_COMMAND}"
  fi

  unset SDT_SHELL_ACTIVE
  unset SDT_OLD_PS1
  unset SDT_OLD_PROMPT_COMMAND
  unset VIRTUAL_ENV_DISABLE_PROMPT
  unset -f sdt_refresh_context
  unset -f sdt_deactivate
}

if [[ "${SDT_OLD_PROMPT_COMMAND}" == "__SDT_EMPTY__" ]]; then
  PROMPT_COMMAND='sdt_refresh_context'
else
  PROMPT_COMMAND="sdt_refresh_context; ${SDT_OLD_PROMPT_COMMAND}"
fi

sdt_refresh_context

echo "NOVΛK™ - SDT shell active"
echo "Branch color: green=clean, red=dirty, yellow=detached/no-repo"
echo "Use 'sdt_deactivate' to leave the NOVΛK™ - SDT shell context."
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
        f"- elapsed_seconds: {timing.get('run_elapsed_sec', 'UNSET')}",
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

FAILURE_THRESHOLDS = [
    (6, "critical"),
    (4, "high"),
    (2, "medium"),
    (0, "low"),
]

WEIGHTED_SEVERITY_THRESHOLDS = [
    (18, "critical"),
    (12, "high"),
    (6, "medium"),
    (0, "low"),
]

PRIORITY_THRESHOLDS = [
    (12.0, "urgent"),
    (7.0, "elevated"),
    (0.0, "normal"),
]


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


def label_from_threshold(value: int | float, thresholds: list[tuple[int | float, str]]) -> str:
    for cutoff, label in thresholds:
        if value >= cutoff:
            return label
    return thresholds[-1][1]


def priority_bucket(score: float) -> str:
    return label_from_threshold(score, PRIORITY_THRESHOLDS)


def approval_gate(
    failure_label: str,
    weighted_severity_label: str,
    priority_label: str,
) -> str:
    if failure_label in {"high", "critical"}:
        return "block"
    if weighted_severity_label in {"high", "critical"}:
        return "block"
    if priority_label == "urgent":
        return "block"
    if failure_label == "medium":
        return "review"
    if weighted_severity_label == "medium":
        return "review"
    if priority_label == "elevated":
        return "review"
    return "proceed"


def operator_mode_for_gate(gate: str) -> str:
    return {
        "block": "immediate-review",
        "review": "review-soon",
        "proceed": "continue",
    }.get(gate, "continue")


def recommendation_for_class(name: str) -> str:
    return {
        "generic-error": "inspect the failing command path, capture full stderr/stdout, and split generic errors into tighter classes",
        "mkdocs": "run mkdocs build locally, validate nav/config, and confirm generated docs still render cleanly",
        "python-traceback": "rerun the failing Python path with full traceback capture and isolate the exact exception origin",
        "python-syntax": "run py_compile and a formatter or linter across the touched Python files before retry",
        "python-indentation": "run py_compile and normalize indentation before rerunning the affected script",
        "permission": "check ownership, file modes, sudo path, and whether the action should run under a different user",
        "missing-command": "verify package installation, binary presence, and PATH before retrying the action",
        "other": "inspect the raw log lines and classify the issue more precisely before retrying",
    }.get(name, "inspect the raw log lines and classify the issue more precisely before retrying")


def decayed_priority_score(name: str, records: list[dict]) -> float:
    score = 0.0
    for age, record in enumerate(reversed(records)):
        classes = record.get("failure_classes", {}) or {}
        count = int(classes.get(name, 0) or 0)
        if count <= 0:
            continue
        score += float(count * severity_weight_for_class(name)) * (0.85 ** age)
    return score


def unique_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        output.append(item)
    return output


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
    history_remediation = history / "HISTORY_REMEDIATION.md"
    history_action_queue = history / "HISTORY_ACTION_QUEUE.md"
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
    priority_rows: list[tuple[float, int, str, str, str]] = []

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

        weight = severity_weight_for_class(key)
        decay_score = decayed_priority_score(key, records)
        priority_label = priority_bucket(decay_score)
        recommendation = recommendation_for_class(key)

        class_signal_lines.append(
            f"- {key}: latest={latest_value}, previous={previous_value if previous_value is not None else 'none'}, delta={delta_value if delta_value is not None else 'n/a'}, previous_signal={previous_signal}, recent_average={fmt_avg(recent_avg)}, rolling_signal={rolling_signal}, current_window_avg={fmt_avg(current_window_class_avg)}, previous_window_avg={fmt_avg(previous_window_class_avg)}, window_signal={window_signal}, priority_bucket={priority_label}"
        )

        imports_seen = int(trend_map[key]["imports_seen"]) if key in trend_map else 0
        total_lines_for_key = int(trend_map[key]["total_lines"]) if key in trend_map else 0

        pain_line = (
            f"- {key}: total_lines={total_lines_for_key}, imports_seen={imports_seen}, severity_weight={weight}, latest_count={latest_value}, previous_count={previous_value if previous_value is not None else 'none'}, recent_average={fmt_avg(recent_avg)}, rolling_signal={rolling_signal}, decay_priority_score={decay_score:.2f}, recommendation={recommendation}"
        )
        pain_rows.append((decay_score, total_lines_for_key, imports_seen, key, pain_line))

        priority_line = (
            f"- {key}: decay_priority_score={decay_score:.2f}, priority_bucket={priority_label}, severity_weight={weight}, total_lines={total_lines_for_key}, imports_seen={imports_seen}, current_window_avg={fmt_avg(current_window_class_avg)}, previous_window_avg={fmt_avg(previous_window_class_avg)}, window_signal={window_signal}, recommendation={recommendation}"
        )
        priority_rows.append((decay_score, weight, key, priority_line, recommendation))

    sorted_pain_lines = [
        line for _, _, _, _, line in sorted(
            pain_rows,
            key=lambda item: (-item[0], -item[1], -item[2], item[3]),
        )
    ]

    sorted_priority_details = sorted(
        priority_rows,
        key=lambda item: (-item[0], -item[1], item[2]),
    )
    sorted_priority_lines = [line for _, _, _, line, _ in sorted_priority_details]

    highest_priority_score = float(sorted_priority_details[0][0]) if sorted_priority_details else 0.0
    highest_priority_bucket = priority_bucket(highest_priority_score)

    failure_threshold_latest = label_from_threshold(latest_failure_lines_count, FAILURE_THRESHOLDS)
    weighted_severity_threshold_latest = label_from_threshold(
        latest_weighted_severity,
        WEIGHTED_SEVERITY_THRESHOLDS,
    )
    approval_state = approval_gate(
        failure_threshold_latest,
        weighted_severity_threshold_latest,
        highest_priority_bucket,
    )
    operator_mode = operator_mode_for_gate(approval_state)

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
        f"- failure_line_threshold_latest: `{failure_threshold_latest}`\\n"
        f"- weighted_severity_threshold_latest: `{weighted_severity_threshold_latest}`\\n"
        f"- highest_priority_bucket: `{highest_priority_bucket}`\\n"
        f"- approval_gate: `{approval_state}`\\n"
        f"- recommended_operator_mode: `{operator_mode}`\\n"
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

    history_operator_pain.write_text(
        "# History Operator Pain\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- ranked_class_count: `{len(sorted_pain_lines)}`\\n"
        f"- approval_gate: `{approval_state}`\\n"
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

    history_priority_queue.write_text(
        "# History Priority Queue\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- ranked_class_count: `{len(sorted_priority_lines)}`\\n"
        f"- highest_priority_bucket: `{highest_priority_bucket}`\\n"
        "\\n## Priority Queue\\n"
        + (
            "\\n".join(sorted_priority_lines[:10])
            if sorted_priority_lines
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    remediation_items: list[str] = []
    if approval_state == "block":
        remediation_items.append("pause promotion or merge, and require operator review before the next attempt")
    elif approval_state == "review":
        remediation_items.append("review the latest failures before the next retry and confirm the remediation owner")
    else:
        remediation_items.append("continue with caution and keep capturing evidence on the next run")

    remediation_items.append(
        f"treat the current weighted severity as `{weighted_severity_threshold_latest}` and the top priority bucket as `{highest_priority_bucket}`"
    )

    remediation_items.extend(
        recommendation
        for _, _, _, _, recommendation in sorted_priority_details[:5]
    )

    unique_remediation_items = unique_preserve_order(remediation_items)

    history_remediation.write_text(
        "# History Remediation\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- approval_gate: `{approval_state}`\\n"
        f"- recommended_operator_mode: `{operator_mode}`\\n"
        f"- weighted_severity_threshold_latest: `{weighted_severity_threshold_latest}`\\n"
        f"- highest_priority_bucket: `{highest_priority_bucket}`\\n"
        "\\n## Immediate Recommendations\\n"
        + "\\n".join(f"- {item}" for item in unique_remediation_items)
        + "\\n",
        encoding="utf-8",
    )

    action_queue_lines: list[str] = []
    for index, (score, weight, key, _, recommendation) in enumerate(sorted_priority_details[:5], start=1):
        action_queue_lines.append(
            f"- {index}. [{approval_state}] {key} | priority_bucket={priority_bucket(score)} | decay_priority_score={score:.2f} | severity_weight={weight} | action={recommendation}"
        )

    if not action_queue_lines:
        action_queue_lines = ["- none"]

    history_action_queue.write_text(
        "# History Action Queue\\n\\n"
        f"- archived_attempts_total: `{attempt_count}`\\n"
        f"- approval_gate: `{approval_state}`\\n"
        f"- recommended_operator_mode: `{operator_mode}`\\n"
        "\\n## Recommended Next Moves\\n"
        + "\\n".join(action_queue_lines)
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
    print(f"UPDATED {history_remediation}")
    print(f"UPDATED {history_action_queue}")
    print(f"UPDATED {failure_patterns}")
    print(f"UPDATED {missed_opportunities}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
        "tools/build_estate_history_report.py": """#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
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

FAILURE_THRESHOLDS = [
    (6, "critical"),
    (4, "high"),
    (2, "medium"),
    (0, "low"),
]

WEIGHTED_SEVERITY_THRESHOLDS = [
    (18, "critical"),
    (12, "high"),
    (6, "medium"),
    (0, "low"),
]

PRIORITY_THRESHOLDS = [
    (12.0, "urgent"),
    (7.0, "elevated"),
    (0.0, "normal"),
]


def now_utc() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")


def label_from_threshold(value: int | float, thresholds: list[tuple[int | float, str]]) -> str:
    for cutoff, label in thresholds:
        if value >= cutoff:
            return label
    return thresholds[-1][1]


def priority_bucket(score: float) -> str:
    return label_from_threshold(score, PRIORITY_THRESHOLDS)


def bucket_rank(label: str) -> int:
    return {
        "normal": 0,
        "elevated": 1,
        "urgent": 2,
    }.get(label, 0)


def approval_gate(
    failure_label: str,
    weighted_severity_label: str,
    priority_label: str,
) -> str:
    if failure_label in {"high", "critical"}:
        return "block"
    if weighted_severity_label in {"high", "critical"}:
        return "block"
    if priority_label == "urgent":
        return "block"
    if failure_label == "medium":
        return "review"
    if weighted_severity_label == "medium":
        return "review"
    if priority_label == "elevated":
        return "review"
    return "proceed"


def operator_mode_for_gate(gate: str) -> str:
    return {
        "block": "immediate-review",
        "review": "review-soon",
        "proceed": "continue",
    }.get(gate, "continue")


def severity_weight_for_class(name: str) -> int:
    return int(SEVERITY_WEIGHTS.get(name, 1))


def recommendation_for_class(name: str) -> str:
    return {
        "generic-error": "inspect the failing command path, capture full stderr/stdout, and split generic errors into tighter classes",
        "mkdocs": "run mkdocs build locally, validate nav/config, and confirm generated docs still render cleanly",
        "python-traceback": "rerun the failing Python path with full traceback capture and isolate the exact exception origin",
        "python-syntax": "run py_compile and a formatter or linter across the touched Python files before retry",
        "python-indentation": "run py_compile and normalize indentation before rerunning the affected script",
        "permission": "check ownership, file modes, sudo path, and whether the action should run under a different user",
        "missing-command": "verify package installation, binary presence, and PATH before retrying the action",
        "other": "inspect the raw log lines and classify the issue more precisely before retrying",
    }.get(name, "inspect the raw log lines and classify the issue more precisely before retrying")


def decayed_priority_score(name: str, records: list[dict]) -> float:
    score = 0.0
    for age, record in enumerate(reversed(records)):
        classes = record.get("failure_classes", {}) or {}
        count = int(classes.get(name, 0) or 0)
        if count <= 0:
            continue
        score += float(count * severity_weight_for_class(name)) * (0.85 ** age)
    return score


def normalize_tags(raw_tags, fallback: str) -> list[str]:
    tags: list[str] = []
    if isinstance(raw_tags, list):
        tags = [str(item).strip() for item in raw_tags if str(item).strip()]
    elif isinstance(raw_tags, str) and raw_tags.strip():
        tags = [raw_tags.strip()]
    if fallback and fallback not in tags:
        tags.insert(0, fallback)
    return tags


def resolve_input(arg: str, base_dir: Path | None = None) -> tuple[str, Path]:
    if "=" in arg:
        label, raw = arg.split("=", 1)
    else:
        label, raw = "", arg

    source = Path(raw)
    if not source.is_absolute() and base_dir is not None:
        source = base_dir / source
    source = source.resolve()

    if source.is_dir():
        ndjson = source / "docs" / "history" / "ATTEMPTS.ndjson"
        derived_label = source.name
    else:
        ndjson = source
        derived_label = source.stem

    final_label = label.strip() or derived_label
    return final_label, ndjson


def read_json_lines(path: Path) -> list[dict]:
    records: list[dict] = []
    if not path.is_file():
        return records
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip():
            continue
        try:
            loaded = json.loads(raw_line)
        except json.JSONDecodeError:
            continue
        if isinstance(loaded, dict):
            records.append(loaded)
    return records


def append_json_line(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True) + "\\n")


def load_records(path: Path) -> list[dict]:
    return read_json_lines(path)


def pick_top_class(classes: dict[str, int]) -> str:
    if not classes:
        return "none"
    return max(
        classes.items(),
        key=lambda kv: (
            severity_weight_for_class(str(kv[0])) * int(kv[1]),
            int(kv[1]),
            str(kv[0]),
        ),
    )[0]


def make_source(
    *,
    origin: str,
    label: str,
    ndjson_path: Path,
    owner: str = "unknown",
    environment: str = "unknown",
    host: str = "unknown",
    repo_class: str = "unknown",
    tags: list[str] | None = None,
    notes: str = "",
    discovered_from: str = "",
) -> dict:
    return {
        "origin": origin,
        "label": label,
        "ndjson_path": ndjson_path.resolve(),
        "owner": owner.strip() or "unknown",
        "environment": environment.strip() or "unknown",
        "host": host.strip() or "unknown",
        "repo_class": repo_class.strip() or "unknown",
        "tags": tags or [],
        "notes": notes.strip(),
        "discovered_from": discovered_from.strip(),
    }


def explicit_source_from_arg(arg: str) -> dict:
    label, ndjson = resolve_input(arg)
    return make_source(
        origin="explicit",
        label=label,
        ndjson_path=ndjson,
        tags=normalize_tags([], "explicit"),
    )


def manifest_source_from_item(item: dict, manifest_path: Path) -> dict:
    if not isinstance(item, dict):
        raise ValueError("manifest entries must be objects")
    label = str(item.get("label", "")).strip()
    raw_path = str(item.get("path", "")).strip()
    if not raw_path:
        raise ValueError("manifest entry missing path")
    entry_label, entry_path = resolve_input(
        f"{label}={raw_path}" if label else raw_path,
        manifest_path.parent,
    )
    return make_source(
        origin="manifest",
        label=entry_label,
        ndjson_path=entry_path,
        owner=str(item.get("owner", "unknown")),
        environment=str(item.get("environment", "unknown")),
        host=str(item.get("host", "unknown")),
        repo_class=str(item.get("repo_class", "unknown")),
        tags=normalize_tags(item.get("tags", []), "manifest"),
        notes=str(item.get("notes", "")),
    )


def load_manifest_entries(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("manifest must be a JSON list")
    entries: list[dict] = []
    for item in data:
        entries.append(manifest_source_from_item(item, path))
    return entries


def discover_sources(roots: list[Path]) -> list[dict]:
    discovered: list[dict] = []
    seen: set[Path] = set()
    for root in roots:
        root_resolved = root.resolve()
        if not root_resolved.exists():
            continue
        for candidate in root_resolved.rglob("ATTEMPTS.ndjson"):
            try:
                if candidate.name != "ATTEMPTS.ndjson":
                    continue
                if candidate.parent.name != "history":
                    continue
                if candidate.parent.parent.name != "docs":
                    continue
            except IndexError:
                continue
            resolved = candidate.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            repo_root = resolved.parent.parent.parent
            label = repo_root.name
            discovered.append(
                make_source(
                    origin="discovered",
                    label=label,
                    ndjson_path=resolved,
                    tags=normalize_tags([], "discovered"),
                    notes=f"auto-discovered from {root_resolved}",
                    discovered_from=str(root_resolved),
                )
            )
    discovered.sort(key=lambda item: (item["label"], str(item["ndjson_path"])))
    return discovered


def join_tags(tags: list[str]) -> str:
    if not tags:
        return "none"
    return ",".join(tags)


def average(values: list[int | float]) -> float:
    if not values:
        return 0.0
    return float(sum(values) / len(values))


def rel_or_abs(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def repo_map(snapshot: dict) -> dict[str, dict]:
    return {
        str(item.get("label", "")): item
        for item in snapshot.get("repos", [])
        if isinstance(item, dict) and str(item.get("label", "")).strip()
    }


def repo_order_map(snapshot: dict) -> dict[str, int]:
    return {
        str(item.get("label", "")): idx
        for idx, item in enumerate(snapshot.get("repos", []), start=1)
        if isinstance(item, dict) and str(item.get("label", "")).strip()
    }


def snapshot_summary_line(snapshot: dict) -> str:
    return (
        f"- {snapshot.get('generated_utc', 'unknown')}: "
        f"usable_sources={snapshot.get('usable_source_count', 0)}, "
        f"block={snapshot.get('sources_in_block', 0)}, "
        f"review={snapshot.get('sources_in_review', 0)}, "
        f"proceed={snapshot.get('sources_in_proceed', 0)}, "
        f"highest_bucket={snapshot.get('highest_priority_bucket_across_estate', 'normal')}, "
        f"total_latest_weighted_severity={snapshot.get('total_latest_weighted_severity_across_sources', 0)}"
    )


def make_snapshot(repo_rows: list[dict], *, generated_utc: str, manifest_count: int, discover_root_count: int, explicit_count: int, merged_count: int, skipped_count: int, highest_bucket: str, block_count: int, review_count: int, proceed_count: int, total_latest_weighted_severity: int) -> dict:
    repos = [
        {
            "label": row["label"],
            "approval_gate": row["approval_gate"],
            "operator_mode": row["operator_mode"],
            "highest_priority_bucket": row["highest_priority_bucket"],
            "repo_priority_score": round(float(row["repo_priority_score"]), 2),
            "latest_weighted_severity": int(row["latest_weighted_severity"]),
            "latest_failure_lines": int(row["latest_failure_lines"]),
            "top_class": row["top_class"],
            "owner": row["owner"],
            "environment": row["environment"],
            "host": row["host"],
            "repo_class": row["repo_class"],
            "tags": list(row["tags"]),
        }
        for row in repo_rows
    ]
    return {
        "generated_utc": generated_utc,
        "manifest_file_count": manifest_count,
        "discover_root_count": discover_root_count,
        "explicit_source_count": explicit_count,
        "unique_merged_source_count": merged_count,
        "usable_source_count": len(repo_rows),
        "skipped_source_count": skipped_count,
        "highest_priority_bucket_across_estate": highest_bucket,
        "sources_in_block": block_count,
        "sources_in_review": review_count,
        "sources_in_proceed": proceed_count,
        "total_latest_weighted_severity_across_sources": total_latest_weighted_severity,
        "repos": repos,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build estate-level SDT history reports from explicit, manifest-driven, or auto-discovered sources."
    )
    parser.add_argument(
        "sources",
        nargs="*",
        help="Explicit sources in the form label=repo-path, repo-path, or ndjson path.",
    )
    parser.add_argument(
        "--manifest",
        action="append",
        default=[],
        help="Path to JSON manifest file. Each entry must be an object with label, path, and optional metadata.",
    )
    parser.add_argument(
        "--discover-root",
        action="append",
        default=[],
        help="Root path to scan recursively for docs/history/ATTEMPTS.ndjson files.",
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    estate_dir = repo / "docs" / "estate"
    estate_dir.mkdir(parents=True, exist_ok=True)

    estate_history_summary = estate_dir / "ESTATE_HISTORY_SUMMARY.md"
    estate_priority_queue = estate_dir / "ESTATE_PRIORITY_QUEUE.md"
    estate_action_queue = estate_dir / "ESTATE_ACTION_QUEUE.md"
    estate_ingest_summary = estate_dir / "ESTATE_INGEST_SUMMARY.md"
    estate_catalog = estate_dir / "ESTATE_CATALOG.md"
    estate_refresh_status = estate_dir / "ESTATE_REFRESH_STATUS.md"
    estate_archive_index = estate_dir / "ESTATE_ARCHIVE_INDEX.md"
    estate_delta = estate_dir / "ESTATE_DELTA.md"
    estate_trends = estate_dir / "ESTATE_TRENDS.md"

    archive_path = repo / "estate" / "archive" / "estate_refresh_history.ndjson"
    refresh_generated_utc = now_utc()

    explicit_sources = [explicit_source_from_arg(arg) for arg in args.sources]
    manifest_sources: list[dict] = []
    for manifest in args.manifest:
        manifest_sources.extend(load_manifest_entries(Path(manifest).resolve()))
    discovered_sources = discover_sources([Path(root).resolve() for root in args.discover_root])

    merged_sources: list[dict] = []
    source_origin_rows: list[dict] = []
    seen_paths: set[Path] = set()

    for source in explicit_sources:
        resolved = Path(source["ndjson_path"]).resolve()
        if resolved not in seen_paths:
            seen_paths.add(resolved)
            merged_sources.append(source)
        source_origin_rows.append(source)

    for source in manifest_sources:
        resolved = Path(source["ndjson_path"]).resolve()
        if resolved not in seen_paths:
            seen_paths.add(resolved)
            merged_sources.append(source)
        source_origin_rows.append(source)

    for source in discovered_sources:
        resolved = Path(source["ndjson_path"]).resolve()
        if resolved not in seen_paths:
            seen_paths.add(resolved)
            merged_sources.append(source)
        source_origin_rows.append(source)

    repo_rows: list[dict] = []
    latest_classes_counter = Counter()
    skipped_sources: list[str] = []

    for source in merged_sources:
        label = str(source["label"])
        ndjson_path = Path(str(source["ndjson_path"])).resolve()

        if not ndjson_path.is_file():
            skipped_sources.append(f"{label} -> missing file: {ndjson_path}")
            continue

        records = load_records(ndjson_path)
        if not records:
            skipped_sources.append(f"{label} -> empty ledger: {ndjson_path}")
            continue

        latest = records[-1]
        latest_classes = {
            str(k): int(v)
            for k, v in (latest.get("failure_classes", {}) or {}).items()
        }

        latest_failure_lines = int(latest.get("failure_line_count", 0))
        latest_weighted_severity = int(latest.get("weighted_severity_total", 0))
        latest_missed = int(latest.get("missed_opportunity_count", 0))
        top_class = pick_top_class(latest_classes)

        class_scores = {
            cls: decayed_priority_score(cls, records)
            for cls in latest_classes.keys()
        }
        highest_class_score = max(class_scores.values()) if class_scores else 0.0
        highest_priority_bucket = priority_bucket(highest_class_score)

        failure_threshold_latest = label_from_threshold(latest_failure_lines, FAILURE_THRESHOLDS)
        weighted_severity_threshold_latest = label_from_threshold(
            latest_weighted_severity,
            WEIGHTED_SEVERITY_THRESHOLDS,
        )
        gate = approval_gate(
            failure_threshold_latest,
            weighted_severity_threshold_latest,
            highest_priority_bucket,
        )
        operator_mode = operator_mode_for_gate(gate)
        action = recommendation_for_class(top_class) if top_class != "none" else "review the latest repo state before the next attempt"

        repo_priority_score = float(latest_weighted_severity) + highest_class_score + float(latest_failure_lines)

        latest_classes_counter.update(latest_classes)

        repo_rows.append(
            {
                "label": label,
                "ndjson_path": ndjson_path,
                "attempts": len(records),
                "latest_source_name": str(latest.get("source_name", "unknown")),
                "latest_failure_lines": latest_failure_lines,
                "latest_weighted_severity": latest_weighted_severity,
                "latest_missed": latest_missed,
                "failure_threshold_latest": failure_threshold_latest,
                "weighted_severity_threshold_latest": weighted_severity_threshold_latest,
                "highest_priority_bucket": highest_priority_bucket,
                "approval_gate": gate,
                "operator_mode": operator_mode,
                "top_class": top_class,
                "action": action,
                "repo_priority_score": repo_priority_score,
                "owner": str(source["owner"]),
                "environment": str(source["environment"]),
                "host": str(source["host"]),
                "repo_class": str(source["repo_class"]),
                "tags": list(source["tags"]),
                "notes": str(source["notes"]),
                "origin": str(source["origin"]),
            }
        )

    repo_rows.sort(
        key=lambda item: (
            -float(item["repo_priority_score"]),
            str(item["label"]),
        )
    )

    block_count = sum(1 for row in repo_rows if row["approval_gate"] == "block")
    review_count = sum(1 for row in repo_rows if row["approval_gate"] == "review")
    proceed_count = sum(1 for row in repo_rows if row["approval_gate"] == "proceed")
    total_attempts = sum(int(row["attempts"]) for row in repo_rows)
    total_latest_weighted_severity = sum(int(row["latest_weighted_severity"]) for row in repo_rows)
    estate_highest_bucket = repo_rows[0]["highest_priority_bucket"] if repo_rows else "normal"

    prior_snapshots = read_json_lines(archive_path)
    previous_snapshot = prior_snapshots[-1] if prior_snapshots else None

    current_snapshot = make_snapshot(
        repo_rows,
        generated_utc=refresh_generated_utc,
        manifest_count=len(args.manifest),
        discover_root_count=len(args.discover_root),
        explicit_count=len(explicit_sources),
        merged_count=len(merged_sources),
        skipped_count=len(skipped_sources),
        highest_bucket=estate_highest_bucket,
        block_count=block_count,
        review_count=review_count,
        proceed_count=proceed_count,
        total_latest_weighted_severity=total_latest_weighted_severity,
    )

    append_json_line(archive_path, current_snapshot)
    all_snapshots = prior_snapshots + [current_snapshot]

    estate_history_summary.write_text(
        "# Estate History Summary\\n\\n"
        f"- estate_source_count: `{len(repo_rows)}`\\n"
        f"- total_archived_attempts_across_sources: `{total_attempts}`\\n"
        f"- sources_in_block: `{block_count}`\\n"
        f"- sources_in_review: `{review_count}`\\n"
        f"- sources_in_proceed: `{proceed_count}`\\n"
        f"- highest_priority_bucket_across_estate: `{estate_highest_bucket}`\\n"
        f"- total_latest_weighted_severity_across_sources: `{total_latest_weighted_severity}`\\n"
        "\\n## Per-Repo Latest State\\n"
        + (
            "\\n".join(
                f"- {row['label']}: attempts={row['attempts']}, latest_source={row['latest_source_name']}, gate={row['approval_gate']}, operator_mode={row['operator_mode']}, priority_bucket={row['highest_priority_bucket']}, latest_failure_lines={row['latest_failure_lines']}, latest_weighted_severity={row['latest_weighted_severity']}, top_class={row['top_class']}, owner={row['owner']}, environment={row['environment']}, host={row['host']}, repo_class={row['repo_class']}, tags={join_tags(row['tags'])}"
                for row in repo_rows
            )
            if repo_rows
            else "- none"
        )
        + "\\n\\n## Latest Failure Classes Across Estate\\n"
        + (
            "\\n".join(
                f"- {key}: {value}"
                for key, value in sorted(latest_classes_counter.items())
            )
            if latest_classes_counter
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    estate_priority_queue.write_text(
        "# Estate Priority Queue\\n\\n"
        f"- ranked_source_count: `{len(repo_rows)}`\\n"
        f"- highest_priority_bucket_across_estate: `{estate_highest_bucket}`\\n"
        "\\n## Repos Requiring Attention\\n"
        + (
            "\\n".join(
                f"- {row['label']}: repo_priority_score={row['repo_priority_score']:.2f}, gate={row['approval_gate']}, operator_mode={row['operator_mode']}, priority_bucket={row['highest_priority_bucket']}, latest_weighted_severity={row['latest_weighted_severity']}, latest_failure_lines={row['latest_failure_lines']}, top_class={row['top_class']}, tags={join_tags(row['tags'])}"
                for row in repo_rows
            )
            if repo_rows
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    estate_action_queue.write_text(
        "# Estate Action Queue\\n\\n"
        f"- ranked_source_count: `{len(repo_rows)}`\\n"
        f"- highest_priority_bucket_across_estate: `{estate_highest_bucket}`\\n"
        "\\n## Recommended Next Moves\\n"
        + (
            "\\n".join(
                f"- {idx}. [{row['approval_gate']}] {row['label']} | owner={row['owner']} | environment={row['environment']} | priority_bucket={row['highest_priority_bucket']} | repo_priority_score={row['repo_priority_score']:.2f} | top_class={row['top_class']} | action={row['action']}"
                for idx, row in enumerate(repo_rows, start=1)
            )
            if repo_rows
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    estate_ingest_summary.write_text(
        "# Estate Ingest Summary\\n\\n"
        f"- explicit_source_count: `{len(explicit_sources)}`\\n"
        f"- manifest_source_count: `{len(manifest_sources)}`\\n"
        f"- discovered_source_count: `{len(discovered_sources)}`\\n"
        f"- unique_merged_source_count: `{len(merged_sources)}`\\n"
        f"- usable_source_count: `{len(repo_rows)}`\\n"
        f"- skipped_source_count: `{len(skipped_sources)}`\\n"
        "\\n## Source Origins\\n"
        + (
            "\\n".join(
                f"- {source['origin']}: {source['label']} -> {source['ndjson_path']} | owner={source['owner']} | environment={source['environment']} | host={source['host']} | repo_class={source['repo_class']} | tags={join_tags(source['tags'])}"
                for source in source_origin_rows
            )
            if source_origin_rows
            else "- none"
        )
        + "\\n\\n## Skipped Sources\\n"
        + (
            "\\n".join(f"- {item}" for item in skipped_sources)
            if skipped_sources
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    estate_catalog.write_text(
        "# Estate Catalog\\n\\n"
        f"- refresh_generated_utc: `{refresh_generated_utc}`\\n"
        f"- registered_source_count: `{len(merged_sources)}`\\n"
        f"- usable_source_count: `{len(repo_rows)}`\\n"
        "\\n## Registered Sources\\n"
        + (
            "\\n".join(
                f"- {source['label']}: origin={source['origin']}, owner={source['owner']}, environment={source['environment']}, host={source['host']}, repo_class={source['repo_class']}, tags={join_tags(source['tags'])}, ledger={source['ndjson_path']}, notes={source['notes'] if source['notes'] else 'none'}"
                for source in merged_sources
            )
            if merged_sources
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    archive_entry_count = len(all_snapshots)
    delta_available = previous_snapshot is not None

    estate_refresh_status.write_text(
        "# Estate Refresh Status\\n\\n"
        f"- refresh_generated_utc: `{refresh_generated_utc}`\\n"
        f"- manifest_file_count: `{len(args.manifest)}`\\n"
        f"- discover_root_count: `{len(args.discover_root)}`\\n"
        f"- explicit_source_count: `{len(explicit_sources)}`\\n"
        f"- unique_merged_source_count: `{len(merged_sources)}`\\n"
        f"- usable_source_count: `{len(repo_rows)}`\\n"
        f"- skipped_source_count: `{len(skipped_sources)}`\\n"
        f"- refresh_archive_entry_count: `{archive_entry_count}`\\n"
        f"- delta_available: `{'yes' if delta_available else 'no'}`\\n"
        f"- highest_priority_bucket_across_estate: `{estate_highest_bucket}`\\n"
        f"- sources_in_block: `{block_count}`\\n"
        f"- sources_in_review: `{review_count}`\\n"
        f"- sources_in_proceed: `{proceed_count}`\\n"
        "\\n## Refresh Inputs\\n"
        + (
            "\\n".join(f"- manifest: {Path(item).resolve()}" for item in args.manifest)
            if args.manifest
            else "- manifest: none"
        )
        + "\\n"
        + (
            "\\n".join(f"- discover_root: {Path(item).resolve()}" for item in args.discover_root)
            if args.discover_root
            else "- discover_root: none"
        )
        + "\\n\\n## Refresh Helper\\n"
        "- run `bash bin/estate-refresh.sh` to refresh from the repo registry\\n"
        "- set `ESTATE_DISCOVER_ROOTS` to one or more space-separated roots when discovery should also run\\n",
        encoding="utf-8",
    )

    previous_map = repo_map(previous_snapshot) if previous_snapshot else {}
    current_map = repo_map(current_snapshot)
    previous_order = repo_order_map(previous_snapshot) if previous_snapshot else {}
    current_order = repo_order_map(current_snapshot)

    if previous_snapshot:
        new_labels = sorted(set(current_map) - set(previous_map))
        removed_labels = sorted(set(previous_map) - set(current_map))

        gate_change_lines: list[str] = []
        severity_change_lines: list[tuple[int, str]] = []
        movement_lines: list[str] = []

        for label in sorted(set(current_map) & set(previous_map)):
            prev = previous_map[label]
            cur = current_map[label]

            if (
                prev.get("approval_gate") != cur.get("approval_gate")
                or prev.get("highest_priority_bucket") != cur.get("highest_priority_bucket")
            ):
                gate_change_lines.append(
                    f"- {label}: gate {prev.get('approval_gate', 'unknown')} -> {cur.get('approval_gate', 'unknown')}, priority_bucket {prev.get('highest_priority_bucket', 'unknown')} -> {cur.get('highest_priority_bucket', 'unknown')}"
                )

            prev_severity = int(prev.get("latest_weighted_severity", 0))
            cur_severity = int(cur.get("latest_weighted_severity", 0))
            if prev_severity != cur_severity:
                delta_value = cur_severity - prev_severity
                severity_change_lines.append(
                    (
                        abs(delta_value),
                        f"- {label}: latest_weighted_severity {prev_severity} -> {cur_severity} (delta {delta_value:+d})",
                    )
                )

            prev_pos = previous_order.get(label)
            cur_pos = current_order.get(label)
            if prev_pos is not None and cur_pos is not None and prev_pos != cur_pos:
                movement_lines.append(
                    f"- {label}: rank {prev_pos} -> {cur_pos}"
                )

        severity_change_lines.sort(key=lambda item: (-item[0], item[1]))

        estate_delta.write_text(
            "# Estate Delta\\n\\n"
            f"- previous_refresh_generated_utc: `{previous_snapshot.get('generated_utc', 'unknown')}`\\n"
            f"- current_refresh_generated_utc: `{current_snapshot.get('generated_utc', 'unknown')}`\\n"
            f"- usable_source_count_delta: `{int(current_snapshot.get('usable_source_count', 0)) - int(previous_snapshot.get('usable_source_count', 0)):+d}`\\n"
            f"- sources_in_block_delta: `{int(current_snapshot.get('sources_in_block', 0)) - int(previous_snapshot.get('sources_in_block', 0)):+d}`\\n"
            f"- sources_in_review_delta: `{int(current_snapshot.get('sources_in_review', 0)) - int(previous_snapshot.get('sources_in_review', 0)):+d}`\\n"
            f"- sources_in_proceed_delta: `{int(current_snapshot.get('sources_in_proceed', 0)) - int(previous_snapshot.get('sources_in_proceed', 0)):+d}`\\n"
            f"- total_latest_weighted_severity_delta: `{int(current_snapshot.get('total_latest_weighted_severity_across_sources', 0)) - int(previous_snapshot.get('total_latest_weighted_severity_across_sources', 0)):+d}`\\n"
            f"- highest_priority_bucket_previous: `{previous_snapshot.get('highest_priority_bucket_across_estate', 'normal')}`\\n"
            f"- highest_priority_bucket_current: `{current_snapshot.get('highest_priority_bucket_across_estate', 'normal')}`\\n"
            "\\n## New Sources\\n"
            + (
                "\\n".join(f"- {label}" for label in new_labels)
                if new_labels
                else "- none"
            )
            + "\\n\\n## Removed Sources\\n"
            + (
                "\\n".join(f"- {label}" for label in removed_labels)
                if removed_labels
                else "- none"
            )
            + "\\n\\n## Gate Or Priority Changes\\n"
            + (
                "\\n".join(gate_change_lines)
                if gate_change_lines
                else "- none"
            )
            + "\\n\\n## Severity Changes\\n"
            + (
                "\\n".join(line for _, line in severity_change_lines[:10])
                if severity_change_lines
                else "- none"
            )
            + "\\n\\n## Rank Movement\\n"
            + (
                "\\n".join(movement_lines)
                if movement_lines
                else "- none"
            )
            + "\\n",
            encoding="utf-8",
        )
    else:
        estate_delta.write_text(
            "# Estate Delta\\n\\n"
            "- previous_refresh_generated_utc: `none`\\n"
            f"- current_refresh_generated_utc: `{current_snapshot.get('generated_utc', 'unknown')}`\\n"
            "- delta_available: `no`\\n\\n"
            "No prior estate refresh exists yet, so delta reporting starts on the next refresh.\\n",
            encoding="utf-8",
        )

    highest_bucket_seen = "normal"
    for snapshot in all_snapshots:
        bucket = str(snapshot.get("highest_priority_bucket_across_estate", "normal"))
        if bucket_rank(bucket) > bucket_rank(highest_bucket_seen):
            highest_bucket_seen = bucket

    top_rank_counter = Counter()
    block_counter = Counter()

    for snapshot in all_snapshots:
        repos = snapshot.get("repos", []) or []
        if repos:
            top_rank_counter.update([str(repos[0].get("label", "unknown"))])
        for item in repos:
            if str(item.get("approval_gate", "")) == "block":
                block_counter.update([str(item.get("label", "unknown"))])

    usable_source_values = [int(snapshot.get("usable_source_count", 0)) for snapshot in all_snapshots]
    total_severity_values = [int(snapshot.get("total_latest_weighted_severity_across_sources", 0)) for snapshot in all_snapshots]
    max_block_count_seen = max((int(snapshot.get("sources_in_block", 0)) for snapshot in all_snapshots), default=0)

    estate_trends.write_text(
        "# Estate Trends\\n\\n"
        f"- refresh_archive_entry_count: `{len(all_snapshots)}`\\n"
        f"- first_refresh_generated_utc: `{all_snapshots[0].get('generated_utc', 'unknown') if all_snapshots else 'none'}`\\n"
        f"- latest_refresh_generated_utc: `{all_snapshots[-1].get('generated_utc', 'unknown') if all_snapshots else 'none'}`\\n"
        f"- highest_priority_bucket_seen: `{highest_bucket_seen}`\\n"
        f"- average_usable_source_count: `{average(usable_source_values):.2f}`\\n"
        f"- average_total_latest_weighted_severity: `{average(total_severity_values):.2f}`\\n"
        f"- max_sources_in_block_seen: `{max_block_count_seen}`\\n"
        "\\n## Refresh History\\n"
        + (
            "\\n".join(snapshot_summary_line(snapshot) for snapshot in all_snapshots[-10:])
            if all_snapshots
            else "- none"
        )
        + "\\n\\n## Sources Most Often Top-Ranked\\n"
        + (
            "\\n".join(
                f"- {label}: {count}"
                for label, count in top_rank_counter.most_common(10)
            )
            if top_rank_counter
            else "- none"
        )
        + "\\n\\n## Sources Most Often Blocked\\n"
        + (
            "\\n".join(
                f"- {label}: {count}"
                for label, count in block_counter.most_common(10)
            )
            if block_counter
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    estate_archive_index.write_text(
        "# Estate Archive Index\\n\\n"
        f"- archive_path: `{rel_or_abs(archive_path, repo)}`\\n"
        f"- refresh_archive_entry_count: `{len(all_snapshots)}`\\n"
        f"- oldest_refresh_generated_utc: `{all_snapshots[0].get('generated_utc', 'unknown') if all_snapshots else 'none'}`\\n"
        f"- latest_refresh_generated_utc: `{all_snapshots[-1].get('generated_utc', 'unknown') if all_snapshots else 'none'}`\\n"
        "\\n## Latest Archive Entries\\n"
        + (
            "\\n".join(snapshot_summary_line(snapshot) for snapshot in all_snapshots[-10:])
            if all_snapshots
            else "- none"
        )
        + "\\n",
        encoding="utf-8",
    )

    print(f"UPDATED {estate_history_summary}")
    print(f"UPDATED {estate_priority_queue}")
    print(f"UPDATED {estate_action_queue}")
    print(f"UPDATED {estate_ingest_summary}")
    print(f"UPDATED {estate_catalog}")
    print(f"UPDATED {estate_refresh_status}")
    print(f"UPDATED {estate_archive_index}")
    print(f"UPDATED {estate_delta}")
    print(f"UPDATED {estate_trends}")
    print(f"UPDATED {archive_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
        "bin/estate-aggregate.sh": """#!/usr/bin/env bash
set -Eeuo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

if [[ "$#" -lt 1 ]]; then
  cat >&2 <<'EOF'
usage:
  estate-aggregate.sh [sources...]
  estate-aggregate.sh --manifest manifest.json
  estate-aggregate.sh --discover-root /path/to/search
  estate-aggregate.sh [sources...] [--manifest manifest.json] [--discover-root /path]
EOF
  exit 2
fi

"${PYTHON_BIN}" "${REPO_DIR}/tools/build_estate_history_report.py" "$@"
""",
        "bin/estate-refresh.sh": """#!/usr/bin/env bash
set -Eeuo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
MANIFEST_PATH="${ESTATE_MANIFEST_PATH:-${REPO_DIR}/estate/estate_sources.json}"
DISCOVER_ROOTS_RAW="${ESTATE_DISCOVER_ROOTS:-}"

ARGS=()

if [[ -f "${MANIFEST_PATH}" ]]; then
  ARGS+=(--manifest "${MANIFEST_PATH}")
fi

if [[ -n "${DISCOVER_ROOTS_RAW}" ]]; then
  # shellcheck disable=SC2206
  DISCOVER_ROOTS=( ${DISCOVER_ROOTS_RAW} )
  for root in "${DISCOVER_ROOTS[@]}"; do
    ARGS+=(--discover-root "${root}")
  done
fi

ARGS+=("$@")

if [[ "${#ARGS[@]}" -lt 1 ]]; then
  cat >&2 <<'EOF'
usage:
  estate-refresh.sh [sources...]
  estate-refresh.sh alpha=/path/to/repo
  ESTATE_DISCOVER_ROOTS="/path/a /path/b" estate-refresh.sh
notes:
  - uses estate/estate_sources.json by default when present
  - accepts extra explicit sources on the command line
EOF
  exit 2
fi

"${PYTHON_BIN}" "${REPO_DIR}/tools/build_estate_history_report.py" "${ARGS[@]}"
""",
        "ops/systemd/estate-refresh.service": """[Unit]
Description=NOVAK SDT estate refresh
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
User=__RUN_AS_USER__
WorkingDirectory=__REPO_DIR__
Environment="ESTATE_RUNNER_MODE=timer"
Environment="ESTATE_DISCOVER_ROOTS=__ESTATE_DISCOVER_ROOTS__"
Environment="ESTATE_MAX_RETRIES=__ESTATE_MAX_RETRIES__"
Environment="ESTATE_RETRY_DELAY_SECONDS=__ESTATE_RETRY_DELAY_SECONDS__"
ExecStart=/usr/bin/env bash __REPO_DIR__/bin/estate-refresh-runner.sh

[Install]
WantedBy=multi-user.target
""",
        "ops/systemd/estate-refresh.timer": """[Unit]
Description=Run NOVAK SDT estate refresh on cadence

[Timer]
OnCalendar=__ON_CALENDAR__
Persistent=true
RandomizedDelaySec=60
Unit=estate-refresh.service

[Install]
WantedBy=timers.target
""",
        "bin/estate-refresh-runner.sh": """#!/usr/bin/env bash
set -Eeuo pipefail

START_EPOCH="$(date +%s)"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCK_DIR="${REPO_DIR}/.estate-refresh.lock"
STATUS_DOC="${REPO_DIR}/docs/estate/ESTATE_RUNNER_STATUS.md"
RUNNER_MODE="${ESTATE_RUNNER_MODE:-manual}"
MANIFEST_PATH="${ESTATE_MANIFEST_PATH:-none}"
DISCOVER_ROOTS="${ESTATE_DISCOVER_ROOTS:-none}"
ARGUMENT_COUNT="$#"
RUN_LABEL="estate-refresh-runner"
REFRESH_CMD="bash ${REPO_DIR}/bin/estate-refresh.sh $*"

mkdir -p "$(dirname "${STATUS_DOC}")"

write_status() {
  local started_utc="$1"
  local finished_utc="$2"
  local outcome="$3"
  local elapsed_seconds="$4"

  cat > "${STATUS_DOC}" <<DOC
# Estate Runner Status

- last_run_started_utc: ${started_utc}
- last_run_finished_utc: ${finished_utc}
- outcome: ${outcome}
- runner_mode: ${RUNNER_MODE}
- manifest_path: ${MANIFEST_PATH}
- discover_roots: ${DISCOVER_ROOTS}
- argument_count: ${ARGUMENT_COUNT}
- elapsed_seconds: ${elapsed_seconds}

## Command
- refresh_command: ${REFRESH_CMD}

## Notes
- run /tmp/estate-systemd render path is handled by install-estate-refresh-timer.sh
- review docs/estate/ESTATE_REFRESH_STATUS.md after each run
DOC
}

notify_event() {
  local event="$1"
  local message="$2"
  if [[ -f "${REPO_DIR}/bin/estate-notify.sh" ]]; then
    set +e
    bash "${REPO_DIR}/bin/estate-notify.sh" \
      --event "${event}" \
      --run-label "${RUN_LABEL}" \
      --message "${message}" \
      --source "${STATUS_DOC}" >/dev/null 2>&1
    set -e
  fi
}

STARTED_UTC="$(date -u '+%F %T UTC')"

if ! mkdir "${LOCK_DIR}" 2>/dev/null; then
  FINISHED_UTC="$(date -u '+%F %T UTC')"
  ELAPSED_SECONDS="$(( $(date +%s) - START_EPOCH ))"
  write_status "${STARTED_UTC}" "${FINISHED_UTC}" "lock-busy" "${ELAPSED_SECONDS}"
  notify_event "lock-busy" "estate refresh runner lock busy"
  exit 75
fi

cleanup() {
  rmdir "${LOCK_DIR}" 2>/dev/null || true
}
trap cleanup EXIT

set +e
bash "${REPO_DIR}/bin/estate-refresh.sh" "$@"
RC="$?"
set -e

FINISHED_UTC="$(date -u '+%F %T UTC')"
ELAPSED_SECONDS="$(( $(date +%s) - START_EPOCH ))"

if [[ "${RC}" -eq 0 ]]; then
  write_status "${STARTED_UTC}" "${FINISHED_UTC}" "success" "${ELAPSED_SECONDS}"
  notify_event "success" "estate refresh runner success"
else
  write_status "${STARTED_UTC}" "${FINISHED_UTC}" "failure" "${ELAPSED_SECONDS}"
  notify_event "failure" "estate refresh runner failure rc=${RC}"
fi

exit "${RC}"
""",
        "bin/install-estate-refresh-timer.sh": """#!/usr/bin/env bash
set -Eeuo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SERVICE_TEMPLATE="${REPO_DIR}/ops/systemd/estate-refresh.service"
TIMER_TEMPLATE="${REPO_DIR}/ops/systemd/estate-refresh.timer"
OUTPUT_DIR="${REPO_DIR}/ops/systemd/rendered"
ON_CALENDAR="${ESTATE_ON_CALENDAR:-daily}"
RUN_AS_USER="${ESTATE_RUN_AS_USER:-root}"
DISCOVER_ROOTS="${ESTATE_DISCOVER_ROOTS:-}"
MAX_RETRIES="${ESTATE_MAX_RETRIES:-2}"
RETRY_DELAY_SECONDS="${ESTATE_RETRY_DELAY_SECONDS:-30}"
INSTALL_MODE="no"

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --output-dir)
      OUTPUT_DIR="$2"
      shift 2
      ;;
    --on-calendar)
      ON_CALENDAR="$2"
      shift 2
      ;;
    --run-as-user)
      RUN_AS_USER="$2"
      shift 2
      ;;
    --discover-roots)
      DISCOVER_ROOTS="$2"
      shift 2
      ;;
    --max-retries)
      MAX_RETRIES="$2"
      shift 2
      ;;
    --retry-delay-seconds)
      RETRY_DELAY_SECONDS="$2"
      shift 2
      ;;
    --install)
      INSTALL_MODE="yes"
      shift
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

mkdir -p "${OUTPUT_DIR}"

python3 - "${SERVICE_TEMPLATE}" "${TIMER_TEMPLATE}" "${OUTPUT_DIR}" "${REPO_DIR}" "${RUN_AS_USER}" "${DISCOVER_ROOTS}" "${ON_CALENDAR}" "${MAX_RETRIES}" "${RETRY_DELAY_SECONDS}" <<INNERPY
from pathlib import Path
import sys

service_template = Path(sys.argv[1]).read_text(encoding="utf-8")
timer_template = Path(sys.argv[2]).read_text(encoding="utf-8")
output_dir = Path(sys.argv[3])
repo_dir = sys.argv[4]
run_as_user = sys.argv[5]
discover_roots = sys.argv[6]
on_calendar = sys.argv[7]
max_retries = sys.argv[8]
retry_delay_seconds = sys.argv[9]

replacements = {
    "__REPO_DIR__": repo_dir,
    "__RUN_AS_USER__": run_as_user,
    "__ESTATE_DISCOVER_ROOTS__": discover_roots,
    "__ON_CALENDAR__": on_calendar,
    "__ESTATE_MAX_RETRIES__": max_retries,
    "__ESTATE_RETRY_DELAY_SECONDS__": retry_delay_seconds,
}

service_text = service_template
timer_text = timer_template

for key, value in replacements.items():
    service_text = service_text.replace(key, value)
    timer_text = timer_text.replace(key, value)

(output_dir / "estate-refresh.service").write_text(service_text, encoding="utf-8")
(output_dir / "estate-refresh.timer").write_text(timer_text, encoding="utf-8")
print(f"WROTE {output_dir / 'estate-refresh.service'}")
print(f"WROTE {output_dir / 'estate-refresh.timer'}")
INNERPY

if [[ "${INSTALL_MODE}" == "yes" ]]; then
  cp "${OUTPUT_DIR}/estate-refresh.service" /etc/systemd/system/estate-refresh.service
  cp "${OUTPUT_DIR}/estate-refresh.timer" /etc/systemd/system/estate-refresh.timer
  systemctl daemon-reload
  echo "INSTALLED /etc/systemd/system/estate-refresh.service"
  echo "INSTALLED /etc/systemd/system/estate-refresh.timer"
  echo "NEXT: systemctl enable --now estate-refresh.timer"
fi
""",
                "bin/estate-notify.sh": """#!/usr/bin/env bash
set -Eeuo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTBOX="${REPO_DIR}/estate/outbox/notifications.ndjson"
STATUS_DOC="${REPO_DIR}/docs/estate/ESTATE_NOTIFICATION_STATUS.md"

EVENT=""
RUN_LABEL=""
STATUS=""
MESSAGE=""
SOURCE=""

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --event)
      EVENT="$2"
      shift 2
      ;;
    --run-label)
      RUN_LABEL="$2"
      shift 2
      ;;
    --status)
      STATUS="$2"
      shift 2
      ;;
    --message)
      MESSAGE="$2"
      shift 2
      ;;
    --source)
      SOURCE="$2"
      shift 2
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

if [[ -z "${EVENT}" ]]; then
  echo "ERROR: --event is required" >&2
  exit 2
fi

case "${EVENT}" in
  lock-busy)
    EXIT_RC=75
    DEFAULT_STATUS="LOCK_BUSY"
    ;;
  failure)
    EXIT_RC=2
    DEFAULT_STATUS="FAIL"
    ;;
  success)
    EXIT_RC=0
    DEFAULT_STATUS="PASS"
    ;;
  *)
    echo "ERROR: unsupported event: ${EVENT}" >&2
    exit 2
    ;;
esac

if [[ -z "${STATUS}" ]]; then
  STATUS="${DEFAULT_STATUS}"
fi

mkdir -p "$(dirname "${OUTBOX}")" "$(dirname "${STATUS_DOC}")"

python3 - "${OUTBOX}" "${STATUS_DOC}" "${EVENT}" "${RUN_LABEL}" "${STATUS}" "${MESSAGE}" "${SOURCE}" <<'INNERPY'
import json
import sys
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

outbox = Path(sys.argv[1])
status_doc = Path(sys.argv[2])
event = sys.argv[3]
run_label = sys.argv[4]
status = sys.argv[5]
message = sys.argv[6]
source = sys.argv[7]

timestamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")

record = {
    "event": event,
    "message": message,
    "run_label": run_label,
    "source": source,
    "status": status,
    "timestamp_utc": timestamp,
}

with outbox.open("a", encoding="utf-8") as f:
    f.write(json.dumps(record, sort_keys=True) + "\\n")

records = []
with outbox.open("r", encoding="utf-8") as f:
    for raw in f:
        raw = raw.strip()
        if raw:
            records.append(json.loads(raw))

counts = Counter(r["event"] for r in records)
last = records[-1]

latest_lines = []
for item in records[-5:]:
    latest_lines.append(
        f"- `{item['timestamp_utc']}` | `{item['event']}` | `{item['status']}` | `{item.get('run_label', '') or '-'}`"
    )

status_doc.write_text(
    "\\n".join(
        [
            "# Estate Notification Status",
            "",
            f"- total_events: `{len(records)}`",
            f"- last_event: `{last['event']}`",
            f"- last_status: `{last['status']}`",
            f"- last_run_label: `{last.get('run_label', '') or '-'}`",
            "",
            "## Counts",
            f"- lock-busy: `{counts.get('lock-busy', 0)}`",
            f"- failure: `{counts.get('failure', 0)}`",
            f"- success: `{counts.get('success', 0)}`",
            "",
            "## Latest 5 events",
            *latest_lines,
            "",
        ]
    ) + "\\n",
    encoding="utf-8",
)
INNERPY

echo "NOTIFY_EVENT=${EVENT} STATUS=${STATUS} RC=${EXIT_RC}"
exit "${EXIT_RC}"
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
