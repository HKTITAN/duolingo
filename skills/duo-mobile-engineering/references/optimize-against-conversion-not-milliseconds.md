---
name: duo-mobile-engineering-optimize-against-conversion-not-milliseconds
summary: Score performance work by conversion through the step, then promote that number to a company-wide guardrail so no other team can quietly spend it.
metadata:
  internal: true
---

# Optimize Against Conversion, Not Milliseconds

## Concept

Latency is a proxy, and a leaky one. A 300ms improvement may change no behaviour at all; a 3-second one may change everything. If you grade performance work on milliseconds you will ship wins that move nothing and kill projects that would have moved a lot, because you never measured the thing you were actually buying — did the user get through the step.

The second half matters more than the first. Performance is a commons: every team can spend it, none of them are charged for it, and it erodes by a hundred small increments that each looked reasonable in isolation. A conversion metric that only the performance team watches is a report. A conversion metric promoted to a guardrail — so every other team's experiment is blocked from regressing it — is a budget.

## What Duolingo does

Source: blog.duolingo.com/android-app-performance (Duolingo blog, 2025-06-11; accessed 2026-09-22)

- Duolingo picked **conversion on three journeys** — app open, session start, session end — over raw startup latency as the optimization target, and prioritized app open first for top-of-funnel impact.
- Conversion here is literal: of the users who tapped the icon, what fraction actually reached the home screen rather than abandoning mid-launch.
- **App open conversion was made a company-wide guardrail metric**, so any team's experiment that regresses it is caught, regardless of which team's code did the regressing.
- Volume of the effort: **200+ A/B tests on Android performance in 2024**.
- Result on entry-level devices: app open conversion moved **91% to 94.7%**, and the share of entry-level users waiting **5+ seconds fell from 39% to 8%**. The company counted **hundreds of thousands of DAU gained**.

The tension worth keeping: a guardrail is a tax on everyone else's velocity. Every team now has an extra way to fail an experiment readout for a reason unrelated to their hypothesis. Duolingo accepted that cost because the alternative — polite quarterly reminders that the number is drifting — had already failed.

## The transferable pattern

1. **Define the step, then define conversion through it.** Not "time to interactive" but "of the people who started this, what fraction finished." It is the same number your product managers already argue about, which is exactly why it works as a shared currency.
2. **Rank steps by traffic, not by how bad they feel.** The worst-feeling screen is often deep in the funnel where few people are. The first step is where everyone is.
3. **Promote the winner to a guardrail.** One number, watched on every experiment, owned by nobody's roadmap. Without this, the next three quarters of feature work quietly undo what you just bought.
4. **Expect diffuse, numerous wins.** Hundreds of small tests, not one heroic rewrite — which is only affordable if your measurement loop is cheap. See [[fix-the-diagnostic-loop-before-the-bug]].

## Apply to your product

- Which single step in your product has the most users passing through it, and what fraction of them currently complete it? If you cannot answer in one query, that is the first fix.
- If you shaved 20% off your slowest screen tomorrow, what number would you show a skeptical executive — and would it move enough to be distinguishable from noise?
- Who is allowed to regress your performance today without anyone noticing, and what would it take to make that regression block their launch instead?

## See also

[[cold-start-is-a-retention-metric]] · [[attack-perceived-time-before-actual-time]] · [[../duo-experimentation/references/guardrail-metrics]]
