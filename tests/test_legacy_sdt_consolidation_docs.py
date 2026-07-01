from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_adjacent_systems_keep_wrapit_name_and_role() -> None:
    text = (ROOT / "docs" / "architecture" / "N_SDT_ADJACENT_SYSTEMS.md").read_text(
        encoding="utf-8"
    )

    assert "Use **N-SDT** as the Novak display name" in text
    assert "repository: `novakprotocol/novak-sdt`" in text
    assert "CLI: `sdt`" in text
    assert "Keep W.R.A.P.I.T. as W.R.A.P.I.T." in text
    assert "Do not rename it to `N-SURE`" in text
    assert "W.R.A.P.I.T. owns evidence that a command ran" in text


def test_legacy_repo_consolidation_records_dispositions() -> None:
    text = (
        ROOT
        / "docs"
        / "architecture"
        / "LEGACY_SDT_REPO_CONSOLIDATION_20260701.md"
    ).read_text(encoding="utf-8")

    assert "`novakprotocol/novak-sdt` | Keep active." in text
    assert "Archived20260701-novak-sdt-born-proof" in text
    assert "Archived20260701-novak-control-plane" in text
    assert "Archived20260701-novak-repo-template" in text
    assert "`novakprotocol/W.R.A.P.I.T.` | Keep active." in text
    assert "`novakprotocol/S.I.G.I.L.` | Keep active." in text
    assert "Do not archive active products or tools" in text


def test_birth_template_parity_records_current_sdt_new_path() -> None:
    text = (
        ROOT / "docs" / "architecture" / "SDT_BIRTH_TEMPLATE_PARITY.md"
    ).read_text(encoding="utf-8")

    assert "`sdt new` is the current N-SDT repo birth path" in text
    assert "The old `novak-repo-template` repo is treated as a legacy template source" in text
    assert "`sdt doctor`" in text
    assert "Do not keep files in a born repo just because the template had them" in text
    assert "Archived20260701-novak-repo-template" in text
