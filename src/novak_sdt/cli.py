#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

START = time.time()


def step(message: str) -> None:
    print()
    print("============================================================")
    print(f"[{time.strftime('%F %T')}] {message}")
    print("============================================================")


def timer() -> None:
    elapsed = int(time.time() - START)
    print(f"----- elapsed: {elapsed}s -----")


def render(text: str, context: dict[str, str]) -> str:
    for key, value in context.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text.rstrip() + "\n"


def write_file(path: Path, content: str, overwrite: bool) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return "kept"
    path.write_text(content, encoding="utf-8")
    return "written"


def in_git_repo(path: Path) -> bool:
    return (path / ".git").exists()


def git_init(path: Path) -> None:
    if not in_git_repo(path):
        subprocess.run(["git", "init"], cwd=path, check=True)
        subprocess.run(["git", "branch", "-M", "main"], cwd=path, check=True)


def maybe_git_commit(path: Path, message: str, enabled: bool) -> None:
    if not enabled:
        return
    subprocess.run(["git", "add", "."], cwd=path, check=True)
    subprocess.run(["git", "commit", "-m", message], cwd=path, check=True)


def core_templates() -> dict[str, str]:
    return {
        ".gitignore": """\
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.local/
""",
        "WHAT_IS_REAL_NOW.md": """\
# WHAT IS REAL NOW

## VERIFIED
- fill me in

## LIKELY
- fill me in

## ASSUMED
- fill me in

## NOT EVIDENCED
- fill me in

## Current next move
- fill me in

## Step after that
- fill me in
""",
        "PROJECT_STATE.md": """\
# PROJECT STATE

## Current objective
- fill me in

## Current branch
- fill me in

## Current next code block
- fill me in

## Step after that
- fill me in

## Risks / blockers
- fill me in
""",
        "README.md": """\
# {{PUBLIC_TITLE}}

**{{PRODUCT_STATEMENT}}**

## What this repo is
{{REPO_SUMMARY}}

## Start here
1. read `docs/product/PRODUCT_STATEMENT.md`
2. read `docs/product/WHAT_THIS_PRODUCT_IS.md`
3. read `docs/product/CURRENT_VS_PLANNED.md`
4. read `WHAT_IS_REAL_NOW.md`
5. read `PROJECT_STATE.md`
""",
    }


def operator_templates() -> dict[str, str]:
    return {
        "docs/operator/ZERO_CONTEXT_HANDOFF_CHECKLIST.md": """\
# ZERO CONTEXT HANDOFF CHECKLIST

## Required identity
- project name
- repo name
- branch
- head commit
- date
- operator
- environment / host

## Required reality block
### VERIFIED
-
### LIKELY
-
### ASSUMED
-
### NOT EVIDENCED
-

## Required operational block
- exact next code block
- exact step after that
- files touched
- blockers
- risks
- rollback point
""",
        "docs/operator/COLD_START_RECOVERY.md": """\
# COLD START RECOVERY

## First 10 minutes
1. identify repo, branch, and head commit
2. read `WHAT_IS_REAL_NOW.md`
3. read `PROJECT_STATE.md`
4. read latest operator docs
5. read latest decision docs
6. inspect git status
7. inspect last 10 commits
8. find exact next code block
9. identify rollback point
10. only then mutate anything
""",
        "docs/operator/NEXT_OPERATOR_PACKET_TEMPLATE.md": """\
# NEXT OPERATOR PACKET

## Identity
- Project:
- Repo:
- Branch:
- Head commit:
- Date:
- Operator:
- Host / environment:

## What changed
-
-

## What is real now
### VERIFIED
-
### LIKELY
-
### ASSUMED
-
### NOT EVIDENCED
-

## Exact next code block
paste exact next command block here

## Step after that
-

## Files touched
-

## Risks / blockers
-

## Rollback point
- commit:
- tag:
- branch:
""",
    }


def product_truth_templates() -> dict[str, str]:
    return {
        "docs/product/PRODUCT_STATEMENT.md": """\
# PRODUCT STATEMENT

## Canonical product statement
{{PRODUCT_STATEMENT}}
""",
        "docs/product/WHAT_THIS_PRODUCT_IS.md": """\
# WHAT THIS PRODUCT IS

## What it is
- {{PRODUCT_NAME}} is {{PRODUCT_TYPE_DESCRIPTION}}

## What problem it solves
- fill me in

## Core object or control surface
- fill me in

## What it is not
- fill me in
""",
        "docs/product/CURRENT_VS_PLANNED.md": """\
# CURRENT VS PLANNED

## Implemented now
- fill me in

## Planned next
- fill me in

## Aspirational / not yet real
- fill me in

## Not evidenced
- fill me in
""",
        "docs/product/PRODUCT_SYSTEM_BOUNDARY.md": """\
# PRODUCT SYSTEM BOUNDARY

## Product
- {{PRODUCT_NAME}} is the product or repo-specific surface

## Supporting system
- SDT is the reusable system behind the repo

## Rule
Do not collapse product identity into system identity.
""",
    }


def required_floor_files() -> list[str]:
    return [
        "WHAT_IS_REAL_NOW.md",
        "PROJECT_STATE.md",
        "docs/operator/ZERO_CONTEXT_HANDOFF_CHECKLIST.md",
        "docs/operator/COLD_START_RECOVERY.md",
        "docs/operator/NEXT_OPERATOR_PACKET_TEMPLATE.md",
        "docs/product/PRODUCT_STATEMENT.md",
        "docs/product/WHAT_THIS_PRODUCT_IS.md",
        "docs/product/CURRENT_VS_PLANNED.md",
        "docs/product/PRODUCT_SYSTEM_BOUNDARY.md",
    ]


