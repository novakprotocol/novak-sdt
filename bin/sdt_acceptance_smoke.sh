#!/usr/bin/env bash
set -Eeuo pipefail
set +H

START_EPOCH="$(date +%s)"
WORKDIR="$(mktemp -d /tmp/sdt-acceptance-XXXXXX)"
NEW_REPO="${WORKDIR}/new-proof"
EXISTING_REPO="${WORKDIR}/existing-proof"
SYSTEMD_OUT="${WORKDIR}/systemd"

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

cleanup() {
  rm -rf "${WORKDIR}"
}
trap cleanup EXIT

step "01 - install package"
python3 -m pip install -e . >/dev/null
sdt --help >/dev/null
timer

step "02 - prove fresh repo birth"
sdt new \
  --path "${NEW_REPO}" \
  --product-name "SDT Acceptance New Proof" \
  --product-statement "SDT Acceptance New Proof verifies fresh birth during acceptance smoke." \
  --public-title "SDT Acceptance New Proof" \
  --repo-summary "Fresh birth smoke proof." \
  --git-commit
sdt doctor --path "${NEW_REPO}"
timer

step "03 - prove existing repo baseline"
mkdir -p "${EXISTING_REPO}"
cat > "${EXISTING_REPO}/README.md" <<'DOC'
# Existing Repo
DOC

sdt baseline \
  --path "${EXISTING_REPO}" \
  --product-name "SDT Acceptance Existing Proof" \
  --product-statement "SDT Acceptance Existing Proof verifies baseline during acceptance smoke." \
  --public-title "SDT Acceptance Existing Proof" \
  --repo-summary "Existing repo baseline smoke proof." \
  --git-commit
sdt doctor --path "${EXISTING_REPO}"
timer

step "04 - prove timer helper render path"
bash "${NEW_REPO}/bin/install-estate-refresh-timer.sh" \
  --output-dir "${SYSTEMD_OUT}" \
  --on-calendar daily \
  --run-as-user root \
  --max-retries 2 \
  --retry-delay-seconds 15

grep -n 'ESTATE_MAX_RETRIES=2' "${SYSTEMD_OUT}/estate-refresh.service"
grep -n 'ESTATE_RETRY_DELAY_SECONDS=15' "${SYSTEMD_OUT}/estate-refresh.service"
grep -n 'OnCalendar=daily' "${SYSTEMD_OUT}/estate-refresh.timer"
timer

step "05 - done"
echo "ACCEPTANCE_SMOKE_PASS"
timer
