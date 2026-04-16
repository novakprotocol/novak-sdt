#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HISTORY = REPO / "docs" / "history"
RAW = HISTORY / "raw"
SCRIPTS = HISTORY / "scripts"
LEDGER = HISTORY / "ATTEMPTS.ndjson"
INDEX_MD = HISTORY / "HISTORY_INDEX.md"
FAIL_MD = HISTORY / "FAILURE_PATTERNS.md"
MISSED_MD = HISTORY / "MISSED_OPPORTUNITIES.md"

RUN_BLOCK = re.compile(
    r"RUN_LABEL:\s+(?P<label>.+?)\n"
    r".*?START_UTC:\s+(?P<start_utc>.+?)\n"
    r".*?\[DAY-[^\]]+\]\s+RUN COMPLETE.*?"
    r"STATUS:\s+(?P<status>PASS|FAIL)\s*"
    r".*?END_UTC:\s+(?P<end_utc>.+?)\n"
    r"RUN_ELAPSED_SEC:\s+(?P<elapsed>\d+)\n"
    r"DAY_TOTAL_SEC:\s+(?P<day_total>\d+)\n"
    r"DAY_RUN_COUNT:\s+(?P<day_run_count>\d+)\n"
    r".*?EXIT_CODE:\s+(?P<exit_code>\d+)",
    re.S,
)

NEXT_RE = re.compile(r"NEXT_(?:PAIR|MOVE)=(?P<next>.+)")
COMMIT_RE = re.compile(r"^\[main (?P<sha>[0-9a-f]+)\] (?P<msg>.+)$", re.M)

ERROR_PATTERNS = [
    r"fatal: .+",
    r"-bash: .+",
    r"ERROR: .+",
    r"Traceback \(most recent call last\):",
    r"Permission denied.+",
    r"command not found",
]

def ensure_dirs() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    SCRIPTS.mkdir(parents=True, exist_ok=True)
    HISTORY.mkdir(parents=True, exist_ok=True)
    if not LEDGER.exists():
        LEDGER.write_text("", encoding="utf-8")

def now_utc() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def load_records() -> list[dict]:
    rows: list[dict] = []
    if not LEDGER.exists():
        return rows
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            continue
    return rows

def write_records(records: list[dict]) -> None:
    records = sorted(records, key=lambda x: (x.get("start_utc", ""), x.get("run_label", "")))
    with LEDGER.open("w", encoding="utf-8") as handle:
        for row in records:
            handle.write(json.dumps(row, sort_keys=True) + "\n")

def unique_errors(text: str) -> list[str]:
    found: list[str] = []
    for pattern in ERROR_PATTERNS:
        for match in re.finditer(pattern, text, re.M):
            msg = match.group(0).strip()
            if msg not in found:
                found.append(msg)
    return found[:12]

def parse_runs(text: str, source_name: str, raw_rel: str) -> list[dict]:
    rows: list[dict] = []
    blocks = list(RUN_BLOCK.finditer(text))

    if not blocks:
        rows.append({
            "record_type": "log_only",
            "imported_utc": now_utc(),
            "source_name": source_name,
            "raw_log": raw_rel,
            "status": "UNKNOWN",
            "run_label": source_name,
            "start_utc": "",
            "end_utc": "",
            "elapsed_sec": None,
            "day_total_sec": None,
            "day_run_count": None,
            "exit_code": None,
            "next_step": "",
            "commit_sha": "",
            "commit_msg": "",
            "error_count": len(unique_errors(text)),
            "errors": unique_errors(text),
            "notes": "No structured RUN COMPLETE block found; raw log preserved.",
        })
        return rows

    for block in blocks:
        chunk = block.group(0)

        commit_match = None
        for m in COMMIT_RE.finditer(chunk):
            commit_match = m

        next_match = None
        for m in NEXT_RE.finditer(chunk):
            next_match = m

        rows.append({
            "record_type": "run_attempt",
            "imported_utc": now_utc(),
            "source_name": source_name,
            "raw_log": raw_rel,
            "run_label": block.group("label").strip(),
            "status": block.group("status").strip(),
            "start_utc": block.group("start_utc").strip(),
            "end_utc": block.group("end_utc").strip(),
            "elapsed_sec": int(block.group("elapsed")),
            "day_total_sec": int(block.group("day_total")),
            "day_run_count": int(block.group("day_run_count")),
            "exit_code": int(block.group("exit_code")),
            "next_step": next_match.group("next").strip() if next_match else "",
            "commit_sha": commit_match.group("sha") if commit_match else "",
            "commit_msg": commit_match.group("msg").strip() if commit_match else "",
            "error_count": len(unique_errors(chunk)),
            "errors": unique_errors(chunk),
            "notes": "",
        })
    return rows

