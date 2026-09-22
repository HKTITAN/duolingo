---
name: duolingo-chains
summary: Ordered skill sequences for jobs that span three or more skills — a retention rescue, a new feature, a launch, a curriculum, an AI feature, a rebuild.
metadata:
  internal: true
---

# Chains — ordered routes for whole jobs

## Concept

A single question routes to one skill ([[../duolingo/SKILL]]). A real job — "fix our retention", "launch this", "teach users to do X" — spans several, and **the order matters**. Running gamification before you know why people leave decorates a leaking bucket. Writing copy before the mechanic exists writes copy for a thing that will change.

These are orderings, not checklists. Skip a link that doesn't apply; don't reorder them.

**What counts as spanning.** Use a chain when the user asked for an end-to-end artifact — a feature, a launch, a curriculum, a rescue — not when a question merely touches several topics. "What's a good streak freeze count" touches four skills and is still one node.

## What Duolingo does

Duolingo's published sequence on its own metric problem ran: define what "good" means → change the metric → re-price the currency feeding it → then ship features against the new number. They changed the measurement *before* the features, which is why the features pointed the right way. Reversing it produces motion without direction. Source: blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22).

## The transferable pattern

### "People sign up and disappear"

`duo-retention` (find the drop-off day and its shape) → `duo-difficulty-calibration` (is the first session mis-targeted?) → `duo-adoption-design` (do they ever reach the value?) → `duo-return-triggers` (cause the next session) → `duo-experimentation` (prove it moved)

**Check frequency before any of it.** If the product is genuinely episodic — used twice a month by design — there is no retention problem to fix and a daily loop will only manufacture guilt.

### New feature, start to ship

`duo-product` (should this exist) → `duo-progression-design` **if** it teaches the user anything → `duo-gamification` if it needs a loop → [[design-handoff]] for the interface → `duo-voice` for every string → `duo-adoption-design` (will anyone start?) → `duo-experimentation` to gate the launch

### Launch / go-to-market

`duo-product` (the one claim) → `duo-growth` (how it spreads) → `duo-proprietary-data-reports` (what you already hold that earns coverage) → `duo-voice` (the words) → [[design-handoff]] (the surface)

Data before words is deliberate: what you can *prove* should decide what you *say*.

### Build a curriculum, course, or onboarding that teaches

`duo-progression-design` (sequence by what the user must do, and scaffold it) → `duo-rules-and-heuristics` (explain, or let them discover?) → `duo-attention-budget` (cap what competes per screen) → `duo-memory-and-decay` (plan for forgetting before launch) → `duo-efficacy-measurement` (embed pre/post now, not later) → `duo-learner-motivation` (lower the cost of being visibly bad at it)

Measurement goes in during construction. Bolted on afterward, it measures whatever was convenient rather than whether the thing worked.

### Ship an AI / LLM feature

`duo-ai-product-strategy` (is a model the right tool here?) → `duo-llm-feature-engineering` (scope the prompts, plan the evals) → `duo-ai-agent-platform` if more than one agent will run → `duo-experimentation` (quality gate) → `duo-voice` (what it says when it fails)

### "We can't ship fast enough"

`duo-experiment-velocity` (what is the binding constraint — usually release cycle or environment cost) → `duo-backend-architecture` or `duo-mobile-engineering` (whichever owns that constraint) → `duo-culture` (is it ownership, not tooling?)

### "It's slow / expensive / we don't know what it's doing"

`duo-production-reliability` (see it first) → `duo-backend-architecture` (the request path) → `duo-infra-cost-efficiency` (attribute the spend)

Never optimize before you can observe. You will speed up the wrong thing and have no way to know.

### Enter a new market or audience

`duo-category-entry` (where to attack, and is the beachhead real?) → `duo-localization` (language, script, market reality) → `duo-inclusive-access` (device, bandwidth, credentials) → `duo-growth` (distribution there) → `duo-motivation-segmentation` (why *these* users came)

### Fix the number the company is graded on

`duo-metric-design` (choose and weight it) → `duo-score-credibility` if outsiders see it → `duo-growth-model` (which lever actually moves it) → `duo-experimentation` (hold the line on causality)

### Fix a team, not a product

`duo-culture` → `duo-product` (is the roadmap the real problem?) → stop. Do not route a team problem into a feature.

## Rules

1. **Each link is a read, then an application** — enter, apply its values to the work in hand, move on. Don't summarize the chain back to the user.
2. **Never run a chain on a one-line question.** See the spanning test above.
3. **[[translate]] applies at every link**, not at the end. A chain that ends in Duolingo's product instead of the user's has failed at every step, not once.
4. **If a diagnosis link comes back empty, stop the chain.** No drop-off found means the retention chain has nothing to fix; say so rather than continuing into gamification to finish the sequence.

## Apply to your product

- For your last cross-functional job, what was the real order — and what got done too early and thrown away?
- Which of your steps is a diagnosis everyone skips because the fix feels more productive?

## See also

[[overlaps]] · [[map]] · [[translate]] · [[design-handoff]]
