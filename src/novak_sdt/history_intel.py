from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
import json
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
    items: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            items.append(json.loads(line))
        except Exception:
            items.append({"raw": line, "parse_error": True})
    return items


def read_change_docs(repo: Path) -> list[Path]:
    change_dir = repo / "docs/changes"
    if not change_dir.exists():
        return []
    return sorted([p for p in change_dir.glob("*.md") if p.is_file()])


def read_status_json(repo: Path) -> dict[str, Any]:
    path = repo / "docs/status/PROJECT_MODEL.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def infer_failure_patterns(repo: Path) -> list[str]:
    findings: list[str] = []
    attempts = read_attempts(repo)
    model = read_status_json(repo)

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

    if model.get("run_command", {}).get("value") == "unknown":
        findings.append("Run path inference is still unresolved.")
    if model.get("trusted_floor_status") == "HEAD_AHEAD_OR_TAG_UNKNOWN":
        findings.append("Trusted-floor discipline issue is present.")

    return dedupe(findings)


def infer_missed_opportunities(repo: Path) -> list[str]:
    findings: list[str] = []
    model = read_status_json(repo)
    change_docs = read_change_docs(repo)

    if not change_docs:
        findings.append("No structured change records are present yet; that limits later human/AI reconstruction quality.")

    if model.get("runtime", {}).get("value") == "unknown":
        findings.append("Runtime inference remains weak; shell wrappers are probably outweighing application code.")
    if model.get("install_command", {}).get("value") == "unknown":
        findings.append("Install path inference remains weak; repo classification is not yet good enough.")
    if model.get("trusted_floor_status") == "HEAD_AHEAD_OR_TAG_UNKNOWN":
        findings.append("Trusted floor is not explicitly frozen at HEAD.")
    if model.get("placeholders_detected"):
        findings.append("Core truth docs still carry unmanaged placeholder-like content.")

    return dedupe(findings)


def infer_priority_queue(repo: Path) -> list[str]:
    return [
        "Tighten project intelligence scan hygiene by excluding .venv, node_modules, caches, site, build, dist, and other generated noise.",
        "Weight runtime/language inference toward application code, imports, manifests, and entrypoints instead of shell wrappers.",
        "Force birth and baseline to run truth refresh immediately after floor creation.",
        "Generate or refresh change records automatically when meaningful repo mutations happen without a matching change document.",
        "Track trusted floor explicitly when HEAD moves past the latest tag.",
        "Append attempt records automatically from truth-refresh and proof runs.",
    ]


def infer_action_queue(repo: Path) -> list[str]:
    return [
        "Run truth refresh on novak-sdt after every proof pass.",
        "Run the same truth refresh on hello-world-sdt and hello-world-sdt-rc4 after meaningful updates.",
        "Add a birth hook so new repos get immediate PROJECT_STATE and WHAT_IS_REAL_NOW drafts instead of blank placeholders.",
        "Add a baseline hook so adopted repos get inferred truth plus a confirmation packet.",
    ]


def infer_remediation(repo: Path) -> list[str]:
    return [
        "Patch project_intel.py to infer Python for hello-world specimens from application files and tests.",
        "Patch project_intel.py to produce canonical product names from repo truth, not raw title casing.",
        "Patch proof flow to call truth refresh automatically.",
        "Patch change bundle flow to update attempts/history surfaces automatically.",
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
    lines = [f"# {title}", "", f"- stamp_utc: {now_utc()}", "", "## Items"]
    if bullets:
        lines.extend([f"- {item}" for item in bullets])
    else:
        lines.append("- none")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
