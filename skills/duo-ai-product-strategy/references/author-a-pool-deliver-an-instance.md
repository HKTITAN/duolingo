---
name: duo-ai-product-strategy-author-a-pool-deliver-an-instance
summary: Make the unit of authorship larger than the unit of delivery — experts write a pool, the system assembles each user's instance from it.
metadata:
  internal: true
---

# Author a Pool, Deliver an Instance

## Concept

Personalization is only cheap when the expensive artifact is not the one you deliver. If your experts author the thing the user receives, then personalizing for N users means authoring N times, and the cost of personalization is the cost of your most expensive people multiplied by your user count. No model fixes that arithmetic; it only makes the authoring slightly faster.

The move is to raise the unit of authorship above the unit of delivery. A human authors a large, judgment-heavy object; a deterministic process derives many candidate instances from it; a selection model picks which instance this user gets right now. Human judgment is then amortized across every instance the object can produce, and personalization costs a lookup rather than a headcount.

## What Duolingo does

Source: blog.duolingo.com/how-duolingo-experts-work-with-ai (Duolingo blog, 2022-09-14; accessed 2026-09-22)

Three distinct layers, and the separation between them is the whole trick:

1. **Authored once, by people.** Content developers write "raw" content per lesson — sentences, dialogues, paragraphs. This is the judgment-heavy artifact, and it is not what any learner is served directly.
2. **Derived mechanically.** Algorithms expand the raw content into a pool of exercise variants. This step adds no new judgment; it only multiplies what the expert already decided.
3. **Selected per user, at request time.** The Birdbrain model picks which items from that pool a given learner sees at that moment, so **no two learners get the same lesson**.

Note where this sits in the pipeline described in [[stage-split-humans-set-constraints-models-multiply]] — layers 2 and 3 are the "mostly AI" and "almost entirely AI" stages, and they are cheap precisely because layer 1 already fixed the constraints they operate inside. The expert never sees the combinatorial explosion; they see one lesson's worth of raw material.

**Tension.** Everything downstream inherits the authored object's blind spots. If the pool is derived from raw material that is narrow or repetitive, personalization faithfully delivers a personalized version of the same narrowness — and because each user sees a different slice, that sameness is hard to detect from any single session. Derivation multiplies quality and flatness with equal efficiency, which is the failure [[simplify-until-automatable-name-what-must-survive]] is about.

## The transferable pattern

Ask one design question — **what is the largest thing a person can author once that the system can still cut many ways?** Too small and you are back to authoring per delivery; too large and the derivation step needs judgment you cannot automate.

Then keep the three layers honest:

- **Authorship** holds all the judgment and is versioned and reviewable as a unit.
- **Derivation** is mechanical and adds no judgment. If your expansion step needs a human to sanity-check each output, it is not derivation, it is authoring wearing a costume.
- **Selection** is where the per-user model lives, and it can only choose among things an expert already approved. That constraint is what makes personalization safe to automate.

The economic test: when you double your users, does authored work go up? If yes, your authorship unit is still the delivery unit.

## Apply to your product

- What do your experts produce today, and is it the thing the user receives? If so, what larger object sits one level above it?
- Could your expansion step run with no human in it — and if not, which specific judgment is it still borrowing?
- When your user count doubles, which of your three layers grows, and which stays flat?

## See also

[[stage-split-humans-set-constraints-models-multiply]] · [[spend-the-automation-budget-on-the-gate]]
