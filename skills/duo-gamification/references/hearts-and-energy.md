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

- Free users have a small heart pool (typically 5); each wrong answer costs one.
- Hearts regenerate slowly, can be earned through practice, or removed entirely with Super Duolingo subscription.
- The mechanic gates failure but not success — getting answers right uses no hearts, so engaged users barely notice the system.

The handbook's *Take the Long View* shows up here too: Duolingo has experimented with the strictness of hearts and pulled back when retention dropped, even when short-term subscription conversion rose ([[../duo-retention/references/retention-vs-revenue]]).

## The transferable pattern

When does a hearts-style system make sense?

| Use it when | Avoid it when |
|---|---|
| Attempts have meaningful information value (a wrong answer means something) | Failure is just trial-and-error, not learning |
| Engaged users almost never hit the limit | Most users hit the limit regularly |
| The off-ramp is dignifying, not coercive | The only way out is to pay |
| You can experimentally calibrate the cap | You're guessing and shipping |

Anti-pattern: capping success-side actions. Hearts that limit *engagement*, not just failure, are extraction in disguise.

## Apply to your product

- Does your product have any cost to mistakes? Should it?
- If you added a hearts-equivalent, what would the ratio look like for an engaged user — frequent collisions or rare ones?
- Would a critic call your version a learning aid or a paywall? (The honest answer matters.)

## See also

[[anti-grind]] · [[../duo-retention/references/loss-aversion]] · [[../duo-retention/references/retention-vs-revenue]]
