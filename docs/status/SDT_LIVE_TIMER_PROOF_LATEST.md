# SDT live timer proof latest

## Stamp
2026-04-18 16:09:01 UTC

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

- last_run_started_utc: 
- last_run_finished_utc: 
- outcome: 
- runner_mode: 
- manifest_path: 
- discover_roots: 
- argument_count: 
- elapsed_seconds: 

## Command
- refresh_command: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_HISTORY_SUMMARY.md
UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_PRIORITY_QUEUE.md
UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ACTION_QUEUE.md
UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_INGEST_SUMMARY.md
UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_CATALOG.md
UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_REFRESH_STATUS.md
UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ARCHIVE_INDEX.md
UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_DELTA.md
UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_TRENDS.md
UPDATED /tmp/sdt-live-timer-proof/repo/estate/archive/estate_refresh_history.ndjson

## Notes
- run WROTE /tmp/estate-systemd/estate-refresh.service
WROTE /tmp/estate-systemd/estate-refresh.timer to render timer and service files
- review  after each run
```

## Timer show
```
NextElapseUSecMonotonic=infinity
LastTriggerUSec=Sat 2026-04-18 16:08:55 UTC
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
Apr 18 11:57:04 novak-ansible-control systemd[1]: sdt-live-proof-once.service: Deactivated successfully.
Apr 18 11:57:04 novak-ansible-control systemd[1]: Stopped sdt-live-proof-once.service - /usr/bin/env bash -lc "bash bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source".
Apr 18 16:07:47 novak-ansible-control systemd[1]: Starting sdt-live-proof-once.service - /usr/bin/env bash -lc "bash bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source"...
Apr 18 16:07:47 novak-ansible-control env[1423355]: ========================================
Apr 18 16:07:47 novak-ansible-control env[1423355]:  NOVAK ANSIBLE CONTROL
Apr 18 16:07:47 novak-ansible-control env[1423355]: ========================================
Apr 18 16:07:47 novak-ansible-control env[1423355]:  12 simultaneous chaos monkeys.
Apr 18 16:07:47 novak-ansible-control env[1423355]:  Determinism wins anyway.
Apr 18 16:07:47 novak-ansible-control env[1423355]: ========================================
Apr 18 16:07:47 novak-ansible-control env[1423351]: /root/.profile: line 11: /.local/bin/env: No such file or directory
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_HISTORY_SUMMARY.md
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_PRIORITY_QUEUE.md
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ACTION_QUEUE.md
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_INGEST_SUMMARY.md
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_CATALOG.md
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_REFRESH_STATUS.md
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ARCHIVE_INDEX.md
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_DELTA.md
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_TRENDS.md
Apr 18 16:07:47 novak-ansible-control env[1423365]: UPDATED /tmp/sdt-live-timer-proof/repo/estate/archive/estate_refresh_history.ndjson
Apr 18 16:07:47 novak-ansible-control systemd[1]: Finished sdt-live-proof-once.service - /usr/bin/env bash -lc "bash bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source".
Apr 18 16:07:54 novak-ansible-control systemd[1]: sdt-live-proof-once.service: Deactivated successfully.
Apr 18 16:07:54 novak-ansible-control systemd[1]: Stopped sdt-live-proof-once.service - /usr/bin/env bash -lc "bash bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source".
Apr 18 16:08:55 novak-ansible-control systemd[1]: Starting sdt-live-proof-once.service - /usr/bin/env bash -lc "bash bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source"...
Apr 18 16:08:55 novak-ansible-control env[1424188]: ========================================
Apr 18 16:08:55 novak-ansible-control env[1424188]:  NOVAK ANSIBLE CONTROL
Apr 18 16:08:55 novak-ansible-control env[1424188]: ========================================
Apr 18 16:08:55 novak-ansible-control env[1424188]:  12 simultaneous chaos monkeys.
Apr 18 16:08:55 novak-ansible-control env[1424188]:  Determinism wins anyway.
Apr 18 16:08:55 novak-ansible-control env[1424188]: ========================================
Apr 18 16:08:55 novak-ansible-control env[1424184]: /root/.profile: line 11: /.local/bin/env: No such file or directory
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_HISTORY_SUMMARY.md
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_PRIORITY_QUEUE.md
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ACTION_QUEUE.md
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_INGEST_SUMMARY.md
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_CATALOG.md
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_REFRESH_STATUS.md
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ARCHIVE_INDEX.md
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_DELTA.md
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_TRENDS.md
Apr 18 16:08:55 novak-ansible-control env[1424198]: UPDATED /tmp/sdt-live-timer-proof/repo/estate/archive/estate_refresh_history.ndjson
Apr 18 16:08:55 novak-ansible-control env[1424208]: bin/estate-refresh-runner.sh: line 24: 2026-04-18: command not found
Apr 18 16:08:55 novak-ansible-control env[1424210]: bin/estate-refresh-runner.sh: line 24: 2026-04-18: command not found
Apr 18 16:08:55 novak-ansible-control env[1424212]: bin/estate-refresh-runner.sh: line 24: success: command not found
Apr 18 16:08:55 novak-ansible-control env[1424214]: bin/estate-refresh-runner.sh: line 24: timer: command not found
Apr 18 16:08:55 novak-ansible-control env[1424216]: bin/estate-refresh-runner.sh: line 24: /tmp/sdt-live-timer-proof/repo/estate/estate_sources.json: Permission denied
Apr 18 16:08:55 novak-ansible-control env[1424218]: bin/estate-refresh-runner.sh: line 24: none: command not found
Apr 18 16:08:55 novak-ansible-control env[1424220]: bin/estate-refresh-runner.sh: line 24: 1: command not found
Apr 18 16:08:55 novak-ansible-control env[1424222]: bin/estate-refresh-runner.sh: line 24: 0: command not found
Apr 18 16:08:55 novak-ansible-control env[1424235]: bin/estate-refresh-runner.sh: line 24: docs/estate/ESTATE_REFRESH_STATUS.md: Permission denied
Apr 18 16:08:55 novak-ansible-control systemd[1]: Finished sdt-live-proof-once.service - /usr/bin/env bash -lc "bash bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source".
```

## Fast truth
- - runner_mode: 
- - outcome: 
