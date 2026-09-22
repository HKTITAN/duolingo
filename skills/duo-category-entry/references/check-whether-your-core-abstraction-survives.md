---
name: duo-category-entry-check-whether-your-core-abstraction-survives
summary: An abstraction that held because one domain was uniform breaks quietly in one that isn't — build depth where fan-out is real, replace it where the invariant is gone.
metadata:
  internal: true
---

# Check Whether Your Core Abstraction Survives

## Concept

Every content or data pipeline rests on an invariant nobody wrote down, because in the original domain it was simply true. When you expand into a second domain, that invariant is the thing most likely to break — and it breaks quietly, as a slow accumulation of special cases rather than a failure. Effort spent at a shared layer is multiplied by everything that depends on it, which is exactly why you must know whether the layer still holds before you invest there.

## What Duolingo does

Source: blog.duolingo.com/developing-math (Duolingo blog, 2024-10-18; accessed 2026-09-22)

- In language courses, every knowledge component — a word, a character, a phrase — is **always represented as text**. Only the prompt and the input format vary, so one exercise pipeline could serve every course.
- Math removed that invariant. The same underlying concept needs **different representations depending on context and difficulty**: addition taught with countable blocks, with integers, or inside a word problem. Rectangular perimeter is technically addition but looks nothing like it, and classifying a trapezoid requires **entirely new visuals and exercise types**.
- The abstraction was not forced. The team treated representation as a property of the concept rather than a rendering detail, which is the expensive answer and the correct one.
- Where the invariant does hold, depth at the shared layer pays for itself repeatedly. Duolingo built **one** new advanced English experience rather than customizing per source language, precisely because the design is translation-free — once built, it reached learners across **20+ English courses** regardless of first language, adding **nearly 200 new units**, with English offered to speakers of **27 languages** by 2025. Source: blog.duolingo.com/how-duolingo-teaches-english (Duolingo blog, 2024-08-07; accessed 2026-09-22)
- **Tension.** These two moves pull opposite ways. Fan-out rewards concentrating effort in the shared layer; a broken invariant means the shared layer is now a constraint. The judgement is knowing which situation you are in, and the cost of guessing wrong is asymmetric — forcing a dead abstraction costs more than replacing it.

## The transferable pattern

Before expanding, write down the invariant your core abstraction assumes. Phrase it as a sentence about the shape of the inputs — "every item is one of these three types", "every record has a single owner", "every unit renders the same way". Then ask whether that sentence is still true in the new domain.

If it holds, **build depth at the layer with the largest fan-out**. One high-quality thing built where everything else is expressed propagates to every surface that sits on it; the same effort spent on a single surface serves only that surface. This inverts the usual instinct to fix the loudest surface first. Count the dependents and let that number decide.

If it does not hold, **replace the abstraction rather than parameterizing it**. The tell is a growing pile of type flags, optional fields and per-case branches that all exist to make one shape pretend to be another. Each one is cheap; the accumulation is what makes the second domain cost three times its estimate, and it degrades the original domain too, because the shared code is now carrying cases it never needed.

The honest version of the question is not "can we make it fit" — you always can — but "what will this cost per new case, forever".

## Apply to your product

- State your core abstraction's hidden assumption in one sentence about the shape of its inputs. Is that sentence true in the domain you are about to enter?
- Which layer of your system has the highest fan-out — the most things expressed through it — and when did you last invest there rather than in the loudest individual surface?
- Where are you already adding optional fields and type flags to make one model cover two shapes? What would replacing it cost compared with another year of that?

## See also

[[port-the-method-and-the-format-vary-the-subject]] · [[port-the-incumbents-goal-not-their-safeguards]] · [[validate-in-the-cheapest-shape-first]]
