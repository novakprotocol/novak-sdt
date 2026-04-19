#!/usr/bin/env bash
set -Eeuo pipefail
set +H

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "ERROR: source this file instead of executing it"
  echo "USE: source /root/novak-sdt/tools/sdt_shell_activate.sh"
  exit 1
fi

if [[ -z "${SDT_OLD_PS1+x}" ]]; then
  export SDT_OLD_PS1="${PS1-}"
fi

if [[ -z "${SDT_OLD_PROMPT_COMMAND+x}" ]]; then
  export SDT_OLD_PROMPT_COMMAND="${PROMPT_COMMAND-__SDT_EMPTY__}"
fi

export SDT_SHELL_ACTIVE=1
export VIRTUAL_ENV_DISABLE_PROMPT=1

sdt_refresh_context() {
  local repo_label
  local branch_label
  local branch_color
  local novak_color
  local repo_color
  local reset_color
  local warn_color
  local clean_color
  local dirty_color

  novak_color='\[\e[1;35m\]'
  repo_color='\[\e[0;37m\]'
  clean_color='\[\e[1;32m\]'
  dirty_color='\[\e[1;31m\]'
  warn_color='\[\e[1;33m\]'
  reset_color='\[\e[0m\]'

  if git rev-parse --show-toplevel >/dev/null 2>&1; then
    repo_label="$(basename "$(git rev-parse --show-toplevel)")"
  else
    repo_label="NO-REPO"
  fi

  if git rev-parse --abbrev-ref HEAD >/dev/null 2>&1; then
    branch_label="$(git rev-parse --abbrev-ref HEAD)"
  else
    branch_label="NO-BRANCH"
  fi

  if [[ "${repo_label}" == "NO-REPO" ]]; then
    branch_color="${warn_color}"
  elif [[ "${branch_label}" == "HEAD" || "${branch_label}" == "NO-BRANCH" ]]; then
    branch_color="${warn_color}"
  else
    if ! git diff --no-ext-diff --quiet --ignore-submodules HEAD -- 2>/dev/null || \
       ! git diff --cached --no-ext-diff --quiet --ignore-submodules -- 2>/dev/null || \
       [[ -n "$(git ls-files --others --exclude-standard 2>/dev/null)" ]]; then
      branch_color="${dirty_color}"
    else
      branch_color="${clean_color}"
    fi
  fi

  export SDT_ACTIVE_REPO="${repo_label}"
  export SDT_ACTIVE_BRANCH="${branch_label}"

  PS1="(${novak_color}NOVΛK™${reset_color}-SDT:${repo_color}${repo_label}${reset_color}@${branch_color}${branch_label}${reset_color}) \u@\h:\w# "
}

sdt_deactivate() {
  if [[ -n "${SDT_OLD_PS1-}" ]]; then
    PS1="${SDT_OLD_PS1}"
  fi

  if [[ "${SDT_OLD_PROMPT_COMMAND-__SDT_EMPTY__}" == "__SDT_EMPTY__" ]]; then
    unset PROMPT_COMMAND
  else
    PROMPT_COMMAND="${SDT_OLD_PROMPT_COMMAND}"
  fi

  unset SDT_SHELL_ACTIVE
  unset SDT_ACTIVE_REPO
  unset SDT_ACTIVE_BRANCH
  unset SDT_OLD_PS1
  unset SDT_OLD_PROMPT_COMMAND
  unset VIRTUAL_ENV_DISABLE_PROMPT
  unset -f sdt_refresh_context
  unset -f sdt_deactivate
}

if [[ "${SDT_OLD_PROMPT_COMMAND}" == "__SDT_EMPTY__" ]]; then
  PROMPT_COMMAND='sdt_refresh_context'
else
  PROMPT_COMMAND="sdt_refresh_context; ${SDT_OLD_PROMPT_COMMAND}"
fi

sdt_refresh_context

echo "NOVΛK™ - SDT shell active: ${SDT_ACTIVE_REPO}@${SDT_ACTIVE_BRANCH}"
echo "Branch color: green=clean, red=dirty, yellow=detached/no-repo"
echo "Use 'sdt_deactivate' to leave the NOVΛK™ - SDT shell context."
