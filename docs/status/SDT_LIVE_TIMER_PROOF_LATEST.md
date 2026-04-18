# SDT live timer proof latest

## Stamp
2026-04-18 11:37:48 UTC

## Unit
- sdt-live-proof-once

## Proof repo
- /tmp/sdt-live-timer-proof/repo

## Source repo
- /tmp/sdt-live-timer-proof/source

## Captured files
- /tmp/sdt-live-timer-proof/capture/timer_status.txt
- /tmp/sdt-live-timer-proof/capture/service_status.txt
- /tmp/sdt-live-timer-proof/capture/journal.txt

## Runner status excerpt

```
# Estate Runner Status

- last_run_started_utc: `2026-04-18 11:37:40 UTC`
- last_run_finished_utc: `2026-04-18 11:37:40 UTC`
- outcome: `success`
- runner_mode: `manual`
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

## Service status excerpt
```
Unit sdt-live-proof-once.service could not be found.
```
