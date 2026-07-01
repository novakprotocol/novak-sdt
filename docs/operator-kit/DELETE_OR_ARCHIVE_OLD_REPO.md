# Delete Or Archive Old Operator Kit Repo

## Old repo

`novakprotocol/novak-sdt-operator-kit`

## Current recommendation

Prefer archive first. Delete only if the owner explicitly wants permanent removal.

## Preconditions

Before archiving or deleting the old repo, confirm:

- `kits/operator-kit/` exists in `novakprotocol/novak-sdt`.
- The consolidation PR is merged.
- N-SDT checks passed or any blockers are recorded.
- The owner agrees the old repo is no longer needed as a separate repo.

## Option A — Archive old repo

PowerShell:

```powershell
gh repo archive novakprotocol/novak-sdt-operator-kit --yes
```

## Option B — Delete old repo

PowerShell:

```powershell
gh repo delete novakprotocol/novak-sdt-operator-kit --yes
```

## Authentication helper

If GitHub CLI prompts for authentication:

```powershell
gh auth login
```

Then rerun the archive or delete command.

## Warning

Deletion is destructive. Archive keeps the old repo available as historical evidence while making clear that active work moved into `novak-sdt`.
