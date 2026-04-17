# SDT internal release gate v0.1

## Scope
This gate is for internal SDT v0.1 only.

## Proven included in v0.1
- `sdt new` births a repo with the current SDT floor
- `sdt baseline` can adopt a non-git existing directory with `--git-commit`
- `sdt doctor` verifies the required floor
- merged main includes baseline non-git adoption repair
- merged main includes timer helper retry-arg render support
- merged main can render systemd timer/service files with retry settings

## Must pass
- editable install works
- compileall works
- fresh repo birth proof works
- existing repo baseline proof works
- doctor passes on both
- timer helper render proof works on main
- one-page real-now handoff exists
- deferred items are explicitly named

## Deferred from v0.1
- PR 19 notification/hardening lane
- doctrine birth-floor bake-in
- live systemd timer fire proof on a real cadence
- broader production packaging and public claims

## Must not be claimed
- public production readiness
- notifications complete
- doctrine baked into repo birth
- full scheduler hardening beyond what has been directly proved
