---
name: duo-measurement-validity
description: Design and report a number that survives an outsider's scrutiny — prove the outcome on an instrument you did not build, break a headline score into components only when they add information, publish the component where you lose, audit bias at intersections instead of one variable at a time, and disclose exactly where your own hand touched the evidence. Also covers the inference traps that make an instrument lie — classifier categories that encode their training population, resemblance mistaken for lineage, non-independent samples, contested definitions. Use when someone asks will this number survive outside scrutiny, is our metric actually valid, should we ship a subscore, why doesn't our completion rate convince buyers, how do we prove our product caused this, is our model biased, can we trust this benchmark, or how do we measure something nobody can measure directly.
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Measurement Validity

Most product metrics are designed to be moved, not to be believed. This skill is about the second kind — a number an outsider with no reason to trust you can be asked to accept, and the inference errors that quietly turn a measurement into a story.

Start with the instrument. Then check what you are allowed to conclude from it.

## Design the instrument

- [[references/benchmark-on-an-instrument-you-did-not-build]] — an internal completion metric proves users moved through your product; an external scale proves the product did something. Includes funding the field that will adjudicate your claim.
- [[references/ship-a-subscore-only-if-it-adds-information]] — the three gates a component score must pass before it earns a place on the dashboard, and why the noisiest component is often the most valuable one.
- [[references/measure-willingness-alongside-capability]] — for anything users decline rather than fail at, nerve is the binding constraint and it moves independently of skill.

## Report it honestly

- [[references/publish-the-component-where-you-lose]] — naming your worst dimension is what makes the good numbers legible as measurement rather than marketing, and what it costs you.
- [[references/clean-cohort-buys-attribution-costs-generality]] — a filtered cohort is the only way to isolate what you caused, and the same filter stops the result generalising. Also covers disclosing the stages of a funded study you were walled off from.
- [[references/audit-bias-at-intersections]] — bias can live at a combination of attributes and vanish when either is checked alone, so a one-row-per-attribute fairness table proves almost nothing.

## Don't let the instrument lie

- [[references/classifier-categories-encode-their-training-population]] — a group the training data never contained gets filed under its nearest surface match, and the misfiling comes back as a finding.
- [[references/resemblance-is-not-lineage]] — contact manufactures shared surface material exactly as descent does; the discriminating evidence is in the generative machinery, not the borrowed inventory.
- [[references/sample-cases-that-could-not-have-influenced-each-other]] — agreement among connected cases is one observation counted many times, and the population predisposed to disagree is the highest-information test.
- [[references/triangulate-weak-independent-sources]] — three signals that fail in different ways beat one that fails silently; disagreement between them localises the error.

## Boundary

This skill stops at the number. Turning a validated result into press coverage, or commissioning research to remove a specific buyer objection, belongs to `duo-timely-data-publishing`. Segmenting users by declared motive in order to decide what to build belongs to `duo-motivation-segmentation`. Visual craft — how a result is charted, typeset or animated — routes out to the external design-engineering skill; this pack does not own pixels.

## Sibling skills

[[../duo-experimentation/SKILL]] · [[../duo-inclusive-access/SKILL]] · [[../duo-difficulty-calibration/SKILL]] · [[../duo-product/SKILL]]

## Sources

Distilled from 21 extracted claims across blog.duolingo.com — subscore validation, efficacy studies, fairness auditing, research grants and the linguistics explainers used here as inference-trap case studies. Every node carries its own dated citation; slugs are checked against `scripts/sources.json`.
