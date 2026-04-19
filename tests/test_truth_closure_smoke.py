from __future__ import annotations

from pathlib import Path
import subprocess


def test_truth_closure_tools_exist() -> None:
    repo = Path('/root/novak-sdt')
    assert (repo / 'tools' / 'run_truth_refresh_and_stage.sh').exists()
    assert (repo / 'tools' / 'install_truth_refresh_hooks.sh').exists()
    assert (repo / 'tools' / 'freeze_trusted_floor.sh').exists()
    assert (repo / 'tools' / 'patch_project_intel_weights.py').exists()
    assert (repo / 'tools' / 'clean_placeholder_docs.py').exists()


def test_install_truth_hooks_help() -> None:
    repo = Path('/root/novak-sdt')
    result = subprocess.run(
        ['bash', str(repo / 'tools' / 'install_truth_refresh_hooks.sh'), str(repo)],
        text=True,
        capture_output=True,
        check=True,
    )
    assert 'INSTALLED_HOOKS' in result.stdout
