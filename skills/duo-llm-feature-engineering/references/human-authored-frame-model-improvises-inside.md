---
name: duo-llm-feature-engineering-human-authored-frame-model-improvises-inside
summary: Humans fix the scenario, the opening line and the destination; the model improvises inside that frame, with the user's measured level injected as imperative constraints every turn.
metadata:
  internal: true
---

# Human-Authored Frame, Model Improvises Inside

## Concept

An unconstrained model drifts — off the intended difficulty, off the intended subject, off the thing the feature was for. The instinct is to script the output, which kills the reason you used a model. The alternative is to **fix the entry conditions instead of the output**.

Humans author three things — the **scenario**, the **opening message**, and **where the exchange should end up**. Those three bound the distribution the model can produce without dictating any particular response. Then, because generic output defaults to a difficulty that is wrong for almost everyone, **inject the user's measured level on every single turn**, and inject it as **imperative constraints rather than prose**. A level mentioned descriptively gets ignored; a list of hard permissions and prohibitions does not. And ship a reporting affordance with it, because the user who hit the failure is your only source of labelled failures at production scale.

## What Duolingo does

Source: blog.duolingo.com/duolingo-max (Duolingo blog, 2023-03-14; accessed 2026-09-22)

- For Roleplay, **curriculum experts write each scenario prompt, write the character's opening message, and tell the model where to take the conversation**, aligned to where the learner currently is in the course. The model improvises only inside that frame.
- **Launched March 2023 with GPT-4 in 188 countries** — Roleplay and Video Call for English speakers learning Spanish, French, German, Italian and Portuguese; Video Call only for Japanese, Korean and Chinese.
- **Reporting is one gesture** — hold the message down, pick a reason — and **those reports feed back into training**.
- **Tension.** The post concedes that technology **"is never perfect"** and commits only to working until mistakes are nearly nonexistent. This is a decision to ship a system known to be wrong sometimes, with a reporting valve attached, rather than to wait for correctness.

Source: blog.duolingo.com/chatbot-language-practice (Duolingo blog, 2024-03-20; accessed 2026-09-22)

- Every Roleplay prompt carries the learner's **CEFR level plus imperative constraints** — only A1 beginner-level language, only simple grammatical structures, only simple present tense, **while still sounding natural and grammatically correct**.
- Prompts also carry the character's **personality, speaking style, background and relationships**, so voice stays consistent across separately-generated turns.
- **Tension, stated as a balance rather than a rule.** Too difficult is discouraging and confusing; too easy and the user gains nothing. There is no safe default — only a measurement.

## The transferable pattern

- **Author the frame, not the output.** Three human-written artifacts per scenario — the situation, the first message, and the intended destination. This is a small, reusable amount of expert work that bounds an unbounded system.
- **Carry the user's measured level on every call.** Not once at session start. Every turn, from a real measurement you already hold.
- **State constraints imperatively and as permissions.** "Only use X. Do not use Y." A paragraph describing the audience is decoration; a list of allowed and forbidden constructions is enforcement.
- **Pair every difficulty constraint with a naturalness constraint**, or you get output that satisfies the limit by being stilted, which fails differently and just as badly.
- **Carry the persona explicitly too**, since consistency across independent calls comes from the prompt, not from continuity.
- **Make reporting one gesture, and wire it to training.** A report form is not a reporting affordance. If it takes more than a press and a choice, you get no data, and unlabelled failures are the ones you never fix.

## Apply to your product

- What measured signal about the user do you already hold that your prompts do not receive on every call?
- Does your prompt state audience level as prose or as explicit allowed-and-forbidden lists — and have you tested which one the output actually respects?
- How many taps does it take a user to report a bad output in your product today, and where does that report go?

## See also

[[one-narrow-prompt-per-move]] · [[isolate-the-high-stakes-generation]] · [[../duo-production-reliability/SKILL]]