def build_gap_report(root: Path, product_name: str) -> str:
    required = required_floor_files()
    present = [p for p in required if (root / p).exists()]
    missing = [p for p in required if not (root / p).exists()]

    return (
        "# SDT BASELINE GAP REPORT\n\n"
        f"## Repo path\n- `{root}`\n\n"
        f"## Product name\n- {product_name}\n\n"
        "## Present\n"
        + "".join(f"- `{p}`\n" for p in present)
        + "\n## Missing before baseline\n"
        + "".join(f"- `{p}`\n" for p in missing)
        + "\n## Rule\n"
        + "This report does not invent missing product truth.\n"
        + "It highlights where human confirmation is still required.\n"
    )


def apply_floor(root: Path, context: dict[str, str], overwrite: bool, include_report: bool) -> None:
    templates: dict[str, str] = {}
    templates.update(core_templates())
    templates.update(operator_templates())
    templates.update(product_truth_templates())

    if include_report:
        templates["docs/status/SDT_BASELINE_GAP_REPORT.md"] = build_gap_report(
            root, context["PRODUCT_NAME"]
        )

    step(f"Applying SDT floor to {root}")
    written = 0
    kept = 0

    for rel_path, raw in templates.items():
        result = write_file(root / rel_path, render(raw, context), overwrite)
        if result == "written":
            written += 1
            print(f"WRITE {rel_path}")
        else:
            kept += 1
            print(f"KEEP  {rel_path}")

    print()
    print(f"written_files={written}")
    print(f"kept_files={kept}")
    timer()


def cmd_new(args: argparse.Namespace) -> int:
    root = Path(args.path).resolve()
    root.mkdir(parents=True, exist_ok=True)

    context = {
        "PRODUCT_NAME": args.product_name,
        "PRODUCT_STATEMENT": args.product_statement,
        "PUBLIC_TITLE": args.public_title or "S.D.T. (Software Digital Thread)",
        "REPO_SUMMARY": args.repo_summary
        or "A repo initialized with the SDT operator floor and product truth floor.",
        "PRODUCT_TYPE_DESCRIPTION": args.product_type_description
        or "a product or serious repo under SDT",
    }

    step(f"Creating new repo at {root}")
    git_init(root)
    timer()

    apply_floor(root, context, overwrite=args.overwrite, include_report=True)
    maybe_git_commit(
        root,
        "sdt: initialize repo with operator and product-truth floors",
        args.git_commit,
    )

    step("DONE")
    print(f"repo_path={root}")
    timer()
    return 0


def cmd_baseline(args: argparse.Namespace) -> int:
    root = Path(args.path).resolve()
    if not root.exists():
        print(f"ERROR: path does not exist: {root}", file=sys.stderr)
        return 1

    context = {
        "PRODUCT_NAME": args.product_name,
        "PRODUCT_STATEMENT": args.product_statement,
        "PUBLIC_TITLE": args.public_title or args.product_name,
        "REPO_SUMMARY": args.repo_summary
        or "A repo baselined with the SDT operator floor and product truth floor.",
        "PRODUCT_TYPE_DESCRIPTION": args.product_type_description
        or "a product or serious repo under SDT",
    }

    if args.report_only:
        step(f"Generating report-only baseline view for {root}")
        print(build_gap_report(root, context["PRODUCT_NAME"]))
        timer()
        return 0

    apply_floor(root, context, overwrite=args.overwrite, include_report=True)
    maybe_git_commit(
        root,
        "sdt: baseline repo with operator and product-truth floors",
        args.git_commit,
    )

    step("DONE")
    print(f"repo_path={root}")
    timer()
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    root = Path(args.path).resolve()
    required = required_floor_files()

    step(f"Checking SDT floor at {root}")
    missing = [p for p in required if not (root / p).exists()]
    present = [p for p in required if (root / p).exists()]

    print(f"present_count={len(present)}")
    print(f"missing_count={len(missing)}")
    print()

    if present:
        print("PRESENT:")
        for item in present:
            print(f" - {item}")
        print()

    if missing:
        print("MISSING:")
        for item in missing:
            print(f" - {item}")
        timer()
        return 1

    print("PASS: SDT operator floor and product truth floor are present")
    timer()
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sdt",
        description="Software Digital Thread repo bootstrap and baseline tool.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--path", required=True, help="Target repo path.")
    common.add_argument(
        "--product-name", required=True, help="Human-readable product or repo name."
    )
    common.add_argument(
        "--product-statement", required=True, help="Canonical short product statement."
    )
    common.add_argument("--public-title", default="", help="README title.")
    common.add_argument("--repo-summary", default="", help="README summary.")
    common.add_argument(
        "--product-type-description",
        default="",
        help="Short description for WHAT_THIS_PRODUCT_IS.",
    )
    common.add_argument(
        "--overwrite", action="store_true", help="Overwrite existing files."
    )
    common.add_argument(
        "--git-commit", action="store_true", help="Create a git commit after writing files."
    )

    new_p = sub.add_parser("new", parents=[common], help="Create a new repo with SDT floors.")
    new_p.set_defaults(func=cmd_new)

    base_p = sub.add_parser(
        "baseline", parents=[common], help="Baseline an existing repo with SDT floors."
    )
    base_p.add_argument(
        "--report-only",
        action="store_true",
        help="Show the baseline gap report without writing files.",
    )
    base_p.set_defaults(func=cmd_baseline)

    doc_p = sub.add_parser("doctor", help="Check whether a repo has the SDT floors.")
    doc_p.add_argument("--path", required=True, help="Target repo path.")
    doc_p.set_defaults(func=cmd_doctor)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
