---
name: duo-llm-feature-engineering-the-filter-holds-the-bar-not-the-generator
summary: Quality at volume is a selection problem — over-generate, filter with expert-owned evaluators scored on named criteria, and reuse the rejects as hard negatives.
metadata:
  internal: true
---

# The Filter Holds the Bar, Not the Generator

## Concept

Generation is cheap and variable. Trying to make the generator good enough that every output ships is the expensive path, and it caps out — you can tune a prompt for a long time and still get a distribution rather than a guarantee.

The cheap path is to accept the distribution and **move the quality bar into a filter**. Deliberately over-generate, then score every candidate against **named, domain-specific criteria** using a model-based evaluator, and keep only what clears the line. The important consequence is organisational, not technical. Your domain experts stop authoring artifacts one at a time and start owning the evaluator — which means their effort stops being linear and starts compounding across every future output, and you can raise the bar later without re-hiring.

## What Duolingo does

Source: blog.duolingo.com/scaling-duoradio (Duolingo blog, 2025-03-11; accessed 2026-09-22)

- Duolingo deliberately generated **surplus** DuoRadio episodes, then ran an LLM-powered filter grading each script on four named criteria — **naturalness, grammaticality, coherence and logic**.
- **Learning Designers own and continuously refine the evaluator prompts.** The experts define what good means; they do not grade every episode.
- Output went from **300 episodes produced in nearly a year to 15,000-plus**, and from **2 courses to 25-plus in under two quarters** — against an internal estimate of **more than 5 years** to do it manually. Reported **99% cost reduction**.
- Downstream usage — **daily sessions from 500K to 5M in under 6 months**, and **DAUs from 100K to 5.5M**.

Source: blog.duolingo.com/test-creation-machine-learning (Duolingo blog, 2022-04-06; accessed 2026-09-22)

- The rejected surplus has a second use. For fill-in-the-blank items, Duolingo generates a passage, removes the sentence most natural to remove, and then **sources the incorrect answer options from other generated texts on similar topics**.
- This matters because plausible-but-wrong is the hardest category to author by hand — **a person writing a wrong answer knows it is wrong and leaks that**, while a near-miss produced by the same generator is wrong for structural reasons instead of authored ones.
- **Tension.** Over-generating is not free — you pay inference on everything you throw away, and the numbers above are the net of that. And an evaluator is itself a model with its own failure modes, which is why the criteria are named and expert-owned rather than a single "is this good?" call.

## The transferable pattern

1. **Name the criteria.** Not "quality" — three to five specific, independently-judgeable properties of a good artifact in your domain. Unnamed criteria produce an evaluator that agrees with whatever it just read.
2. **Score each criterion separately** and set a threshold per criterion, so a candidate cannot pass by being excellent on one axis and unacceptable on another.
3. **Give the evaluator to your domain experts as their artifact.** They edit it, they tighten it, they own its version history. This is the step that makes the whole thing compound.
4. **Calibrate the evaluator against human judgement periodically** on a held-out sample, or it drifts and you will not notice, because everything it approves looks approved.
5. **Keep the rejects.** They are your hard negatives, your adversarial test cases, your distractors — the material that is most expensive to author deliberately and that you have already paid for.
6. **Budget for the waste.** Decide the over-generation ratio explicitly; it is a cost lever you can tune, not an accident.

## Apply to your product

- What are the three to five properties that make an artifact in your domain good, stated so two reviewers would score the same candidate the same way?
- Who in your organisation would own the evaluator, and is their time currently spent producing artifacts one at a time?
- What do you throw away today that would make a useful negative example, a test fixture, or a decoy?

## See also

[[dont-collapse-the-candidate-set]] · [[examples-from-your-corpus-beat-more-instructions]] · [[../duo-ai-agent-platform/SKILL]]
