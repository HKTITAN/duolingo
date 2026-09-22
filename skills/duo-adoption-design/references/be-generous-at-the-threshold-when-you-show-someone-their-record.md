---
name: duo-adoption-design-be-generous-at-the-threshold-when-you-show-someone-their-record
summary: Gate personal recaps behind a minimum-activity threshold, and when migrating earned status, publish a rounding rule that favours the user.
metadata:
  internal: true
---

# Be Generous at the Threshold When You Show Someone Their Record

## Concept

Two moments hand the user a number that describes them: the personal recap, and the migration that recomputes what they earned. Both are emotionally asymmetric. A flattering recap is a small pleasure; an unflattering one is an accusation the user was successfully avoiding, and guilt drives uninstalls rather than returns. A migration that recomputes exactly will always find someone whose hard-won standing shrank, and that is the objection that dominates every redesign. The fix in both cases is a stated threshold, set generously, published in advance.

## What Duolingo does

- For the 2020 Year in Review, only learners **active at least 7 days** who completed **20 or more lessons** received a personalized report. The threshold was chosen to be enough activity that the report would feel exciting, without alienating casual learners — a filter on who receives a positive emotion.
- Tension: compute cost forced a **data cutoff of October 31, 2020**, so November and December were silently excluded from something titled "Year in Review." A correctness compromise made for a deadline, and worth knowing before you copy the pattern.
- On the tree-to-path migration, Duolingo published the rounding rule rather than just applying it: if **more than 50%** of the levels in a completed unit belonged to skills the learner had previously taken to Legendary, **the entire unit was granted Legendary status**.
- Incomplete levels were handled by placing the learner **earlier in the path** and then skipping past completed content, rather than by demoting them.
- Tension, acknowledged: rounding up credits some learners for work they did not do. Duolingo also warned learners they might see Stories they had already read, because Stories were re-placed by difficulty rather than by completion history — the migration was honest about where it was approximate.

Source: blog.duolingo.com/duolingo-2020-year-in-review (Duolingo blog, 2021-05-03; accessed 2026-09-22)

Source: blog.duolingo.com/new-duolingo-home-screen-design (Duolingo blog, 2022-05-06; accessed 2026-09-22)

## The transferable pattern

The emotional payload of a recap depends entirely on the numbers being flattering. There is no copywriting that rescues "you did three things this year." So set an eligibility floor and send the recap only above it. Silence is a better outcome than a reminder of the lapse.

For migrations, the loudest objection to a redesign is never the layout — it is the fear that earned standing was quietly taken away. An explicit generous threshold is cheap to implement, impossible to argue with, and converts the biggest source of migration anger into a visible act of good faith.

Four rules:

1. **State the rule before you apply it,** in plain numbers. An unpublished rule reads as an excuse afterwards.
2. **Round toward the user.** Over-crediting costs you very little; under-crediting costs you the relationship.
3. **Never demote.** If the new model would place someone lower, place them earlier and let them skip forward instead.
4. **Name what is approximate.** Users forgive a stated approximation and resent a discovered one.

Then check what your deadline quietly cut. An incomplete number under a complete-sounding title is a trust cost you pay later.

## Apply to your product

- If you sent a personal recap tomorrow, what fraction of recipients would see a number that embarrasses them? Where is your eligibility floor?
- In your next data model change, which users could lose standing they earned? What is your published rounding rule, and does it round their way?
- What is your recap actually measuring, and does the title over-claim relative to the window you could afford to compute?

## See also

[[one-ordered-path-beats-a-branching-surface]] · [[turn-the-session-into-three-named-buckets]] · [[../duo-gamification/references/progression-design]]
