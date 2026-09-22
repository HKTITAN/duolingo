---
name: duo-memory-and-decay-spacing-beats-massing-at-equal-cost
summary: The same repetitions spread across days build durable capability; massed into one sitting they buy a passing score and nothing else.
metadata:
  internal: true
---

# Spacing Beats Massing at Equal Cost

## Concept

Hold total effort constant and change only how it is distributed across time, and durability changes dramatically. Twenty repetitions crammed into one night and four repetitions a day for five days are the same twenty repetitions — only one of them survives the week.

The mechanism is that forgetting has to begin before a retrieval can interrupt it. A repetition performed while the item is still sitting in working memory refreshes nothing; it feels effortless precisely because nothing was retrieved. Spacing puts each repetition at a point of real effortful recall, and puts elapsed time (and sleep) between passes so the trace can consolidate.

So the design parameter is session **frequency**, not session **length**.

## What Duolingo does

Source: blog.duolingo.com/spaced-repetition-for-learning (Duolingo blog, 2023-12-26; accessed 2026-09-22)

- The worked example is stated plainly: **20 repetitions of a word crammed the night before a test** versus **4 repetitions a day for 5 days** — identical count of 20, radically different retention. Personalized practice lessons pull items from across the whole path and return them at widening intervals.
- Duolingo's learning-science writing puts numbers on the tradeoff repeatedly, always in the same direction: **1 hour a day beats 5 hours once a week**, and a hyperpolyglot's version of the same rule is **15 minutes daily over a single 3-hour weekly block** (blog.duolingo.com/are-some-people-better-at-learning-languages (Duolingo blog, 2023-07-25; accessed 2026-09-22)).
- Consumer guidance lands on **5 minutes every day over 1 hour once a week**, and the product is built to match — the average lesson takes about **5 minutes**, sized to fit a daily gap rather than a study block (blog.duolingo.com/benefits-of-learning-a-language (Duolingo blog, 2021-08-17; accessed 2026-09-22)).
- The motivation guidance prescribes **15–20 minutes a day** and pairs it with routine-anchoring — attach the session to something that already happens (commute, first phone check, lunch) so the daily decision to start disappears (blog.duolingo.com/sticking-with-it-tips-for-staying-motivated (Duolingo blog, 2026-06-04; accessed 2026-09-22)).

**The tension, stated by Duolingo itself:** spacing does **not** improve immediate performance, and at first it may feel like it is making no difference at all. That is not a footnote — it is the reason most teams never ship it. Any team optimizing an in-session metric (score in this session, completion rate of this session, time-on-task) will measure spacing as a regression and kill it on the evidence.

## The transferable pattern

Distribution of effort is a free variable most products never touch. They tune content and length; they leave frequency to chance.

1. **Make frequency the design target.** Size the unit of work to fit into a day that has no room for it, then ask for it on more days. Shorter and more often beats longer and rarer at equal total cost.
2. **Anchor the unit to an existing routine**, because the expensive part of a daily habit is the decision, not the work.
3. **Guard the measurement.** Before you run the experiment, write down that in-session performance is expected to get *worse* and name the durability metric — retention at 7, 14 and 30 days — that is allowed to overrule it. Do this first; done afterwards it reads as excuse-making.
4. **Do not claim the win on totals.** Spacing does not add effort, it relocates it. If your pitch is "users will do more," you have pitched something else.

## Apply to your product

- What is the smallest useful unit of work in your product, and could someone complete it in a gap they already have — or does it require a block they have to schedule?
- Which of your dashboards would show spacing as a loss? Who owns that number, and have they agreed in advance what durability result would outrank it?
- Where are you currently rewarding a long session (a streak of minutes, a completion bar, a marathon badge) when you meant to reward a returning one?

## See also

[[sleep-is-a-free-consolidation-pass-you-can-skip]] · [[per-item-half-life-not-a-fixed-ladder]] · [[../duo-retention/references/habit-loop]]
