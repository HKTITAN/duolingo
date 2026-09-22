---
name: duo-ai-agent-platform-verification-becomes-the-bottleneck
summary: Making generation cheap does not remove the queue, it moves it — first to verification, then to human review, which automation of the prior stage never raises.
metadata:
  internal: true
---

# Verification Becomes the Bottleneck

## Concept

Automating production feels like solving the problem because the visible stage gets fast. It is not solved. Every downstream stage has a fixed human-throughput ceiling that the speed-up does not touch, so the queue relocates rather than disappearing.

Producing artifacts faster than the next stage can absorb them converts output into backlog — and backlog is worse than no output, because it also consumes the attention of the people you were trying to free.

So plan the whole chain before automating one stage of it. The useful question is not "can a model do this step" but "what is the ceiling of the step immediately after it, and what happens when I flood it".

## What Duolingo does

Source: blog.duolingo.com/ai-ios-unit-test-generation-pipeline (Duolingo blog, 2026-06-24; accessed 2026-09-22)

- Duolingo built a pipeline that generates iOS unit tests and opens them as PRs. Over roughly 17 weeks it merged **250 PRs** carrying about **85,000 lines of test code**, **4,460 test functions** across **233 classes**, at a rate of about **20 test PRs per day**.
- Coverage of the app's MVVM layer went from **9% to 30%**, a **+240% relative increase** — repositories **+352%**, ViewModels **+203%**, DataSources **+192%**.
- **76% of generated PRs passed CI on the first attempt**, so verification by machine was largely working.
- Generation stopped being the constraint. Reviewer bandwidth became it, and the team's stated next move is a second reviewer agent that checks each generated test before a human ever sees it.

**Tension.** Every one of those 250 PRs still required human review and approval. The pipeline is described as almost entirely autonomous, and the qualifier is doing all the work — it is autonomous up to the review gate, which it cannot cross. The headline throughput number and the actual limit on the system are two different numbers, and only one of them is in the title.

## The transferable pattern

Before you automate a stage, draw the chain it sits in and mark the ceiling of each stage after it.

1. **Name the next stage's capacity in the same unit as your new output rate.** Items per day in, items per day absorbed. If the second number is smaller, you are building a queue, not a capability.
2. **Automate verification before, or alongside, generation.** The cheapest way to protect a human reviewer is to ensure most of what reaches them is already known-good.
3. **Instrument the gate, not the producer.** A dashboard of how much you generated tells you nothing about whether the system is working. Time-in-queue at the human step does.
4. **Accept that a human gate may be the design.** If review cannot be automated, size the producer to the reviewer rather than pretending the reviewer will scale.

The compounding version of this: each time you automate a stage, the bottleneck moves one step downstream and the next fix is a different kind of problem. Plan two moves ahead.

## Apply to your product

- In the workflow you most want to automate, who or what is the stage immediately after the one you are targeting, and how many items per day can it actually absorb?
- If your automation worked perfectly tomorrow, what would be sitting in a queue by Friday, and whose queue is it?
- What fraction of the produced items could be machine-verified before a person sees them, and what would that verifier need to check?

## See also

[[run-it-manually-and-categorize-failures-first]] · [[every-producer-needs-a-janitor]] · [[grade-the-artifact-not-the-prose]] · [[../duo-experimentation/references/guardrail-metrics]]
