---
name: duo-localization-localize-to-a-consumption-budget
summary: Translate to what the consumer can process — reading speed, pixels, timing — ranking information by importance and preserving intent over words.
metadata:
  internal: true
---

# Localize to a Consumption Budget

## Concept

The binding constraint on a translation is almost never fidelity to the source. It is the consumer's processing rate — how fast they read, how long the text is on screen, how much of the interface they can take in before acting, and how much command of the medium they actually have. An accurate rendering that cannot be consumed in the time and space available has failed at the only job it had. Accept the budget first and the work changes shape: instead of matching words you are ranking information by importance, deciding what is expendable, and carrying intent rather than vocabulary.

## What Duolingo does

Source: blog.duolingo.com/how-are-subtitles-made (Duolingo blog, 2022-09-28; accessed 2026-09-22)

- Duolingo's globalization lead, previously a subtitler at a major streaming company, describes the craft as budget-first — translators cut words not critical to the story so that a viewer can finish reading inside the speaker's time.
- The unit of preservation is intent, not literal meaning. German *weltschmerz*, literally "world pain", is rendered as feeling like you are carrying the world on your shoulders — longer than the word, shorter than the footnote, and consumable at speed.
- This is also what makes supposedly untranslatable concepts translatable: once you are preserving intent, there is no requirement that a word map to a word.
- Duolingo's localization team applies the same method to push notifications and in-app copy, which have their own budgets — a notification tray line, a button, a toast.

Tension, stated openly: the balance between direct translation, timing fit and emotional connection has no fixed answer. It sits somewhere in the middle and is decided case by case, which means it cannot be delegated to a rule or a glossary.

Source: blog.duolingo.com/what-is-translanguaging (Duolingo blog, 2023-01-23; accessed 2026-09-22)

- The same logic applied to users rather than text. Duolingo publishes translanguaging — Ofelia García's framework covering code-switching, translation and biliteracy — with an explicit level rule: you can use it at any level, which helps you start using a new language right away.
- The framing matters as much as the permission. Its guidance ends by telling teachers to have students participate using their full repertoire so that those practices are "the norm, not an exception" — because a behaviour that is permitted but marked still reads as deviant, and people avoid it.

## The transferable pattern

- **Name the budget before the copy.** Characters, seconds on screen, words before a scroll, taps before the action. A translator or writer without a number will optimise for completeness and blow it.
- **Rank, then cut.** Decide in advance which piece of information is load-bearing and which is decoration, so the cut is a content decision made once rather than a truncation made by a renderer.
- **Preserve intent, not vocabulary.** The unit that must survive is what the user should understand or feel, not the source sentence. This is the only way concepts with no local equivalent ever ship.
- **Accept that the accuracy-versus-fit balance is a judgement call.** Codify the budget; do not try to codify the tradeoff. Route it to a person who knows the market.
- **Let partial competence participate, and make the mixed mode normal.** Gating use on full command removes exactly the practice that produces command — and an accommodation framed as an exception tells users they do not belong, so they opt out of the participation you were enabling.

## Apply to your product

- For your three highest-traffic strings, what is the actual budget — how many characters, and how long is it on screen before the user must act?
- When a translation does not fit, does someone decide what to drop, or does a component decide for you?
- Where does your product require full command of something — a language, a format, a jargon — before it will let a person participate at all, and is the halfway mode framed as normal or as a fallback?

## See also

[[layout-overrides-your-content-policy]] · [[localize-into-the-register-people-speak]] · [[../duo-inclusive-access/SKILL]]
