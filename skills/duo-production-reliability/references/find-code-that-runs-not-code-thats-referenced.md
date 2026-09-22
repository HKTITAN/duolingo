---
name: duo-production-reliability-find-code-that-runs-not-code-thats-referenced
summary: Static analysis finds unreferenced code; only runtime instrumentation finds code that is referenced but never executes, which is where finished experiments leave their residue.
metadata:
  internal: true
---

# Find the code that runs, not the code that is referenced

## Concept

Static analysis answers "is this symbol referenced anywhere." In a product where the server decides what the client does, that question has stopped being useful. Every concluded A/B test leaves a losing branch that is still wired up. Every remote config flag leaves a path that compiles, links and is referenced but has not executed in production for a year. The only instrument that distinguishes shipped-and-used from shipped-and-dead is the running product itself. And the argument for doing the cleanup matters as much as the detection: framed as maintenance velocity it loses every prioritization contest, because the benefit accrues to the team rather than to anyone the company measures.

## What Duolingo does

Source: blog.duolingo.com/emerge-tools-reaper (Duolingo blog, 2024-09-27; accessed 2026-09-22)

- Progression of methods: delete files and see what breaks, then static analysis with Periphery, then runtime instrumentation — Emerge Tools' Reaper, integrated in **one line of code** into every beta build from **version 7.7.0 in January 2024**.
- The critical methodological move: they **union the reports across all released versions** rather than trusting any single build. A single version produces false positives from new classes whose A/B tests have not activated yet, and from rarely reached flows such as course completion.
- Numbers: **2,684 unused classes out of 8,567 monitored**. Two cleanup passes removed **over 10,000 lines, nearly 1% of the codebase**, in single commits of **6,876 and 3,873 lines**. Four entire exercise types turned out never to be used. The iOS codebase is roughly **20x larger than ten years ago**.
- The framing that funded the work: less code means smaller app size, which matters most for users in areas with **lower connectivity** — plus the point that unreferenced code still costs review time every time a dependency changes.
- Tension: even after cross-version filtering, some classes looked used only because beta users rarely reach certain flows. The output is a **review queue, not a delete script**. Duolingo treats human review as part of the method.

## The transferable pattern

1. **Instrument the running system, not the source tree.** If anything outside your binary decides which branch executes — a flag service, an entitlement, a rollout percentage — reachability in source is not evidence of use.
2. **Union across versions and across time.** One build's data is a snapshot of one population. Dead code is what is absent from every window, not from the current one.
3. **Expect the residue to be concluded experiments.** The losing arm of a finished test is the single richest source of code that looks alive and is not.
4. **Change the ledger the work is judged on.** Argue deletion on the metric your company already funds — download size, cold start, install conversion where bandwidth is scarce — not on developer comfort. Same work, different budget line.
5. **Keep a human between the report and the delete.** The instrument is a prioritized suspect list. Treating it as ground truth is how you remove the flow only 0.3% of people reach.

## Apply to your product

- What fraction of your codebase is gated behind a remote switch? That fraction is the part static analysis cannot reason about at all.
- When you concluded your last three experiments, who deleted the losing branch, and can you prove it?
- If you had to justify a two-week cleanup to someone who only tracks acquisition or revenue, which number would you put the work on?

## See also

[[sampled-tracing-versus-request-identity]] · [[a-dated-public-moment-funds-the-rebuild]] · [[../duo-experimentation/SKILL]]
