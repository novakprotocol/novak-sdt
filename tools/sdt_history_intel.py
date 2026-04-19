#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from novak_sdt.history_intel import write_history_outputs


def main() -> int:
    parser = argparse.ArgumentParser(description="Derive history intelligence docs from repo evidence")
    parser.add_argument("--repo", required=True, help="Target repository path")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    result = write_history_outputs(repo)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
