from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def test_script_refresh_cli(tmp_path: Path) -> None:
    script = tmp_path / "demo.sh"
    script.write_text("#!/usr/bin/env bash\necho hi\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, "-m", "novak_sdt.cli", "script-refresh", "--script", str(script)],
        text=True,
        capture_output=True,
        check=True,
    )

    assert '"risk_class": "S0"' in result.stdout
