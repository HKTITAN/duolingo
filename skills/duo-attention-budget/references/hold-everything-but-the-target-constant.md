---
name: duo-attention-budget-hold-everything-but-the-target-constant
summary: A unit that teaches one thing must hold every other variable fixed, so the user's pattern detection has nowhere else to go.
metadata:
  internal: true
---

# Hold Everything but the Target Constant

## Concept

Attention is the bottleneck in acquiring any skill, and simultaneous novelty splits it. If the one thing you want noticed is varying *and* three other things are varying, the user has no way to tell which variation carries the signal — so the pattern you are trying to teach competes with noise you introduced yourself.

The fix is a controlled experiment run on the user's attention: hold every variable constant except the target. Their pattern detection then has nowhere else to go. This is the same discipline as an A/B test — one change at a time — applied to a teaching surface rather than a metric.

## What Duolingo does

Source: blog.duolingo.com/language-rules-learning-grammar-on-duolingo (Duolingo blog, 2020-10-02; accessed 2026-09-22)

- Grammar Lessons deliberately introduce **no new vocabulary at all**. Every word in the lesson is already known, so the learner's entire budget lands on the grammatical pattern being taught.
- Duolingo did not just strip novelty — it built **new exercise formats specifically for salience**:
  - **Table exercises** that lay out verb endings side by side so the pattern is visible as a shape rather than inferred across separate screens.
  - **Two-blank exercises** that force a direct contrast between two confusable forms in the same sentence, making the difference the only thing in play.
- The cost is real: a unit built this way carries less content per minute than a mixed one. Duolingo pays that cost deliberately on the units where a single pattern is the point, not everywhere.

## The transferable pattern

When a unit of your product exists to teach one thing:

- **Freeze the surroundings.** Use content, controls, and layout the user has already seen. Novelty anywhere other than the target is a leak.
- **Make the target the only varying dimension.** If two things change between step 1 and step 2, the user learns neither reliably.
- **Build a format for the comparison, not just the content.** Two confusable options presented side by side in one view teach the distinction; the same two options on separate screens do not, because the user has to hold one in memory to compare.
- **Accept the throughput cost.** A controlled unit covers less ground per minute. It is worth it only where the pattern matters more than the coverage — so choose those units deliberately rather than applying this everywhere.

This is also a diagnostic. If users consistently miss a distinction you thought you taught, check whether anything else was varying in the same view.

## Apply to your product

- Pick one thing your product tries to teach in-flow. List everything else that is new on that screen — how much of the user's attention is left for the target?
- Where do you present two similar options on separate screens, so the user has to hold one in working memory to compare it against the other?
- Which of your units are coverage units and which are pattern units? Are you paying the throughput cost in the right places?

## See also

[[three-kinds-of-effort-cap-cut-and-add]] · [[familiar-content-is-a-load-reduction-technique]] · [[salience-is-a-budget-and-it-front-loads]]
