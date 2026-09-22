---
name: duo-gamification-beat-your-own-best
summary: Target the user's own previous best alongside fixed thresholds, and put earned status somewhere other people can see it.
metadata:
  internal: true
---

# Beat Your Own Best

## Concept

Fixed achievement thresholds have a distribution problem. For most of your base they are either already exhausted or permanently out of reach, and in both cases they stop motivating. A personal-record target has no such ceiling: it regenerates automatically for every user at every skill level, because the bar is whatever they last did.

The second half is where you put the result. A badge buried in a profile page has an audience of one and motivates only while that one person is looking at it. Status is only status if someone else can see it.

## What Duolingo does

Duolingo rebuilt its Achievements system along both axes at once.

- **Moved status out of the buried profile page** and into a shareable trophy shelf, so earned badges became something to show rather than something to find.
- **Tiered the difficulty deliberately**, from easy entry badges (adding friends) to genuinely rare ones (a year-long streak), so the set stays live for both a first-week user and a veteran.
- **Added Personal Records** as a separate class of target: daily most XP, perfect lessons, longest streak, and best league finish. Each one is scored against the user's own history rather than a global threshold. Source: blog.duolingo.com/achievement-badges (Duolingo blog, 2023-12-11; accessed 2026-09-22)
- The perfect-run chain described in [[combo-multipliers]] feeds one of those records, so within-session momentum ladders into a personal best instead of evaporating at the end of the session.

The tensions. A personal record set during an unusual burst becomes a bar the user may never clear again, which converts a motivator into a standing reproach — records need either multiple categories or a decay so there is always one in reach. And making status public is the same decision as making effort public: users who are behind now see that too, which is why the competitive surfaces around it ([[../duo-retention/references/leagues]]) ship with an opt-out.

## The transferable pattern

1. **Run both target types.** Fixed thresholds give newcomers a legible ladder; personal records give everyone else a bar that never runs out.
2. **Tier the fixed set from trivial to rare.** A set where every item is hard has nothing for a new user; a set where every item is easy has nothing for anyone else.
3. **Keep several records live at once.** Multiple categories mean at least one is usually within reach, which stops a single lucky peak from becoming a permanent ceiling.
4. **Surface status where it is visible to others.** If earned status lives only on a settings-adjacent page, it is a receipt, not a reward.
5. **Give the visibility an off switch.** Public standing is motivating to some and exposing to others.

## Apply to your product

- What could a user beat their own record at this week, and does your product currently track it?
- Where does earned status live in your product — somewhere others encounter it, or somewhere only the owner navigates to?
- Is your easiest achievement reachable in a first session, and your hardest genuinely rare?

## See also

[[combo-multipliers]] · [[celebration-artifacts]] · [[rate-by-opponent-strength]] · [[xp-system]] · [[../duo-retention/references/leagues]]
