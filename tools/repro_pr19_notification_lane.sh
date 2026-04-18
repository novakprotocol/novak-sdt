#!/usr/bin/env bash
set -Eeuo pipefail
set +H

START_EPOCH="$(date +%s)"
REPO_ROOT="$(pwd)"
REPRO_BRANCH="feat/repro-pr19-notify-local"
REMOTE_BRANCH="origin/feat/mkdocs-burst-ij-hardening-notify-35-38"
WORKDIR="/tmp/sdt-pr19-repro"
PROOF_REPO="${WORKDIR}/proof"
SOURCE_REPO="${WORKDIR}/source"
REPORT="${WORKDIR}/repro_report.txt"

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

rm -rf "${WORKDIR}"
mkdir -p "${WORKDIR}"

step "01 - fetch and checkout closed PR19 code locally"
git fetch origin
git checkout -B "${REPRO_BRANCH}" "${REMOTE_BRANCH}"
timer

step "02 - install package from repro branch"
python3 -m pip install -e . >/dev/null
timer

step "03 - create source repo"
mkdir -p "${SOURCE_REPO}/docs/history"
cat > "${SOURCE_REPO}/docs/history/ATTEMPTS.ndjson" <<'DOC'
{"archived_copy":"docs/history/raw/pr19-01.log","archived_utc":"2026-04-18 00:15:01 UTC","failure_classes":{"generic-error":1},"failure_line_count":1,"line_count":2,"missed_opportunity_count":0,"source_name":"pr19-01.log","weighted_severity_total":2}
DOC
timer

step "04 - birth proof repo"
sdt new \
  --path "${PROOF_REPO}" \
  --product-name "SDT PR19 Repro Proof" \
  --product-statement "SDT PR19 Repro Proof reproduces the old notification lane behavior." \
  --public-title "SDT PR19 Repro Proof" \
  --repo-summary "Closed PR19 repro harness." \
  --git-commit || true
timer

step "05 - bash syntax check helper if present"
{
  if [[ -f "${PROOF_REPO}/bin/estate-notify.sh" ]]; then
    echo "===== bash -n estate-notify.sh ====="
    bash -n "${PROOF_REPO}/bin/estate-notify.sh"
  else
    echo "estate-notify.sh missing"
  fi
} >> "${REPORT}" 2>&1 || true
timer

step "06 - force lock-busy path"
mkdir -p "${PROOF_REPO}/.estate-refresh.lock"
set +e
bash "${PROOF_REPO}/bin/estate-refresh-runner.sh" "alpha=${SOURCE_REPO}" >> "${REPORT}" 2>&1
LOCK_RC="$?"
set -e
rmdir "${PROOF_REPO}/.estate-refresh.lock" || true
echo "LOCK_RC=${LOCK_RC}" >> "${REPORT}"
timer

step "07 - force failure path"
export ESTATE_MANIFEST_PATH="/tmp/does-not-exist.json"
export ESTATE_MAX_RETRIES="2"
export ESTATE_RETRY_DELAY_SECONDS="0"
set +e
bash "${PROOF_REPO}/bin/estate-refresh-runner.sh" >> "${REPORT}" 2>&1
FAIL_RC="$?"
set -e
unset ESTATE_MANIFEST_PATH
unset ESTATE_MAX_RETRIES
unset ESTATE_RETRY_DELAY_SECONDS
echo "FAIL_RC=${FAIL_RC}" >> "${REPORT}"
timer

step "08 - run success path"
set +e
bash "${PROOF_REPO}/bin/estate-refresh-runner.sh" "alpha=${SOURCE_REPO}" >> "${REPORT}" 2>&1
SUCCESS_RC="$?"
set -e
echo "SUCCESS_RC=${SUCCESS_RC}" >> "${REPORT}"
timer

step "09 - capture generated notification artifacts"
{
  echo
  echo "===== ESTATE_NOTIFICATION_STATUS.md ====="
  sed -n '1,220p' "${PROOF_REPO}/docs/estate/ESTATE_NOTIFICATION_STATUS.md"
  echo
  echo "===== notifications.ndjson ====="
  tail -n 40 "${PROOF_REPO}/estate/outbox/notifications.ndjson"
} >> "${REPORT}" 2>&1 || true
timer

step "10 - write repo summary"
cat > "${REPO_ROOT}/docs/status/SDT_NOTIFICATION_REPRO_LATEST.md" <<DOC
# SDT notification repro latest

## Stamp
$(date -u '+%F %T UTC')

## Branch under repro
- ${REMOTE_BRANCH}

## Report
- ${REPORT}

## Return codes
- lock_rc: ${LOCK_RC}
- fail_rc: ${FAIL_RC}
- success_rc: ${SUCCESS_RC}

## Next
Use this repro to replace broad PR19 claims with a smaller rebuild slice.
DOC

sed -n '1,220p' "${REPO_ROOT}/docs/status/SDT_NOTIFICATION_REPRO_LATEST.md"
timer

step "11 - return to main"
git checkout main
timer
