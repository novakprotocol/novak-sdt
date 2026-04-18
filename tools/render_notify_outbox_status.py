#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: render_notify_outbox_status.py <outbox_ndjson> <output_md>", file=sys.stderr)
        return 2

    outbox = Path(sys.argv[1])
    output = Path(sys.argv[2])

    records = []
    if outbox.exists():
        for raw in outbox.read_text(encoding="utf-8").splitlines():
            raw = raw.strip()
            if raw:
                records.append(json.loads(raw))

    counts = Counter(r["event"] for r in records)
    latest = records[-5:]

    lines = [
        "# Rendered Notify Outbox Status",
        "",
        f"- total_events: `{len(records)}`",
        f"- lock-busy: `{counts.get('lock-busy', 0)}`",
        f"- failure: `{counts.get('failure', 0)}`",
        f"- success: `{counts.get('success', 0)}`",
        "",
        "## Latest 5 events",
    ]

    if latest:
        for item in latest:
            lines.append(
                f"- `{item.get('timestamp_utc', 'unknown')}` | `{item.get('event', 'unknown')}` | `{item.get('status', 'unknown')}` | `{item.get('run_label', '-')}`"
            )
    else:
        lines.append("- none")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
