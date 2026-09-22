---
name: duo-category-entry-wire-the-second-line-into-the-existing-habit-currency
summary: A second product line with its own streak and rewards competes for the same daily slot; sharing the currency widens the first product instead.
metadata:
  internal: true
---

# Wire the Second Line into the Existing Habit Currency

## Concept

Users have one daily slot for your app, not one per product line. If the new line arrives with its own counter, its own points and its own goals, you have shipped a second product that competes with the first for that slot. If it feeds the same ones, you have widened the first. The difference costs almost nothing at design time and is close to unfixable later, because by then both currencies have real balances in them.

## What Duolingo does

Source: blog.duolingo.com/new-subjects (Duolingo blog, 2023-10-11; accessed 2026-09-22)

- When Math and Music entered the main app in **October 2023**, a lesson in any subject counted toward **the same streak**; XP earned in any subject counted toward **the same leaderboard**; XP Boosts earned in a language course applied **across all subjects**; and shared quests spanned subjects.
- Navigation reused what already existed — subjects are switched with **the same course picker** learners had been using for multiple languages, so the new line needed no new mental model. Source: blog.duolingo.com/duolingo-launches-math-app (Duolingo blog, 2022-10-26; accessed 2026-09-22)
- The same source describes the shared surfaces in detail — daily quests, achievements, and friend quests completable in Math — inside one app that now spans **40+ languages plus Math and Music**.
- **Tension.** Parity was selective, not wholesale. Legendary levels were **withheld from Math** until Duolingo could confirm the mechanic was appropriate and helpful for that subject. Sharing the currency is the default; cloning every mechanic is not, because a mechanic tuned for one domain can be meaningless or actively misleading in another.
- The retention logic is the point. A learner bored of one subject can keep the streak alive with another, which converts what would have been churn into a lateral move — see [[../duo-retention/references/streak-mechanics]].

## The transferable pattern

Decide one thing before you build the second line — does it share the habit currency or not? The currency is whatever your product counts and the user cares about losing: the streak, the points, the level, the completion percentage, the weekly goal, the standing in a ranking.

Sharing it produces a specific effect. Any line becomes a valid way to satisfy the daily habit, so a user tired of one has somewhere to go that is still inside your product. The new line becomes a relief valve for the old one rather than a rival for the same fifteen minutes.

Three rules for doing it well.

1. **Share the currency on day one.** Merging two counters later means deciding whose balance survives, and both answers make someone angry.
2. **Reuse the existing navigation.** The switch between lines should use the control users already know, not a new top-level surface that implies a new product.
3. **Hold back mechanics selectively.** Port the currency wholesale; port the mechanics only where they still mean something. A mechanic that rewards speed may be right in one domain and wrong in another, and shipping it everywhere for consistency teaches the wrong behaviour.

## Apply to your product

- What does your product count that a user would be upset to lose? Would activity in a new line add to that count, or start a second one?
- If someone got bored of your main use case tomorrow, is there anywhere inside your product for them to go that still keeps their progress alive?
- Which of your existing mechanics would be actively misleading if applied unchanged to the new line, and what would you hold back until you had evidence?

## See also

[[port-the-method-and-the-format-vary-the-subject]] · [[check-whether-your-core-abstraction-survives]] · [[../duo-retention/SKILL]] · [[../duo-gamification/SKILL]]
