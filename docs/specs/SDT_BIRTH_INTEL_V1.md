# SDT Birth Intel V1

## Goal

Improve born-repo truth quality at creation time so a fresh repo starts closer to reality before manual cleanup.

## Why

Fresh-specimen proof now shows:

- advisory hooks work
- explicit cross-repo truth refresh works
- application repos can infer correctly after refresh

But birth output still has gaps:

- placeholder-like INSTALLATION text
- latest_tag unknown on fresh repos
- README/operator shell drift
- initial repo_type/language/run/test inference still needs stronger first-pass quality

## Scope

1. tighten birth-time project intel weighting
2. reduce placeholder leakage in born docs
3. improve first-pass run/test command inference
4. evaluate optional first trusted-floor tag on fresh repo birth

## Success criteria

- fresh hello-world specimen births with Python favored immediately
- run/test command inference is sensible before manual cleanup
- INSTALLATION placeholder warnings are reduced or gone
- README/operator shell drift is reduced
