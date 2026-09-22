---
name: duo-rules-and-heuristics-two-memory-systems-explanation-loads-the-wrong-one
summary: Knowing a rule and being able to run it live in different memory systems; documentation only builds the first.
metadata:
  internal: true
---

# Two Memory Systems — Explanation Loads the Wrong One

## Concept

Being able to state a rule and being able to act on it are stored separately. Explicit memory holds facts and is built by being told. Implicit memory holds skills and procedures and is built only by doing. The proof is everywhere: almost nobody can state the rules of the system they operate most fluently, and they operate it perfectly anyway. So a document, however correct, loads the store that does not drive performance — and a consciously retrieved rule can actively slow a person down, because the lookup step costs more time than the moment allows.

## What Duolingo does

- Duolingo's learning scientists split **implicit memory** (instincts for what sounds right) from **explicit memory** (being able to describe how the system works), and state that if the goal is use, knowing how to describe a conjugation does not get you there. Source: blog.duolingo.com/what-is-memory (Duolingo blog, 2023-01-24; accessed 2026-09-22)
- Course design has learners produce and recognise new material in their **very first lesson**, before any rule is stated, with exercises that visually foreground the relevant information so the pattern gets noticed rather than announced. The post's own illustration: nobody recites a conjugation rule mid-conversation. Source: blog.duolingo.com/what-is-implicit-learning (Duolingo blog, 2023-08-03; accessed 2026-09-22)
- The measurement consequence is stated directly: implicit knowledge surfaces as a hunch, not as knowledge — "our brain doesn't announce what it's learned." Duolingo documents rules its own fluent readers demonstrably follow and have never consciously noticed (no possessive after "the"; /ʊ/ always needs a following consonant). Source: blog.duolingo.com/how-your-brain-finds-patterns (Duolingo blog, 2023-07-27; accessed 2026-09-22)
- Duolingo goes further and argues that **focusing on memorising rules can hinder** a learner's ability to communicate. Source: blog.duolingo.com/can-duolingo-make-me-fluent (Duolingo blog, 2024-11-18; accessed 2026-09-22)

**Tension.** This is not a clean win for implicit-only. Duolingo later shipped Grammar Skills and Smart Tips into its four biggest courses because pure implicit learning was not sufficient — targeted explanation at the point of error measurably reduced subsequent errors. The honest position is that explanation cannot substitute for use, not that explanation is worthless. See [[where-explicit-instruction-earns-its-place]].

## The transferable pattern

Two consequences, one for building and one for measuring.

**Building.** If users will perform an action under time pressure, no volume of documentation produces competence at it. Rule text is retrieved consciously and slowly, which is exactly wrong for real-time work, and the retrieval consumes the working memory the task itself needs. The lever is repetitions under realistic conditions, not a better-written page.

**Measuring.** Never test whether someone has learned something by asking them to explain it. Articulation and competence are separate systems, so an explanation test understates real capability and rewards the wrong preparation. Test whether they choose correctly, fast, with the real distractors present. A user who cannot describe the rule but picks right every time has learned it. A user who recites it and then hesitates has not.

This also reframes a common complaint. "Our users clearly didn't read the docs" is usually false. They read them, stored them in the wrong place, and could not retrieve them at the decision point.

## Apply to your product

- Take the one thing your users most often get wrong. Is your current fix a better explanation, or more reps of the decision itself?
- How do you currently certify that someone knows your system — a quiz they can answer at leisure, or a timed decision with realistic distractors?
- Which of your power users could not write your own documentation if you asked them to? What does that tell you about where their skill actually lives?

## See also

[[explanation-lands-at-the-moment-of-the-error]] · [[let-them-induce-it-from-volume-then-confirm]] · [[the-practitioner-cannot-state-their-own-rule]]
