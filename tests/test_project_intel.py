from __future__ import annotations

import json
from pathlib import Path

from novak_sdt.project_intel import write_outputs


def test_project_intel_writes_outputs(tmp_path: Path) -> None:
    repo = tmp_path / "demo"
    repo.mkdir()

    (repo / "docs/product").mkdir(parents=True)
    (repo / "docs/status").mkdir(parents=True)
    (repo / "tests").mkdir(parents=True)
    (repo / "bin").mkdir(parents=True)

    (repo / "pyproject.toml").write_text(
        """
[project]
name = "demo-tool"
version = "0.0.1"
""".strip()
        + "\n",
        encoding="utf-8",
    )

    (repo / "README.md").write_text("# Demo Tool\n", encoding="utf-8")
    (repo / "PROJECT_STATE.md").write_text("fill in later\n", encoding="utf-8")
    (repo / "WHAT_IS_REAL_NOW.md").write_text("fill in later\n", encoding="utf-8")
    (repo / "docs/product/PRODUCT_STATEMENT.md").write_text("fill in later\n", encoding="utf-8")
    (repo / "docs/INSTALLATION.md").write_text("fill in later\n", encoding="utf-8")
    (repo / "bin/run-hello-world.sh").write_text("#!/usr/bin/env bash\n", encoding="utf-8")
    (repo / "tests/test_smoke.py").write_text("def test_smoke():\n    assert True\n", encoding="utf-8")

    result = write_outputs(repo, apply_docs=True)

    assert result["score"] >= 0
    assert (repo / "docs/status/PROJECT_MODEL.json").exists()
    assert (repo / "docs/status/SDT_CONFIRMATION_PACKET.md").exists()
    assert (repo / "docs/status/SDT_COMPLETENESS_REPORT.md").exists()
    assert (repo / "docs/status/SDT_DRIFT_REPORT.md").exists()

    model = json.loads((repo / "docs/status/PROJECT_MODEL.json").read_text(encoding="utf-8"))
    assert model["product_name"]["value"] == "demo-tool"
    assert model["run_command"]["value"] == "bash bin/run-hello-world.sh"

    project_state = (repo / "PROJECT_STATE.md").read_text(encoding="utf-8")
    assert "SDT:BEGIN inferred project state" in project_state

    what_is_real_now = (repo / "WHAT_IS_REAL_NOW.md").read_text(encoding="utf-8")
    assert "SDT:BEGIN inferred what is real now" in what_is_real_now


def test_project_intel_detects_placeholders(tmp_path: Path) -> None:
    repo = tmp_path / "demo2"
    repo.mkdir()
    (repo / "docs/product").mkdir(parents=True)
    (repo / "docs/status").mkdir(parents=True)

    (repo / "README.md").write_text("TBD\n", encoding="utf-8")
    (repo / "PROJECT_STATE.md").write_text("fill in\n", encoding="utf-8")
    (repo / "WHAT_IS_REAL_NOW.md").write_text("<owner>\n", encoding="utf-8")
    (repo / "docs/product/PRODUCT_STATEMENT.md").write_text("TODO\n", encoding="utf-8")
    (repo / "docs/INSTALLATION.md").write_text("TBD\n", encoding="utf-8")

    result = write_outputs(repo, apply_docs=False)
    assert result["issues"]
