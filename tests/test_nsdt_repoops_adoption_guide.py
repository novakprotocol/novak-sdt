from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs" / "architecture" / "N_SDT_REPOOPS_ADOPTION_GUIDE.md"


def test_nsdt_repoops_adoption_guide_exists_and_is_scoped() -> None:
    text = GUIDE.read_text(encoding="utf-8")

    assert "Accepted as the current narrow adoption path" in text
    assert "This guide intentionally covers only two layers" in text
    assert "- N-SDT" in text
    assert "- RepoOps" in text
    assert "bring adjacent product/evidence systems into" in text


def test_nsdt_repoops_adoption_guide_records_layer_contract() -> None:
    text = GUIDE.read_text(encoding="utf-8")

    assert "N-SDT explains the repo." in text
    assert "RepoOps governs the repo." in text
    assert "N-SDT = what is true and how to continue" in text
    assert "RepoOps = how the repo is operated and checked" in text
    assert "Do not make N-SDT write RepoOps governance files by default." in text
    assert "Do not make RepoOps rewrite N-SDT truth files by default." in text


def test_nsdt_repoops_adoption_guide_records_sequence_and_done() -> None:
    text = GUIDE.read_text(encoding="utf-8")

    assert "Run N-SDT report-only." in text
    assert "Run `sdt doctor`." in text
    assert "Run RepoOps in dry-run or report mode." in text
    assert "RepoOps profile choice is recorded." in text
    assert "Existing important files were not silently overwritten." in text
