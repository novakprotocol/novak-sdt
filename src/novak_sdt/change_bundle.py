from __future__ import annotations

from pathlib import Path
import importlib.util
import sys


def _load_tool_module():
    repo_root = Path(__file__).resolve().parents[2]
    tool_path = repo_root / "tools" / "sdt_change_bundle.py"

    spec = importlib.util.spec_from_file_location("sdt_change_bundle_tool", tool_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load tool module from {tool_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_change_bundle(args) -> int:
    module = _load_tool_module()

    argv = [
        "sdt_change_bundle.py",
        "--repo",
        args.repo,
        "--title",
        args.title,
        "--type",
        args.type,
        "--why",
        args.why,
    ]

    if getattr(args, "apply_proof", False):
        argv.append("--apply-proof")

    for command in getattr(args, "command", []) or []:
        argv.extend(["--command", command])

    for proof_ref in getattr(args, "proof_ref", []) or []:
        argv.extend(["--proof-ref", proof_ref])

    old_argv = sys.argv[:]
    try:
        sys.argv = argv
        return int(module.main())
    finally:
        sys.argv = old_argv
