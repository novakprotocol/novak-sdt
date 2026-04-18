#!/usr/bin/env bash
set -Eeuo pipefail
set +H

python3 -W error::SyntaxWarning -m py_compile src/novak_sdt/extended_floor.py
python3 -W error::SyntaxWarning -m compileall -q src
echo "PYTHON_WARNING_GATE_PASS"
