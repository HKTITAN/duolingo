---
name: duo-gamification-two-regimes-of-one-counter
summary: One accumulating counter has to motivate through two different psychologies — momentum early, protected value late.
metadata:
  internal: true
---

# Two Regimes of One Counter

## Concept

Any counter that only goes up has a built-in decay problem: each increment is a shrinking proportion of the total. The number keeps growing while the *felt* progress collapses. That means the same mechanic is doing two different jobs at two different points in a user's tenure. Early on, the number **moving** is the reward. Later, the number **existing** is the asset, and loss aversion takes over from novelty.

A counter tuned for only one of those regimes goes flat in the other: all celebration and no stakes bores veterans; all stakes and no celebration never gets a new user to the stakes.

## What Duolingo does

Duolingo designs the streak explicitly for both regimes, and publishes the arithmetic behind why it has to.

- Going from a **2-day to a 3-day streak is a 50% increase**. Going from **200 to 201 is a 0.5% increase**. Same single day of work, a hundredfold difference in proportional progress.
- Early regime: rich celebration on extension — animation, character reaction, milestone art — so the increment itself is the payoff while the total is still small. See [[celebration-moments]].
- Late regime: the framing shifts to protecting accumulated value. Reminders talk about losing hard-earned progress, and Streak Freezes exist as insurance on the balance rather than as a reward for the day's work.
- Source: blog.duolingo.com/how-duolingo-streak-builds-habit (Duolingo blog, 2022-01-31; accessed 2026-09-22)

The tension: the late regime runs on fear, and a mechanic whose only late-stage fuel is fear of loss is the one users describe with a sigh rather than a smile. Duolingo mitigates it by keeping big milestone celebrations sparse but real — a periodic return to the early regime's register — rather than letting the counter become pure liability. The other cost is a cliff: a veteran's balance is worth so much that its loss can end the relationship outright, which is why the safety valve ([[power-ups]]) is not optional at that end of the curve.

## The transferable pattern

Split the counter's lifecycle before you design its feedback.

1. **Early — amplify the delta.** The increment is small in absolute terms, so pay for it with attention: motion, sound, a named threshold within reach. Anticipation of the next threshold is part of the reward.
2. **Late — defend the balance.** Stop advertising the increment, which is now statistically invisible, and start making the total legible: show it, make it public, make it recoverable after a slip.
3. **Mark the handoff.** Pick the point where proportional progress stops being felt and make sure a different mechanic is carrying the load past it. If you cannot name that point, you have one mechanic pretending to be two.

Anti-pattern: reusing the same celebration at every magnitude. It reads as generous at 3 and as noise at 300.

## Apply to your product

- What is your one accumulating number, and at what value does a single increment stop being felt?
- What does a long-tenured user lose if they stop — and does your product ever say it out loud?
- Do your celebrations scale with the magnitude of the total, or are they identical at every value?

## See also

[[celebration-moments]] · [[power-ups]] · [[anti-grind]] · [[../duo-retention/references/streak-mechanics]] · [[../duo-retention/references/loss-aversion]]
