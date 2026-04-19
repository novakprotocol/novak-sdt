from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
import json
from typing import Any


def now_utc() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")


def append_attempt(
    repo: Path,
    *,
    lane: str,
    event: str,
    status: str,
    note: str,
    command: str,
    extra: dict[str, Any] | None = None,
) -> Path:
    history_dir = repo / "docs/history"
    history_dir.mkdir(parents=True, exist_ok=True)

    path = history_dir / "ATTEMPTS.ndjson"
    payload: dict[str, Any] = {
        "stamp_utc": now_utc(),
        "lane": lane,
        "event": event,
        "status": status,
        "note": note,
        "command": command,
    }
    if extra:
        payload.update(extra)

    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True) + "\n")

    return path
