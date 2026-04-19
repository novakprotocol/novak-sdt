from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
import subprocess
from typing import Any


def now_utc() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")


def git_output(repo: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def write_trusted_floor_status(repo: Path) -> dict[str, Any]:
    latest_tag = git_output(repo, "describe", "--tags", "--abbrev=0")
    head_commit = git_output(repo, "rev-parse", "HEAD")
    head_branch = git_output(repo, "branch", "--show-current")
    tag_commit = git_output(repo, "rev-list", "-n", "1", latest_tag) if latest_tag != "unknown" else "unknown"

    status = "HEAD_EQUALS_LATEST_TAG" if latest_tag != "unknown" and head_commit == tag_commit else "HEAD_AHEAD_OR_TAG_UNKNOWN"

    path = repo / "docs/status/TRUSTED_FLOOR_STATUS.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Trusted Floor Status",
        "",
        f"- stamp_utc: {now_utc()}",
        f"- branch: {head_branch}",
        f"- head_commit: {head_commit}",
        f"- latest_tag: {latest_tag}",
        f"- latest_tag_commit: {tag_commit}",
        f"- trusted_floor_status: {status}",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return {
        "latest_tag": latest_tag,
        "head_commit": head_commit,
        "latest_tag_commit": tag_commit,
        "trusted_floor_status": status,
        "status_path": str(path),
    }
