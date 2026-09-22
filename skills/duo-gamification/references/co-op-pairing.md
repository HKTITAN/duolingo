---
name: duo-gamification-co-op-pairing
summary: In a shared-goal feature, filter partners by recent activity before pairing — a dormant partner turns a motivator into a debt.
metadata:
  internal: true
---

# Co-op Pairing

## Concept

A cooperative goal — two users, one target, one reward — is one of the strongest motivators available, because now someone else is depending on you. It is also the most fragile, because it fails for reasons the user cannot control.

If you pair an active user with a dormant one, the active user carries the whole goal alone and then loses anyway. What they learn is that the feature is a tax. Punishing your most engaged users for someone else's absence is an expensive way to lose them.

## What Duolingo does

Friends Quests pair two people against a shared weekly target, with eligibility filtered on activity.

- Pairing draws only from **mutual followers who are currently active**, stated explicitly so a learner does not have to carry the quest alone.
- The cycle is fixed and short: pairing runs **after 1 p.m. EST on Tuesdays**, and the pair has **5 days** to finish.
- The social prior behind the whole feature: learners who follow friends are **5.6x more likely to finish their course**.
- Source: blog.duolingo.com/friends-quests (Duolingo blog, 2022-09-09; accessed 2026-09-22)

The cost is user choice, and the post fields the complaint head-on: "I never get paired with my best friend" — because that friend is inactive. The system is choosing a partner who will show up over the partner the user wanted, and it has to explain that tradeoff rather than hide it. Duolingo also shipped an opt-out toggle, which is the admission that an obligation to another person is not universally welcome even when it works.

Two further tensions worth naming before copying this. An activity filter concentrates the feature on your already-active core and structurally excludes returning users from the mechanic most likely to re-engage them. And a short fixed window means a partner who goes quiet on day two leaves no time to recover, so the filter has to be paired with a forgiving failure state rather than a full forfeit.

## The transferable pattern

1. **Filter on recent behavior, not on relationship.** The question is not who the user likes, it is who will show up inside the window. Match on the second.
2. **Explain the substitution.** Users will notice they did not get the partner they expected. A one-line reason converts a bug report into an understood constraint.
3. **Keep the window short and the cycle fixed.** A predictable start and a few days to finish limits how much a partner's silence can cost.
4. **Make it opt-out.** Obligation to another person is a strong motivator and a real burden, and the sign differs across your base.
5. **Do not let one person's absence fully void the other's work.** Credit effort even when the shared goal fails, or the mechanic teaches your best users to avoid it.

## Apply to your product

- Is there a goal in your product that two users could share, where both contributing is genuinely better than one?
- What is your activity threshold for "will show up this week", and do you have the data to apply it before pairing?
- If a partner vanishes mid-window, what does the remaining user get for the work they already did?

## See also

[[nested-deadlines]] · [[xp-system]] · [[anti-grind]] · [[../duo-retention/references/daily-quests]] · [[../duo-growth/SKILL]]
