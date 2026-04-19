#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import traceback

from novak_sdt.attempt_log import append_attempt
from novak_sdt.project_intel import write_outputs
from novak_sdt.history_intel import write_history_outputs
from novak_sdt.trusted_floor import write_trusted_floor_status


def main() -> int:
    parser = argparse.ArgumentParser(description="Run SDT project intelligence, history intelligence, and trusted floor refresh")
    parser.add_argument("--repo", required=True, help="Target repository path")
    parser.add_argument("--no-apply-docs", action="store_true", help="Do not write managed sections into core docs")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    command = f"python3 tools/sdt_truth_refresh.py --repo {repo}"

    try:
        project = write_outputs(repo=repo, apply_docs=not args.no_apply_docs)
        history = write_history_outputs(repo=repo)
        trusted = write_trusted_floor_status(repo=repo)

        append_attempt(
            repo,
            lane="truth-refresh",
            event="truth-refresh",
            status="PASS",
            note="truth refresh completed successfully",
            command=command,
            extra={
                "score": project["score"],
                "trusted_floor_status": trusted["trusted_floor_status"],
            },
        )

        print(json.dumps(
            {
                "project_intel": project,
                "history_intel": history,
                "trusted_floor": trusted,
            },
            indent=2,
        ))
        return 0
    except Exception as exc:
        append_attempt(
            repo,
            lane="truth-refresh",
            event="truth-refresh",
            status="FAIL",
            note=str(exc),
            command=command,
            extra={"traceback": traceback.format_exc()},
        )
        raise


if __name__ == "__main__":
    raise SystemExit(main())
