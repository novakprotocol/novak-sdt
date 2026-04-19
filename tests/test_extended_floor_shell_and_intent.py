from pathlib import Path

def test_extended_floor_contains_shell_and_intent() -> None:
    text = Path("src/novak_sdt/extended_floor.py").read_text(encoding="utf-8")
    assert '"docs/templates/SDT_CHANGE_INTENT_TEMPLATE.md"' in text
    assert '"tools/sdt_shell_activate.sh"' in text
    assert '"tools/install_novak_shell_shortcuts.sh"' in text
