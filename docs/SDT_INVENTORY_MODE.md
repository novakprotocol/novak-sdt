# SDT Inventory Mode

## Purpose

Inventory mode captures what a serious server or infra repo is actually running on.

This is the runtime truth layer for:
- packages
- services
- processes
- listening ports
- filesystems
- memory
- network identity
- pending updates

## Output

A snapshot writes:

- `docs/status/inventory/<label>/inventory.json`
- `docs/status/inventory/<label>/INVENTORY_SUMMARY.md`
- raw text captures under `docs/status/inventory/<label>/`
- `docs/status/LATEST_INVENTORY.json`
- `docs/status/INVENTORY_LEDGER.ndjson`

## Main command

```bash
bash bin/sdt-inventory-snapshot.sh <repo_path> <label>
```

## Recommended use

Take one snapshot:
- before bootstrap
- before install
- after install
- after major change

Then compare those snapshots in Git.
