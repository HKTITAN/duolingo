---
name: duo-product-ruthless-prioritization
summary: Cut, don't fit more in. The skill of saying no to good ideas that aren't the best ones.
metadata:
  internal: true
---

# Ruthless Prioritization

## Concept

Most prioritization frameworks (RICE, ICE, MoSCoW) are tools for *fitting more in*. Ruthless prioritization is the opposite: a skill for *cutting more out*. The presumption is that almost every roadmap is too long, that the marginal item costs the focal items, and that the highest-leverage decision is usually subtraction.

## What Duolingo does

Source: blog.duolingo.com/growth-model-duolingo (Duolingo blog, 2023-02-17; accessed 2026-09-22)

- **They found the one lever by simulating all of them.** With DAU stagnating in 2018, the Data Science team built a Markov model of seven user states, then systematically pulled each transition rate to see the downstream DAU effect. One lever dominated: **Current User Retention Rate (CURR)**. They staffed a team on CURR alone — not on the other six — and DAU grew **4x since 2019**.
- **Order is treated as a decision, not a residue.** Duolingo's growth guidelines say to sequence by ROI, because the highest-ROI work "will have a longer period of paying compound interest," and note this gets overlooked when a team plans a quarter as a list of things to accomplish: *"Order matters!"* (blog.duolingo.com/growth-principles (Duolingo blog, 2023-11-03; accessed 2026-09-22))
- **Optimize the biggest hurdle, not the most enthusiastic user.** Friend Streak was broken into a 6-step funnel; the team identified sending the *initial invite* as the choke point and concluded a **1% gain there** exposes far more learners than optimizing the power users who already hold 5 streaks (blog.duolingo.com/product-lessons-friend-streak (Duolingo blog, 2024-09-20; accessed 2026-09-22)).
- **Prioritize on the user's behalf, too.** Chess Game Review was scoped from the start to surface only key moments out of a 40-plus-move game, explicitly to avoid the information overload of standard engine analysis. Completeness is not a feature; it hands the ranking problem back to the person least able to do it (blog.duolingo.com/engineering-game-review (Duolingo blog, 2026-09-08; accessed 2026-09-22)).
- Saying no is treated as a senior skill, not an obstruction.

Tension the Growth Model post admits: a single prioritized metric eventually saturates. **90% of DAU now sit in the Current User state**, which makes CURR an increasingly imprecise and hard-to-move measure — the same trap DAU itself fell into in 2018. A focus metric buys a phase of growth, not a permanent one, and you have to plan its replacement before it stalls.

## The transferable pattern

Three rules:

1. **Default to no.** Every "yes" is a tax on the existing yeses. Make people earn the yes; don't ask them to defend the no.
2. **Cut by half twice.** Look at the roadmap, cut the bottom half. Now look at the remainder, cut the bottom half again. The result is closer to focus than the original.
3. **Sunset is part of prioritization.** Projects already shipped count too. A project drawing maintenance attention without commensurate value is a candidate for sunset, not just deprioritization.

A useful test: if you suddenly had to do half as much, what would you keep? That's your real priority list.

## Apply to your product

- How long is your current roadmap? Could it be half the length?
- What's a feature you ship and maintain that you'd kill if shipping cost was higher?
- When was the last time your team cut a project that was still in flight? How did it feel?

## See also

[[ship-it]] · [[kill-criteria-product]] · [[bounded-deliberation]] · [[teach-the-invariant]] · [[take-the-long-view]] · [[../duo-experimentation/references/kill-criteria]] · [[../duo-culture/references/no-process-without-purpose]]
