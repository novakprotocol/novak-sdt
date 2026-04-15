#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import html
import subprocess
from pathlib import Path

CLASSIC_REQUIRED = [
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

EXTENDED_REQUIRED = [
    "README.md",
    "sdt.yaml",
    "CHANGELOG.md",
    "DECISION_LOG.md",
    "ROLLBACK_LOG.md",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE",
    "docs/operator",
    "docs/standards",
    "docs/decisions",
]


def run(cmd: list[str], cwd: Path) -> str:
    try:
        return subprocess.check_output(cmd, cwd=cwd, text=True).strip()
    except Exception as exc:
        return f"UNAVAILABLE: {exc}"


def split_paths(root: Path, paths: list[str]) -> tuple[list[str], list[str]]:
    present: list[str] = []
    missing: list[str] = []
    for rel in paths:
        if (root / rel).exists():
            present.append(rel)
        else:
            missing.append(rel)
    return present, missing


def snapshot(root: Path) -> dict:
    docs_dir = root / "docs"
    docs: list[str] = []
    if docs_dir.exists():
        docs = sorted(str(p.relative_to(root)) for p in docs_dir.rglob("*.md"))

    classic_present, classic_missing = split_paths(root, CLASSIC_REQUIRED)
    extended_present, extended_missing = split_paths(root, EXTENDED_REQUIRED)

    return {
        "generated_utc": dt.datetime.now(dt.UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "repo_path": str(root),
        "branch": run(["git", "branch", "--show-current"], root),
        "head_commit": run(["git", "rev-parse", "HEAD"], root),
        "git_status": run(["git", "status", "--short"], root),
        "git_log": run(["git", "log", "--oneline", "--decorate", "-8"], root),
        "classic_present": classic_present,
        "classic_missing": classic_missing,
        "extended_present": extended_present,
        "extended_missing": extended_missing,
        "docs": docs,
    }


def bullets_md(items: list[str]) -> str:
    if not items:
        return "- none\n"
    return "".join(f"- `{item}`\n" for item in items)


def items_html(items: list[str]) -> str:
    if not items:
        return "<li>none</li>"
    return "".join(f"<li><code>{html.escape(item)}</code></li>" for item in items)


def render_md(data: dict) -> str:
    generated_utc = data.get("generated_utc", "")
    repo_path = data.get("repo_path", "")
    branch = data.get("branch", "")
    head_commit = data.get("head_commit", "")
    git_status = data.get("git_status", "") or "(clean)"
    git_log = data.get("git_log", "")

    classic_present = data.get("classic_present", [])
    classic_missing = data.get("classic_missing", [])
    extended_present = data.get("extended_present", [])
    extended_missing = data.get("extended_missing", [])
    docs = data.get("docs", [])

    return (
        "# SDT Repo Report\n\n"
        "## Identity\n"
        f"- Generated UTC: {generated_utc}\n"
        f"- Repo path: `{repo_path}`\n"
        f"- Branch: `{branch}`\n"
        f"- Head commit: `{head_commit}`\n\n"
        "## Classic SDT floor files present\n"
        f"{bullets_md(classic_present)}\n"
        "## Classic SDT floor files missing\n"
        f"{bullets_md(classic_missing)}\n"
        "## Extended metadata and governance surfaces present\n"
        f"{bullets_md(extended_present)}\n"
        "## Extended metadata and governance surfaces missing\n"
        f"{bullets_md(extended_missing)}\n"
        "## Docs discovered\n"
        f"{bullets_md(docs)}\n"
        "## Git status\n"
        "```text\n"
        f"{git_status}\n"
        "```\n\n"
        "## Recent commits\n"
        "```text\n"
        f"{git_log}\n"
        "```\n"
    )


def render_html(data: dict) -> str:
    generated_utc = html.escape(data.get("generated_utc", ""))
    repo_path = html.escape(data.get("repo_path", ""))
    branch = html.escape(data.get("branch", ""))
    head_commit = html.escape(data.get("head_commit", ""))
    git_status = html.escape(data.get("git_status", "") or "(clean)")
    git_log = html.escape(data.get("git_log", ""))

    classic_present = data.get("classic_present", [])
    classic_missing = data.get("classic_missing", [])
    extended_present = data.get("extended_present", [])
    extended_missing = data.get("extended_missing", [])
    docs = data.get("docs", [])

    return (
        "<!doctype html>\n"
        "<html lang=\"en\">\n"
        "<head><meta charset=\"utf-8\"><title>SDT Repo Report</title></head>\n"
        "<body>\n"
        "<h1>SDT Repo Report</h1>\n"
        "<h2>Identity</h2>\n"
        "<ul>\n"
        f"<li>Generated UTC: <code>{generated_utc}</code></li>\n"
        f"<li>Repo path: <code>{repo_path}</code></li>\n"
        f"<li>Branch: <code>{branch}</code></li>\n"
        f"<li>Head commit: <code>{head_commit}</code></li>\n"
        "</ul>\n"
        "<h2>Classic SDT floor files present</h2>\n"
        f"<ul>{items_html(classic_present)}</ul>\n"
        "<h2>Classic SDT floor files missing</h2>\n"
        f"<ul>{items_html(classic_missing)}</ul>\n"
        "<h2>Extended metadata and governance surfaces present</h2>\n"
        f"<ul>{items_html(extended_present)}</ul>\n"
        "<h2>Extended metadata and governance surfaces missing</h2>\n"
        f"<ul>{items_html(extended_missing)}</ul>\n"
        "<h2>Docs discovered</h2>\n"
        f"<ul>{items_html(docs)}</ul>\n"
        "<h2>Git status</h2>\n"
        f"<pre>{git_status}</pre>\n"
        "<h2>Recent commits</h2>\n"
        f"<pre>{git_log}</pre>\n"
        "</body>\n"
        "</html>\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate SDT repo reports.")
    parser.add_argument("--path", required=True, help="Target repo path")
    parser.add_argument("--outdir", default="", help="Optional output directory")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    outdir = Path(args.outdir).resolve() if args.outdir else root / "docs" / "status"
    outdir.mkdir(parents=True, exist_ok=True)

    data = snapshot(root)

    md_path = outdir / "SDT_REPO_REPORT.md"
    html_path = outdir / "SDT_REPO_REPORT.html"
    md_path.write_text(render_md(data), encoding="utf-8")
    html_path.write_text(render_html(data), encoding="utf-8")

    print(f"WROTE {md_path}")
    print(f"WROTE {html_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
