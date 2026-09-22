---
name: duo-ai-product-strategy-stage-split-humans-set-constraints-models-multiply
summary: Divide an AI-assisted pipeline by stage with a monotonic human-to-model gradient — humans where errors propagate, models where work multiplies.
metadata:
  internal: true
---

# Stage Split — Humans Set Constraints, Models Multiply

## Concept

"Which products should AI build?" is the wrong unit of decision. Inside any single product there are stages that deserve opposite answers.

The sorting rule is error behavior. An error in a stage that defines structure propagates into every artifact built downstream of it, and is expensive to detect because the artifacts look fine individually. That is where scarce expert judgment earns its cost. Late stages, by contrast, multiply out across users and items in volumes you could never staff, and their errors are local, visible and individually correctable. Run the gradient monotonically from human at the start to model at the end, and both kinds of failure land where they are cheapest.

## What Duolingo does

Source: blog.duolingo.com/how-duolingo-experts-work-with-ai (Duolingo blog, 2022-09-14; accessed 2026-09-22)

Course creation is split into **four stages** with an explicit human-to-AI gradient:

1. **Curriculum design** — mostly human. This sets the constraints every later stage inherits.
2. **Raw content writing** — human, with AI tooling assisting.
3. **Exercise generation from the raw content** — mostly AI.
4. **Per-learner lesson assembly** — almost entirely AI, driven by the Birdbrain model.

Two other splits follow the same shape:

- **Triage, not judgment.** Duolingo receives roughly **200,000 learner-submitted reports per day** and uses ML to flag the ones most likely to be missing translations worth adding, plus to prioritize which course improvements to make. The model handles volume; the expert still makes the fix (blog.duolingo.com/can-duolingo-make-me-fluent (Duolingo blog, 2024-11-18; accessed 2026-09-22)).
- **Kill the blank page, not the judgment.** A staff writer, initially hostile to the idea, had GPT-3 produce **four paragraphs within seconds**, spent roughly **10 minutes** iterating prompts, and got a draft judged **too general and too short to publish** — which still saved hours, because reacting to a structure is faster than generating one. Her framing: it will write for her, but it will not think for her (blog.duolingo.com/im-a-writer-heres-why-im-not-scared-of-gpt-3 (Duolingo blog, 2023-02-15; accessed 2026-09-22)).

**Two tensions, both named by the sources.** The gradient is not clean — even in the AI-led generation stage, some exercise types such as reading-comprehension questions are still written by humans, because the model cannot reliably hit the specific learning objective of that lesson. And the human side is not frictionless: the writer's first reaction was feeling insulted and threatened, and she resisted for weeks. Acceptance came only after the tool visibly failed to replace her judgment.

## The transferable pattern

- List your pipeline as stages, then ask of each one — if this stage is wrong, does the error stay local or does it contaminate everything built on top? Contaminating errors buy human review; local errors do not.
- Keep the gradient monotonic. A pipeline that hands work back and forth between people and models loses the accountability that makes the split worth having.
- Expect and publish the exceptions. Some late-stage work carries an objective the model cannot reliably target, and the honest version of the map has that carve-out drawn on it rather than hidden.
- At any stage, prefer the model doing the cold start or the sorting over the model doing the final call. A draft that is too generic is still cheaper to react to than a blank page, and a ranked queue concentrates scarce attention on the highest-yield subset.
- Plan for the human reaction. People whose stage is being automated read the map as a verdict on their value, and adoption tends to come after the tool visibly fails at something they do well.

Making each stage behave reliably once you have drawn this map — prompting, decomposition, evaluation, verification — is the sibling skill `duo-llm-feature-engineering`, not this one.

## Apply to your product

- Draw your pipeline as stages. For each, write what happens downstream if that stage is wrong — and let the propagating ones keep the humans.
- Where in your product does a model currently make the final call on something whose error is expensive to detect?
- Which of your experts' time goes to cold starts or to sorting volume, and what would they do with that time back?

## See also

[[author-a-pool-deliver-an-instance]] · [[name-the-real-ml-problem-first]] · [[../duo-culture/SKILL]]
