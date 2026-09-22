---
name: duo-product-teach-the-invariant
summary: Build the core on what is shared everywhere, name the axes along which variants differ, and point users outward for the rest.
metadata:
  internal: true
---

# Teach the Invariant, Name the Axes

## Concept

Variant coverage grows combinatorially and never terminates: below the country there is the region, below the region the city, then age, then class. A product that tries to model every variant inside itself takes on unbounded maintenance and is stale the day it ships. The alternative is a three-part split — build the core on the invariant that transfers everywhere, publish the **axes** along which variation happens so users can recognize differences when they meet them, and hand off the specific variant to sources more current than anything you could ship.

## What Duolingo does

Source: blog.duolingo.com/spanish-dialects (Duolingo blog, 2025-08-21; accessed 2026-09-22)

- The scale is why modelling everything is impossible: **400M+ Spanish speakers** across **20+ countries** where it is official.
- Rather than covering variants exhaustively, Duolingo profiles **6 dialects along 5 fixed axes** — pronunciation, the second-person pronoun, other languages spoken there, slang, and food words — and catalogues **5 distinct second-person pronouns** (vos, tú, usted, vosotros, ustedes) as the clearest worked axis.
- It warns up front that listed features are **neither universal within a country nor exclusive to it**, which is the honest version of "these are axes, not buckets."
- It closes with an explicit division of labour: use the product for broad foundations, and add music, film, television and social accounts from the specific country you care about. The handoff is stated, not implied.
- Where one variant must be chosen, the rule is **pick what users will actually encounter, not the prestige form**. Duolingo's Arabic course teaches Modern Standard Arabic, but specifically a less formal spoken register — "not the version that would appear in poetry or very formal news broadcasts, but instead the version that would be used once a newscaster stopped reading from their script" (blog.duolingo.com/what-makes-arabic-hard-and-why-that-shouldnt-stop-you-from-learning-it (Duolingo blog, 2026-04-27; accessed 2026-09-22)).

The tension is unresolved and stated: Modern Standard Arabic is nobody's native variety, so the choice buys universality across the whole region at the price of immediate usability in any single country. An invariant core always costs somebody their specific case.

## The transferable pattern

1. **Find the part that is true everywhere and build there.** The shared core is what makes the product transfer; variants are what make it a maintenance treadmill.
2. **Ship the axes, not the matrix.** Teaching users the four or five dimensions along which cases differ equips them for every case, including ones you have never seen.
3. **State that the axes are tendencies.** Users who take your axes as strict categories will be wrong in the field and blame you for it.
4. **Publish the handoff explicitly.** Name which sources to go to for the specific case. An unstated boundary reads as a gap; a stated one reads as scope.
5. **When one variant must be built in, pick the one users meet in the wild** — the documented, canonical form is the easiest to build against and the most likely to leave users saying "I learned this and still could not use it."

## Apply to your product

- What is the invariant core of your domain, and how much of your surface area is really variant handling?
- Could you list the axes along which your users' situations differ, on one page, today?
- Where have you built against the canonical version of something when your users encounter a messier one?

## See also

[[difficulty-with-mitigations]] · [[intuitive-by-default]] · [[ruthless-prioritization]] · [[take-the-long-view]]
