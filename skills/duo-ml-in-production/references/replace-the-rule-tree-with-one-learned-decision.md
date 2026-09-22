---
name: duo-ml-in-production-replace-the-rule-tree-with-one-learned-decision
summary: Years of won A/B tests compound into branching logic nobody can reason about — replace the whole tree with a single learned decision.
metadata:
  internal: true
---

# Replace the Rule Tree With One Learned Decision

## Concept

Every successful experiment leaves a condition behind, and almost none are ever removed — deleting a winning branch feels like handing back a win. Over a few years the decision fragments across the codebase into a tree no single person can hold in their head, whose original authors have left, and where any new change might collide with a rule nobody can explain.

That tree looks like a record of wins. It is a liability wearing the costume of one. You cannot optimize a system you cannot reason about, and each marginal experiment on top of it gets slower and less trustworthy. At some point the correct move is not another branch — it is deleting all of them and letting one learned decision consume the same inputs.

## What Duolingo does

Source: blog.duolingo.com/machine-learning-ads (Duolingo blog, 2025-03-18; accessed 2026-09-22)

- By 2023 the post-session ad decision — show the in-house subscription ad, or an external network ad — had become a tangled decision tree split across parts of the codebase, the accumulated residue of years of A/B tests.
- They collapsed the whole tree into one ML call and let the model decide.
- The replacement produced **millions of dollars in incremental annual revenue within the first few months**, growing to **tens of millions per year** after refinement.
- That decision space became Duolingo's **largest revenue source**, driving roughly **a quarter of year-over-year revenue growth**.
- **The tension is in the approval, not the model.** Leadership initially refused. The first version only optimized a single screen, so the upside was capped, and an ML system carries permanent maintenance cost. The proposal cleared the bar only once it was rescoped to require almost no new infrastructure.

## The transferable pattern

A branching rule set is worth replacing with a learned decision when three things are true at once:

1. **The branches share one objective.** Every condition is ultimately answering the same question, just badly and in pieces. If the branches serve genuinely different goals, you have a design problem, not a modeling problem.
2. **Nobody can predict the output.** If a competent engineer cannot say what the system will do for a given input without tracing code, the tree has exceeded human working memory and its behavior is now emergent.
3. **You already log the inputs and the outcome.** This is what makes the swap cheap. The learned version needs no new pipeline — it reads the same signals the branches read, and the outcome you were already measuring becomes the label.

Scope the first version to need no new infrastructure, even at the cost of capped upside. A capped win that ships beats an uncapped one that does not clear the funding bar — and once the call site exists, widening its inputs is an increment rather than a project.

Budget for the standing cost honestly. A rule tree is free to leave alone; a model needs monitoring, retraining and an owner. If the decision is made rarely or the payoff per decision is small, keep the rules and delete the dead branches instead.

## Apply to your product

- Which decision in your system has accumulated the most conditions, and when did someone last remove one rather than add one?
- Can you state, without reading code, what that decision will output for a given input? If not, who can?
- Are the inputs and the outcome of that decision already logged together? If they are, the learned replacement is an integration; if they are not, logging them is the real first project.

## See also

[[rank-the-noise-dont-filter-it]] · [[pick-the-metric-sensitive-where-users-care]] · [[../duo-experimentation/SKILL]]
