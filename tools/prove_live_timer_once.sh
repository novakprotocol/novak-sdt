#!/usr/bin/env bash
set -Eeuo pipefail
set +H

START_EPOCH="$(date +%s)"
REPO_ROOT="$(pwd)"
WORKDIR="/tmp/sdt-live-timer-proof"
PROOF_REPO="${WORKDIR}/repo"
SOURCE_REPO="${WORKDIR}/source"
UNIT_NAME="sdt-live-proof-once"

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

cleanup_unit() {
  systemctl stop "${UNIT_NAME}.timer" 2>/dev/null || true
  systemctl stop "${UNIT_NAME}.service" 2>/dev/null || true
  systemctl reset-failed "${UNIT_NAME}.service" 2>/dev/null || true
}
trap cleanup_unit EXIT

rm -rf "${WORKDIR}"
mkdir -p "${WORKDIR}"

step "01 - install package"
python3 -m pip install -e . >/dev/null
timer

step "02 - create proof repo"
sdt new \
  --path "${PROOF_REPO}" \
  --product-name "SDT Live Timer Proof" \
  --product-statement "SDT Live Timer Proof verifies a real scheduled fire on the host." \
  --public-title "SDT Live Timer Proof" \
  --repo-summary "Live timer proof." \
  --git-commit
timer

step "03 - create source repo with history data"
mkdir -p "${SOURCE_REPO}/docs/history"
cat > "${SOURCE_REPO}/docs/history/ATTEMPTS.ndjson" <<'DOC'
{"archived_copy":"docs/history/raw/live-01.log","archived_utc":"2026-04-18 00:00:01 UTC","failure_classes":{"generic-error":1},"failure_line_count":1,"line_count":2,"missed_opportunity_count":0,"source_name":"live-01.log","weighted_severity_total":2}
{"archived_copy":"docs/history/raw/live-02.log","archived_utc":"2026-04-18 00:00:11 UTC","failure_classes":{"python-traceback":1},"failure_line_count":1,"line_count":3,"missed_opportunity_count":1,"source_name":"live-02.log","weighted_severity_total":5}
DOC
timer

step "04 - schedule one retained live run"
cleanup_unit
systemd-run \
  --unit "${UNIT_NAME}" \
  --on-active=10s \
  --working-directory="${PROOF_REPO}" \
  --setenv=ESTATE_RUNNER_MODE=timer \
  --property=Type=oneshot \
  --property=RemainAfterExit=yes \
  /usr/bin/env bash -lc "bash bin/estate-refresh-runner.sh alpha=${SOURCE_REPO}"
timer

step "05 - wait for timer to fire"
sleep 18
timer

step "06 - capture proof"
mkdir -p "${WORKDIR}/capture"

systemctl show "${UNIT_NAME}.timer" \
  -p Id -p ActiveState -p SubState -p Result -p LastTriggerUSec -p NextElapseUSecMonotonic \
  > "${WORKDIR}/capture/timer_show.txt" 2>&1 || true

systemctl show "${UNIT_NAME}.service" \
  -p Id -p ActiveState -p SubState -p Result -p ExecMainStatus \
  > "${WORKDIR}/capture/service_show.txt" 2>&1 || true

journalctl -u "${UNIT_NAME}.service" --no-pager -n 200 \
  > "${WORKDIR}/capture/journal.txt" 2>&1 || true

RUNNER_MODE_LINE="$(grep -m1 'runner_mode:' "${PROOF_REPO}/docs/estate/ESTATE_RUNNER_STATUS.md" || true)"
OUTCOME_LINE="$(grep -m1 'outcome:' "${PROOF_REPO}/docs/estate/ESTATE_RUNNER_STATUS.md" || true)"

cat > "${REPO_ROOT}/docs/status/SDT_LIVE_TIMER_PROOF_LATEST.md" <<DOC
# SDT live timer proof latest

## Stamp
$(date -u '+%F %T UTC')

## Unit
- ${UNIT_NAME}

## Proof repo
- ${PROOF_REPO}

## Source repo
- ${SOURCE_REPO}

## Captured files
- ${WORKDIR}/capture/timer_show.txt
- ${WORKDIR}/capture/service_show.txt
- ${WORKDIR}/capture/journal.txt

## Key expectations
- runner_mode should be \`timer\`
- outcome should be \`success\`
- timer unit should show a trigger
- service unit should retain a visible result

## Runner status excerpt
\`\`\`
$(sed -n '1,80p' "${PROOF_REPO}/docs/estate/ESTATE_RUNNER_STATUS.md" 2>/dev/null || true)
\`\`\`

## Timer show
\`\`\`
$(sed -n '1,120p' "${WORKDIR}/capture/timer_show.txt" 2>/dev/null || true)
\`\`\`

## Service show
\`\`\`
$(sed -n '1,120p' "${WORKDIR}/capture/service_show.txt" 2>/dev/null || true)
\`\`\`

## Journal excerpt
\`\`\`
$(sed -n '1,120p' "${WORKDIR}/capture/journal.txt" 2>/dev/null || true)
\`\`\`

## Fast truth
- ${RUNNER_MODE_LINE}
- ${OUTCOME_LINE}
DOC

sed -n '1,240p' "${REPO_ROOT}/docs/status/SDT_LIVE_TIMER_PROOF_LATEST.md"
timer

step "07 - done"
echo "LIVE_TIMER_PROOF_FIXED_DONE"
timer
