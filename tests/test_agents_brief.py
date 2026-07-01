from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_agents_brief_keeps_nsdt_repoops_boundary_visible() -> None:
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    assert "N-SDT is the truth and continuity layer." in text
    assert "RepoOps is the repository operations layer." in text
    assert "WhyPy currently contains the active RepoOps source" in text
    assert "Do not merge RepoOps into N-SDT." in text
    assert "Do not split RepoOps into a standalone repo yet." in text
    assert "Do not pick random target repos for adoption." in text
    assert "Run `sdt baseline --report-only`." in text


def test_readme_points_agents_to_agent_brief() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "- `AGENTS.md`" in text
