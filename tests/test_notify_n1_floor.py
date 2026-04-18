import json
import subprocess
from pathlib import Path


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=check)


def test_notify_n1_born_floor_and_return_codes(tmp_path: Path) -> None:
    repo = tmp_path / "proof"

    run(
        [
            "sdt",
            "new",
            "--path",
            str(repo),
            "--product-name",
            "SDT Notify N1 Test Proof",
            "--product-statement",
            "SDT Notify N1 Test Proof validates notify floor and return codes.",
            "--public-title",
            "SDT Notify N1 Test Proof",
            "--repo-summary",
            "Notify N1 pytest proof.",
            "--git-commit",
        ]
    )

    required = [
        "estate/notification_config.json",
        "estate/outbox/notifications.ndjson",
        "docs/estate/ESTATE_FAILURE_POLICY.md",
        "docs/estate/ESTATE_NOTIFICATIONS.md",
        "docs/estate/ESTATE_NOTIFICATION_STATUS.md",
        "bin/estate-notify.sh",
    ]
    for rel in required:
        assert (repo / rel).exists(), rel

    r1 = run(
        [
            "bash",
            str(repo / "bin/estate-notify.sh"),
            "--event",
            "lock-busy",
            "--run-label",
            "pytest-lock",
            "--message",
            "lock proof",
        ],
        check=False,
    )
    assert r1.returncode == 75, r1.stdout + r1.stderr

    r2 = run(
        [
            "bash",
            str(repo / "bin/estate-notify.sh"),
            "--event",
            "failure",
            "--run-label",
            "pytest-fail",
            "--message",
            "fail proof",
        ],
        check=False,
    )
    assert r2.returncode == 2, r2.stdout + r2.stderr

    r3 = run(
        [
            "bash",
            str(repo / "bin/estate-notify.sh"),
            "--event",
            "success",
            "--run-label",
            "pytest-pass",
            "--message",
            "pass proof",
        ],
        check=False,
    )
    assert r3.returncode == 0, r3.stdout + r3.stderr

    outbox = repo / "estate/outbox/notifications.ndjson"
    records = [json.loads(line) for line in outbox.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert [r["event"] for r in records] == ["lock-busy", "failure", "success"]

    status_doc = (repo / "docs/estate/ESTATE_NOTIFICATION_STATUS.md").read_text(encoding="utf-8")
    assert "last_event: `success`" in status_doc
    assert "lock-busy: `1`" in status_doc
    assert "failure: `1`" in status_doc
    assert "success: `1`" in status_doc
