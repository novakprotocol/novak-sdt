#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from novak_sdt.project_intel import write_outputs
from novak_sdt.history_intel import write_history_outputs


def main() -> int:
    parser = argparse.ArgumentParser(description="Infer project truth and write SDT intelligence outputs")
    parser.add_argument("--repo", required=True, help="Target repository path")
    parser.add_argument(
        "--no-apply-docs",
        action="store_true",
        help="Do not write managed sections into core docs",
    )
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    result = write_outputs(repo=repo, apply_docs=not args.no_apply_docs)
    history = write_history_outputs(repo)
    print(json.dumps({"project_intel": result, "history_intel": history}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
