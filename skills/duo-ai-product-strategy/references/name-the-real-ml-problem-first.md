---
name: duo-ai-product-strategy-name-the-real-ml-problem-first
summary: State your objective precisely before buying a model — it is often not the objective the off-the-shelf system was trained for.
metadata:
  internal: true
---

# Name the Real ML Problem First

## Concept

Teams reach for a model that solves the problem they can name in one sentence, and the one-sentence version is usually wrong. The everyday framing is "produce the correct output." The framing your system actually depends on is often "produce the complete set of outputs a user could legitimately give and be right."

Those are different objectives, with different training data and different failure modes. A system trained to emit one good answer is trained on data with one target per input; it has no reason to enumerate, and no incentive to cover the tail. If your product's correctness rule needs coverage, an off-the-shelf generator will look impressive in a demo and quietly fail in production — not because the model is weak, but because you bought the wrong objective.

## What Duolingo does

Source: blog.duolingo.com/using-ai-to-open-up-bottlenecks-in-course-content-creation (Duolingo blog, 2020-08-31; accessed 2026-09-22)

- Duolingo grades a learner response by matching it against an expert-curated list of acceptable translations. So the ML problem is not translation quality — it is **recall over the whole acceptable space**, and that list is authored by people, which makes it the real cost ceiling on shipping new content.
- The combinatorics are brutal. One English sentence — "Unfortunately, someone put my wool sweater in the dryer" — has **over 6 billion** acceptable Chinese translations. Ordinary sentences routinely run to the hundreds.
- Commercial translation systems cannot help by design. They are trained on corpora with a single target per source, so they emit one output.
- Rather than solve it alone, Duolingo published the problem as the **STAPLE** shared task, with data covering English courses for **Hungarian, Japanese, Korean, Portuguese and Vietnamese** speakers.
- Result — the best team scored about **0.55 weighted F1** on a 0.0-to-1.0 scale, comfortably above Amazon Translate as a baseline. Good, and far from solved.
- The best-performing entries did one thing beyond coverage — they paid attention to **how often learners actually produced each translation**, not just whether it was valid.

**Tension.** The task did not close the problem. Models badly **underproduced Japanese and Korean**, because levels of formality multiply the acceptable set in ways the systems did not model — the failure was concentrated exactly where the combinatorics were worst, which is where a naive benchmark average hides it.

## The transferable pattern

- Write your objective as a scoring function before you evaluate a vendor. "Given this input, the system must return X, and it is wrong if Y." Precision-shaped and recall-shaped objectives look identical in a one-line pitch and diverge completely in production.
- When your system judges user input against an enumerated set, the cost of maintaining that set — not model quality — is your scaling constraint. Attack the enumeration.
- If the objective is genuinely unsolved, consider publishing it as a benchmark with your data. You get the field's effort aimed at your constraint, a public baseline, and a number that tells you honestly how far from solved you are.
- Where many outputs are all correct, rank them by how often your real users produce each one. Observed frequency is a label your competitors do not have, and it aligns effort with real-world impact instead of spreading it evenly over a tail nobody hits.
- Report the objective broken out by segment. Aggregate scores conceal that a system fails hardest on the hardest slice.

## Apply to your product

- Write the one sentence that says what your model must output and what makes an output wrong. Is that a precision problem, a recall problem, or a ranking problem — and does the system you are about to buy optimize for it?
- Is there a list, taxonomy or ruleset in your product that humans maintain by hand and that grows combinatorially with your catalog?
- What usage frequency do you observe that nobody outside your company can see, and could it weight a model's effort toward the cases that actually occur?

## See also

[[point-ai-at-unit-economics-not-features]] · [[stage-split-humans-set-constraints-models-multiply]]
