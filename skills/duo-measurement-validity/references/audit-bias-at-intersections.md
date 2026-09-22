---
name: duo-measurement-validity-audit-bias-at-intersections
summary: Bias can appear only at a combination of attributes and vanish when either is examined alone, so one-variable-at-a-time fairness analysis nets out the effects that matter.
metadata:
  internal: true
---

# Audit Bias at Intersections

## Concept

People belong to several categories at once, and a measurement can be unfair to a particular combination while looking clean on every attribute taken separately. Checking one variable at a time averages over the others, which nets out precisely the interaction effects you were auditing for. The standard fairness report — a table of one row per attribute, all green — is therefore compatible with real, large, systematic bias. Auditing at intersections is more sensitive and more expensive, and it never finishes, because a human built the instrument.

## What Duolingo does

Source: blog.duolingo.com/fairness (Duolingo blog, 2021-06-30; accessed 2026-09-22)

- The Duolingo English Test is taken in **207 countries and territories**, so its population spans combinations of attributes no single-variable audit covers.
- The testing industry's standard tool is Differential Item Functioning — checking whether a question behaves differently for one demographic group holding ability constant — and it is conventionally run **one variable at a time**.
- Duolingo's Assessment Research team, led on this work by psychometrician Dr. Will Belzak, replaced that with a **multidimensional, person-centric** method — how age affects responses *within* gender, and how responses vary by gender *within each age group* — so an effect that exists only at a combination is visible rather than averaged away. The method was published in **Psychological Methods**, an external peer-reviewed venue, rather than kept as an internal practice.
- Duolingo states the limit rather than claiming the problem solved — because humans create tests, bias can never be escaped entirely. The method makes detection more sensitive and correction more strategic; it does not make the instrument fair.
- The cost, which any team adopting this will hit immediately: intersecting attributes multiplies the number of cells and shrinks each one. Small cells mean low power on the comparisons that matter most and a rising rate of false alarms across the many comparisons you are now running. Sensitivity is bought with sample size and with a plan for multiple comparisons, not for free.

## The transferable pattern

- **Audit combinations, not columns.** If your fairness report has one row per attribute, it can only detect bias that is uniform across every other attribute — the least interesting kind.
- **Pick the intersections before you look.** Name the combinations you have reason to worry about, from support tickets, from who churns, from who your training data under-represents. Testing every intersection post hoc guarantees findings that will not replicate.
- **Report cell sizes next to every effect.** An intersection with too few cases is not evidence of fairness; it is an absence of evidence, and the two get conflated constantly.
- **Publish the method externally if the stakes justify it.** A method that has survived outside review is a much stronger answer to an accusation than a method that has only survived your own team.
- **State the residual.** An audit that concludes "no bias found" is not credible. One that concludes "these intersections were checked at this power, these were too small to check, and here is what we corrected" is.

## Apply to your product

- Which two user attributes, combined, describe a group your training data or your test population barely contains?
- If your model or your scoring rule were unfair to that specific combination, which dashboard would move — and would anyone read it as a fairness problem rather than as noise?
- What is the smallest intersection you currently report a result for, and do you know its sample size off the top of your head?

## See also

[[classifier-categories-encode-their-training-population]] · [[../duo-inclusive-access/references/audit-fairness-against-the-delivery-context]] · [[../duo-experimentation/references/guardrail-metrics]]
