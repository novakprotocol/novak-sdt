from pathlib import Path


def test_extended_floor_contains_change_index() -> None:
    text = Path("src/novak_sdt/extended_floor.py").read_text(encoding="utf-8")
    assert '"docs/changes/CHANGE_INDEX.md"' in text
    assert 'Change Index: changes/CHANGE_INDEX.md' in text
