#!/usr/bin/env bash
set -Eeuo pipefail
set +H

if [[ $# -lt 1 ]]; then
  echo "Usage: bash bin/history-import.sh /path/to/log1.txt [/path/to/log2.txt ...]"
  exit 1
fi

ARGS=()
for f in "$@"; do
  ARGS+=(--log-file "$f")
done

python3 tools/archive_history_log.py "${ARGS[@]}"
