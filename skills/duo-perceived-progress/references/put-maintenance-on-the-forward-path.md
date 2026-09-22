---
name: duo-perceived-progress-put-maintenance-on-the-forward-path
summary: If the only way to do upkeep is to visibly go backwards, users skip the upkeep; the cost was framing, not effort.
metadata:
  internal: true
---

# Put Maintenance on the Forward Path

## Concept

Every durable product accumulates maintenance work — reviewing what has decayed, revisiting what was done sloppily, shoring up the weak parts. It is frequently the single highest-value action available to a user. It is also the action they will avoid, because the affordance you built for it asks them to move backwards on the same display that has been telling them forward motion is the point.

The user is reading your layout correctly. If upkeep lives behind a "return to earlier work" door, doing it looks like losing ground. Interleaving the same work into the forward track changes nothing about the work and everything about whether it happens. The barrier was never effort; it was the direction the interface implied.

## What Duolingo does

Source: blog.duolingo.com/new-duolingo-home-screen-design (Duolingo blog, 2022-05-06; accessed 2026-09-22)

- The old home screen was a **tree of skills that visibly cracked when the material decayed**, and repairing one meant going back to it. That system is **retired** — do not treat it as current. It was replaced by a single linear path.
- In the path, **practice sessions and Stories are interleaved directly into the forward sequence**. Review is not a detour from the route; it is a stop on it.
- Duolingo states the framing reason plainly — reviewing should not feel like going back to old lessons, because practice is also forward progress. The design change is a relabelling of the same activity, which is precisely why it was cheap.
- The redesign also collapsed the old tree's parallel branches into **one next thing at a time**, removing the choice of which item to repair. Fewer routes means the maintenance work cannot be deprioritised by picking a different branch.

**The tension, and it is a real cost.** The cracked skill was an honest signal. It told the user exactly which material had decayed and let them target it. Folding review into the path hides that diagnosis — the system now decides what needs review, the user cannot see the decay state, and the user's own sense of what they are weak at goes unused. You are trading a visible, actionable, demoralising signal for an invisible, automatic, comfortable one. Be sure that trade is the one you want. See [[../duo-memory-and-decay/references/give-mastered-things-a-visible-decay-state]] for the case on the other side.

## The transferable pattern

- Find the highest-value action in your product that requires the user to move backwards in your own visual metaphor. That is your most underused feature, and framing is why.
- Put the maintenance work **on the forward track and label it as progress** — not as a separate mode, a cleanup tab, or a warning badge. Same work, same position in the queue as new work.
- Any state that renders as damage invites avoidance rather than repair. Decay shown as a broken thing gets ignored; decay scheduled as the next thing gets done.
- When you automate the choice of what to review, you also remove the user's ability to target their own known weak spots. Keep a deliberate route back to that, or accept you have taken it away.
- Reducing the number of visible next options makes the unglamorous item harder to skip. This is a real benefit and a real loss of agency — decide which one your users need more.

## Apply to your product

- What upkeep do your users skip, and does your interface currently make doing it look like moving backwards?
- Could that work be scheduled into the main flow as the next step, with the same visual treatment as new work?
- If you hide the decay state, how does a user who knows they are weak at something specific get to it on purpose?

## See also

[[shorten-the-unit-of-completion]] · [[name-the-capability-gained-at-the-end]] · [[../duo-memory-and-decay/references/make-forward-motion-do-the-reviewing]] · [[../duo-memory-and-decay/references/give-mastered-things-a-visible-decay-state]]
