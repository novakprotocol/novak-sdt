from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
import json
import re
from typing import Any


def now_utc() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def read_attempts(repo: Path) -> list[dict[str, Any]]:
    path = repo / "docs/history/ATTEMPTS.ndjson"
    if not path.exists():
        return []

    attempts: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            attempts.append(json.loads(line))
        except Exception:
            attempts.append({"raw": line, "parse_error": True})
    return attempts


def read_change_docs(repo: Path) -> list[Path]:
    change_dir = repo / "docs/changes"
    if not change_dir.exists():
        return []
    return sorted([p for p in change_dir.glob("*.md") if p.is_file()])


def read_status_docs(repo: Path) -> dict[str, str]:
    status_dir = repo / "docs/status"
    if not status_dir.exists():
        return {}
    docs: dict[str, str] = {}
    for path in sorted(status_dir.glob("*.md")):
        docs[path.name] = read_text(path)
    return docs


def infer_failure_patterns(repo: Path) -> list[str]:
    findings: list[str] = []
    attempts = read_attempts(repo)
    status_docs = read_status_docs(repo)

    if not attempts:
        findings.append("No ATTEMPTS.ndjson evidence is present yet, so recurring execution failure patterns are not evidenced.")
    else:
        parse_errors = sum(1 for item in attempts if item.get("parse_error"))
        if parse_errors:
            findings.append(f"{parse_errors} ATTEMPTS.ndjson lines could not be parsed cleanly.")
        fail_markers = 0
        for item in attempts:
            text = json.dumps(item).lower()
            if any(word in text for word in ["fail", "error", "timeout", "rollback", "broken"]):
                fail_markers += 1
        if fail_markers:
            findings.append(f"{fail_markers} attempt records contain failure-like markers.")
        else:
            findings.append("Attempt records do not yet show obvious repeated failure markers.")

    for name, text in status_docs.items():
        lower = text.lower()
        if "head is ahead of latest tag" in lower:
            findings.append("Trusted-floor discipline issue: HEAD is ahead of the latest tag.")
        if "placeholder-like text still exists" in lower:
            findings.append("Core truth docs still contain placeholder-like content.")
        if "run_command is unknown" in lower:
            findings.append("Run path inference is still unresolved.")

    return dedupe(findings)


def infer_missed_opportunities(repo: Path) -> list[str]:
    findings: list[str] = []
    status_docs = read_status_docs(repo)
    change_docs = read_change_docs(repo)

    if not change_docs:
        findings.append("No structured change records are present yet; that limits later human/AI reconstruction quality.")

    for name, text in status_docs.items():
        lower = text.lower()
        if "missing managed inferred project state section" in lower:
            findings.append("Managed inferred sections are not yet being written back consistently into PROJECT_STATE.md.")
        if "missing managed inferred truth section" in lower:
            findings.append("Managed inferred sections are not yet being written back consistently into WHAT_IS_REAL_NOW.md.")
        if "docs/product/product_statement.md does not mention inferred product name" in lower:
            findings.append("Product docs and inferred naming are drifting apart.")
        if "runtime is unknown" in lower:
            findings.append("Runtime inference remains weak; shell wrappers are probably outweighing application code.")
        if "install_command is unknown" in lower:
            findings.append("Install path inference remains weak; repo classification is not yet good enough.")
        if "no change documents detected" in lower:
            findings.append("No change bundle history is being used yet to enrich repo memory.")
    return dedupe(findings)


def infer_priority_queue(repo: Path) -> list[str]:
    priorities: list[str] = []

    priorities.append("Tighten project intelligence scan hygiene by excluding .venv, node_modules, caches, site, build, dist, and other generated noise.")
    priorities.append("Recompute completeness and drift after writing managed sections so first-run reports reflect post-write truth, not pre-write gaps.")
    priorities.append("Weight runtime/language inference toward application code, imports, manifests, and entrypoints instead of shell wrappers.")
    priorities.append("Wire history intelligence into every serious SDT run so FAILURE_PATTERNS, MISSED_OPPORTUNITIES, and queues are continuously re-derived.")
    priorities.append("Generate or refresh change records automatically when meaningful repo mutations happen without a matching change document.")
    priorities.append("Track trusted floor explicitly when HEAD moves past the latest tag.")

    return dedupe(priorities)


def infer_action_queue(repo: Path) -> list[str]:
    return [
        "Run project intelligence and history intelligence on novak-sdt after every proof pass.",
        "Run the same intelligence pass on hello-world-sdt and hello-world-sdt-rc4 after meaningful updates.",
        "Add a birth hook so new repos get an immediate first-draft PROJECT_STATE and WHAT_IS_REAL_NOW instead of blank placeholders.",
        "Add a baseline hook so adopted repos get inferred truth plus a confirmation packet.",
    ]


def infer_remediation(repo: Path) -> list[str]:
    return [
        "Patch project_intel.py to ignore generated noise and recompute drift after managed writes.",
        "Patch project_intel.py to infer Python runtime for hello-world specimens from application files and tests.",
        "Add history_intel.py output generation into the SDT proof path.",
        "Add a trusted-floor status doc that explicitly states the current trusted floor, latest tag, and whether HEAD is ahead.",
    ]


def dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def write_doc(path: Path, title: str, bullets: list[str]) -> None:
    body = [f"# {title}", "", f"- stamp_utc: {now_utc()}", "", "## Items"]
    if bullets:
        body.extend([f"- {item}" for item in bullets])
    else:
        body.append("- none")
    path.write_text("\n".join(body) + "\n", encoding="utf-8")


def write_history_outputs(repo: Path) -> dict[str, Any]:
    history_dir = repo / "docs/history"
    history_dir.mkdir(parents=True, exist_ok=True)

    failure_patterns = infer_failure_patterns(repo)
    missed_opportunities = infer_missed_opportunities(repo)
    priority_queue = infer_priority_queue(repo)
    action_queue = infer_action_queue(repo)
    remediation = infer_remediation(repo)

    write_doc(history_dir / "FAILURE_PATTERNS.md", "Failure Patterns", failure_patterns)
    write_doc(history_dir / "MISSED_OPPORTUNITIES.md", "Missed Opportunities", missed_opportunities)
    write_doc(history_dir / "HISTORY_PRIORITY_QUEUE.md", "History Priority Queue", priority_queue)
    write_doc(history_dir / "HISTORY_ACTION_QUEUE.md", "History Action Queue", action_queue)
    write_doc(history_dir / "HISTORY_REMEDIATION.md", "History Remediation", remediation)

    index_lines = [
        "# History Index",
        "",
        f"- stamp_utc: {now_utc()}",
        "",
        "## Core history docs",
        "- ATTEMPTS.ndjson",
        "- FAILURE_PATTERNS.md",
        "- MISSED_OPPORTUNITIES.md",
        "- HISTORY_PRIORITY_QUEUE.md",
        "- HISTORY_ACTION_QUEUE.md",
        "- HISTORY_REMEDIATION.md",
    ]
    (history_dir / "HISTORY_INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    return {
        "failure_patterns": failure_patterns,
        "missed_opportunities": missed_opportunities,
        "priority_queue": priority_queue,
        "action_queue": action_queue,
        "remediation": remediation,
        "history_dir": str(history_dir),
    }
