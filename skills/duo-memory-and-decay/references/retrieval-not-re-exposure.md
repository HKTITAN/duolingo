---
name: duo-memory-and-decay-retrieval-not-re-exposure
summary: Review that shows the answer strengthens recognition; review that makes the user produce it cold strengthens the thing real use requires.
metadata:
  internal: true
---

# Retrieval, Not Re-Exposure

## Concept

Spacing only pays off if the spaced event is a retrieval. Re-reading, re-watching or skimming a highlight reel is re-exposure: the cue does the work, the user feels fluent, and almost nothing is strengthened. This is the fluency illusion — ease of processing mistaken for mastery.

Picking the right answer from options you supplied is the same failure in interactive clothing. The trace that gets strengthened is "that looks right," not "produce this from nothing." Real use never supplies the option set, so recognition practice trains a capability that does not transfer, and recognition-based tests systematically overstate what the user actually has.

Physical production — typing, tracing, assembling, saying it out loud — goes one step further: it adds a motor retrieval route to the same memory and forces commitment to a complete representation rather than selection among presented ones.

## What Duolingo does

Source: blog.duolingo.com/spaced-repetition-for-learning (Duolingo blog, 2023-12-26; accessed 2026-09-22)

- Duolingo's guidance always pairs spacing with active recall: answer the review question and *then* check; with a flashcard, force the recall before flipping. The exercise design makes the learner produce rather than recognize.
- **Flashcards** (launched **November 2025**) ship as stacks of **5 cards** showing a word in the learner's own language, requiring them to say or type the translation unaided. The framing is explicit: recognizing a word is one thing, recalling it in the moment is an entirely different task (blog.duolingo.com/duolingo-flashcards (Duolingo blog, 2025-11-18; accessed 2026-09-22)).
- For the **10 languages Duolingo teaches in non-Latin writing systems**, lessons recruit motor encoding directly: tracing Arabic letters with a finger along a directional guide, dragging components to assemble Korean syllable blocks, a reference chart paired with drills rather than multiple choice alone (blog.duolingo.com/learning-other-writing-systems (Duolingo blog, 2021-07-22; accessed 2026-09-22)).
- A staff study routine pushes the same rule to its limit: never turn off speaking exercises, use the microphone to speak answers "even when I could have typed them," write lists by hand from memory — because producing from scratch is what the real situation will demand (blog.duolingo.com/how-to-learn-german-for-travel (Duolingo blog, 2022-11-21; accessed 2026-09-22)).

**The tension, admitted in that last post:** production is context-dependent. The same author skipped speaking exercises on a subway platform. A product that *requires* production has to degrade gracefully when the environment forbids it, or it just gets skipped — and a skipped retrieval is worth less than an easier one that happened.

## The transferable pattern

1. **Audit what your review surface actually asks for.** If the answer is visible at the moment the user engages, you built re-exposure and are measuring it as practice.
2. **Make the user commit before the reveal.** An answer typed, spoken, drawn or chosen-then-defended before feedback is a retrieval. A summary the user nods along to is not.
3. **Prefer production to selection when the stakes justify the friction.** Selection is cheap and scales; production is where transfer comes from. Reserve production for the items that carry real consequence downstream.
4. **Never certify on recognition.** If your assessment offers options and the real task does not, your pass rate is measuring the wrong capability and will look fine right up until the field contradicts it.
5. **Have a low-friction fallback.** Detect the context that forbids the hard mode and offer the easier retrieval rather than nothing.

## Apply to your product

- Where in your product does a user confirm they know something without ever producing it? What would the produce-it version look like?
- Which of your success metrics are recognition-shaped, and what would happen to them if you switched to unaided production tomorrow?
- What is your graceful degradation when the user cannot do the effortful version — hands full, in public, on a slow connection?

## See also

[[three-conditions-for-practice-to-pay]] · [[delay-the-retry-and-weight-the-queue]] · [[vary-the-encoding-context]]
