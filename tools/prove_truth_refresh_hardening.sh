#!/usr/bin/env bash
set -Eeuo pipefail
set +H

START_EPOCH="$(date +%s)"

step() {
  echo
  echo "============================================================"
  echo "[$(date '+%F %T')] $1"
  echo "============================================================"
}

timer() {
  local now elapsed
  now="$(date +%s)"
  elapsed="$((now - START_EPOCH))"
  echo "----- elapsed: ${elapsed}s -----"
}

REPO="${1:-/root/novak-sdt}"

step "01 - install editable package"
cd /root/novak-sdt
. .venv/bin/activate
python3 -m pip install -e . >/dev/null
timer

step "02 - run hardening tests"
python3 -m pytest -q tests/test_project_truth_hardening.py
timer

step "03 - refresh target repo truth"
python3 tools/sdt_truth_refresh.py --repo "${REPO}"
timer

step "04 - show key truth outputs"
sed -n '1,220p' "${REPO}/docs/status/SDT_COMPLETENESS_REPORT.md"
echo
sed -n '1,220p' "${REPO}/docs/status/SDT_DRIFT_REPORT.md"
echo
sed -n '1,220p' "${REPO}/docs/status/TRUSTED_FLOOR_STATUS.md"
timer
