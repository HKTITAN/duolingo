---
name: duo-growth-social-mechanics
summary: Friends, leaderboards, and presence as growth surfaces, not just retention surfaces.
metadata:
  internal: true
---

# Social Mechanics

## Concept

Social mechanics serve two jobs: they make existing users stick (friends to compare with, presence to maintain), and they pull new users in (the user adds their friends to compete). Most products treat one of these as the primary; the move is to design for both at once.

## What Duolingo does

- **The graph is an activation metric, and it has a number.** Duolingo states that **learners who add friends are 5.6x more likely to finish their course**, and pushes contact syncing from the profile tab on the strength of it. Learners with **at least one shared streak are 22% more likely to complete their daily lesson**. Source: blog.duolingo.com/friends-social-features (Duolingo blog, 2023-06-06; accessed 2026-09-22)
- **Friend leaderboards, a Feed, and weekly Friends Quests** stack on top of that one graph rather than each building their own — high-five friends for milestones like 10 lessons in a day, a 365-day streak, or a Diamond League promotion. Same source.
- **Solo completeness is shipped, not assumed.** Duolingo launched a **universal matching system so learners without friends can still join Friends Quests** — the social feature does not require a social graph to enter. Source: blog.duolingo.com/product-highlights (Duolingo blog, 2025-12-10; accessed 2026-09-22)
- **Presence signals** — users see their friends' activity without it being an attention tax.
- The mechanics are *additive* — a solo user has a fine experience; a user with friends has a better one. No one is locked out by their network.

## The transferable pattern

Three rules:

1. **Solo experience must be complete.** If your product requires friends to be useful, you have a coordination problem instead of a product. Friends amplify, they don't gate.
2. **Comparison is the engine.** The retention lift from social comes from "where do I rank vs. people I know," not from "look what my friend did."
3. **Presence without anxiety.** The user should know their friends are using the product, not feel surveilled by them.

Anti-pattern: social features bolted on as a separate tab. If users have to *go to* the social features, they're not amplifying anything.

## Apply to your product

- Does your product have any social surface? If not, would a comparison-based one map to your activity?
- If you have social, is the solo experience still complete?
- What does presence feel like — supportive or surveillance?

## See also

[[viral-loops]] · [[referrals]] · [[../duo-retention/references/leagues]]
