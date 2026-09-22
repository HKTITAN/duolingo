---
name: duo-llm-feature-engineering-scope-generation-to-work-with-no-rhetorical-goal
summary: Generated output clears a quality bar when the task needs coverage and variety rather than persuasion, novelty or truth — use that as the first filter on any AI content pipeline.
metadata:
  internal: true
---

# Scope Generation to Work With No Rhetorical Goal

## Concept

Every well-known failure mode of generated text is a failure of commitment. Invented facts, an argument that goes nowhere, prose with no point of view, a conclusion the writer does not hold — each is what happens when a system is asked to mean something and cannot.

Which gives you a clean first filter. Work that requires only **coverage, variety, and on-topic plausibility** is structurally immune to all of those failures, because none of them can occur in a task with no rhetorical goal. Work that requires persuasion, originality, or a load-bearing factual claim is exposed to all of them at once. Sort your proposed AI content pipeline into those two piles before you write a single prompt. The quality bar you can hold is decided at that step, not at the prompt-tuning step.

## What Duolingo does

Source: blog.duolingo.com/test-creation-machine-learning (Duolingo blog, 2022-04-06; accessed 2026-09-22)

- Duolingo used **GPT-3** to generate items for the Duolingo English Test, and states the rationale in terms of what the output does *not* have to do — it is not trying to persuade anyone that an argument is true, not teaching anything new, not producing an emotion. It exists to exercise a skill so the skill can be measured.
- Because the artifact carries no rhetorical load, "plausible, well-formed, on-topic" is the whole bar, and it is a bar a generator can clear at volume.
- **Human-in-the-loop filtering, editing and review sits on top regardless**, plus a separate dedicated pass for **accuracy, fairness and bias** — retained whether an item was machine-authored or human-authored, so the safety review is not a concession made for the model.
- **Tension, stated by Duolingo itself.** The post concedes the boundary directly — this technology may not produce a **"Pulitzer-worthy op-ed column."** The scoping is not a claim that generation is universally good enough; it is a claim about one class of work.

## The transferable pattern

Before costing a generation pipeline, ask what the artifact is *for*, and put it in one of three tiers.

- **Green — no rhetorical goal.** Practice items, test cases, synthetic records, permutations of a known pattern, variant copy for a slot whose meaning is already decided, example inputs. Success is coverage and variety. Generate at volume; review by sampling.
- **Amber — a factual or functional goal, but a bounded one.** Summaries of a supplied document, extraction, classification, rewrites that must preserve meaning. Generate, but the pipeline needs a check against the source, not a taste review.
- **Red — a rhetorical goal.** Anything that has to persuade, take a position, be original, or assert a fact the system does not hold. A model can draft here, but a named human owns the claim and the byline.

Two rules that survive the sort. **The safety review is tier-independent** — bias, fairness and harm checks apply to green output exactly as they do to human output, because the risk is in the artifact, not in the author. And **be suspicious of a green task with a red tail**, where 99% of instances are pure coverage and the remaining 1% carry a real claim. That tail is where the pipeline will hurt you.

## Apply to your product

- List the artifacts you want to generate. Which of them would be unchanged if nobody believed a word of them, and which carry a claim someone will act on?
- For the amber ones, what would a check against the source actually compare, and do you have that source in a machine-readable form?
- Which reviews do you run on human-authored content today, and can you justify not running them on generated content?

## See also

[[the-filter-holds-the-bar-not-the-generator]] · [[dont-collapse-the-candidate-set]] · [[../duo-inclusive-access/SKILL]]
