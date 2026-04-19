#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path
import re


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "change"


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an SDT change bundle scaffold")
    parser.add_argument("--repo", required=True, help="Target repository path")
    parser.add_argument("--title", required=True, help="Human-readable change title")
    parser.add_argument("--type", required=True, help="Change type, e.g. wording-change")
    parser.add_argument("--why", required=True, help="Why the change is being made")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    stamp = datetime.now(UTC).strftime("%Y-%m-%d")
    slug = slugify(args.title)

    changes_dir = repo / "docs/changes"
    status_dir = repo / "docs/status"

    index_path = changes_dir / "CHANGE_INDEX.md"
    change_path = changes_dir / f"{stamp}-{slug}.md"
    prestate_path = status_dir / f"{slug.upper().replace('-', '_')}_PRESTATE.md"
    poststate_path = status_dir / f"{slug.upper().replace('-', '_')}_POSTSTATE.md"

    write_if_missing(
        index_path,
        "# Change Index\n\n- Add change records here in chronological order.\n",
    )

    write_if_missing(
        change_path,
        "\n".join(
            [
                f"# Change Record — {args.title}",
                "",
                "## Change type",
                f"- {args.type}",
                "",
                "## Why this changed",
                args.why,
                "",
                "## What changed",
                "- fill in exact files and old/new behavior",
                "",
                "## What did not change",
                "- fill in non-changes explicitly",
                "",
                "## Verification required",
                "- fill in run/test/proof steps",
                "",
                "## Notes for future human or AI readers",
                "- explain intent, scope, and expected interpretation later",
                "",
            ]
        ),
    )

    write_if_missing(
        prestate_path,
        "\n".join(
            [
                f"# {args.title} pre-state",
                "",
                "## Stamp",
                datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
                "",
                "## Branch",
                "- fill in current branch",
                "",
                "## Commit",
                "- fill in current commit",
                "",
                "## Current truth",
                "- fill in current output/state/tests",
                "",
            ]
        ),
    )

    write_if_missing(
        poststate_path,
        "\n".join(
            [
                f"# {args.title} post-state",
                "",
                "## Stamp",
                datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
                "",
                "## Branch",
                "- fill in current branch",
                "",
                "## Commit",
                "- fill in current commit",
                "",
                "## New truth",
                "- fill in new output/state/tests",
                "",
            ]
        ),
    )

    print(f"CHANGE_INDEX={index_path}")
    print(f"CHANGE_RECORD={change_path}")
    print(f"PRESTATE={prestate_path}")
    print(f"POSTSTATE={poststate_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
