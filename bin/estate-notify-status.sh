#!/usr/bin/env bash
set -Eeuo pipefail
set +H

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTBOX="${REPO_DIR}/estate/outbox/notifications.ndjson"
OUTPUT="${REPO_DIR}/docs/estate/ESTATE_NOTIFICATION_STATUS_RENDERED.md"

python3 "${REPO_DIR}/tools/render_notify_outbox_status.py" "${OUTBOX}" "${OUTPUT}"
sed -n '1,160p' "${OUTPUT}"
