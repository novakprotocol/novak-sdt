#!/usr/bin/env bash
set -Eeuo pipefail
set +H

REPO_DIR="${1:-$(pwd)}"
SOURCE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "${REPO_DIR}"

python3 "${SOURCE_ROOT}/tools/sdt_truth_refresh.py" --repo "${REPO_DIR}"

git add \
  PROJECT_STATE.md \
  WHAT_IS_REAL_NOW.md \
  docs/product/PRODUCT_STATEMENT.md \
  docs/history/ATTEMPTS.ndjson \
  docs/history/FAILURE_PATTERNS.md \
  docs/history/HISTORY_ACTION_QUEUE.md \
  docs/history/HISTORY_INDEX.md \
  docs/history/HISTORY_PRIORITY_QUEUE.md \
  docs/history/HISTORY_REMEDIATION.md \
  docs/history/MISSED_OPPORTUNITIES.md \
  docs/status/PROJECT_MODEL.json \
  docs/status/SDT_COMPLETENESS_REPORT.md \
  docs/status/SDT_CONFIRMATION_PACKET.md \
  docs/status/SDT_DRIFT_REPORT.md \
  docs/status/TRUSTED_FLOOR_STATUS.md \
  docs/INSTALLATION.md || true

echo "TRUTH_REFRESH_AND_STAGE_DONE repo=${REPO_DIR}"
