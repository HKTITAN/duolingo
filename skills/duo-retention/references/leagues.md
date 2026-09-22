---
name: duo-retention-leagues
summary: Weekly time-boxed competition with promotion and demotion; social retention without permanent rankings.
metadata:
  internal: true
---

# Leagues

## Concept

A league is a time-boxed cohort (usually weekly) of similar-skill users competing on a normalized metric (XP earned). At week's end, top users promote up a tier, bottom users demote down. The reset is the magic: there's always a current race, and falling behind in absolute terms doesn't mean you're behind forever.

## What Duolingo does

Source: blog.duolingo.com/duolingo-leagues-leaderboards (Duolingo blog, 2023-05-03; accessed 2026-09-22)

- Leaderboards were first tested in **2018** with **5 leagues**. There are **10** today, topped by Diamond — Duolingo widened the ladder deliberately so that "reaching the top was an even bigger achievement."
- A new weekly league begins **every Sunday** in your own timezone. You are matched with learners who have **similar study habits and a similar timezone** — not your friends, and not necessarily people studying your language, because the competition runs across all courses.
- The metric (XP) is something the user already produces by doing the core action; leagues *add* a layer rather than introducing a new task.
- The top of the ladder gets its own extra loop: the top 10 in Diamond qualify for the multi-round **Diamond Tournament**, which does not run every week.

Tension Duolingo has published on both sides. XP is grindable, and they say the competition "can feel 'unfair' for learners who are more focused on content than gaining thousands of XP per week" — so they **rebalanced XP toward path lessons**, worth roughly **+1.8M minutes/day** of Time Spent Learning Well at full adjustment (blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22)). And the opt-out is awkward: Leaderboards can only be disabled from web Settings, by toggling off "Make My Profile Public" — an exit coupled to an unrelated privacy control.

## The transferable pattern

A league works when:

1. The competition metric is the **same metric** as core engagement. Adding a separate "league activity" is a tax.
2. The cohort is small enough that **personal action visibly moves the rank**. In a 1000-person league, one lesson is rounding error.
3. Time is **bounded and recurring**. Permanent leaderboards reward early adopters and punish newcomers; weekly resets keep everyone in the same race.
4. The **boundary effects matter**. The middle zone exists; design it. Users in the middle should still feel something at week's end.

Leagues fail when the cohort is too large, the metric is divorced from real activity, or the reset is too long (monthly leagues lose the urgency that makes them work).

## Apply to your product

- Do you have a metric users already produce that could become a league metric?
- What is the smallest cohort size where individual action visibly matters?
- What week-end moment do you want to engineer — the sprint to promote, the panic to avoid demotion, or both?

## See also

[[habit-loop]] · [[loss-aversion]] · [[../duo-growth/references/social-mechanics]] · [[../duo-experimentation/references/metric-selection]]
