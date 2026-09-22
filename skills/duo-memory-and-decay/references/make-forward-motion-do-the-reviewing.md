---
name: duo-memory-and-decay-make-forward-motion-do-the-reviewing
summary: Going back costs effort with no felt progress, so most users skip it; if step N+1 structurally requires step N, retrieval happens as a side effect of moving forward.
metadata:
  internal: true
---

# Make Forward Motion Do the Reviewing

## Concept

Review is a cost the user pays with no felt progress. That is why review features get built, get measured, and get used by almost nobody — they compete with the thing the user actually came to do.

The structural fix is to stop making it a separate activity. If step N+1 genuinely requires step N as a component, then retrieval of N happens automatically as a side effect of doing N+1. Reinforcement rides on motivation instead of competing with it, and the user never has to choose between progress and consolidation.

There is a second reason this matters: users are bad judges of their own readiness. Familiar material feels easy to process, and fluency of processing gets mistaken for mastery, so "I'll move on when I feel ready" systematically keeps people parked on things they already have.

## What Duolingo does

Source: blog.duolingo.com/review-exercises-help-measure-learner-recall (Duolingo blog, 2021-12-02; accessed 2026-09-22)

- Duolingo's own analysis found an asymmetry: learners who answered Review Exercises correctly had completed **more lessons in the *next* skills**, while **completing more *previous* skills showed no significant effect**. Demonstrated recall predicted forward progress; volume of prior work did not.
- The learner-facing guidance follows from it: move steadily down the course and push into new material **even when it feels uncomfortable**, because personalized practice is built into the path — the app decides what to review and when, not the learner (blog.duolingo.com/duolingo-101-how-to-learn-a-language-on-duolingo (Duolingo blog, 2024-12-02; accessed 2026-09-22)).
- Practically, this means the review is not a destination. It is interleaved into the forward path, so the user's only decision is whether to continue.

**The tension.** The asymmetry is partly definitional — earlier content cannot reinforce concepts taught later, so the finding is less surprising than it looks. And the whole rule only pays off if your content genuinely compounds. A flat set of independent topics gets nothing from this: there is no step N that step N+1 requires, and pretending otherwise produces fake prerequisites that annoy users without reinforcing anything. Check whether your sequence actually composes before you build on it.

## The transferable pattern

1. **Test whether your content compounds.** Pick any item and ask what earlier item it structurally requires. If the honest answer is "nothing," this pattern is not available to you and you need explicit review instead.
2. **Sequence so new work consumes old work.** Design the next step to need the previous one as a component, not merely to follow it in an ordering.
3. **Interleave, do not relocate.** Review that lives in its own tab is review that competes. Review inside the forward flow is review that happens.
4. **Take the pacing decision away from the user** where you can measure readiness better than they can feel it — and be explicit that discomfort is expected rather than a signal to stop.
5. **Measure with demonstrated recall, not accumulated volume.** How much a user has completed is a weaker predictor than whether they can still produce something from earlier.

## Apply to your product

- Does your sequence compound, or is it a list of independent topics in an arbitrary order? Be honest — this single answer decides whether the pattern applies.
- Where does review currently live in your product, and what percentage of active users ever open it?
- Do you gate progress on completion or on demonstrated recall? Which one is in your dashboard?

## See also

[[give-mastered-things-a-visible-decay-state]] · [[three-conditions-for-practice-to-pay]] · [[../duo-gamification/references/progression-design]]
