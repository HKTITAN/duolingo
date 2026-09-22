---
name: duo-return-triggers-one-signal-ambient-surface
summary: A surface outside your app gets a sub-second glance, so give it exactly one state-of-risk variable.
metadata:
  internal: true
---

# One-Signal Ambient Surface

## Concept

An ambient surface — a home-screen widget, a lock-screen complication, a watch face, a status tile — is read in under a second and is never navigated. The viewer is not there to explore; they are passing over it on the way to something else. That budget buys you exactly one variable. A surface carrying one unambiguous state converts a glance into an action. A surface carrying four converts it into passive reading, which is how most widgets die quietly on a second screen.

## What Duolingo does

Source: blog.duolingo.com/widget-feature (Duolingo blog, 2023-08-29; accessed 2026-09-22)

- The widget shows exactly two things — the current streak number, and whether today's lesson is already done. Nothing else.
- User research and feature testing confirmed that reminding someone of the streak and whether it was at risk was sufficient on its own. The team deliberately declined to add more stats or surrounding context.
- **Half of learners with the widget installed have a streak of at least 6 months.**
- It took **more than a year** from hackathon prototype to launch — iOS in **July 2022**, Android in **March 2023**. An ambient surface is a platform project, not a screen.
- Tension the post concedes itself — widget installers self-select as more committed. Duolingo states the retention lift survived controlling for that, but the raw "half have a six-month streak" figure overstates the causal effect. Treat installer numbers as an upper bound until you run a holdout.

## The transferable pattern

Pick the single variable that answers "do I need to act right now?" and put only that on the ambient surface.

1. **One state, not a dashboard.** The variable should be binary or near-binary at a glance — done or not done, safe or at risk, over or under. If the viewer has to compare two numbers to decide, you have spent a second you did not have.
2. **Risk beats progress.** Cumulative totals are pleasant and inert. A value that can be lost today produces an action today.
3. **Mirror the in-app state exactly.** An ambient surface that lags or disagrees with the app teaches people to stop trusting it, and an untrusted surface is worse than no surface.
4. **Budget it as infrastructure.** Multiple platforms, background refresh, sizing variants, and a stale-data story. Scope it like a service, not a component.
5. **Measure against a holdout, not against installers.** The people who add your surface are your best people already.

## Apply to your product

- If your users could see one number from your product without opening it, which one would change what they do in the next ten minutes?
- Is that number something they can lose, or only something they have accumulated?
- What would your install-cohort retention look like against a randomized holdout rather than against non-installers?

## See also

[[ask-for-permission-at-an-earned-peak]] · [[piggyback-an-existing-high-frequency-trigger]] · [[../duo-retention/references/streak-freeze]]
