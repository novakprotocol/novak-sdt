#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

CLI = Path("/root/novak-sdt/src/novak_sdt/cli.py")
text = CLI.read_text(encoding="utf-8")

if "import subprocess" not in text:
    text = text.replace("import argparse\n", "import argparse\nimport subprocess\n", 1)
if "import sys" not in text:
    text = text.replace("import argparse\n", "import argparse\nimport sys\n", 1)

helper = '''

def run_truth_refresh(root: Path) -> None:
    tool_path = Path(__file__).resolve().parents[2] / "tools" / "sdt_truth_refresh.py"
    if not tool_path.exists():
        step(f"Truth refresh tool missing at {tool_path}; skipping")
        return

    step(f"Refreshing SDT truth surfaces for {root}")
    result = subprocess.run(
        [sys.executable, str(tool_path), "--repo", str(root)],
        text=True,
        capture_output=True,
        check=False,
    )

    if result.stdout.strip():
        print(result.stdout)
    if result.stderr.strip():
        print(result.stderr)

    if result.returncode != 0:
        raise SystemExit(result.returncode)
'''

if "def run_truth_refresh(root: Path) -> None:" not in text:
    text = text.replace("def cmd_new(args: argparse.Namespace) -> int:\n", helper + "\ndef cmd_new(args: argparse.Namespace) -> int:\n", 1)

def patch_function(source: str, func_name: str) -> str:
    pattern = re.compile(rf"(def {func_name}\(args: argparse\.Namespace\) -> int:\n)(.*?)(?=\ndef |\Z)", re.DOTALL)
    match = pattern.search(source)
    if not match:
        raise SystemExit(f"FAILED: could not find {func_name}")

    head = match.group(1)
    body = match.group(2)

    if "run_truth_refresh(root)" in body:
        return source

    idx = body.rfind("\n    return 0")
    if idx == -1:
        raise SystemExit(f"FAILED: could not find final return in {func_name}")

    body = body[:idx] + "\n    run_truth_refresh(root)\n" + body[idx:]
    return source[:match.start()] + head + body + source[match.end():]

text = patch_function(text, "cmd_new")
text = patch_function(text, "cmd_baseline")

CLI.write_text(text, encoding="utf-8")
print(f"PATCHED {CLI}")
