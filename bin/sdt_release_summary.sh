#!/usr/bin/env bash
set -Eeuo pipefail
set +H

echo "===== CURRENT TAG ====="
git describe --tags --exact-match 2>/dev/null || echo "NO_EXACT_TAG"

echo
echo "===== HEAD ====="
git log --oneline --decorate -5

echo
echo "===== OPEN PRs ====="
gh pr list --repo novakprotocol/novak-sdt --limit 20 || true

echo
echo "===== KEY DOCS ====="
for path in \
  docs/releases/SDT_INTERNAL_v0.1_RELEASE.md \
  docs/releases/SDT_INTERNAL_v0.1.1_RC2_RELEASE.md \
  docs/status/SDT_INTERNAL_RELEASE_GATE_V0_1.md \
  docs/status/SDT_ONE_PAGE_REAL_NOW.md \
  docs/status/SDT_LIVE_TIMER_PROOF_LATEST.md \
  docs/status/SDT_NOTIFICATION_REBUILD_SPEC.md
do
  if [[ -f "$path" ]]; then
    echo "PRESENT $path"
  else
    echo "MISSING $path"
  fi
done
