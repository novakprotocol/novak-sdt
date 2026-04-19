from __future__ import annotations

import json
from pathlib import Path

from novak_sdt.project_intel import list_files, write_outputs, infer_primary_language
from novak_sdt.history_intel import write_history_outputs
from novak_sdt.trusted_floor import write_trusted_floor_status


def test_list_files_ignores_noise(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    (repo / ".venv").mkdir(parents=True)
    (repo / ".venv" / "x.py").write_text("print('x')\n", encoding="utf-8")
    (repo / "app").mkdir(parents=True)
    (repo / "app" / "main.py").write_text("print('ok')\n", encoding="utf-8")
    files = list_files(repo)
    paths = {str(p.relative_to(repo)) for p in files}
    assert "app/main.py" in paths
    assert ".venv/x.py" not in paths


def test_python_beats_shell_for_hello_world_shape(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    (repo / "app").mkdir(parents=True)
    (repo / "bin").mkdir(parents=True)
    (repo / "tests").mkdir(parents=True)

    for idx in range(2):
        (repo / "app" / f"mod{idx}.py").write_text("print('ok')\n", encoding="utf-8")
    for idx in range(1):
        (repo / "tests" / f"test_{idx}.py").write_text("assert True\n", encoding="utf-8")
    for idx in range(3):
        (repo / "bin" / f"run{idx}.sh").write_text("#!/usr/bin/env bash\n", encoding="utf-8")

    files = list_files(repo)
    field = infer_primary_language(files)
    assert field.value == "Python"


def test_write_outputs_recomputes_after_doc_write(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    (repo / "docs/product").mkdir(parents=True)
    (repo / "docs/status").mkdir(parents=True)
    (repo / "app").mkdir(parents=True)
    (repo / "tests").mkdir(parents=True)
    (repo / "README.md").write_text("# Demo Product\n", encoding="utf-8")
    (repo / "PROJECT_STATE.md").write_text("fill in later\n", encoding="utf-8")
    (repo / "WHAT_IS_REAL_NOW.md").write_text("fill in later\n", encoding="utf-8")
    (repo / "docs/product/PRODUCT_STATEMENT.md").write_text("fill in later\n", encoding="utf-8")
    (repo / "docs/INSTALLATION.md").write_text("fill in later\n", encoding="utf-8")
    (repo / "app" / "main.py").write_text("print('ok')\n", encoding="utf-8")
    (repo / "tests" / "test_smoke.py").write_text("def test_smoke():\n    assert True\n", encoding="utf-8")

    result = write_outputs(repo, apply_docs=True)

    assert (repo / "docs/status/PROJECT_MODEL.json").exists()
    issues = "\n".join(result["issues"])
    assert "PROJECT_STATE.md missing" not in issues
    assert "WHAT_IS_REAL_NOW.md missing" not in issues


def test_history_and_trusted_floor_outputs(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    (repo / "docs/history").mkdir(parents=True)
    (repo / "docs/status").mkdir(parents=True)
    (repo / "docs/history" / "ATTEMPTS.ndjson").write_text(
        '{"event":"failure","note":"timeout"}\n{"event":"success"}\n',
        encoding="utf-8",
    )
    (repo / "docs/status" / "PROJECT_MODEL.json").write_text(
        json.dumps({
            "run_command": {"value": "unknown"},
            "trusted_floor_status": "HEAD_AHEAD_OR_TAG_UNKNOWN",
            "runtime": {"value": "unknown"},
            "install_command": {"value": "unknown"},
            "placeholders_detected": ["x"],
        }) + "\n",
        encoding="utf-8",
    )

    history = write_history_outputs(repo)
    assert history["failure_patterns"]
    assert (repo / "docs/history/HISTORY_INDEX.md").exists()

    trusted = write_trusted_floor_status(repo)
    assert (repo / "docs/status/TRUSTED_FLOOR_STATUS.md").exists()
    assert "trusted_floor_status" in trusted
