---
name: duo-memory-and-decay-give-mastered-things-a-visible-decay-state
summary: A permanently-complete badge is a lie; let the completed thing visibly degrade so the review request lives in the map instead of a notification.
metadata:
  internal: true
---

# Give Mastered Things a Visible Decay State

## Concept

Capability decays whether or not the interface admits it. A badge that says COMPLETE forever is therefore a factual claim your product keeps making after it has stopped being true — and the cost is not cosmetic. The user believes the thing is banked, stops maintaining it, loses it, and blames the product rather than the gap.

The fix is to model completion as a state that degrades on a schedule and to render that degradation. This moves the review request out of a push notification — an interruption the user resents, arriving from outside — and into the map they are already scanning. And it inverts the emotion: restoring something that visibly cracked is a satisfying action with a clear before and after, where "please review this" is an obligation.

A maintenance loop is not a nagging system. It is the difference between an acquisition funnel and a product whose value depends on retained capability.

## What Duolingo does

Source: blog.duolingo.com/how-weve-improved-the-duolingo-learning-experience-this-year-and-a-sneak-peek-toward-2020 (Duolingo blog, 2019-12-11; accessed 2026-09-22)

- When the spaced-repetition algorithm decided a skill was due, the gold **Level 5 skill icon became a visibly "shattered" icon**, and a single practice lesson restored it to gold. The decay was a rendered state on the object itself, not a message about the object.
- **The tension is in the same post, stated by Duolingo:** the previous redesign — **Crown Levels** — had *removed* explicit spaced repetition at the skill level. The shattered icon was them designing their way back out of a regression they had shipped. A progression redesign that optimizes for forward motion will quietly delete your maintenance loop, and you will not notice until capability starts rotting.
- **Mark as retired:** this is the crowns-and-tree era. Duolingo has since replaced the branching tree with the linear **path**, so the specific shattered-crown artifact is not the current interface. The pattern — decay rendered on the object, restoration as a one-action fix — is what carries.
- The framing Duolingo gives users is a trained physical capability, not an endpoint: if you used to run an 8-minute mile, you would not assume you could do it today. The prescription is daily low-intensity exposure over occasional heavy sessions (blog.duolingo.com/how-to-stay-fluent (Duolingo blog, 2024-10-01; accessed 2026-09-22)).
- Their own staff describe this as the normal condition rather than a failure mode — capability is a level you maintain, and it fluctuates with current exposure (blog.duolingo.com/what-does-it-feel-like-to-be-bilingual (Duolingo blog, 2023-09-19; accessed 2026-09-22)).

## The transferable pattern

1. **Make "complete" a decaying state in the data model.** If completion is a boolean that only ever flips one way, every downstream surface will inherit the lie.
2. **Render the decay on the object**, in the view the user already visits. This is the whole trick: it converts an outbound interruption into an inbound observation.
3. **Make restoration one action with a visible result.** Cracked to whole. If repairing costs more than the badge is worth, nobody repairs anything.
4. **Tell users at the point of completion that it will fade.** Expectation-setting here is what prevents the user from reading their own decay as personal failure.
5. **Audit every progression redesign for the maintenance loop it deletes.** Forward-motion redesigns are attractive, measurable and quietly load-bearing in the wrong direction.
6. **Do not weaponize it.** Decay used as guilt is a notification with extra steps; the state should be informative and the repair should feel good.

## Apply to your product

- What does your product currently mark as permanently done? Is it still true a year later?
- If you rendered staleness on those objects, which screen would carry it — and how many of your notifications could you then delete?
- Who owns the maintenance loop in your roadmap? If nobody does, which upcoming redesign is going to remove it without noticing?

## See also

[[decay-is-graded-and-fine-grain-goes-first]] · [[make-forward-motion-do-the-reviewing]] · [[../duo-retention/references/notification-discipline]] · [[../duo-gamification/references/progression-design]]
