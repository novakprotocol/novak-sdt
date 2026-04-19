from __future__ import annotations

from pathlib import Path

from novak_sdt.attempt_log import append_attempt


def test_append_attempt_creates_ndjson(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()

    path = append_attempt(
        repo,
        lane="truth-refresh",
        event="truth-refresh",
        status="PASS",
        note="ok",
        command="python3 tools/sdt_truth_refresh.py --repo demo",
        extra={"score": 77},
    )

    text = path.read_text(encoding="utf-8")
    assert '"lane": "truth-refresh"' in text
    assert '"status": "PASS"' in text
    assert '"score": 77' in text
