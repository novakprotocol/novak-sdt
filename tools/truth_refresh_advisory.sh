#!/usr/bin/env bash
set -Eeuo pipefail
set +H

REPO_ROOT="${1:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
cd "${REPO_ROOT}"

if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
  exit 0
fi

CHANGED="$(git diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null || true)"
if [[ -z "${CHANGED}" ]]; then
  exit 0
fi

TRUTH_REGEX='^(PROJECT_STATE\.md|WHAT_IS_REAL_NOW\.md|docs/status/.*|docs/history/.*|docs/product/PRODUCT_STATEMENT\.md|docs/INSTALLATION\.md|docs/LATEST_RUN\.md|docs/LATEST_INVENTORY\.md|docs/SYSTEM_AND_COMPONENT_STATUS\.md|docs/FRESHNESS_GAUGE\.md)$'

MEANINGFUL="$(printf '%s\n' "${CHANGED}" | grep -Ev "${TRUTH_REGEX}" || true)"

if [[ -z "${MEANINGFUL}" ]]; then
  exit 0
fi

echo
echo "============================================================"
echo "[SDT ADVISORY] meaningful repo mutation detected"
echo "============================================================"
printf '%s\n' "${MEANINGFUL}" | sed 's/^/ - /'
echo
echo "Truth surfaces were NOT auto-mutated by this hook."
echo "Run these explicitly when appropriate:"
echo "  bash tools/run_truth_refresh_and_stage.sh ${REPO_ROOT}"
echo "  git status --short"
echo
exit 0
