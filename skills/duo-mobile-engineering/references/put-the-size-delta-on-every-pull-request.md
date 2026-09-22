---
name: duo-mobile-engineering-put-the-size-delta-on-every-pull-request
summary: Gradual regression is a monitoring failure — comment the metric delta on every PR with a threshold that routes large changes outside the owning team.
metadata:
  internal: true
---

# Put the Size Delta on Every Pull Request

## Concept

Slow regression is not an engineering failure, it is a monitoring failure. With hundreds of changes per release, a periodic report tells you the number moved but not which change moved it. Triage then costs more than anyone will pay, so the regression is accepted by default, every period, forever.

Attributing the delta to a single diff at review time changes the economics completely: the cost becomes visible while the author still remembers why they made the choice, and it is one person's decision rather than a team's archaeology. Broadcasting the largest deltas beyond the owning team is the second half — that is what converts a technical number into a product tradeoff conversation, because the team shipping the feature is rarely the team that feels the cost.

## What Duolingo does

Source: blog.duolingo.com/emerge-tool-app-size (Duolingo blog, 2023-07-14; accessed 2026-09-22)

- Duolingo had tracked iOS download and install size **in a spreadsheet since 2014** and watched it grow anyway: **a constant ~50MB per year from 2020**. Measurement without attribution changed nothing for nearly a decade.
- They switched to size analysis **on every GitHub PR**, posting a comment with the **base-vs-branch delta and per-file impact**, plus **Slack notifications for the largest increases** — deliberately routing big changes to an audience wider than the owning team.
- Total reduction achieved: **20%**. Assets were **32% of total app size**.
- The best find came from **comparing the same asset across platforms**: one screen's artwork shipped as a **1.6MB PDF on iOS and a 19KB asset on Android**. The cause was a gaussian-blur glow versus a radial-gradient glow — a vector effect that must be rasterized explodes, while the same visual as gradient stops is tiny. Changing the source file brought the PDF to **44KB**, and over **10MB** was saved across that family of images.
- They also ran a heuristic static analysis matching asset filenames against names referenced in code, finding and deleting **17MB of unused images**, and estimated a further **50MB** from a PDF-to-SVG migration. iOS **15 was made the minimum once 99% of users met it**.

Two tensions Duolingo names. The dead-asset analysis **produced false positives — assets deleted that were actually in use** — caught only by the public beta before release. And the decision to bundle **over 1,000 more images on iOS than Android** rather than download them is a deliberate size cost accepted to keep the app working offline and on poor connections.

## The transferable pattern

- **Attribute continuously, not periodically.** Any metric that drifts — artifact size, cold-start time, query count, dependency count, p95 — should be diffed per change and posted where the change is reviewed. A monthly report on a drifting number is a record of the drift, not a control on it.
- **Set a threshold that escalates outward.** Small deltas inform the author; large deltas need an audience that includes someone who will ask whether the feature is worth it.
- **Cross-compare equivalents to find the order-of-magnitude bugs.** Two implementations of the same thing that differ by 100x is a pipeline defect, not a platform cost — and the fix is usually upstream in the source file, not in your code.
- **Treat automated deletion as a proposal, not a decision.** Heuristic dead-code and dead-asset detection produces false positives; you need a staged release channel to catch them before users do.

## Apply to your product

- Which number in your product has grown every quarter for years while everyone agreed it was a problem? Why is it not on your pull requests?
- What threshold would make a regression somebody else's problem to approve rather than the author's to rationalize?
- Do you have two implementations of the same asset, query, or payload on different platforms? Put their sizes side by side today.

## See also

[[treat-the-build-loop-as-a-shipped-feature]] · [[measure-from-your-worst-region-and-device]] · [[../duo-experimentation/references/guardrail-metrics]]
