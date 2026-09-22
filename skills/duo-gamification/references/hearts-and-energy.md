---
name: duo-gamification-hearts-and-energy
summary: Capped attempts as a forcing function for engagement and a monetization lever; the most controversial mechanic in the suite.
metadata:
  internal: true
---

# Hearts and Energy

## Concept

A "hearts" or "energy" system caps the user's attempts within a window. Run out of hearts, and the session pauses until they regenerate (over time, by paying, by watching an ad, or by practicing). The mechanic introduces a soft scarcity that reframes mistakes from "free" to "costly" — and gives the user a gentle off-ramp instead of unlimited failure.

This is the most controversial mechanic in Duolingo's suite. Defenders point to better attention; critics point to monetization and frustration.

## What Duolingo does

Duolingo ran the failure-gated version for years, then replaced it.

**Hearts (the old system).** Five hearts; one lost per wrong exercise; after five mistakes the learner had to complete a practice lesson to earn one back. Gems could buy hearts, and Super/Max subscribers got unlimited ones. Duolingo defended the mechanic pedagogically — hearts "keep you from moving too quickly through the course and help you focus." Source: blog.duolingo.com/duolingo-101-how-to-learn-a-language-on-duolingo (Duolingo blog, 2024-12-02; accessed 2026-09-22)

**Energy (the replacement, July 2025).** A battery each lesson draws down, refilled by getting several answers in a row right. Reviewing your mistakes at lesson end costs nothing. Bonus energy for perfect lessons, adding a friend, and reward chests. It recharges fully in about a day — same as Hearts. Source: blog.duolingo.com/duolingo-energy (Duolingo blog, 2025-07-03; accessed 2026-09-22)

**The number that forced the change:** under Hearts, beginners were **2X more likely to run out mid-lesson**. A failure-gated resource taxes hardest exactly the cohort with the least accumulated reason to stay.

The honest tension: Energy is still monetized — rewarded ads and gem refills — and Duolingo says it "supports that mission by helping us sustain that model." This is a rebalanced extraction point, not a removed one.

## The transferable pattern

When does a hearts-style system make sense?

| Use it when | Avoid it when |
|---|---|
| Attempts have meaningful information value (a wrong answer means something) | Failure is just trial-and-error, not learning |
| Engaged users almost never hit the limit | Most users hit the limit regularly |
| The off-ramp is dignifying, not coercive | The only way out is to pay |
| You can experimentally calibrate the cap | You're guessing and shipping |

Anti-pattern: capping success-side actions. A meter that limits *engagement*, not just failure, is extraction in disguise.

The Energy switch is the sharpest version of this rule: don't drain on failure, drain on usage and refill on competence. Failure-draining charges beginners the most; usage-draining charges everyone evenly and pays out for getting good.

## Apply to your product

- Does your product have any cost to mistakes? Should it?
- If you added a hearts-equivalent, what would the ratio look like for an engaged user — frequent collisions or rare ones?
- Would a critic call your version a learning aid or a paywall? (The honest answer matters.)

## See also

[[anti-grind]] · [[../duo-retention/references/loss-aversion]] · [[../duo-retention/references/retention-vs-revenue]]
