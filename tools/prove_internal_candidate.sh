#!/usr/bin/env bash
set -Eeuo pipefail
set +H

START_EPOCH="$(date +%s)"
REPO_ROOT="$(pwd)"
OUTDIR="/tmp/sdt-internal-candidate-proof"

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

rm -rf "${OUTDIR}"
mkdir -p "${OUTDIR}"

step "01 - acceptance smoke"
bash bin/sdt_acceptance_smoke.sh | tee "${OUTDIR}/01_acceptance.txt"
timer

step "02 - live timer proof"
if [[ -x tools/prove_live_timer_once.sh ]]; then
  bash tools/prove_live_timer_once.sh | tee "${OUTDIR}/02_live_timer.txt"
else
  echo "SKIP no live timer proof script" | tee "${OUTDIR}/02_live_timer.txt"
fi
timer

step "03 - notify n1 proof"
if [[ -x tools/prove_notify_n1.sh ]]; then
  bash tools/prove_notify_n1.sh | tee "${OUTDIR}/03_notify_n1.txt"
else
  echo "SKIP no notify n1 proof script" | tee "${OUTDIR}/03_notify_n1.txt"
fi
timer

step "04 - write proof summary"
cat > docs/status/SDT_INTERNAL_CANDIDATE_PROOF.md <<DOC
# SDT internal candidate proof

## Stamp
$(date -u '+%F %T UTC')

## Acceptance smoke
- /tmp/sdt-internal-candidate-proof/01_acceptance.txt

## Live timer proof
- /tmp/sdt-internal-candidate-proof/02_live_timer.txt

## Notify N1 proof
- /tmp/sdt-internal-candidate-proof/03_notify_n1.txt
DOC

sed -n '1,160p' docs/status/SDT_INTERNAL_CANDIDATE_PROOF.md
timer
