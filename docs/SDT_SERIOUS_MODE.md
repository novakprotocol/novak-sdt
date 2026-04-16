# SDT Serious Mode

Serious mode adds execution receipts to SDT.

## Output artifacts

A serious-mode run writes:

- `docs/status/run-receipts/<run_id>/run.json`
- `docs/status/run-receipts/<run_id>/run.md`
- `docs/status/run-receipts/<run_id>/stdout.log`
- `docs/status/run-receipts/<run_id>/steps.log`
- `docs/status/LATEST_RUN.json`
- `docs/status/RUN_LEDGER.ndjson`

## Main command

```bash
bash bin/sdt-serious-run.sh <repo_path> <day_number> <run_label> <run_body_script>
```

## Rule

Serious mode does not replace Git.
It complements Git with execution receipts.
