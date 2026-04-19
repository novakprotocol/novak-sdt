#!/usr/bin/env bash
set -Eeuo pipefail
set +H

REPO_DIR="${1:-$(pwd)}"
TAG_NAME="${2:-}"

if [[ -z "${TAG_NAME}" ]]; then
  TAG_NAME="trusted-floor-$(date +%Y%m%d-%H%M%S)"
fi

cd "${REPO_DIR}"

git tag -a "${TAG_NAME}" -m "SDT trusted floor freeze"
git push origin "${TAG_NAME}" || true

echo "TRUSTED_FLOOR_TAG=${TAG_NAME}"
