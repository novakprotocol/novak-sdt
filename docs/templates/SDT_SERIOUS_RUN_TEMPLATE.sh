#!/usr/bin/env bash
set -Eeuo pipefail
set +H

step "01 - show repo truth"
pwd
git log --oneline --decorate -5 || true
git status --short || true
timer

step "02 - run tests"
set_test_summary "replace with the real test summary"
timer

step "03 - record next step"
add_note "replace this with what changed and why"
set_next_step "replace with the actual next step"
set_public_url "replace with an actual URL if one exists"
timer
