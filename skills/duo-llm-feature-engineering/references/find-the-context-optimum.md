---
name: duo-llm-feature-engineering-find-the-context-optimum
summary: Prompt size has a peak, not a budget — include the worked example for a fix that recurs everywhere, omit it for one-offs, and expect to keep retuning.
metadata:
  internal: true
---

# Find the Context Optimum

## Concept

Better prompting is not more context. Every concrete worked example you paste in buys consistency on the cases it came from and spends two things — context window, and generality. Too specific and the prompt fails on the next case that is slightly different. Too general and it fails on the case it sees a hundred times, reinventing the same fix badly each time.

So treat prompt size as a **quantity with an optimum**, not a budget to fill. The discriminator is frequency. A fix that recurs across every instance earns its exact worked example, because the example is what makes the model apply it the same way every time. A fix that appeared once does not, and pasting it in narrows the prompt toward a situation that will not recur.

## What Duolingo does

Source: blog.duolingo.com/automating-jvm-golden-path (Duolingo blog, 2025-12-17; accessed 2026-09-22)

- Duolingo automated **JVM Golden Path upgrades** — moving services onto a target stack of **Gradle 8, Kotlin 2.1.20, Spring Boot 3.x, Base Library 3.x, JDK 21, OpenTelemetry 1.33.6 and Debian Bookworm**.
- The architecture puts deterministic work first — **OpenRewrite recipes** handle Gradle files, the javax-to-jakarta rename and Java 21 method replacements — and the **AI agents fill the gaps and fix post-upgrade errors**. A **deterministic build check** drives the fix loop, and only a **clean build produces a PR**, so the model never gets to judge its own work.
- Tuning the per-component prompt templates, the team had to **find the right balance between adding solutions from completed upgrades and generalizing those solutions**. Their stated failure mode for the naive approach — dumping every diff in **"bloats the context window"** and yields an **overly-specific prompt** that does not work at scale.
- Reported effect — the process sped up **"by weeks."**
- **Tension, and Duolingo says so plainly.** This is framed as an **unresolved tradeoff**, not a solved rule; they are still refining the prompts to reduce manual work. They also concede they have **"only upgraded a handful of repos"** so far, so the sample behind the tuning is small.
- **Determinism is not free of failure either.** One OpenRewrite recipe **introduced a conflicting dependency** that broke builds and was hard to trace — and the agents, while good at debugging strategy, **could not locate where the conflict came from**.

## The transferable pattern

- **Sort candidate examples by observed frequency, not by how instructive they feel.** The ones you see constantly go in with their full worked detail. The one-offs stay out, or get compressed to a single line of guidance.
- **Do the deterministic transformation first.** Anything a rules engine can do reliably should be done before the model is called — it shrinks the problem, removes a whole class of invented output, and gives the model a known-good starting point.
- **Gate on an oracle the model cannot argue with.** A check that passes or fails on its own terms is what makes an unattended loop safe; a model grading its own output is not a gate.
- **Budget context deliberately.** Decide what fraction of the window goes to examples versus to the instance itself, and notice when examples start crowding out the actual input.
- **Re-measure after every addition.** An example that helped the case it came from and quietly hurt six others is the normal outcome, and it is invisible without a fixed evaluation set.
- **Do not assume the deterministic layer is the safe one.** A rules engine that makes a wrong change makes it silently and everywhere, and neither you nor the model may be able to trace it.

## Apply to your product

- Which failure does your pipeline hit most often, and is its exact fix in the prompt verbatim — or is the model re-deriving it every run?
- What share of your prompt is worked examples, and when did you last remove one and check whether anything got worse?
- What part of your task could a deterministic rule handle completely, and what would the pass-or-fail check on the result be?

## See also

[[examples-from-your-corpus-beat-more-instructions]] · [[prompt-as-template-not-freeform]] · [[../duo-ai-agent-platform/SKILL]]
