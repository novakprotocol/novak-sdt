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


def test_change_bundle_cli_apply_proof(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir(parents=True, exist_ok=True)

    subprocess.run(["git", "init", "-b", "main"], cwd=repo, check=True, capture_output=True, text=True)
    subprocess.run(["git", "config", "user.name", "novakprotocol"], cwd=repo, check=True, capture_output=True, text=True)
    subprocess.run(["git", "config", "user.email", "devnull@example.invalid"], cwd=repo, check=True, capture_output=True, text=True)

    (repo / "README.md").write_text("proof repo\n", encoding="utf-8")
    subprocess.run(["git", "add", "README.md"], cwd=repo, check=True, capture_output=True, text=True)
    subprocess.run(["git", "commit", "-m", "init"], cwd=repo, check=True, capture_output=True, text=True)

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
            "Demonstrate native SDT CLI proof capture.",
            "--apply-proof",
            "--command",
            "python3 -c \"print('proof-ok')\"",
            "--proof-ref",
            "docs/status/EXAMPLE_PROOF.md",
        ],
        text=True,
        capture_output=True,
        check=True,
    )

    assert "CHANGE_RECORD=" in result.stdout

    poststate = (repo / "docs/status/RENAME_HELLO_WORLD_TO_HELLO_WORLDS_POSTSTATE.md").read_text(encoding="utf-8")
    assert "## Applied proof" in poststate
    assert "- branch: main" in poststate
    assert "## Commands" in poststate
    assert "proof-ok" in poststate
    assert "## Proof references" in poststate
    assert "docs/status/EXAMPLE_PROOF.md" in poststate

    change_record = next((repo / "docs/changes").glob("*rename-hello-world-to-hello-worlds.md")).read_text(encoding="utf-8")
    assert "## Verification performed" in change_record
    assert "docs/status/EXAMPLE_PROOF.md" in change_record
