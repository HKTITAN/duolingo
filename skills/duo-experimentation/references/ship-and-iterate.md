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

Duolingo's growth guidelines name this anti-pattern outright: **don't pull your punches.** If you have a good new feature but want to change things about it, don't shut it down to tweak and re-test. If the imperfect version is *strictly an improvement* over what exists, launch it to new users — that starts the compound gains — and make the improvements through follow-up experiments. Source: blog.duolingo.com/growth-principles (Duolingo blog, 2023-11-03; accessed 2026-09-22)

- **The companion rule is symmetric:** decide as soon as you're confident you have the data. Letting a finished experiment sit on the back burner "collecting more data" is the same mistake with the sign flipped.
- Reversibility is the relevant axis. Easily-reversed changes can ship and be measured in production; hard-to-reverse changes need testing.
- Ordering matters for the same reason — Duolingo prioritizes high-ROI experiments first because an earlier launch pays compound interest for longer.

**The limit is written into the rule itself.** It only licenses shipping when the version is *strictly* an improvement. It says nothing about the case that actually generates the arguments — better on one axis, worse on another — and treating it as general permission to ship rough work is a misreading.

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
