#!/usr/bin/env bash
set -Eeuo pipefail
set +H

START_EPOCH="$(date +%s)"
REPO_ROOT="$(pwd)"
WORKDIR="/tmp/sdt-notify-n1-proof"
PROOF_REPO="${WORKDIR}/proof"

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

step "01 - install package"
python3 -m pip install -e . >/dev/null
timer

step "02 - create proof repo"
sdt new \
  --path "${PROOF_REPO}" \
  --product-name "SDT Notify N1 Proof" \
  --product-statement "SDT Notify N1 Proof verifies helper return codes, outbox writes, and notification status rendering." \
  --public-title "SDT Notify N1 Proof" \
  --repo-summary "Notify N1 proof." \
  --git-commit
sdt doctor --path "${PROOF_REPO}"
timer

step "03 - lock-busy event"
set +e
bash "${PROOF_REPO}/bin/estate-notify.sh" \
  --event lock-busy \
  --run-label notify-lock-01 \
  --message "lock busy proof"
LOCK_RC="$?"
set -e
test "${LOCK_RC}" -eq 75
timer

step "04 - failure event"
set +e
bash "${PROOF_REPO}/bin/estate-notify.sh" \
  --event failure \
  --run-label notify-fail-01 \
  --message "failure proof"
FAIL_RC="$?"
set -e
test "${FAIL_RC}" -eq 2
timer

step "05 - success event"
set +e
bash "${PROOF_REPO}/bin/estate-notify.sh" \
  --event success \
  --run-label notify-pass-01 \
  --message "success proof"
SUCCESS_RC="$?"
set -e
test "${SUCCESS_RC}" -eq 0
timer

step "06 - verify outbox and status doc"
PROOF_REPO="${PROOF_REPO}" python3 - <<'PY'
import json
import os
from pathlib import Path

proof_repo = Path(os.environ["PROOF_REPO"])
outbox = proof_repo / "estate/outbox/notifications.ndjson"
status_doc = proof_repo / "docs/estate/ESTATE_NOTIFICATION_STATUS.md"

records = [json.loads(line) for line in outbox.read_text(encoding="utf-8").splitlines() if line.strip()]
assert [r["event"] for r in records] == ["lock-busy", "failure", "success"], records
text = status_doc.read_text(encoding="utf-8")
assert "last_event: `success`" in text, text
assert "lock-busy: `1`" in text, text
assert "failure: `1`" in text, text
assert "success: `1`" in text, text
print("OUTBOX_AND_STATUS_PASS")
PY
timer

step "07 - write latest proof note"
cat > "${REPO_ROOT}/docs/status/SDT_NOTIFY_N1_LATEST.md" <<DOC
# SDT Notify N1 latest

## Stamp
$(date -u '+%F %T UTC')

## Proof repo
- ${PROOF_REPO}

## Return codes
- lock-busy: ${LOCK_RC}
- failure: ${FAIL_RC}
- success: ${SUCCESS_RC}

## Outbox
- ${PROOF_REPO}/estate/outbox/notifications.ndjson

## Status doc
- ${PROOF_REPO}/docs/estate/ESTATE_NOTIFICATION_STATUS.md
DOC

sed -n '1,220p' "${REPO_ROOT}/docs/status/SDT_NOTIFY_N1_LATEST.md"
echo
sed -n '1,220p' "${PROOF_REPO}/docs/estate/ESTATE_NOTIFICATION_STATUS.md"
timer

step "08 - done"
echo "NOTIFY_N1_PROOF_PASS"
timer
