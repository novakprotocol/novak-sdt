from __future__ import annotations

import os
import shutil
from pathlib import Path
import subprocess

import pytest


REPO = Path(__file__).resolve().parents[1]


def test_truth_closure_tools_exist() -> None:
    repo = REPO
    assert (repo / 'tools' / 'run_truth_refresh_and_stage.sh').exists()
    assert (repo / 'tools' / 'install_truth_refresh_hooks.sh').exists()
    assert (repo / 'tools' / 'freeze_trusted_floor.sh').exists()
    assert (repo / 'tools' / 'patch_project_intel_weights.py').exists()
    assert (repo / 'tools' / 'clean_placeholder_docs.py').exists()


def test_install_truth_hooks_help() -> None:
    if os.name == 'nt':
        pytest.skip('truth hook installer smoke requires a POSIX shell')
    bash = shutil.which('bash')
    if bash is None:
        pytest.skip('bash is unavailable')

    repo = REPO
    result = subprocess.run(
        [bash, str(repo / 'tools' / 'install_truth_refresh_hooks.sh'), str(repo)],
        text=True,
        capture_output=True,
        check=True,
    )
    assert 'INSTALLED_ADVISORY_HOOKS' in result.stdout
