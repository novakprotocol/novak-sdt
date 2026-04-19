from __future__ import annotations

import subprocess
from pathlib import Path


def test_change_bundle_cli(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        [
            "sdt",
            "change-bundle",
            "--repo",
            str(repo),
            "--title",
            "Rename Hello World to Hello Worlds",
            "--type",
            "wording-change",
            "--why",
            "Demonstrate native SDT CLI change bundle scaffolding.",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert "CHANGE_RECORD=" in result.stdout
    assert (repo / "docs/changes/CHANGE_INDEX.md").exists()
    assert (repo / "docs/status/RENAME_HELLO_WORLD_TO_HELLO_WORLDS_PRESTATE.md").exists()
    assert (repo / "docs/status/RENAME_HELLO_WORLD_TO_HELLO_WORLDS_POSTSTATE.md").exists()

    matches = list((repo / "docs/changes").glob("*rename-hello-world-to-hello-worlds.md"))
    assert len(matches) == 1
