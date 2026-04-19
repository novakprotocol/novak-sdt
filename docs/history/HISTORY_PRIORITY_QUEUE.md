# History Priority Queue

- stamp_utc: 2026-04-19 17:12:52 UTC

## Items
- Tighten project intelligence scan hygiene by excluding .venv, node_modules, caches, site, build, dist, and other generated noise.
- Recompute completeness and drift after writing managed sections so first-run reports reflect post-write truth, not pre-write gaps.
- Weight runtime/language inference toward application code, imports, manifests, and entrypoints instead of shell wrappers.
- Wire history intelligence into every serious SDT run so FAILURE_PATTERNS, MISSED_OPPORTUNITIES, and queues are continuously re-derived.
- Generate or refresh change records automatically when meaningful repo mutations happen without a matching change document.
- Track trusted floor explicitly when HEAD moves past the latest tag.
