from __future__ import annotations

from pathlib import Path

from novak_sdt.history_intel import write_history_outputs


def test_history_intel_writes_outputs(tmp_path: Path) -> None:
    repo = tmp_path / "demo"
    repo.mkdir()
    (repo / "docs/history").mkdir(parents=True)
    (repo / "docs/status").mkdir(parents=True)

    (repo / "docs/history/ATTEMPTS.ndjson").write_text(
        '{"event":"failure","note":"timeout"}\n{"event":"success"}\n',
        encoding="utf-8",
    )
    (repo / "docs/status/SDT_DRIFT_REPORT.md").write_text(
        "# SDT Drift Report\n\n- HEAD is ahead of latest tag\n",
        encoding="utf-8",
    )

    result = write_history_outputs(repo)

    assert result["failure_patterns"]
    assert (repo / "docs/history/FAILURE_PATTERNS.md").exists()
    assert (repo / "docs/history/MISSED_OPPORTUNITIES.md").exists()
    assert (repo / "docs/history/HISTORY_PRIORITY_QUEUE.md").exists()
    assert (repo / "docs/history/HISTORY_ACTION_QUEUE.md").exists()
    assert (repo / "docs/history/HISTORY_REMEDIATION.md").exists()
    assert (repo / "docs/history/HISTORY_INDEX.md").exists()
