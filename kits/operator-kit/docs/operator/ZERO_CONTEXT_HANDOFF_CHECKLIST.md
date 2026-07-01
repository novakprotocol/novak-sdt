# Zero-Context Handoff Checklist

## Purpose

Use this when handing a repo or project to another human or AI with minimal prior context.

## Required identity

- Project name
- Repo name
- Branch
- Head commit
- Date
- Operator
- Environment / host

## Required reality block

### Verified

What is proved now.

### Likely

What seems true but is not fully proved.

### Assumed

What the next operator should verify first.

### Not evidenced

What is unknown, stale, blocked, or unverified.

## Required operational block

- Exact next command block
- Exact step after that
- Files touched
- Blockers
- Risks
- Rollback point

## Required reading order

1. `WHAT_IS_REAL_NOW.md`
2. `PROJECT_STATE.md`
3. Latest operator docs
4. Latest decision docs
5. Latest execution/status docs if present

## Stop rule

A handoff is incomplete if the next operator cannot tell:

- where they are
- what is real
- what to run next
- what could break
