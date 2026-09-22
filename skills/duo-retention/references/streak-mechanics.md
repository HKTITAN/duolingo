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

Source: blog.duolingo.com/improving-the-streak (Duolingo blog, 2020-11-19; accessed 2026-09-22)

- Until 2019 the streak only extended if you hit your **self-chosen daily goal**. Duolingo found that learners on the highest "intense" tier were the *least* likely to be on a streak — almost 40% of learners active two days in a row with no streak had picked "intense." The goal had become a barrier to the habit.
- They A/B tested separating the two mechanics. One lesson now extends the streak; daily-goal progress is shown beside it. Result: **+3.3% Day-14 retention, +1% daily active learners, +10.5% share of daily learners on a streak within 20 days** (+19% for new learners), all relative. A year on, just over half of daily learners held a 7+ day streak, versus about a third before.
- The streak still resets to zero on a missed day — the cliff is intentional. The one exception is [[streak-freeze]].
- Reaching 7 days is the published activation bar: those learners are **3.6x more likely to complete their course** (blog.duolingo.com/how-duolingo-streak-builds-habit (Duolingo blog, 2022-01-31; accessed 2026-09-22)).
- Streaks are made socially visible (profile, leaderboards) so they accrue identity weight, not just numerical weight.

Tension Duolingo names out loud: once the streak stopped enforcing the daily goal, **fewer learners actually reached their daily goals**. They took lower per-day output in exchange for continuity — "we can't teach people if they stop using Duolingo."

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
