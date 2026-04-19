#!/usr/bin/env bash
set -Eeuo pipefail
set +H

REPO_ROOT="${1:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
HOOK_DIR="${REPO_ROOT}/.git/hooks"

mkdir -p "${HOOK_DIR}"

for hook in post-commit post-merge; do
  if [[ -f "${HOOK_DIR}/${hook}" && ! -f "${HOOK_DIR}/${hook}.bak.sdt" ]]; then
    mv "${HOOK_DIR}/${hook}" "${HOOK_DIR}/${hook}.bak.sdt"
  fi

  cat > "${HOOK_DIR}/${hook}" <<HOOK
#!/usr/bin/env bash
set -Eeuo pipefail
set +H
bash "${REPO_ROOT}/tools/truth_refresh_advisory.sh" "${REPO_ROOT}" || true
HOOK
  chmod +x "${HOOK_DIR}/${hook}"
done

echo "INSTALLED_ADVISORY_HOOKS repo=${REPO_ROOT}"
