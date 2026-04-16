#!/usr/bin/env bash
set -Eeuo pipefail
set +H

if [[ $# -ne 2 ]]; then
  echo "Usage: bash bin/sdt-inventory-snapshot.sh <repo_path> <label>"
  exit 1
fi

REPO_PATH="$1"
LABEL="$2"

python3 tools/sdt_inventory_snapshot.py \
  --repo-path "${REPO_PATH}" \
  --label "${LABEL}"
