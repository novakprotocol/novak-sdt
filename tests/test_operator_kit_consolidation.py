from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_operator_kit_files_exist():
    required = [
        "kits/operator-kit/README.md",
        "kits/operator-kit/docs/operator/ZERO_CONTEXT_HANDOFF_CHECKLIST.md",
        "kits/operator-kit/docs/operator/COLD_START_RECOVERY.md",
        "kits/operator-kit/docs/templates/NEXT_OPERATOR_PACKET_TEMPLATE.md",
        "kits/operator-kit/docs/templates/WHAT_IS_REAL_NOW_TEMPLATE.md",
        "kits/operator-kit/docs/templates/OPERATOR_HANDOFF_TEMPLATE.md",
        "kits/operator-kit/examples/minimal-repo-floor/README.md",
        "kits/operator-kit/examples/minimal-repo-floor/WHAT_IS_REAL_NOW.md",
        "kits/operator-kit/examples/minimal-repo-floor/PROJECT_STATE.md",
        "kits/operator-kit/examples/minimal-repo-floor/docs/operator/NEXT_OPERATOR_PACKET.md",
        "docs/operator-kit/README.md",
        "docs/operator-kit/MIGRATION_FROM_OLD_OPERATOR_KIT.md",
        "docs/operator-kit/DELETE_OR_ARCHIVE_OLD_REPO.md",
    ]

    for path in required:
        assert (ROOT / path).exists(), path


def test_operator_kit_boundary_is_clear():
    text = (ROOT / "kits/operator-kit/README.md").read_text(encoding="utf-8")

    assert "N-SDT operator kit" in text
    assert "RepoOps" in text
    assert "not RepoOps" in text
    assert "Use N-SDT first" in text
    assert "Use RepoOps second" in text


def test_old_repo_not_claimed_removed():
    migration = (ROOT / "docs/operator-kit/MIGRATION_FROM_OLD_OPERATOR_KIT.md").read_text(
        encoding="utf-8"
    )

    assert "The old repo was not deleted" in migration
    assert "The old repo was not archived" in migration
