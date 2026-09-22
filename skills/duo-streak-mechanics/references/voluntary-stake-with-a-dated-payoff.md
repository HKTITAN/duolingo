---
name: duo-streak-mechanics-voluntary-stake-with-a-dated-payoff
summary: Let users stake something they own on a self-set commitment and date the payoff at the retention horizon you care about.
metadata:
  internal: true
---

# Voluntary Stake With a Dated Payoff

## Concept

A chain you hand someone is a commitment they never agreed to. A stake is different — the user chooses to put something of their own at risk against a promise they made, which converts a vague intention into a loss they have already partly paid for.

Two parameters do the work. **What is staked** (currency they earned, or their standing with another person) and **when it pays off**. The payoff date is not a detail: it is where the retention lift lands. Pick the horizon you actually care about and put the payoff exactly there.

## What Duolingo does

Source: blog.duolingo.com/how-streaks-keep-duolingo-learners-committed-to-their-language-goals (Duolingo blog, 2017-05-10; accessed 2026-09-22)

- The **Streak Wager** A/B test let learners spend in-game currency at the end of a lesson to bet they would keep a **7-day streak**, **doubling their stake** on success. Results: statistically significant increases in **Day-1, Day-7 and Day-14 retention**, with **Day-7 the largest at +14%** — the lift concentrated at the wager's own horizon rather than spreading evenly.
- The stake is the user's own earned currency, at a moment when they have just succeeded. Opt-in, self-set, and refused at no cost.
- **The paired variant.** Friend Streak (August 2024) lets a person share a streak with up to **5 friends**; each shared streak is tracked **separately from the personal one**, invitations must be **accepted by the other side**, and either party can "nudge" the other. Learners with at least one shared streak are **22% more likely to complete their daily lesson**, and the effect rises with more shared streaks (blog.duolingo.com/friend-streak (Duolingo blog, 2024-08-05; accessed 2026-09-22)).
- The team's own read is that it works **without requiring the two people to do anything together** — compared to studying beside a friend at a library. **57% of users** had at least one friend at launch (blog.duolingo.com/product-lessons-friend-streak (Duolingo blog, 2024-09-20; accessed 2026-09-22)).
- **The exit, and its flaw.** Duolingo publishes step-by-step instructions for switching Friend Streak and Friends Quests off, and for leaving leaderboards. But the leaderboard opt-out is **reachable only on the website, not in the app**, and works by making your whole profile private — the exit is coupled to an unrelated privacy setting (blog.duolingo.com/introvert-language-learning-tips (Duolingo blog, 2026-09-15; accessed 2026-09-22)).

## The transferable pattern

- Let the user set the terms. A stake imposed by you is a penalty; a stake the user chose is a commitment device, and only the second one raises retention.
- **Date the payoff at your horizon.** The lift concentrates where the reward sits, so treat the payoff date as a tuning parameter and test more than one.
- Stake something already earned inside the product, never real money the user has not spent — the loss has to be real enough to bind and small enough to be survivable.
- The two-sided version recruits a second enforcer for free, but only if both sides opt in and the shared counter is **separate** from the private one. One person's slip should never destroy the other's record.
- Parallel commitment beats coordination. "Someone else is also doing this today" produces accountability without the scheduling cost that kills most social features.
- Ship a documented exit and publish the instructions yourself. Competitive and social mechanics raise the average by helping some users a lot and making the product aversive for others; without an exit, the aversive segment's only move is to leave. Do not couple that exit to an unrelated setting.

## Apply to your product

- What have your users already earned inside your product that they would risk on their own promise?
- Which retention day genuinely matters to your business, and is your reward landing on it or somewhere convenient?
- If you add a paired or public version, what is the opt-out, and can a user find and use it without leaving the app?

## See also

[[activation-threshold-as-one-shared-target]] · [[the-chain-will-certify-a-token-action]] · [[../duo-gamification/references/self-imposed-stakes]] · [[../duo-gamification/references/co-op-pairing]]
