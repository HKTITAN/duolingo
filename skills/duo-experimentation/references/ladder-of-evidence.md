---
name: duo-experimentation-ladder-of-evidence
summary: Four methods with four different blind spots — interviews, controlled experiments, A/B tests, outcome studies — run continuously, not chosen between.
metadata:
  internal: true
---

# The Ladder of Evidence

## Concept

Teams argue about which research method is the real one. The argument is a category error: each method answers a question the others structurally cannot. Qualitative work finds desire but never effect size. A small controlled experiment establishes that a mechanism works but not that it survives your whole population. An A/B test measures in-product behavior but says nothing about whether the product does its job in the world. An outcome study answers exactly that, and is far too slow to steer a weekly decision. A team running only one rung mistakes its blind spot for an absence of risk.

## What Duolingo does

Duolingo runs all four rungs continuously rather than picking one. Source: blog.duolingo.com/how-duolingo-works-with-learners (Duolingo blog, 2022-04-04; accessed 2026-09-22)

| Rung | Method | What it settled |
|---|---|---|
| 1 | UX interviews | Produced Practice Hub — a need no dashboard surfaced |
| 2 | Small pre/post controlled experiment | Explicit grammar treatment: 36%→86% accuracy vs control 40%→54% |
| 3 | A/B tests at scale | "Hundreds of experiments" running at any given time |
| 4 | Third-party-assessed efficacy studies | Whether learners actually reach the claimed proficiency level |

Notice the direction of information flow. Rung 1 generates hypotheses that rungs 2 and 3 cannot invent, because instrumentation only sees behaviors that already exist in the product. Rung 4 audits the metric that rung 3 optimizes — it is the check on whether the proxy the whole experiment program is tuned against still points at the real thing.

Tensions worth keeping: rung 2 results come from small, heavily filtered populations and routinely shrink when they meet rung 3. Rung 4 studies run with university collaborators on a timescale of months to years, so they can only ever confirm or indict decisions that were already made — they cannot arbitrate this quarter's roadmap.

## The transferable pattern

Ask which rung a claim came from before you weigh it:

1. **Desire** — interviews, diary studies, support tickets. Tells you what to build. Never tells you how much it moves.
2. **Mechanism** — a small controlled comparison on a narrow, filtered population. Tells you the idea works in principle. Effect size is inflated.
3. **Survival** — a randomized test on everyone. Tells you what it is worth in production. Blind to anything happening outside the product.
4. **Terminal outcome** — an independent, external assessment of whether the product delivers its stated promise. Slow, expensive, and the only thing that catches a proxy that has drifted.

Rule: never let a rung-1 finding ship unmeasured, and never let rung 3 be your only evidence that the product works. Budget for rung 4 on a yearly cadence even though it will never inform a sprint.

## Apply to your product

- Which of the four rungs does your team not run at all, and what class of mistake does that leave uncaught?
- What was the last thing you built that came from a conversation rather than a dashboard?
- If your primary experiment metric quietly stopped correlating with the outcome you promise customers, how would you find out?

## See also

[[outcome-not-engagement]] · [[metric-selection]] · [[design-the-population]] · [[unmeasurable-wins]]
