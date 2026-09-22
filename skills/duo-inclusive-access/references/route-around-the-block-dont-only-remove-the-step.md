---
name: duo-inclusive-access-route-around-the-block-dont-only-remove-the-step
summary: Removing an inaccessible step preserves access; rerouting it through an intact adjacent capability preserves the outcome.
metadata:
  internal: true
---

# Route Around the Block, Don't Only Remove the Step

## Concept

A skip is the floor, not the ceiling. When you delete an inaccessible step you keep the user in the product, but you also delete whatever that step was producing for them. Rerouting is the better move when it is available — find an intact capability that reaches the same outcome by a different path, and offer that instead of an absence.

The reason rerouting works more often than intuition suggests is that capabilities which feel like one faculty are usually served by overlapping machinery. A function lost through one route can sometimes be rebuilt through a neighbouring route that is still working. This is why "you can't do X" is rarely the end of the analysis: the right question is what X was *for*, and what else in the person's repertoire produces that.

## What Duolingo does

Source: blog.duolingo.com/music-and-language-in-the-brain (Duolingo blog, 2023-12-13; accessed 2026-09-22)

- Duolingo published the mechanism behind melodic intonation therapy: patients who lose speech to left-hemisphere damage can relearn it by **singing**, because singing engages the right hemisphere, and over time the speech network rewires onto the healthy side. The capability was not restored by lowering the demand — it was restored by delivering the same demand down a different channel.

Source: blog.duolingo.com/learning-with-hearing-aids (Duolingo blog, 2026-01-20; accessed 2026-09-22)

- The product-side analogue has the same shape. An audio exercise that a user cannot hear is not only skippable: "Repeat what you hear" offers a **Reveal** that shows the text while the character says it again, so the exercise is completed by reading plus watching rather than by hearing.
- The channel changes rather than the demand: the same item is completed by reading and watching instead of by hearing. Reveal ships *alongside* the skip options rather than replacing them — see [[escape-hatches-at-the-granularity-of-the-blocked-modality]] for the four graduated hatches it sits next to.

## The transferable pattern

For each blocked step, write down the outcome it was supposed to produce, separately from the mechanics of how it produces it. Then look for another route to that same outcome using something the user still has. A visual channel substituting for an auditory one, a typed channel substituting for a spoken one, an asynchronous channel substituting for a live one — the substitution is legitimate when it lands the same result, and it is a cop-out when it only lands the same checkbox.

Ship both layers. The skip is the safety net that guarantees nobody is stuck; the reroute is what makes the accommodation worth having rather than merely tolerable. And be honest in your own metrics about which one a user took, because a population that always routes around a step is telling you the primary path is wrong for more people than you modelled.

## Apply to your product

- Take your least accessible required step. What is it actually producing for the user — information, a decision, a confirmation, a piece of practice? Which of those could arrive another way?
- Do you currently ship a skip where a reroute was possible, because the skip was a one-line change?
- If you instrument the alternate path, would you be willing to act on the result if most users chose it?

## See also

[[a-slow-decomposed-version-is-not-the-answer-key]] · [[never-penalise-what-you-are-not-measuring]] · [[../duo-design/SKILL]]
