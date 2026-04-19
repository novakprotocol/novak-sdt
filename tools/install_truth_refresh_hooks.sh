#!/usr/bin/env bash
set -Eeuo pipefail
set +H

REPO_DIR="${1:-$(pwd)}"
HOOK_DIR="${REPO_DIR}/.git/hooks"

mkdir -p "${HOOK_DIR}"

cat > "${HOOK_DIR}/post-commit" <<'HOOK'
#!/usr/bin/env bash
set -Eeuo pipefail
set +H

repo_root="$(git rev-parse --show-toplevel)"
cd "${repo_root}"

if [[ -x tools/run_truth_refresh_and_stage.sh ]]; then
  tools/run_truth_refresh_and_stage.sh "${repo_root}" >/tmp/sdt-post-commit-truth.log 2>&1 || true
fi
HOOK
chmod +x "${HOOK_DIR}/post-commit"

cat > "${HOOK_DIR}/post-merge" <<'HOOK'
#!/usr/bin/env bash
set -Eeuo pipefail
set +H

repo_root="$(git rev-parse --show-toplevel)"
cd "${repo_root}"

if [[ -x tools/run_truth_refresh_and_stage.sh ]]; then
  tools/run_truth_refresh_and_stage.sh "${repo_root}" >/tmp/sdt-post-merge-truth.log 2>&1 || true
fi
HOOK
chmod +x "${HOOK_DIR}/post-merge"

echo "INSTALLED_HOOKS repo=${REPO_DIR}"
