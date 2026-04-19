# SDT live timer proof latest

## Stamp
2026-04-19 15:21:49 UTC

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

## Runner status excerpt
```
# Estate Runner Status

- last_run_started_utc: 2026-04-19 15:21:42 UTC
- last_run_finished_utc: 2026-04-19 15:21:42 UTC
- outcome: success
- runner_mode: timer
- manifest_path: none
- discover_roots: none
- argument_count: 1
- elapsed_seconds: 0

## Command
- refresh_command: bash /tmp/sdt-live-timer-proof/repo/bin/estate-refresh.sh alpha=/tmp/sdt-live-timer-proof/source

## Notes
- run /tmp/estate-systemd render path is handled by install-estate-refresh-timer.sh
- review docs/estate/ESTATE_REFRESH_STATUS.md after each run
```

## Timer show
```
NextElapseUSecMonotonic=infinity
LastTriggerUSec=Sun 2026-04-19 15:21:42 UTC
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
Apr 19 15:21:42 novak-ansible-control systemd[1]: Starting sdt-live-proof-once.service - /usr/bin/env bash --noprofile --norc bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source...
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_HISTORY_SUMMARY.md
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_PRIORITY_QUEUE.md
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ACTION_QUEUE.md
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_INGEST_SUMMARY.md
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_CATALOG.md
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_REFRESH_STATUS.md
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_ARCHIVE_INDEX.md
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_DELTA.md
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/docs/estate/ESTATE_TRENDS.md
Apr 19 15:21:42 novak-ansible-control env[1709866]: UPDATED /tmp/sdt-live-timer-proof/repo/estate/archive/estate_refresh_history.ndjson
Apr 19 15:21:42 novak-ansible-control systemd[1]: Finished sdt-live-proof-once.service - /usr/bin/env bash --noprofile --norc bin/estate-refresh-runner.sh alpha=/tmp/sdt-live-timer-proof/source.
```

## Fast truth
- - runner_mode: timer
- - outcome: success
