---
name: duo-attention-budget-three-kinds-of-effort-cap-cut-and-add
summary: Split the effort your product demands into inherent, wasted, and productive — cap the first, cut the second, deliberately add the third.
metadata:
  internal: true
---

# Three Kinds of Effort: Cap, Cut, and Add

## Concept

Working memory is the binding constraint on any screen, and not all the effort you spend on it is the same kind. Three buckets: effort that is **inherent** to the task (a hard thing is hard), effort **wasted on presentation** (decoding your interface, your jargon, your layout), and effort spent on **real processing** (actively producing an answer instead of passively reading one).

The first is a ceiling you set by scoping the unit. The second is pure loss — every unit of it is a unit unavailable for the task. The third is the product working: friction that forces production is what creates retention. Treating all three as "friction to remove" is the common and expensive mistake.

## What Duolingo does

Source: blog.duolingo.com/why-can-learning-feel-overwhelming (Duolingo blog, 2024-12-24; accessed 2026-09-22)

- Duolingo applies John Sweller's **intrinsic / extraneous / germane cognitive load** taxonomy as an explicit design guideline for its learning designers — it is stated as a working rule, not an academic aside.
- **Cap the intrinsic**: bite-sized lessons bound how much task-inherent difficulty can arrive at once.
- **Cut the extraneous**: a hard limit on how many brand-new words may appear in a single sentence.
- **Add the germane**: exercises force the user to interact and produce, rather than read an explanation.
- Tension the post leaves open: germane load is *deliberately added friction*, and the post gives **no test** for telling it apart from extraneous friction in a new domain. That distinction is the entire judgement call, and you inherit it unresolved.
- A second tension, from Duolingo's own advice elsewhere: it tells new learners to study in **one 30-minute block rather than 15 minutes morning and evening**, because getting into "German mode" carries a fixed warm-up cost that a short session mostly consumes — and it notes that less settling-in time is needed as proficiency rises. That cuts directly against the bite-sized positioning the company markets as the reason people stick around. Source: blog.duolingo.com/can-you-learn-two-languages-at-the-same-time (Duolingo blog, 2025-02-05; accessed 2026-09-22)

## The transferable pattern

Before you simplify anything, sort the effort:

1. **Inherent** — irreducible given what the user is trying to accomplish. You cannot delete it; you can only decide how much of it arrives per unit. Cap it by shrinking the unit, not by lying about the task.
2. **Wasted** — spent on your presentation: ambiguous labels, dense screens, unexplained terms, a novel control where a conventional one would do. Cut without mercy. It buys nothing.
3. **Productive** — spent because the user had to retrieve, decide, or produce rather than skim. Add it on purpose.

The usable field test for bucket 2 versus bucket 3: **does removing this friction change what the user ends up able to do?** If yes, it was productive. If the outcome is identical and the path was just shorter, it was waste.

Warm-up cost is a fourth line item people forget. Sessions have a fixed entry price, and it is highest when the mode is unfamiliar — so short sessions are an expert affordance often sold to novices as convenience.

## Apply to your product

- Take your most-complained-about flow and sort every step into the three buckets. How much of what users call "too hard" is actually bucket 2?
- Where have you removed a step that made people think, and shipped a smoother flow that produces worse outcomes?
- What is the fixed warm-up cost of a session in your product, and what fraction of your median session length does it eat?

## See also

[[hold-everything-but-the-target-constant]] · [[cap-novelty-then-force-immediate-use]] · [[salience-is-a-budget-and-it-front-loads]]
