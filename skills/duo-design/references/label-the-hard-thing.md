---
name: duo-design-label-the-hard-thing
summary: Tell users a task is hard before they attempt it — the label moves blame for failure onto the task and converts success from baseline into achievement.
metadata:
  internal: true
---

# Label the Hard Thing

## Concept

When someone fails at an unlabelled task, they attribute the failure to themselves: *I am bad at this.* When the interface said in advance that the task was hard, the same failure gets attributed to the task: *that was the hard one.* The label costs a single line of UI and pays on both sides of the outcome — it raises tolerance for failing and it upgrades succeeding from "did the normal thing" to "beat the hard thing." Most products do the opposite, hiding difficulty to avoid scaring people off, and so spend their hardest moments manufacturing self-doubt.

## What Duolingo does

Source: blog.duolingo.com/duolingo-difficult-exercises (Duolingo blog, 2021-09-24; accessed 2026-09-22)

- When the system serves an adaptively harder exercise, it shows a small **difficulty indicator at the top of the screen** — an explicit "this is a hard exercise," delivered before the attempt rather than as consolation after it.
- The indicator is a single lightweight element in the existing header region, not a modal, an interstitial, or a separate screen. The cost of the intervention is close to zero.
- Reported outcomes were all directional and all positive: learners **spent more time studying**, were **more likely to return the next day**, and were **more likely to start a paid trial**. Signalling difficulty did not drive people away; it made the harder content feel worth doing.
- The framing pairs with how Duolingo has softened the price of ordinary failure elsewhere — mistakes are made cheap so that attempting hard things stays rational ([[error-as-delight]]).

## The transferable pattern

Three rules:

1. **Label before, not after.** Difficulty shown after a failure reads as an excuse the product is making for itself. Shown before, it is a contract the user accepted.
2. **Keep the label small and in place.** It is a stakes marker, not a warning screen. Anything heavy enough to interrupt will be read as a suggestion to back out.
3. **Only label what is genuinely harder.** A difficulty marker that appears everywhere is a badge, and a badge that never means anything gets ignored — then the real ones are ignored too.

Anti-patterns:
- Hiding difficulty to protect completion rate, which protects the number and damages the person.
- Labelling difficulty without changing anything else, so hard tasks carry the same reward, the same feedback, and the same consequence for failing.
- Using difficulty labels as a paywall tease rather than as an honest description of the task.

## Apply to your product

- Which steps in your flow have the highest failure rate, and does the user know in advance that they are the hard ones?
- When a user fails one of those steps, does your copy leave them attributing the failure to themselves?
- Do your hardest tasks get any more recognition on success than your easiest ones?

## See also

[[error-as-delight]] · [[celebration-design]] · [[../duo-gamification/references/ramp-up-difficulty]] · [[../duo-voice/references/error-copy]]
