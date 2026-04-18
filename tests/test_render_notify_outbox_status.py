import json
import subprocess
from pathlib import Path


def test_render_notify_outbox_status(tmp_path: Path) -> None:
    outbox = tmp_path / "notifications.ndjson"
    outbox.write_text(
        "\n".join(
            [
                json.dumps({"event": "lock-busy", "status": "LOCK_BUSY", "run_label": "a", "timestamp_utc": "2026-04-18 00:00:00 UTC"}),
                json.dumps({"event": "success", "status": "PASS", "run_label": "b", "timestamp_utc": "2026-04-18 00:00:01 UTC"}),
            ]
        ) + "\n",
        encoding="utf-8",
    )
    output = tmp_path / "status.md"

    subprocess.run(
        ["python3", "tools/render_notify_outbox_status.py", str(outbox), str(output)],
        check=True,
        text=True,
        capture_output=True,
    )

    text = output.read_text(encoding="utf-8")
    assert "total_events: `2`" in text
    assert "lock-busy: `1`" in text
    assert "success: `1`" in text
