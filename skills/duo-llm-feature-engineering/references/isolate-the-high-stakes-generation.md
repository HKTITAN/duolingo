---
name: duo-llm-feature-engineering-isolate-the-high-stakes-generation
summary: When one prompt must produce a critical artifact and run an ongoing interaction, split the artifact into its own call so it gets the full constraint budget.
metadata:
  internal: true
---

# Isolate the High-Stakes Generation

## Concept

Instruction-following degrades as the number of simultaneous constraints in one context rises. The degradation is not a clean cutoff where the last rule gets dropped — it is that the model produces something which **half-satisfies everything** instead of fully satisfying the one thing that actually mattered.

So when a single prompt is being asked to both produce a critical artifact and manage an ongoing interaction, split them. Generate the artifact in its own call, with its own constraints and nothing else competing for attention, then **feed the finished artifact into the interaction prompt as a fixed input**. The interaction prompt now receives a settled thing rather than another job. Latency is usually available for free, because there is almost always dead time before the interaction starts.

## What Duolingo does

Source: blog.duolingo.com/ai-and-video-call (Duolingo blog, 2025-04-22; accessed 2026-09-22)

- Duolingo generates the Video Call **opening question in a separate "Conversation Prep" call**, run **while the call is ringing** — the latency is hidden inside a moment the user already expects to wait through.
- The finished question is then **passed into the main conversation prompt** as a given, not re-derived.
- **They learned this by shipping the combined version first.** With one prompt doing both jobs, the post says plainly that it **"overloads the LLM"** — the result was overly complex sentences that **dropped the required vocabulary**, which was the single constraint the whole feature existed to satisfy.
- Note what failed. It was not that the output was broken; it was fluent and plausible. The constraint that mattered most was the one quietly sacrificed, which is exactly the failure that survives a casual review.
- The same feature stacks this with the decomposition in [[one-narrow-prompt-per-move]] and the memory step in [[memory-as-extracted-facts-not-transcripts]] — separate calls, each with one job.

## The transferable pattern

- **Find the constraint the feature exists for.** In any prompt carrying many rules, one of them is the reason the feature ships. That one should not share a context with housekeeping.
- **Split it into its own call, with its own evaluation.** A dedicated call is separately testable — you can assert the constraint on its output directly, which you cannot do when it is buried in a conversational turn.
- **Hide the latency in dead time.** Connection setup, a loading state, a confirmation screen, the moment between an action and its result. Pre-compute during a wait the user is already having.
- **Pass the artifact forward as data, not as an instruction.** The downstream prompt should receive a finished value it must use, not a rule it must apply.
- **Watch for the specific symptom.** Output that is fluent, plausible, and quietly missing the one required element means constraint competition, not a weak model. Adding emphasis to the rule rarely fixes it; removing its competitors does.
- **Cost check.** Two calls cost more than one. The trade is worth making only for the constraints that carry the feature; splitting everything is just a slower monolith.

## Apply to your product

- In your busiest prompt, which single requirement, if silently dropped, would make the feature pointless? Is it sharing a call with anything else?
- Where in your flow does the user already wait, and what could you pre-compute during that wait?
- If you asserted that one requirement on the output today, would your pipeline even be able to check it?

## See also

[[one-narrow-prompt-per-move]] · [[prompt-as-template-not-freeform]] · [[human-authored-frame-model-improvises-inside]]
