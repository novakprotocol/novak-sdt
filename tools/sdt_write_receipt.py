#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path


def run_cmd(cmd: list[str], cwd: Path) -> str:
    try:
        return subprocess.check_output(cmd, cwd=str(cwd), stderr=subprocess.STDOUT, text=True).rstrip()
    except Exception as exc:
        return f"UNAVAILABLE: {exc}"


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def tail_text(path: Path, count: int = 60) -> list[str]:
    if not path.exists():
        return []
    return read_text(path).splitlines()[-count:]


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def build_md(data: dict) -> str:
    lines: list[str] = []
    lines.append(f"# SDT Execution Receipt — {data['run_label']}")
    lines.append("")
    lines.append("## Identity")
    lines.append(f"- Run ID: `{data['run_id']}`")
    lines.append(f"- Status: `{data['status']}`")
    lines.append(f"- Operator: `{data['operator']}`")
    lines.append(f"- Host: `{data['host']}`")
    lines.append(f"- Repo path: `{data['repo_path']}`")
    lines.append(f"- Branch before: `{data['git']['branch_before']}`")
    lines.append(f"- Head before: `{data['git']['head_before']}`")
    lines.append(f"- Branch after: `{data['git']['branch_after']}`")
    lines.append(f"- Head after: `{data['git']['head_after']}`")
    lines.append("")
    lines.append("## Timing")
    lines.append(f"- Start local: `{data['timing']['start_local']}`")
    lines.append(f"- Start UTC: `{data['timing']['start_utc']}`")
    lines.append(f"- End local: `{data['timing']['end_local']}`")
    lines.append(f"- End UTC: `{data['timing']['end_utc']}`")
    lines.append(f"- Run elapsed sec: `{data['timing']['run_elapsed_sec']}`")
    lines.append(f"- Day total sec: `{data['timing']['day_total_sec']}`")
    lines.append(f"- Day run count: `{data['timing']['day_run_count']}`")
    lines.append("")
    lines.append("## Outcome")
    lines.append(f"- Next step: `{data['next_step'] or 'UNSET'}`")
    lines.append(f"- Public URL: `{data['public_url'] or 'UNSET'}`")
    lines.append(f"- Test summary: `{data['test_summary'] or 'UNSET'}`")
    lines.append("")
    lines.append("## Notes")
    notes = data['notes'].strip()
    lines.append(notes if notes else "- none")
    lines.append("")
    lines.append("## Steps")
    steps = data.get('steps', [])
    if steps:
        lines.extend(f"- `{item}`" for item in steps)
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Recent commits")
    lines.append("```text")
    lines.append(data['git']['recent_commits'] or "UNAVAILABLE")
    lines.append("```")
    lines.append("")
    lines.append("## Stdout tail")
    lines.append("```text")
    lines.extend(data.get('stdout_tail', []) or ["(no stdout captured)"])
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-path", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--day-number", required=True)
    parser.add_argument("--run-label", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--operator", required=True)
    parser.add_argument("--host", required=True)
    parser.add_argument("--start-local", required=True)
    parser.add_argument("--start-utc", required=True)
    parser.add_argument("--end-local", required=True)
    parser.add_argument("--end-utc", required=True)
    parser.add_argument("--run-elapsed-sec", type=int, required=True)
    parser.add_argument("--day-total-sec", type=int, required=True)
    parser.add_argument("--day-run-count", type=int, required=True)
    parser.add_argument("--branch-before", required=True)
    parser.add_argument("--head-before", required=True)
    parser.add_argument("--remote-url", required=True)
    parser.add_argument("--status-before-file", required=True)
    parser.add_argument("--stdout-log", required=True)
    parser.add_argument("--steps-log", required=True)
    parser.add_argument("--notes-file", required=True)
    parser.add_argument("--next-step", default="")
    parser.add_argument("--public-url", default="")
    parser.add_argument("--test-summary", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(args.repo_path).resolve()
    run_dir = repo / "docs" / "status" / "run-receipts" / args.run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    stdout_log = Path(args.stdout_log)
    steps_log = Path(args.steps_log)
    notes_file = Path(args.notes_file)
    status_before_file = Path(args.status_before_file)

    data = {
        "schema_version": 1,
        "generated_utc": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "run_id": args.run_id,
        "day_number": args.day_number,
        "run_label": args.run_label,
        "status": args.status,
        "operator": args.operator,
        "host": args.host,
        "repo_path": str(repo),
        "next_step": args.next_step,
        "public_url": args.public_url,
        "test_summary": args.test_summary,
        "notes": read_text(notes_file),
        "timing": {
            "start_local": args.start_local,
            "start_utc": args.start_utc,
            "end_local": args.end_local,
            "end_utc": args.end_utc,
            "run_elapsed_sec": args.run_elapsed_sec,
            "day_total_sec": args.day_total_sec,
            "day_run_count": args.day_run_count,
        },
        "git": {
            "branch_before": args.branch_before,
            "head_before": args.head_before,
            "remote_url": args.remote_url,
            "status_before": read_text(status_before_file).rstrip(),
            "branch_after": run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"], repo),
            "head_after": run_cmd(["git", "rev-parse", "HEAD"], repo),
            "recent_commits": run_cmd(["git", "log", "--oneline", "--decorate", "-10"], repo),
        },
        "steps": [line for line in read_text(steps_log).splitlines() if line.strip()],
        "stdout_tail": tail_text(stdout_log, 60),
    }

    write_json(run_dir / "run.json", data)
    (run_dir / "run.md").write_text(build_md(data), encoding="utf-8")

    latest = {
        "run_id": data["run_id"],
        "run_label": data["run_label"],
        "status": data["status"],
        "generated_utc": data["generated_utc"],
        "head_after": data["git"]["head_after"],
        "next_step": data["next_step"],
        "public_url": data["public_url"],
        "repo_path": data["repo_path"],
    }
    write_json(repo / "docs" / "status" / "LATEST_RUN.json", latest)

    ledger = repo / "docs" / "status" / "RUN_LEDGER.ndjson"
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with ledger.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(latest) + "\n")

    print(f"WROTE {run_dir / 'run.json'}")
    print(f"WROTE {run_dir / 'run.md'}")
    print(f"WROTE {repo / 'docs' / 'status' / 'LATEST_RUN.json'}")
    print(f"APPENDED {ledger}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
