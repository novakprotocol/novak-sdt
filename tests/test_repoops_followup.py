from __future__ import annotations

import subprocess
from pathlib import Path


def test_baseline_report_only_prints_repoops_followup(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()

    result = subprocess.run(
        [
            "sdt",
            "baseline",
            "--path",
            str(repo),
            "--product-name",
            "Adapter Proof",
            "--product-statement",
            "Adapter Proof validates N-SDT to RepoOps next-step guidance.",
            "--report-only",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert "RepoOps next step:" in result.stdout
    assert "review the missing N-SDT truth and continuity files" in result.stdout
    assert "run `sdt baseline` before RepoOps dry-run" in result.stdout


def test_baseline_prints_repoops_followup_after_apply(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()

    result = subprocess.run(
        [
            "sdt",
            "baseline",
            "--path",
            str(repo),
            "--product-name",
            "Adapter Proof",
            "--product-statement",
            "Adapter Proof validates N-SDT to RepoOps next-step guidance.",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert "RepoOps next step:" in result.stdout
    assert "run RepoOps dry-run or report mode" in result.stdout
    assert "choose the smallest RepoOps profile that fits" in result.stdout
    assert "review suggested merges and record exceptions" in result.stdout
