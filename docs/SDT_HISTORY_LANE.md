# SDT History Lane

## Purpose

The SDT History Lane preserves the execution history of a repo as first-class project truth.

It is intended to keep:

- successful runs
- failed runs
- raw transcripts
- archived run scripts
- normalized attempt records
- failure pattern summaries
- missed-opportunity summaries

## Why it matters

Without a history lane, valuable execution knowledge is lost in:

- terminal scrollback
- pasted logs
- temporary notes
- operator memory
- chat history

With a history lane, the repo keeps a durable record that can later support:

- handoff
- replay
- audit
- charting
- AI analysis
- missed-opportunity review
- playbook refinement

## Files

- `bin/history-import.sh`
- `tools/archive_history_log.py`
- `docs/history/ATTEMPTS.ndjson`
- `docs/history/HISTORY_INDEX.md`
- `docs/history/FAILURE_PATTERNS.md`
- `docs/history/MISSED_OPPORTUNITIES.md`

## Current scope

This adds the history lane to SDT core itself.

It does not yet prove that every future born repo automatically receives this lane by default.
That birth-path integration is the next step.
