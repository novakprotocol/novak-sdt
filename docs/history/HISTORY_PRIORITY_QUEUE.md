# History Priority Queue

- stamp_utc: 2026-04-19 18:55:19 UTC

## Items
- Tighten project intelligence scan hygiene by excluding .venv, node_modules, caches, site, build, dist, and other generated noise.
- Weight runtime/language inference toward application code, imports, manifests, and entrypoints instead of shell wrappers.
- Force birth and baseline to run truth refresh immediately after floor creation.
- Generate or refresh change records automatically when meaningful repo mutations happen without a matching change document.
- Track trusted floor explicitly when HEAD moves past the latest tag.
- Append attempt records automatically from truth-refresh and proof runs.
