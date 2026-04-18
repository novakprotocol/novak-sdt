import json
import os
import subprocess
from pathlib import Path


def run(cmd: list[str], *, check: bool = True, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    return subprocess.run(
        cmd,
        text=True,
        capture_output=True,
        check=check,
        env=merged_env,
    )


def make_source_repo(source_dir: Path) -> None:
    history_dir = source_dir / "docs/history"
    history_dir.mkdir(parents=True, exist_ok=True)
    (history_dir / "ATTEMPTS.ndjson").write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "archived_copy": "docs/history/raw/test-01.log",
                        "archived_utc": "2026-04-18 00:00:01 UTC",
                        "failure_classes": {"generic-error": 1},
                        "failure_line_count": 1,
                        "line_count": 2,
                        "missed_opportunity_count": 0,
                        "source_name": "test-01.log",
                        "weighted_severity_total": 2,
                    }
                ),
                json.dumps(
                    {
                        "archived_copy": "docs/history/raw/test-02.log",
                        "archived_utc": "2026-04-18 00:00:11 UTC",
                        "failure_classes": {"python-traceback": 1},
                        "failure_line_count": 1,
                        "line_count": 3,
                        "missed_opportunity_count": 1,
                        "source_name": "test-02.log",
                        "weighted_severity_total": 5,
                    }
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def birth_repo(repo_dir: Path, name: str) -> None:
    run(
        [
            "sdt",
            "new",
            "--path",
            str(repo_dir),
            "--product-name",
            name,
            "--product-statement",
            f"{name} validates the generated estate refresh runner wrapper.",
            "--public-title",
            name,
            "--repo-summary",
            "Runner wrapper pytest proof.",
            "--git-commit",
        ]
    )


def test_runner_wrapper_success_status_and_notify(tmp_path: Path) -> None:
    repo = tmp_path / "runner-success"
    source = tmp_path / "source-success"

    make_source_repo(source)
    birth_repo(repo, "SDT Runner Wrapper Success Proof")

    result = run(
        [
            "bash",
            str(repo / "bin/estate-refresh-runner.sh"),
            f"alpha={source}",
        ],
        check=False,
        env={"ESTATE_RUNNER_MODE": "timer"},
    )

    assert result.returncode == 0, result.stdout + result.stderr

    status_doc = (repo / "docs/estate/ESTATE_RUNNER_STATUS.md").read_text(encoding="utf-8")
    assert "- outcome: success" in status_doc, status_doc
    assert "- runner_mode: timer" in status_doc, status_doc
    assert "- argument_count: 1" in status_doc, status_doc
    assert "refresh_command: bash " in status_doc, status_doc

    outbox = repo / "estate/outbox/notifications.ndjson"
    records = [json.loads(line) for line in outbox.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert records, "notification outbox is empty"
    assert records[-1]["event"] == "success", records
    assert records[-1]["run_label"] == "estate-refresh-runner", records

    notify_status = (repo / "docs/estate/ESTATE_NOTIFICATION_STATUS.md").read_text(encoding="utf-8")
    assert "last_event: `success`" in notify_status, notify_status
    assert "success: `1`" in notify_status, notify_status


def test_runner_wrapper_lock_busy_status_and_notify(tmp_path: Path) -> None:
    repo = tmp_path / "runner-lock-busy"
    source = tmp_path / "source-lock-busy"

    make_source_repo(source)
    birth_repo(repo, "SDT Runner Wrapper Lock Busy Proof")

    (repo / ".estate-refresh.lock").mkdir()

    result = run(
        [
            "bash",
            str(repo / "bin/estate-refresh-runner.sh"),
            f"alpha={source}",
        ],
        check=False,
    )

    assert result.returncode == 75, result.stdout + result.stderr

    status_doc = (repo / "docs/estate/ESTATE_RUNNER_STATUS.md").read_text(encoding="utf-8")
    assert "- outcome: lock-busy" in status_doc, status_doc

    outbox = repo / "estate/outbox/notifications.ndjson"
    records = [json.loads(line) for line in outbox.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert records, "notification outbox is empty"
    assert records[-1]["event"] == "lock-busy", records

    notify_status = (repo / "docs/estate/ESTATE_NOTIFICATION_STATUS.md").read_text(encoding="utf-8")
    assert "last_event: `lock-busy`" in notify_status, notify_status
    assert "lock-busy: `1`" in notify_status, notify_status
