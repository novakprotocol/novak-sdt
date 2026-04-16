#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import platform
import socket
import subprocess
from datetime import UTC, datetime
from pathlib import Path


def run_shell(command: str) -> str:
    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True,
        executable="/bin/bash",
    )
    text = result.stdout
    if result.stderr:
        text = text + ("\n" if text else "") + result.stderr
    return text.rstrip() + "\n"


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    write_text(path, json.dumps(payload, indent=2) + "\n")


def detect_package_command() -> str:
    if Path("/usr/bin/rpm").exists():
        return "rpm -qa | sort"
    if Path("/usr/bin/dpkg-query").exists():
        return "dpkg-query -W -f='${Package}\\t${Version}\\n' | sort"
    return "echo 'package manager inventory unavailable'"


def detect_updates_command() -> str:
    if Path("/usr/bin/dnf").exists():
        return "dnf -q check-update || true"
    if Path("/usr/bin/apt").exists():
        return "apt list --upgradable 2>/dev/null || true"
    return "echo 'update inventory unavailable'"


def main() -> int:
    parser = argparse.ArgumentParser(description="Write an SDT runtime inventory snapshot.")
    parser.add_argument("--repo-path", required=True)
    parser.add_argument("--label", required=True)
    args = parser.parse_args()

    repo = Path(args.repo_path).resolve()
    out_dir = repo / "docs" / "status" / "inventory" / args.label
    out_dir.mkdir(parents=True, exist_ok=True)

    captures: dict[str, str] = {
        "hostnamectl.txt": "hostnamectl || true",
        "os-release.txt": "cat /etc/os-release || true",
        "kernel.txt": "uname -a || true",
        "ip-addresses.txt": "ip -br addr || true",
        "routes.txt": "ip route || true",
        "resolv.conf.txt": "cat /etc/resolv.conf || true",
        "filesystems.txt": "df -h || true",
        "memory.txt": "free -m || true",
        "services-enabled.txt": "systemctl list-unit-files --type=service --no-pager || true",
        "services-running.txt": "systemctl list-units --type=service --state=running --no-pager || true",
        "processes.txt": "ps -eo pid,ppid,user,%cpu,%mem,comm,args --sort=-%cpu | head -n 200 || true",
        "ports.txt": "ss -lntup || true",
        "packages.txt": detect_package_command(),
        "updates.txt": detect_updates_command(),
    }

    files_written: dict[str, str] = {}
    for filename, command in captures.items():
        path = out_dir / filename
        write_text(path, run_shell(command))
        files_written[filename] = str(path.relative_to(repo))

    summary_md = f"""# Runtime Inventory Snapshot — {args.label}

## Identity
- label: `{args.label}`
- generated_utc: `{datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")}`
- host: `{socket.gethostname()}`
- fqdn: `{socket.getfqdn()}`
- platform: `{platform.platform()}`
- python: `{platform.python_version()}`
- repo_path: `{repo}`

## Files written
- `docs/status/inventory/{args.label}/hostnamectl.txt`
- `docs/status/inventory/{args.label}/os-release.txt`
- `docs/status/inventory/{args.label}/kernel.txt`
- `docs/status/inventory/{args.label}/ip-addresses.txt`
- `docs/status/inventory/{args.label}/routes.txt`
- `docs/status/inventory/{args.label}/resolv.conf.txt`
- `docs/status/inventory/{args.label}/filesystems.txt`
- `docs/status/inventory/{args.label}/memory.txt`
- `docs/status/inventory/{args.label}/services-enabled.txt`
- `docs/status/inventory/{args.label}/services-running.txt`
- `docs/status/inventory/{args.label}/processes.txt`
- `docs/status/inventory/{args.label}/ports.txt`
- `docs/status/inventory/{args.label}/packages.txt`
- `docs/status/inventory/{args.label}/updates.txt`

## Rule
This snapshot is for truth and diffing.
Do not put secret values in repo inventory.
"""
    write_text(out_dir / "INVENTORY_SUMMARY.md", summary_md)

    payload = {
        "schema_version": 1,
        "label": args.label,
        "generated_utc": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "repo_path": str(repo),
        "host": {
            "hostname": socket.gethostname(),
            "fqdn": socket.getfqdn(),
            "platform": platform.platform(),
            "python": platform.python_version(),
            "user": os.getenv("SUDO_USER") or os.getenv("USER") or "unknown",
        },
        "files": files_written,
    }

    write_json(out_dir / "inventory.json", payload)
    write_json(repo / "docs" / "status" / "LATEST_INVENTORY.json", payload)

    ledger = repo / "docs" / "status" / "INVENTORY_LEDGER.ndjson"
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with ledger.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload) + "\n")

    print(f"WROTE {out_dir / 'inventory.json'}")
    print(f"WROTE {out_dir / 'INVENTORY_SUMMARY.md'}")
    print(f"WROTE {repo / 'docs' / 'status' / 'LATEST_INVENTORY.json'}")
    print(f"APPENDED {ledger}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
