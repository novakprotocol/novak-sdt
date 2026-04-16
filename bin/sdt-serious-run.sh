#!/usr/bin/env bash
set -Eeuo pipefail
set +H

usage() {
  echo "Usage: bash bin/sdt-serious-run.sh <repo_path> <day_number> <run_label> <run_body_script>"
}

if [[ $# -ne 4 ]]; then
  usage
  exit 1
fi

REPO_PATH="$(python3 -c "from pathlib import Path; import sys; print(Path(sys.argv[1]).resolve())" "$1")"
DAY_NUMBER="$2"
RUN_LABEL="$3"
RUN_BODY="$(python3 -c "from pathlib import Path; import sys; print(Path(sys.argv[1]).resolve())" "$4")"

if [[ ! -d "${REPO_PATH}" ]]; then
  echo "ERROR: repo_path does not exist: ${REPO_PATH}"
  exit 1
fi

if [[ ! -f "${RUN_BODY}" ]]; then
  echo "ERROR: run body does not exist: ${RUN_BODY}"
  exit 1
fi

slugify() {
  printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed 's/^-//; s/-$//' | cut -c1-80
}

STATE_DIR="${REPO_PATH}/.sdt-state"
STATE_FILE="${STATE_DIR}/${DAY_NUMBER}.env"
RUNS_DIR="${REPO_PATH}/docs/status/run-receipts"

mkdir -p "${STATE_DIR}" "${RUNS_DIR}"

if [[ -f "${STATE_FILE}" ]]; then
  . "${STATE_FILE}"
else
  DAY_TOTAL_SEC=0
  DAY_RUN_COUNT=0
fi

RUN_STAMP_UTC="$(date -u '+%Y-%m-%dT%H-%M-%SZ')"
RUN_ID="${RUN_STAMP_UTC}--$(slugify "${RUN_LABEL}")"
RUN_DIR="${RUNS_DIR}/${RUN_ID}"
STDOUT_LOG="${RUN_DIR}/stdout.log"
STEPS_LOG="${RUN_DIR}/steps.log"
NOTES_FILE="${RUN_DIR}/notes.txt"
STATUS_BEFORE_FILE="${RUN_DIR}/git_status_before.txt"

mkdir -p "${RUN_DIR}"
: > "${STDOUT_LOG}"
: > "${STEPS_LOG}"
: > "${NOTES_FILE}"
: > "${STATUS_BEFORE_FILE}"

START_EPOCH="$(date +%s)"
START_LOCAL="$(date '+%F %T %Z')"
START_UTC="$(date -u '+%F %T UTC')"

OPERATOR_NAME="${SUDO_USER:-${USER}}"
HOST_NAME="$(hostname -f 2>/dev/null || hostname)"

cd "${REPO_PATH}"

BRANCH_BEFORE="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo UNAVAILABLE)"
HEAD_BEFORE="$(git rev-parse HEAD 2>/dev/null || echo UNAVAILABLE)"
REMOTE_URL="$(git remote get-url origin 2>/dev/null || echo UNAVAILABLE)"
git status --short > "${STATUS_BEFORE_FILE}" 2>/dev/null || true

NEXT_STEP=""
PUBLIC_URL=""
TEST_SUMMARY=""
STEP_INDEX=0

step() {
  STEP_INDEX="$((STEP_INDEX + 1))"
  local title="$1"
  local ts_utc
  ts_utc="$(date -u '+%F %T UTC')"
  echo
  echo "============================================================"
  echo "[${DAY_NUMBER}] [${ts_utc}] ${title}"
  echo "============================================================"
  printf '%02d | %s | %s\n' "${STEP_INDEX}" "${ts_utc}" "${title}" >> "${STEPS_LOG}"
}

timer() {
  local now elapsed current_total current_runs
  now="$(date +%s)"
  elapsed="$((now - START_EPOCH))"
  current_total="$((DAY_TOTAL_SEC + elapsed))"
  current_runs="$((DAY_RUN_COUNT + 1))"
  echo "----- run_elapsed_sec: ${elapsed} | day_total_if_success_sec: ${current_total} | day_run_count_if_success: ${current_runs} -----"
}

add_note() {
  printf '%s\n' "$1" >> "${NOTES_FILE}"
}

set_next_step() {
  NEXT_STEP="$1"
}

set_public_url() {
  PUBLIC_URL="$1"
}

set_test_summary() {
  TEST_SUMMARY="$1"
}

finish() {
  local exit_code="$1"
  local end_epoch end_local end_utc elapsed status
  local new_day_total new_day_run_count

  end_epoch="$(date +%s)"
  end_local="$(date '+%F %T %Z')"
  end_utc="$(date -u '+%F %T UTC')"
  elapsed="$((end_epoch - START_EPOCH))"

  if [[ "${exit_code}" -eq 0 ]]; then
    status="PASS"
    new_day_total="$((DAY_TOTAL_SEC + elapsed))"
    new_day_run_count="$((DAY_RUN_COUNT + 1))"
    printf 'DAY_TOTAL_SEC=%s\nDAY_RUN_COUNT=%s\n' "${new_day_total}" "${new_day_run_count}" > "${STATE_FILE}"
    DAY_TOTAL_SEC="${new_day_total}"
    DAY_RUN_COUNT="${new_day_run_count}"
  else
    status="FAIL"
  fi

  python3 "${REPO_PATH}/tools/sdt_write_receipt.py"     --repo-path "${REPO_PATH}"     --run-id "${RUN_ID}"     --day-number "${DAY_NUMBER}"     --run-label "${RUN_LABEL}"     --status "${status}"     --operator "${OPERATOR_NAME}"     --host "${HOST_NAME}"     --start-local "${START_LOCAL}"     --start-utc "${START_UTC}"     --end-local "${end_local}"     --end-utc "${end_utc}"     --run-elapsed-sec "${elapsed}"     --day-total-sec "${DAY_TOTAL_SEC}"     --day-run-count "${DAY_RUN_COUNT}"     --branch-before "${BRANCH_BEFORE}"     --head-before "${HEAD_BEFORE}"     --remote-url "${REMOTE_URL}"     --status-before-file "${STATUS_BEFORE_FILE}"     --stdout-log "${STDOUT_LOG}"     --steps-log "${STEPS_LOG}"     --notes-file "${NOTES_FILE}"     --next-step "${NEXT_STEP}"     --public-url "${PUBLIC_URL}"     --test-summary "${TEST_SUMMARY}"

  echo
  echo "============================================================"
  echo "[${DAY_NUMBER}] RUN COMPLETE"
  echo "============================================================"
  echo "RUN_LABEL:          ${RUN_LABEL}"
  echo "STATUS:             ${status}"
  echo "START_LOCAL:        ${START_LOCAL}"
  echo "START_UTC:          ${START_UTC}"
  echo "END_LOCAL:          ${end_local}"
  echo "END_UTC:            ${end_utc}"
  echo "RUN_ELAPSED_SEC:    ${elapsed}"
  echo "DAY_TOTAL_SEC:      ${DAY_TOTAL_SEC}"
  echo "DAY_RUN_COUNT:      ${DAY_RUN_COUNT}"
  echo "STATE_FILE:         ${STATE_FILE}"
  echo "RECEIPT_DIR:        ${RUN_DIR}"
  echo "EXIT_CODE:          ${exit_code}"
}

trap 'rc=$?; finish "$rc"; exit "$rc"' EXIT

exec > >(tee -a "${STDOUT_LOG}") 2>&1

echo
echo "============================================================"
echo "[${DAY_NUMBER}] RUN START"
echo "============================================================"
echo "RUN_LABEL:          ${RUN_LABEL}"
echo "START_LOCAL:        ${START_LOCAL}"
echo "START_UTC:          ${START_UTC}"
echo "DAY_TOTAL_SEC_IN:   ${DAY_TOTAL_SEC}"
echo "DAY_RUN_COUNT_IN:   ${DAY_RUN_COUNT}"
echo "STATE_FILE:         ${STATE_FILE}"
echo "RUN_BODY:           ${RUN_BODY}"
echo "REPO_PATH:          ${REPO_PATH}"

source "${RUN_BODY}"
