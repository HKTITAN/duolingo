---
name: duo-difficulty-calibration-the-narrow-band-between-bored-and-lost
summary: Target a difficulty band with an upper bound as well as a lower one; the ratio of familiar to novel is the design parameter, not the total volume.
metadata:
  internal: true
---

# The Narrow Band Between Bored and Lost

## Concept

Difficulty is usually treated as a floor: make sure it is hard enough to be worth doing. That is half a specification. Too far past the user's current capacity and they lack the surrounding context to bridge the gap, so they disengage from frustration; at exactly their current capacity nothing new is encoded, so they disengage from boredom. Both failure modes cost you the same user.

The fix is to specify a **band**, and to control it with a ratio rather than a volume. A session that is overwhelmingly made of things the user already handles, with a small deliberate dose of the genuinely new embedded inside it, gives the new material a familiar surround to attach to. That ratio — not session length, not item count — is the dial. Doubling the session while holding the ratio keeps the experience calibrated; holding the length while raising the novel fraction breaks it.

## What Duolingo does

Source: blog.duolingo.com/right-level-of-difficulty (Duolingo blog, 2024-04-02; accessed 2026-09-22)

- Courses are built on Krashen's **"i + 1"** and Vygotsky's zone of proximal development. Learning designers track every word and structure already taught (the "i"), and each lesson introduces only **5–7 new items**, placed inside sentences built entirely from already-known material, with the new word visually flagged.
- Stories target a **90 / 10 split** — 90% previously-seen vocabulary and grammar, 10% new.
- Both failure modes are named explicitly: **i+20** produces discouragement and quitting; **i+0** produces stagnation and boredom.
- **The tension.** The unexplained 10% is a cost paid on purpose — unknown items train the user to infer from context. But where something is genuinely unguessable, Duolingo inserts an explicit comprehension check rather than trusting inference. The deliberate gap has a floor under it.

Source: blog.duolingo.com/why-can-learning-feel-overwhelming (Duolingo blog, 2024-12-24; accessed 2026-09-22)

- When load runs persistently too high, learners miss crucial information, draw incorrect connections between pieces, and lose motivation to continue. Duolingo revisits the load question whenever it builds a new course or updates an old one — not once at launch.

Source: blog.duolingo.com/are-some-people-better-at-learning-languages (Duolingo blog, 2023-07-25; accessed 2026-09-22)

- Among the factors Duolingo says actually determine outcomes is "whether you push yourself to do the hard things" — best results at the cusp of current knowledge, contrasted explicitly with coasting through an easy review while half-attending to something else.

## The transferable pattern

Write the specification as an interval, not a threshold, and enforce both ends.

1. **Name the upper failure mode.** "Too hard" needs a behavioral definition — abandonment, repeated retry, help-seeking — or your system will optimize toward the floor forever.
2. **Control the ratio, not the volume.** Fix the fraction of each session that is genuinely new, and let total length vary independently. A small fixed dose embedded in known material is a different experience from the same dose delivered alone.
3. **Make the new element visible.** Flagging what is new tells the user which part of the difficulty is intentional, which is the difference between a stretch and a bug.
4. **Put a floor under the deliberate gap.** Leaving some fraction unexplained is a real technique — as long as anything genuinely unrecoverable gets an explicit check rather than being left to inference.

## Apply to your product

- What fraction of a typical session is material your user has already handled successfully? If you cannot answer that number, it is not a parameter — it is an accident.
- What is your equivalent of the upper bound, and what behavior would tell you a user has crossed it?
- When something new appears, can the user tell it is new? What would it cost to mark it?

## See also

[[model-the-item-and-the-user-jointly]] · [[read-error-rate-with-completion-rate]] · [[users-will-grind-what-they-already-know]] · [[../duo-attention-budget/references/familiar-content-is-a-load-reduction-technique]]
