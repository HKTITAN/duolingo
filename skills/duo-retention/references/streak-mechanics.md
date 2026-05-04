---
name: duo-retention-streak-mechanics
summary: A daily counter that increments with consistent action and resets on miss; the canonical investment mechanic.
metadata:
  internal: true
---

# Streak Mechanics

## Concept

A streak is a counter that increments each day the user takes a small qualifying action and resets (or shrinks) when they don't. It is the load-bearing **investment** beat in Duolingo's [[habit-loop]] — every day completed is a day the user does not want to throw away.

A streak is a [[loss-aversion]]-powered habit engine. Without loss aversion as the underlying force, it's just a number.

## What Duolingo does

- The streak resets to zero on a missed day — the cliff is intentional, not friendly.
- The qualifying action is small (one short lesson) so the bar to extend never feels like effort once the habit is formed.
- Streaks are made socially visible (profile, leaderboards) so they accrue identity weight, not just numerical weight.
- Long streaks unlock badges, milestones, and occasional press cycles ("365-day club") that reinforce identity.
- The reset rule has one explicit exception: [[streak-freeze]].

## The transferable pattern

A streak works when:

1. The qualifying action is **trivially achievable** even on a bad day. If the bar is too high, the streak is fragile and users abandon at the first slip.
2. The reset rule is **clear and harsh**. Soft resets feel paternalistic and weaken loss aversion.
3. The counter accumulates **identity**, not just points. "I'm a 200-day streak person" is the actual mechanism.
4. There is a **safety valve** ([[streak-freeze]]) — without it, one bad week forces churn.

Streaks fail when the action grows in scope, when resets feel arbitrary, or when there's no recovery path after a break.

## Apply to your product

- What is the *minimum* qualifying action a user must do daily? Make it smaller.
- Is your reset rule legible to a new user in one sentence?
- What identity does a long streak give the user that they would lose by stopping?

## See also

[[habit-loop]] · [[streak-freeze]] · [[loss-aversion]] · [[../duo-voice/references/threat-copy]]
