---
name: duo-memory-and-decay-reactivate-dont-restart
summary: A returning user is not a new user; forgotten capability is inaccessible, not destroyed, so probe for the residue instead of resetting them to zero.
metadata:
  internal: true
---

# Reactivate, Don't Restart

## Concept

The default reactivation flow hands a returning user the beginner path. It is the easiest thing to build — the onboarding already exists — and it throws away the single biggest asset that user has.

Forgotten material is inaccessible, not destroyed. The classic demonstration is the savings paradigm: relearn something you once knew and it comes back measurably faster than it went in the first time, even when a direct test of recall scores you at zero. The substrate outlives the performance. So the cost to rebuild is nothing like the cost to build, and a flow that charges the rebuild price of a first build is both wasteful and insulting — the returner can feel that they know more than the product is giving them credit for, and leaves.

The right shape is a probe: find out quickly what is still there, then refresh the layer that decayed rather than re-teaching everything uniformly.

## What Duolingo does

Source: blog.duolingo.com/how-to-relearn-a-language (Duolingo blog, 2022-09-06; accessed 2026-09-22)

- Duolingo published an explainer on **Ebbinghaus's savings paradigm** — discovered in the **late 1800s** — applied directly to attrition, with advice for returners: prioritize **vocabulary recovery specifically**, because that is the layer that decayed, and use conversation to surface the holes you do not know you have.
- The research it cites includes a case of an adoptee relearning words from a language she had no conscious memory of ever speaking.
- The strongest version of the evidence comes from studies of people adopted from Korea who stopped hearing Korean entirely: they recognized Korean sounds **no better than people who had never learned Korean at all** — a measured score of zero — and yet **relearned the language measurably faster than true beginners** (blog.duolingo.com/can-you-forget-your-first-language (Duolingo blog, 2024-02-20; accessed 2026-09-22)).

**The tensions.** Two, and both bound the rule. First, the same post notes that children forget faster and more completely than adults do — the residue is real but weaker when the original capability was acquired shallowly or young, so "assume residual competence" has a depth boundary and will sometimes be wrong. Second, the layers decay at different rates, so a reactivation path that refreshes uniformly is only marginally better than one that restarts: you have to know which layer went.

## The transferable pattern

1. **Treat "returning after a gap" as its own state**, distinct from new and from active. If your system only has those two, every returner is misclassified by definition.
2. **Open with a probe, not a curriculum.** A short diagnostic that finds the edge of what is still accessible is worth more than any amount of re-onboarding, and it costs the user less.
3. **Expect the probe to under-report.** A cold score of zero does not mean the residue is gone; it means retrieval failed. Size the rebuild on relearning speed observed over the first few sessions, not on the entry score.
4. **Refresh the fast-decaying layer.** Do not re-run the structural teaching that is almost certainly intact.
5. **Say the reasoning out loud.** "You did this before — this will come back faster than it went in" is both true and the single most useful thing you can tell someone who is embarrassed about the gap.
6. **Bound the assumption.** For users whose original engagement was shallow or long past, fall back to the beginner path gracefully rather than stranding them above their level.

## Apply to your product

- What happens today when someone returns after six months away? Is it the new-user flow, and who decided that?
- Could you build a five-minute probe that distinguishes "still has it," "had it, lost access" and "never really had it"?
- What signal would tell you a returner is above the level you assigned them — and can they correct you without starting over?

## See also

[[decay-is-graded-and-fine-grain-goes-first]] · [[what-protects-a-skill-through-a-lapse]] · [[../duo-retention/references/churn-diagnostics]]
