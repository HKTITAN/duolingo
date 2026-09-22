---
name: duo-progression-design-scaffold-and-fade-on-a-schedule
summary: Support starts high and decays on a planned schedule; the fade is the design, not an afterthought.
metadata:
  internal: true
---

# Scaffold and Fade on a Schedule

## Concept

Drop someone into the unsupported version of a hard task and you produce failure, not difficulty — they learn that the task is impossible, which is the opposite of what you wanted. So support has to start high. But if the support stays, the user keeps routing through it and never builds the direct capability; they become fluent in the scaffold instead of in the thing. The only version that works is support that starts high and decays on a schedule you designed before you shipped the first easy version. The fade is the product decision. The scaffold is just the on-ramp to it.

## What Duolingo does

Source: blog.duolingo.com/duoradio-listening-practice (Duolingo blog, 2023-11-02; accessed 2026-09-22)

- DuoRadio episodes **start bilingual** — using both the user's existing language and the target one — and **gradually move to fully target-language episodes**. The support is scheduled out episode by episode, not left to a settings toggle.
- Each episode is deliberately built from words, phrases and grammar the user met in their **recent lessons**, recombined in a new context. Re-encountering an item outside its original drill is what converts drill-bound recognition into usable knowledge, because the memory stops being cued by the drill's surface form.
- Comprehension checks (matching, listen-and-select) are embedded **mid-episode**, so the easy channel does not turn the session into passive consumption. Launched across the Spanish, French, German, Japanese and Italian courses for English speakers.
- The same fade runs inside ordinary lessons. Listening exercises **early in a unit present the audio alongside the written words; at higher levels the same exercise arrives as audio with no text at all** — plus a turtle button to slow playback and unlimited replays, so the user controls rate while the system controls the fade (blog.duolingo.com/covering-all-the-bases-duolingos-approach-to-listening-skills (Duolingo blog, 2026-05-05; accessed 2026-09-22)).
- Difficulty also ramps *within* a task type rather than by swapping task types: courses start on single words and short phrases immediately, **front-load each unit with recognition-focused exercises**, then lengthen and complicate sentences gradually across the course (blog.duolingo.com/covering-all-the-bases-duolingos-approach-to-reading-skills (Duolingo blog, 2025-02-10; accessed 2026-09-22)).

## The transferable pattern

Write the fade schedule at the same time you write the scaffold, and treat "when does this come off" as a required field.

Three mechanics worth stealing:

- **Pair the hard channel with an easy one, then strip the easy one.** Transcript beside the audio, annotation beside the raw output, generated code beside the config, worked answer beside the problem. Same task, one fewer support each stage.
- **Ramp inside a fixed task type.** Keep the shape of the task stable while length or complexity rises, so when a user fails they can tell it was the load, not the format. Changing both at once makes failure uninformative.
- **Recombine old material in new surroundings.** A support that only ever appears in the same wrapper trains recognition of the wrapper. Re-present the same content in a different context and you find out whether the capability actually transferred.

Keep two controls separate: **rate** (replay, slow down, pause) can stay forever, because it costs nothing and removes anxiety. **Support** (the parallel easy channel) must decay, because it substitutes for the skill. Confusing the two is how a product ends up with a permanent crutch that everyone defends as an accessibility feature.

## Apply to your product

- Name one support in your product that has no removal schedule. What would the user be able to do unaided six sessions from now if it decayed instead?
- Which of your controls are rate controls (safe to keep) and which are substitution controls (must fade)?
- When a user fails a step, can they tell whether it was the difficulty or the changed format? If not, you are ramping two variables at once.

## See also

[[make-the-scaffold-removable-by-the-user]] · [[the-crutch-that-makes-you-cheap-to-build]] · [[recognition-then-guided-then-production]] · [[../duo-gamification/references/ramp-up-difficulty]]
