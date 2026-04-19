#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path
import re
import subprocess


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "change"


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def append_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"
    path.write_text(existing + content, encoding="utf-8")


def git_value(repo: Path, *args: str) -> str:
    if not (repo / ".git").exists():
        return "unknown"
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo,
            text=True,
            capture_output=True,
            check=True,
        )
        return result.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def run_command(repo: Path, command: str) -> tuple[int, str, str]:
    result = subprocess.run(
        command,
        cwd=repo,
        text=True,
        capture_output=True,
        shell=True,
        check=False,
    )
    return result.returncode, result.stdout, result.stderr


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an SDT change bundle scaffold")
    parser.add_argument("--repo", required=True, help="Target repository path")
    parser.add_argument("--title", required=True, help="Human-readable change title")
    parser.add_argument("--type", required=True, help="Change type, e.g. wording-change")
    parser.add_argument("--why", required=True, help="Why the change is being made")
    parser.add_argument(
        "--apply-proof",
        action="store_true",
        help="Append proof capture into the poststate and change record",
    )
    parser.add_argument(
        "--command",
        action="append",
        default=[],
        help="Command to run in the target repo and capture into the proof bundle; may be repeated",
    )
    parser.add_argument(
        "--proof-ref",
        action="append",
        default=[],
        help="Proof reference or artifact path to append; may be repeated",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    stamp = datetime.now(UTC).strftime("%Y-%m-%d")
    stamp_full = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
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
                stamp_full,
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
                stamp_full,
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

    if args.apply_proof:
        branch = git_value(repo, "branch", "--show-current")
        commit = git_value(repo, "rev-parse", "HEAD")

        append_text(
            poststate_path,
            "\n".join(
                [
                    "",
                    "## Applied proof",
                    f"- stamp: {stamp_full}",
                    f"- branch: {branch}",
                    f"- commit: {commit}",
                    "",
                ]
            ),
        )

        if args.command:
            append_text(poststate_path, "## Commands\n\n")
            append_text(change_path, "\n## Verification performed\n- applied_proof: yes\n")
            for command in args.command:
                rc, stdout, stderr = run_command(repo, command)
                append_text(
                    poststate_path,
                    "\n".join(
                        [
                            f"### `{command}`",
                            f"- returncode: {rc}",
                            "",
                            "#### stdout",
                            "```text",
                            stdout.rstrip(),
                            "```",
                            "",
                            "#### stderr",
                            "```text",
                            stderr.rstrip(),
                            "```",
                            "",
                        ]
                    ),
                )
                append_text(change_path, f"- command: `{command}`\n- returncode: `{rc}`\n")
        else:
            append_text(change_path, "\n## Verification performed\n- applied_proof: yes\n- no commands supplied\n")

        if args.proof_ref:
            append_text(
                poststate_path,
                "\n".join(
                    [
                        "",
                        "## Proof references",
                        *[f"- {item}" for item in args.proof_ref],
                        "",
                    ]
                ),
            )
            append_text(
                change_path,
                "\n".join(
                    [
                        "",
                        "## Proof references",
                        *[f"- {item}" for item in args.proof_ref],
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
