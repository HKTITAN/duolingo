---
name: duo-backend-architecture-predict-only-what-users-dont-care-about
summary: The cost of a wrong optimistic render scales with how much the value matters — never predict money, fairness, or hard-won state.
metadata:
  internal: true
---

# Predict Only What Users Don't Care About

## Concept

Optimistic rendering buys perceived speed by spending a small probability of being wrong. That is a good trade for a toggle nobody is watching and a terrible one for the single number a user is staring at. The cost of a wrong prediction scales with how much the value matters: being wrong about a follow state costs nothing; being wrong about a balance or a ranking reads as the product either cheating the user or being untrustworthy about the one thing they came to check. Latency is recoverable. Trust is not. So predict the cheap things, and wait for confirmation on anything touching money, fairness, or state the user worked to earn.

## What Duolingo does

Source: blog.duolingo.com/frontend-prediction (Duolingo blog, 2026-04-15; accessed 2026-09-22)

- Duolingo predicts on the client: **course progress** (so lessons work offline), **XP and leaderboard standing** on the session-end card, and **follow buttons**, which flip instantly.
- The session-end card is often shown **several seconds before the backend finishes** — that gap is the whole product benefit.
- It names the other side of the line explicitly: **monetized resources such as gem purchases** and **critical outcomes such as leaderboard promotions** must reflect confirmed backend results, not predictions.
- **The line is genuinely blurry, and they say so.** Duolingo predicts leaderboard *standing* on the session-end card while holding that *promotions* must not be predicted, and admits that a user seeing "You're #1" and later being demoted is an infuriating experience. This is a judgment call the team re-makes per feature, not a rule that resolves itself.
- **A structural consequence:** their user model holds XP, gems, streaks and more in one object, and the post states that tying prediction logic to a monolithic model makes partial rollbacks harder. Smaller, modular pieces of state let different values carry different rollback policies.

## The transferable pattern

Sort every client-rendered value by what a wrong guess costs:

- **Safe to predict** — reversible, low-stakes, unobserved: toggles, subscriptions, reordering, read/unread, local counters nobody audits.
- **Never predict** — anything denominated in money, anything determining a competitive or fairness outcome, anything the user spent real effort to obtain, and anything another person will see before the correction lands.

Two design rules follow:

1. **Rollback policy is chosen per value, so state must be divisible per value.** The three real policies are *never correct*, *correct silently at the next natural boundary*, and *correct immediately in place*. If a balance, a score and a status all live inside one object, you cannot roll back one without touching the others — so you end up applying the most permissive policy to the most sensitive value.
2. **Decide at the field level, not the screen level.** A single screen routinely contains one value that is fine to guess and one that is not. Predicting the screen forces the wrong answer onto half of it.

## Apply to your product

- List the values your client renders before the server confirms them. Which one, if wrong, would a user describe as the product taking something from them?
- Is your client state divisible enough to correct one field without disturbing its neighbours — or is it one object with one policy?
- When a prediction is wrong today, what does the user actually see, and did anyone choose that behavior deliberately?

## See also

[[prefer-a-loading-state-to-a-rollback]] · [[version-clients-by-last-good-config]] · [[../duo-gamification/SKILL]]
