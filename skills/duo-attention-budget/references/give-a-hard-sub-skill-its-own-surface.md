---
name: duo-attention-budget-give-a-hard-sub-skill-its-own-surface
summary: Move a hard sub-skill onto a dedicated surface so the main flow can assume it is in progress rather than blocking on it.
metadata:
  internal: true
---

# Give a Hard Sub-Skill Its Own Surface

## Concept

Two concurrent demands on attention degrade both. When a prerequisite sub-skill and the main task compete inside the same unit, the user does neither well — and the resulting failure is ambiguous, so they read it as "I am bad at this" rather than "I have not got that one piece yet."

The move is structural: give the sub-skill its own surface. The main flow then stops blocking on mastery and can assume the sub-skill is *in progress* — improving on a parallel track — while every step of the main flow stays about the thing it is actually for.

## What Duolingo does

Source: blog.duolingo.com/learning-to-read-japanese-characters (Duolingo blog, 2023-09-06; accessed 2026-09-22)

- Duolingo added a **separate character tab** on the Japanese home screen, with **three sub-tabs — hiragana, katakana, kanji** — carrying tracing, spelling, and reading drills.
- The reason: decoding the symbol and decoding the sentence's meaning were competing inside the same exercise, so learners did neither well and got discouraged. With a dedicated tab, main-path lessons stay focused on sentence meaning.
- The scale that makes this unavoidable: **46 hiragana characters**, each one a syllable, against **thousands of kanji**. That is exactly the load you do not want sitting inside the main loop.
- The tradeoff Duolingo took on: a second surface is a second thing to maintain, a second place to be discovered, and a second progress model that can diverge from the main path. Splitting also means a user can advance the main path while the sub-skill lags — which is the point, but it means the main path must be designed to tolerate a weak prerequisite rather than assume a strong one.

## The transferable pattern

- **Diagnose by asking what two things are being demanded at once.** If a step requires both a prerequisite mechanic and the actual judgement, and users fail at a rate that surprises you, the two are competing.
- **Split the prerequisite onto a dedicated surface** with its own practice, its own pacing, and its own sense of progress. Sub-dividing it further is worth it when the sub-skill has genuinely different modes.
- **Let the main flow assume "in progress," not "mastered."** Design the main path so a user with a half-learned prerequisite still gets meaning out of it — supports, fallbacks, or partial credit — instead of gating entry on the prerequisite.
- **Watch the scale signal.** When a prerequisite is bounded and small, inline it. When it is large or open-ended, it will never fit inside the main loop and trying to squeeze it there quietly ruins both.
- **Pay the costs knowingly.** Another surface means another discovery problem, another progress model, and the possibility of the two tracks drifting apart. The gain is that neither task is degraded by the other.

## Apply to your product

- What prerequisite does your main flow silently assume — a notation, a mental model, a query language, a file format — and where does it show up as unexplained failure?
- If that prerequisite had its own place to practise, what could the main flow stop blocking on?
- How would your main path behave for a user whose prerequisite is only half learned? Does it degrade usefully, or does it just fail?

## See also

[[isolate-the-new-element-at-the-front]] · [[hold-everything-but-the-target-constant]] · [[../duo-product/SKILL]]
