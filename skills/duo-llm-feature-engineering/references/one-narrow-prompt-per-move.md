---
name: duo-llm-feature-engineering-one-narrow-prompt-per-move
summary: Build a conversational feature as a small state machine of narrow prompts selected by explicit rules, with a mid-flight override and a programmed ending.
metadata:
  internal: true
---

# One Narrow Prompt Per Move

## Concept

The natural way to build a conversational feature is one long prompt driving a free-running exchange. It demos well and degrades in production, because that single prompt has to satisfy every goal simultaneously — hold a persona, hit a difficulty target, advance toward an objective, stay on topic, and know when to stop. Loaded with all of them at once, it half-satisfies each.

Decompose instead. **One narrowly-scoped prompt per conversational move**, and explicit rules that select the next prompt from observable state — who spoke last, how many exchanges have occurred, whether the objective is met. Each prompt's job becomes small enough to be tractable, testable, and improvable on its own. Session length stops being an emergent property and becomes a controlled one.

## What Duolingo does

Source: blog.duolingo.com/chatbot-language-practice (Duolingo blog, 2024-03-20; accessed 2026-09-22)

- In Duolingo Roleplay, **every character response comes from a different prompt** — one optimised for **forming questions**, one for **statements that invite a follow-up**, one for **changing subject**, one for **closing**.
- A **flow chart governs which prompt takes over**, driven by **who spoke last and how many exchanges have occurred**.
- Duolingo's own analogy for the architecture — **a series of one-question conversations with different call-centre reps**, each handed the transcript so far. The continuity the user perceives comes from the passed transcript, not from one long-running context.

Source: blog.duolingo.com/ai-and-video-call (Duolingo blog, 2025-04-22; accessed 2026-09-22)

- Two additions were required once this shipped. A **mid-flight evaluation** asks whether the user wants to lead the conversation, and if so instructs the model to **abandon the agenda it was going to pursue**.
- And a **programmed Closer** — after N turns the system tells the character it is time to go — because a generative session **has no intrinsic stopping point**. The ending must be injected, not hoped for.
- **Tension, with the real failure verbatim.** Duolingo shipped the rigid version first. A learner said they had finished the whole Spanish course, and the character replied **"That's nice. Have you heard about Swiss folk music?"** An agenda plus a conversational surface produces the worst failure in the category — visibly ignoring what the user just said.

## The transferable pattern

- **Enumerate the moves your interaction actually makes.** Most conversational features have four to six — open, ask, acknowledge and extend, redirect, resolve, close. Write one prompt per move.
- **Select the next move with code, not with the model.** Explicit rules over observable state. A model choosing its own next move re-creates the single-prompt problem one level up.
- **Pass forward a transcript, not a context.** Each call gets what was said; it does not need to have been present.
- **Add an override that beats the agenda.** A cheap check each turn for whether the user has taken the lead, with the authority to discard the planned move. Without it, the more competent your planning is, the more rudely the system ignores people.
- **Program the ending.** Decide the stopping condition — turn count, objective met, time — and have the system state it. Sessions that do not end are a cost problem before they are a quality problem.
- **The payoff is debuggability.** When something goes wrong you can name which move produced it, fix that prompt, and regression-test it alone.

## Apply to your product

- Write down every distinct move your AI interaction makes. Is one prompt carrying all of them?
- What observable signal would tell you the user has taken the lead, and what does your system currently do with that signal?
- How does a session in your product end today — and what happens if the user never stops replying?

## See also

[[isolate-the-high-stakes-generation]] · [[memory-as-extracted-facts-not-transcripts]] · [[human-authored-frame-model-improvises-inside]]
