---
name: duo-experiment-velocity-marginal-cost-decides-which-ideas-get-tested
summary: Test volume is set by the cost of the marginal test, and that cost quietly selects which ideas are allowed to be tested at all.
metadata:
  internal: true
---

# Marginal Cost Decides Which Ideas Get Tested

## Concept

A team's experiment volume is not a measure of how much it values experimentation. It is a measure of what one more experiment costs. The second-order effect matters more than the first. When a test costs days of setup, nobody says out loud that speculative ideas are banned — they just spend the scarce slots on the ideas they already believe, because those are the ones worth the effort. That is precisely the population of ideas least likely to teach anyone anything, since a confirmed belief changes no decision. Drive the marginal cost toward a form and a line of code and the portfolio shifts on its own — long-shot ideas become rational to test, and the expected information per test goes up even as the hit rate goes down.

## What Duolingo does

Source: blog.duolingo.com/life-at-duolingo-julie-wang (Duolingo blog, 2023-09-15; accessed 2026-09-22)

- A Duolingo iOS engineer describes running an A/B test as **filling out a quick form online and adding a one-line definition in any codebase**, including the iOS client. The unit of work for starting an experiment is a form field, not a project.
- The same account describes the supporting environment — backend staging servers presented as near-perfect simulations of production, with a client debug setting that routes a local build's traffic to a chosen staging server. Cheap tests depend on being able to exercise a variant end to end without a release.
- The output of that cost structure is the volume other Duolingo posts report — **750+ A/B tests per quarter as of 2025**, with a few hundred live at once in a given week (blog.duolingo.com/improving-duolingo-one-experiment-at-a-time (Duolingo blog, 2020-01-10; accessed 2026-09-22)).
- The low cost is paired with a rule that keeps it from degrading into churn — a hypothesis is required even for the smallest changes. PMs form and test one for anything from a copy change upward, which is how the habit survives on low-stakes work, where habits are actually formed (blog.duolingo.com/why-i-interned-at-duolingo-rebecca-hu-product-management-intern (Duolingo blog, 2022-08-26; accessed 2026-09-22)).
- A related growth rule pushes in the same direction and carries an honest gap. Duolingo's stated guideline is not to pull your punches — if a version is strictly better than what exists, launch it and improve it with follow-up tests rather than holding it back to perfect it first. The rule offers no guidance for the common case where a change is better on one axis and worse on another, which is most changes (blog.duolingo.com/growth-principles (Duolingo blog, 2023-11-03; accessed 2026-09-22)).

## The transferable pattern

- **Measure the cost, not the intent.** Time the next test from decision to live. That number, not your stated values, predicts how many you will run next quarter.
- **Watch what the cost selects for.** When slots are scarce, teams spend them on ideas with an internal advocate. Expensive tests therefore produce a portfolio of confirmations, and the portfolio looks healthy from the inside.
- **Aim for a form plus one line.** Anything more than that and the owner starts asking whether the idea is worth it, which is the exact filter you do not want applied to speculative bets.
- **Non-production environments are part of the cost.** If a variant can only be exercised by shipping it, your marginal cost includes a release cycle no matter how good the assignment tooling is.
- **Cheap is not free — keep one piece of friction.** A required written hypothesis costs a sentence and prevents the volume from turning into a stream of unread results nobody can interpret afterwards.
- **A strictly-better version should ship and iterate, not wait.** The imperfect version starts compounding today; reserve the debate for changes that trade one dimension against another.

## Apply to your product

- Time your last three experiments from "we should try this" to "it is collecting data." What was the largest single block of that time, and is it the same block every time?
- List the ideas your team has discussed but not tested this quarter. How many were skipped because they seemed unlikely rather than because they were unimportant?
- If a test cost twenty minutes to launch, which currently unthinkable idea would you try first — and what does it cost you to not know that answer?

## See also

[[experiments-as-shared-infrastructure]] · [[take-the-domain-owner-off-the-engineering-queue]] · [[../duo-experimentation/references/hypothesis-design]] · [[../duo-experimentation/references/ship-and-iterate]]
