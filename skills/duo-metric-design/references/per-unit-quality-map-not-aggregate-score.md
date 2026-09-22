---
name: duo-metric-design-per-unit-quality-map-not-aggregate-score
summary: An overall score says something is wrong; a color-coded per-unit map says which part to open — aggregation destroys the locality needed to act.
metadata:
  internal: true
---

# Per-Unit Quality Map, Not Aggregate Score

## Concept

An aggregate quality score answers a question nobody needs answered. "This artifact scores 72" tells the person responsible that something is wrong and gives them no way to find it. The information that would have made the number actionable — *where* — was destroyed in the act of averaging.

Report quality at the unit of work instead, rendered visually: every chapter, section, endpoint, screen or module colored by the metric. The reader's eye lands on the red one and they open it. The same view also lets you diff two versions of an artifact after an experiment and see which sections differ — which is how you learn *why* one version won rather than only *that* it won.

## What Duolingo does

Source: blog.duolingo.com/how-were-improving-duolingos-course-creation-process (Duolingo blog, 2019-09-09; accessed 2026-09-22)

- The Tree Filter offers **four views**, each color-coding individual skills across a whole course: **lexemes per lesson**, **lessons per skill**, **skill quit rate**, and **vocabulary CEFR level**.
- Drill-down is built in: hovering a skill shows **which specific words exceed that skill's CEFR level**. The map points at the unit; the hover points at the offending item inside it.
- The same per-unit view was used **post hoc to explain why one course version beat another** — not just to confirm that it did.
- Targets rendered on the map came from analysis of real course data: **6–7 lexemes per lesson**, **4–6 lessons per skill at level 0**.

Scope note: the Tree Filter is tied to Duolingo's retired "tree" course structure, which has since been replaced by the path. The visualization pattern survived the structural change; the specific tool did not.

## The transferable pattern

1. **Pick the unit of work your producers actually edit.** Not the unit your database happens to store, and not the whole artifact.
2. **Render one metric at a time across all units.** Multiple metrics on one map produces a picture nobody can read; make them separate views and let the reader switch.
3. **Color by distance from target, not by raw value.** The reader needs "this one is out of range," not "this one is 8."
4. **Make every cell open the thing.** A map you cannot click is a chart; a map you can click is a workflow.
5. **Support drill-down to the offending item.** Unit-level tells you which file; item-level tells you which line. Both are needed to close the loop.
6. **Keep the maps after experiments.** Diffing per-unit views between two variants is the cheapest available mechanism for turning a win into an explanation.

The tradeoff: per-unit views make it easy to fix the worst cells and call it done, while a systemic problem spread evenly across every unit shows up as uniform mid-range color and gets ignored. Keep one aggregate around to catch that case — just do not grade anyone on it alone.

## Apply to your product

- What is the smallest unit of your product that one person owns and can edit alone — and do you report any quality number at that granularity?
- When your dashboard shows a metric degrading, how many clicks does it take someone to reach the specific thing to fix?
- After your last winning experiment, could you say which part of the change did the work?

## See also

[[leading-indicators-for-the-people-doing-the-work]] · [[refuse-to-measure-the-vague-goal]] · [[../duo-experimentation/SKILL]]
