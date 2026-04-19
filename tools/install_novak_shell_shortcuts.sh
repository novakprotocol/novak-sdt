#!/usr/bin/env bash
set -Eeuo pipefail
set +H

SHORTCUTS_FILE="${HOME}/.novak_sdt_shell_shortcuts.sh"
BASHRC_FILE="${HOME}/.bashrc"
SOURCE_LINE='[[ -f "${HOME}/.novak_sdt_shell_shortcuts.sh" ]] && source "${HOME}/.novak_sdt_shell_shortcuts.sh"'

cat > "${SHORTCUTS_FILE}" <<'EOS'
novak() {
  local target
  target="${1:-$PWD}"

  if [[ -d "${target}" ]]; then
    cd "${target}" || return 1
  fi

  if [[ -f "./tools/sdt_shell_activate.sh" ]]; then
    source ./tools/sdt_shell_activate.sh
  else
    echo "No SDT shell helper found in: $(pwd)"
    return 1
  fi
}

nsdt() {
  novak "$@"
}
EOS

chmod 0644 "${SHORTCUTS_FILE}"
touch "${BASHRC_FILE}"

if ! grep -Fqx "${SOURCE_LINE}" "${BASHRC_FILE}"; then
  printf '\n%s\n' "${SOURCE_LINE}" >> "${BASHRC_FILE}"
fi

echo "WROTE ${SHORTCUTS_FILE}"
echo "UPDATED ${BASHRC_FILE}"
echo "For immediate use in the current shell:"
echo "  source ${SHORTCUTS_FILE}"
