from pathlib import Path


def test_extended_floor_contains_notify_contract() -> None:
    text = Path("src/novak_sdt/extended_floor.py").read_text(encoding="utf-8")

    required_snippets = [
        '"estate/notification_config.json"',
        '"estate/outbox/notifications.ndjson"',
        '"docs/estate/ESTATE_FAILURE_POLICY.md"',
        '"docs/estate/ESTATE_NOTIFICATIONS.md"',
        '"docs/estate/ESTATE_NOTIFICATION_STATUS.md"',
        '"bin/estate-notify.sh"',
        'Estate Notification Status: estate/ESTATE_NOTIFICATION_STATUS.md',
    ]

    for snippet in required_snippets:
        assert snippet in text, snippet
