---
name: duo-adoption-design-lower-the-exposure-before-you-lower-the-difficulty
summary: Users avoid high-exposure tasks because of the witness, not the difficulty; teach inside a task they already want to finish, in a consequence-free space.
metadata:
  internal: true
---

# Lower the Exposure Before You Lower the Difficulty

## Concept

When people skip the hardest part of your product, the instinct is to make it easier. Often that is the wrong dial. The thing being avoided is not the difficulty — it is being seen failing at it. Difficulty is private; exposure is not. Two design moves follow: remove the audience before you remove the challenge, and teach the mechanic inside a task the user already wants to finish rather than in front of it.

## What Duolingo does

- Duolingo's learning scientists analysed why gamers make good language learners and singled out the **game tutorial** as the mechanism: a safe place to learn mechanics and controls without serious consequences, **often woven into the narrative so players do not realise they are learning something new**.
- The same analysis names games as controlled environments that strip out the intimidating variables of real-world practice — the fear of judgment is a variable, and it is designed out.
- For learners who describe themselves as introverted, Duolingo recommends a **ladder of increasing exposure** rather than a difficulty ramp: write privately, talk to yourself, record yourself, shadow audio, then converse with an AI partner or a Duolingo character on Video Call, described as "a low-pressure way to practice" before speaking to a person.
- The ladder is **branched by level** — different suggestions for A1/A2 versus B1/B2 — so the rehearsal step is calibrated, not generic encouragement.
- Note what the rungs hold constant: the underlying task is the same at every step. Only the number of witnesses changes, from zero to one synthetic to one real.

Source: blog.duolingo.com/video-games-for-language-learning (Duolingo blog, 2023-04-04; accessed 2026-09-22)

Source: blog.duolingo.com/introvert-language-learning-tips (Duolingo blog, 2026-09-15; accessed 2026-09-22)

## The transferable pattern

Performance anxiety is a function of who is watching, and it suppresses exactly the repetition that would produce the competence that removes the anxiety. That loop does not break on its own. A zero-stakes rehearsal surface breaks it by letting the reps happen before exposure is survivable.

Design consequences:

1. **Audit your avoided steps for a witness.** Anything published, shared, scored publicly, sent to a colleague, or attached to the user's name is an exposure event, not just a hard step.
2. **Build the rehearsal rung.** A draft mode, a private sandbox, a dry run against fake data, a version nobody is notified about. Hold the task constant and remove the audience.
3. **Teach inside the task, not before it.** The desire to finish supplies the attention a tutorial needs. A mechanic learned in the act of using it is learned; a mechanic explained up front is memorized and then has to be recalled under pressure.
4. **Order the rungs so each one is a small step in exposure.** The user should never jump from private to fully public in one move.

The cheap failure mode is a front-loaded tour with no consequences and no task attached. That has removed the stakes but also removed the motivation, so nothing sticks.

## Apply to your product

- Take the step users most often abandon. Is it hard, or is it watched? What changes if you keep the difficulty and delete the audience?
- Do you have a rehearsal mode — a place to do the real thing where nothing is recorded, sent, or scored?
- Where are you explaining mechanics before the user has a reason to care? Could that explanation live inside the first task instead?

## See also

[[ship-a-coached-variant-of-the-thing-people-avoid]] · [[every-context-gated-step-needs-a-skip-and-a-fallback]] · [[../duo-product/references/intuitive-by-default]]