def dedupe(records: list[dict]) -> list[dict]:
    seen: set[tuple] = set()
    out: list[dict] = []
    for row in records:
        key = (
            row.get("record_type"),
            row.get("run_label"),
            row.get("start_utc"),
            row.get("raw_log"),
            row.get("status"),
        )
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out

def render_index(records: list[dict]) -> None:
    attempts = [r for r in records if r.get("record_type") == "run_attempt"]
    total = len(attempts)
    passed = sum(1 for r in attempts if r.get("status") == "PASS")
    failed = sum(1 for r in attempts if r.get("status") == "FAIL")

    lines = [
        "# History Index",
        "",
        f"- generated_utc: `{now_utc()}`",
        f"- total_attempts: `{total}`",
        f"- pass_count: `{passed}`",
        f"- fail_count: `{failed}`",
        "",
        "## Recent attempts",
        "",
        "| Start UTC | Status | Run label | Elapsed sec | Next step | Commit | Errors |",
        "|---|---|---|---:|---|---|---:|",
    ]

    for row in sorted(attempts, key=lambda x: x.get("start_utc", ""), reverse=True)[:40]:
        lines.append(
            f"| `{row.get('start_utc','')}` | `{row.get('status','')}` | "
            f"`{row.get('run_label','')}` | `{row.get('elapsed_sec','')}` | "
            f"`{row.get('next_step','')}` | `{row.get('commit_sha','')}` | `{row.get('error_count','')}` |"
        )

    INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

def render_failures(records: list[dict]) -> None:
    counter: Counter[str] = Counter()
    for row in records:
        for err in row.get("errors", []):
            counter[err] += 1

    lines = [
        "# Failure Patterns",
        "",
        f"- generated_utc: `{now_utc()}`",
        "",
        "| Error pattern | Count |",
        "|---|---:|",
    ]
    for err, count in counter.most_common(50):
        lines.append(f"| `{err}` | `{count}` |")

    FAIL_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

def render_missed(records: list[dict]) -> None:
    lines = [
        "# Missed Opportunities",
        "",
        "This page is a review surface for gaps, retries, and avoidable failures.",
        "",
        f"- generated_utc: `{now_utc()}`",
        "",
        "## Suggested review prompts",
        "",
        "- Which failures repeated more than once?",
        "- Which commands assumed files that did not exist yet?",
        "- Which steps were blocked by auth or environment drift?",
        "- Which tools were documented as present but not actually verified?",
        "- Which steps should have been turned into wrappers earlier?",
        "",
        "## Recent attempts",
        "",
    ]

    for row in sorted(records, key=lambda x: x.get("start_utc", ""), reverse=True)[:15]:
        if row.get("record_type") != "run_attempt":
            continue
        lines.extend([
            f"### {row.get('run_label','UNKNOWN')}",
            "",
            f"- status: `{row.get('status','')}`",
            f"- start_utc: `{row.get('start_utc','')}`",
            f"- elapsed_sec: `{row.get('elapsed_sec','')}`",
            f"- next_step: `{row.get('next_step','')}`",
            f"- commit_sha: `{row.get('commit_sha','')}`",
        ])
        if row.get("errors"):
            lines.append("- errors:")
            for err in row["errors"]:
                lines.append(f"  - `{err}`")
        lines.append("")

    MISSED_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

def main() -> int:
    parser = argparse.ArgumentParser(description="Archive shell history logs into docs/history.")
    parser.add_argument("--log-file", action="append", required=True, help="Path to a transcript/log file")
    args = parser.parse_args()

    ensure_dirs()
    records = load_records()

    for log_file in args.log_file:
        src = Path(log_file).expanduser().resolve()
        if not src.exists():
            print(f"SKIP missing log file: {src}")
            continue

        text = src.read_text(encoding="utf-8", errors="replace")
        dst_name = f"{now_utc()}__{src.name}"
        dst = RAW / dst_name
        shutil.copy2(src, dst)
        raw_rel = f"raw/{dst_name}"

        parsed = parse_runs(text, src.name, raw_rel)
        for row in parsed:
            row["source_sha256"] = sha256_text(text)
            records.append(row)

    records = dedupe(records)
    write_records(records)
    render_index(records)
    render_failures(records)
    render_missed(records)

    print(f"WROTE {LEDGER}")
    print(f"WROTE {INDEX_MD}")
    print(f"WROTE {FAIL_MD}")
    print(f"WROTE {MISSED_MD}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
