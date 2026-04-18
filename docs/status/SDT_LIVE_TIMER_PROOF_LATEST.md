# SDT live timer proof latest

## Stamp
2026-04-18 11:57:04 UTC

## Unit
- sdt-live-proof-once

## Proof repo
- /tmp/sdt-live-timer-proof/repo

## Source repo
- /tmp/sdt-live-timer-proof/source

## Captured files
- /tmp/sdt-live-timer-proof/capture/timer_show.txt
- /tmp/sdt-live-timer-proof/capture/service_show.txt
- /tmp/sdt-live-timer-proof/capture/journal.txt

## Key expectations
- runner_mode should be `timer`
- outcome should be `success`
- timer unit should show a trigger
- service unit should retain a visible result

## Runner status excerpt
```
# Estate Runner Status

- last_run_started_utc: `2026-04-18 11:56:56 UTC`
- last_run_finished_utc: `2026-04-18 11:56:56 UTC`
- outcome: `success`
- runner_mode: `timer`
- manifest_path: `/tmp/sdt-live-timer-proof/repo/estate/estate_sources.json`
- discover_roots: `none`
- argument_count: `1`
- elapsed_seconds: `0`

## Command
- refresh_command: `bash bin/estate-refresh.sh alpha=/tmp/sdt-live-timer-proof/source`

## Notes
- run `bash bin/install-estate-refresh-timer.sh --output-dir /tmp/estate-systemd` to render timer and service files
- review `docs/estate/ESTATE_REFRESH_STATUS.md` after each run
```

## Timer show
```
NextElapseUSecMonotonic=infinity
LastTriggerUSec=Sat 2026-04-18 11:56:56 UTC
Result=success
Id=sdt-live-proof-once.timer
ActiveState=active
SubState=running
```

## Service show
```
Result=success
ExecMainStatus=0
Id=sdt-live-proof-once.service
ActiveState=active
SubState=exited
```

## Journal excerpt
```
Apr 18 11:37:40 novak-ansible-control systemd[1]: Started sdt-live-proof-once.service - /usr/bin/env bash /tmp/sdt-live-timer-proof/repo/bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source.
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_HISTORY_SUMMARY.md
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_PRIORITY_QUEUE.md
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ACTION_QUEUE.md
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_INGEST_SUMMARY.md
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_CATALOG.md
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_REFRESH_STATUS.md
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ARCHIVE_INDEX.md
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_DELTA.md
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_TRENDS.md
Apr 18 11:37:40 novak-ansible-control env[1360896]: UPDATED /tmp/sdt-live-timer-proof/repo/estate/archive/estate_refresh_history.ndjson
Apr 18 11:37:40 novak-ansible-control systemd[1]: sdt-live-proof-once.service: Deactivated successfully.
Apr 18 11:38:50 novak-ansible-control systemd[1]: Started sdt-live-proof-once.service - /usr/bin/env bash /tmp/sdt-live-timer-proof/repo/bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source.
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_HISTORY_SUMMARY.md
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_PRIORITY_QUEUE.md
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ACTION_QUEUE.md
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_INGEST_SUMMARY.md
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_CATALOG.md
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_REFRESH_STATUS.md
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ARCHIVE_INDEX.md
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_DELTA.md
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_TRENDS.md
Apr 18 11:38:50 novak-ansible-control env[1361783]: UPDATED /tmp/sdt-live-timer-proof/repo/estate/archive/estate_refresh_history.ndjson
Apr 18 11:38:50 novak-ansible-control systemd[1]: sdt-live-proof-once.service: Deactivated successfully.
Apr 18 11:56:56 novak-ansible-control systemd[1]: Starting sdt-live-proof-once.service - /usr/bin/env bash -lc "bash bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source"...
Apr 18 11:56:56 novak-ansible-control env[1367275]: ========================================
Apr 18 11:56:56 novak-ansible-control env[1367275]:  NOVAK ANSIBLE CONTROL
Apr 18 11:56:56 novak-ansible-control env[1367275]: ========================================
Apr 18 11:56:56 novak-ansible-control env[1367275]:  12 simultaneous chaos monkeys.
Apr 18 11:56:56 novak-ansible-control env[1367275]:  Determinism wins anyway.
Apr 18 11:56:56 novak-ansible-control env[1367275]: ========================================
Apr 18 11:56:56 novak-ansible-control env[1367269]: /root/.profile: line 11: /.local/bin/env: No such file or directory
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_HISTORY_SUMMARY.md
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_PRIORITY_QUEUE.md
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ACTION_QUEUE.md
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_INGEST_SUMMARY.md
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_CATALOG.md
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_REFRESH_STATUS.md
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ARCHIVE_INDEX.md
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_DELTA.md
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_TRENDS.md
Apr 18 11:56:56 novak-ansible-control env[1367285]: UPDATED /tmp/sdt-live-timer-proof/repo/estate/archive/estate_refresh_history.ndjson
Apr 18 11:56:56 novak-ansible-control systemd[1]: Finished sdt-live-proof-once.service - /usr/bin/env bash -lc "bash bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source".
```

## Fast truth
- - runner_mode: `timer`
- - outcome: `success`
