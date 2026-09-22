---
name: duo-mobile-engineering
description: Make a shipped client app start fast, stay small, and stay cheap to change — startup budgets scored against conversion rather than milliseconds, deferring non-first-screen work, perceived versus actual latency, device-tier and worst-region equity, profiling loops, binary size as a monitored metric, and how to migrate a large client codebase without freezing the product. Use when someone says the app feels slow, cold start takes too long, our binary keeps growing every release, users on cheap Android phones churn, CI builds take forever, should we migrate to a new language or architecture, how do we pay down client tech debt, who owns deleting legacy code, or why did our performance work not move a single metric.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo Mobile Engineering — Map of Content

Performance work fails in a predictable way: it gets filed as polish, funded as polish, measured in milliseconds nobody can connect to behaviour, and then quietly undone by the next four quarters of feature work. The same is true of client tech debt — the cleanup that is nobody's job never happens.

This skill collects the moves that break that cycle: tie speed to a conversion number someone is accountable for, make the measurement loop cheap enough that you can be surprised, put regression deltas where changes are reviewed, and stage migrations so the expensive decision waits for evidence.

This skill is a **graph**: scan the descriptions, follow only the `[[wikilinks]]` you need.

**Boundary.** Server-driven UI — shipping interface changes without a release, the config/data split, client versioning, the server contract — is not here. That pain feels like an app-store problem but the answer is a backend one: [[../duo-backend-architecture/SKILL]]. Pixel craft (easing curves, token values, contrast, component props) is out of scope for this whole pack; route it to the external design-engineering skill.

## Measure the right thing

- [[references/optimize-against-conversion-not-milliseconds]] — score performance by conversion through the step, then make that number a company-wide guardrail.
- [[references/cold-start-is-a-retention-metric]] — startup is churn, not polish; precompute the warmup if you ship faster than it can mature.
- [[references/measure-from-your-worst-region-and-device]] — a check invisible at 20ms is a product-killing block at 1000ms, and payload size is a CPU cost.

## Buy back the milliseconds

- [[references/defer-everything-the-first-screen-doesnt-need]] — audit what runs before first render, push the rest past it, then codify deferral as a utility.
- [[references/attack-perceived-time-before-actual-time]] — render the screen you were going to show next and do the blocking work behind it.

## See what is actually happening

- [[references/fix-the-diagnostic-loop-before-the-bug]] — automate instrumentation and build the shareable trace viewer before you start optimizing.
- [[references/verify-the-harness-and-route-around-vendors]] — a green test on a differently-assembled artifact is a silent lie; file the vendor bug and ship your own workaround anyway.

## Stop the slow regressions

- [[references/put-the-size-delta-on-every-pull-request]] — gradual growth is a monitoring failure; attribute the delta to one diff at review time.
- [[references/treat-the-build-loop-as-a-shipped-feature]] — disjoint boundaries, cached prebuilt tooling, and finding which resource actually binds.

## Change a large codebase without stopping

- [[references/mandate-new-code-first-backfill-on-evidence]] — split the reversible commitment from the expensive one, and fund cleanup as a standing mandate.
- [[references/prove-the-shape-in-the-hardest-part-first]] — skeleton before slice; pilot a new architecture in your ugliest component before writing the guide.
- [[references/a-fixed-window-beats-a-trickle]] — concentrate mechanical migrations to collapse dual maintenance, but never freeze releases while you do it.
- [[references/generate-the-boilerplate-instead-of-relaxing-the-standard]] — fix the typing, not the rule; prefer representations that fail at compile time.

## Sibling skills

- [[../duo-backend-architecture/SKILL]] — where server-driven UI, client versioning and the data contract live.
- [[../duo-experimentation/SKILL]] — guardrail metrics and readouts; every performance win here was an A/B test.
- [[../duo-product/SKILL]] — whether the work is worth funding, and what "polished" means in review.
- [[../duo-culture/SKILL]] — ownership clarity and who is accountable for the code nobody wants to delete.

## Sources

Distilled from engineering posts on blog.duolingo.com, 2015–2025 — Android performance, baseline profiles, app size, the Kotlin migration, the 2021 Android reboot, iOS MVVM and macros, and CI build times. Each node carries its own dated citation.
