---
name: duo-experimentation-design-the-population
summary: Who is eligible to enter a comparison decides what it measures — exclusion criteria and counterfactual framing, not just arms.
metadata:
  internal: true
---

# Design the Population

## Concept

Most experiment design attention goes to the arms. The larger source of wrong answers is the population: who was allowed in. Admit users who could already do the thing you are about to measure and your result is confounded with prior ability. Admit users who are getting the same capability somewhere else and your result is confounded with that other source. Ask people to rank options most of them have only ever used one of, and you measure familiarity. In each case the number you publish describes your selection, not your product.

## What Duolingo does

Two different studies, the same discipline applied to entry criteria:

- **Exclusion by prior exposure.** For an experiment on the Spanish preterite, Duolingo recruited only learners who had not yet encountered that structure in lessons *and* who self-reported knowing little Spanish — two separate filters, one for in-product exposure and one for outside knowledge. The English efficacy study admitted only learners taking no other classes and reporting no or very little prior English: **263 learners**, measured from the end of A1 through the end of A2 with a third-party assessment (Avant STAMP) rather than an in-house score. Source: blog.duolingo.com/how-well-does-duolingo-teach-english (Duolingo blog, 2022-09-19; accessed 2026-09-22)
- **Counterfactual framing to strip a distribution advantage.** Market share cannot tell you whether users prefer your product, because it is confounded by price, access and acceptance. Duolingo surveyed only test takers who had taken **more than one** English proficiency exam — removing the inexperience confound — and asked which they would choose *if every test were universally accepted*, removing the distribution confound. An overwhelming majority chose the Duolingo English Test. Source: blog.duolingo.com/future-of-digital-testing (Duolingo blog, 2023-06-06; accessed 2026-09-22)

Tensions in both: 263 participants across a full proficiency level is a small study, and filtering to users with no outside instruction produces a population less representative than the one you ship to — clean attribution bought with generalizability. The preference survey is published as "an overwhelming majority" with no sample size and no margin: a well-designed question reported in a form nobody can audit. Design the question well *and* publish the n.

## The transferable pattern

Write the entry criteria before the arms, and write down what each one is protecting against:

1. **Exclude prior capability.** Anyone who could already do the thing cannot show you whether you taught it.
2. **Exclude competing sources.** If the capability could arrive from somewhere else during the study, that route is a silent second treatment.
3. **Restrict comparisons to people who can actually compare.** A preference question is only meaningful among users with experience of more than one option.
4. **Ask the counterfactual, not the observed.** "Which would you choose if access were equal" separates preference from distribution.
5. **Measure with an instrument you do not control** when the claim is about the outside world.
6. **Report the n and the exclusions with the result.** A filtered population is a strength only if the filter is visible.

## Apply to your product

- For your last study or survey, who was excluded — and can you say what confound each exclusion removed?
- Are you reading adoption or market share as evidence of preference, when access and price differ between the options?
- Is the claim you want to make about behavior inside your product, or about the world? If the second, whose instrument would you trust to measure it?

## See also

[[quasi-experiments]] · [[baseline-at-first-contact]] · [[ladder-of-evidence]] · [[sample-size]]
