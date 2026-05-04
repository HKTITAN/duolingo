---
name: duo-experimentation-ship-and-iterate
summary: When "good enough to ship" beats "perfect to test"; the line between testing and stalling.
metadata:
  internal: true
---

# Ship and Iterate

## Concept

A culture obsessed with experimentation can become a culture afraid to ship. Every change becomes a test; every test takes time; nothing actually moves. The discipline is knowing when to test (decisions with high uncertainty and reversible cost) and when to ship (decisions with low ambiguity, low cost to revert, or where the test would take longer than the iteration loop).

This is the *Ship It* principle of the handbook applied to experimentation specifically.

## What Duolingo does

- Not every change is tested. Bug fixes, copy improvements, obvious quality-of-life wins ship.
- Tests are reserved for decisions where the team's prior is genuinely uncertain or the stakes are high.
- The decision *whether* to test is made fast — debating "should we test this" for a week defeats the purpose.
- Reversibility is the relevant axis. Easily-reversed changes can ship and be measured in production; hard-to-reverse changes need testing.

## The transferable pattern

A useful matrix:

| | Low cost to revert | High cost to revert |
|---|---|---|
| **High uncertainty** | Ship and monitor | Test |
| **Low uncertainty** | Ship | Ship (and align well first) |

Three rules:

1. **Test for uncertainty, not for permission.** Testing as a gate to ship is bureaucracy. Testing as a way to resolve genuine team disagreement is leverage.
2. **Reversibility unlocks shipping.** If you can roll back in an hour, the test threshold is much lower than if you can't.
3. **Consider the test's own cost.** A two-week test on a one-day change is upside-down. Sometimes shipping and reading the data is the experiment.

Anti-pattern: testing every change because "we're a Show-Don't-Tell culture." That's *Show Don't Tell* misread; the principle is to use evidence to *decide*, not to require evidence before deciding anything.

## Apply to your product

- What was the last change your team tested that you'd now agree could have just shipped?
- What's currently in your "we should test it" backlog that's actually a "we should ship it"?
- Where does test-vs-ship decision-making slow you down?

## See also

[[show-dont-tell]] · [[novelty-effects]] · [[kill-criteria]] · [[../duo-product/references/ship-it]] · [[../duo-product/references/ruthless-prioritization]]
