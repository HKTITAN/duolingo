---
name: duo-ai-product-strategy
description: Decide where to point AI so it changes your cost structure instead of adding a feature — which bottleneck absorbs the automation budget, how to divide labor between expert staff and models, when to adopt a capability that is still visibly bad, and how to make AI-produced output trustworthy enough for a skeptical or regulated buyer. Use when someone asks "should we build this with AI at all", "what is our AI strategy", "where do we actually apply AI", "will this be a moat or just a feature", "how do we automate content production without wrecking quality", "which work stays human", "is it too early to adopt this", "how do we get enterprise or regulated customers to accept AI output", or "what is the real ML problem behind this bottleneck". Distilled from Duolingo's public posts on the English Test, LLM-assisted content, and expert-plus-AI pipelines.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Duolingo AI Product Strategy — Map of Content

Most AI roadmaps are lists of features. Duolingo's public record reads differently — the model gets pointed at whatever makes the incumbent expensive, at whichever internal constraint gates everything else, and at the stages of a pipeline where errors are local and cheap. This skill packages that judgment for products that have nothing to do with language learning.

This is a **graph**. Scan the descriptions, follow only the `[[wikilinks]]` you need.

Where this skill stops: it answers "build it, here, for this reason." Making the model behave once built — prompting, decomposition, memory, evals, verification, agent permissions — belongs to the sibling skill `duo-llm-feature-engineering`.

## Where to aim

- [[references/attack-the-incumbents-physical-bottleneck]] — when a competitor's guarantee rests on scarcity, generation dissolves their whole cost structure, and you must re-supply the guarantee you deleted.
- [[references/point-ai-at-unit-economics-not-features]] — steps, authoring and evaluation are the three cost lines worth attacking; a feature is copied in a quarter, a cost structure is not.
- [[references/spend-the-automation-budget-on-the-gate]] — find the one constraint everything queues behind, and justify the spend by the work it unlocks rather than by throughput.

## Getting the problem right before you build

- [[references/name-the-real-ml-problem-first]] — your objective is often not the one the off-the-shelf model was trained for; state it as a scoring function first.

## Dividing the labor

- [[references/stage-split-humans-set-constraints-models-multiply]] — split the pipeline by stage, not by product, with a monotonic human-to-model gradient.
- [[references/author-a-pool-deliver-an-instance]] — make the unit of authorship larger than the unit of delivery, so personalization costs a lookup instead of a headcount.

## Timing and discipline

- [[references/adopt-early-gate-on-your-own-quality-bar]] — buy the integration years while quality improves on someone else's budget, but only against a bar you defined before the tool existed.
- [[references/simplify-until-automatable-name-what-must-survive]] — name the one thing the feature must keep doing, standardize the rest, and schedule the sameness you just bought.

## Sibling skills

- [[../duo-product/SKILL]] — the long-view product judgment these bets sit inside.
- [[../duo-experimentation/SKILL]] — every quality claim here was an experiment or an efficacy study before it was a strategy.
- [[../duo-culture/SKILL]] — the talent-density math behind "fewer than 1,000 people, 21 million daily users."
- [[../duo-growth/SKILL]] — what a cost-structure advantage lets you do in the market once you have one.

## Sources

blog.duolingo.com posts on the Duolingo English Test, LLM-assisted course content, expert-plus-AI pipelines, DuoRadio scaling, responsible-AI standards and company strategy (2020-2026), all cited with dates inside the nodes.
