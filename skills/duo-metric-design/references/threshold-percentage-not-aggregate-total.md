---
name: duo-metric-design-threshold-percentage-not-aggregate-total
summary: Grade on the share of users who clear a meaningful bar, not the sum — an aggregate lets a power-user cohort absorb your entire improvement.
metadata:
  internal: true
---

# Threshold Percentage, Not Aggregate Total

## Concept

An aggregate total hides its own distribution. Total hours, total actions, total volume can all rise sharply while the users you built the change for do not move at all, because a small hyperactive cohort is elastic enough to absorb the whole gain. You then ship the feature, bank the win, and quietly make the product better only for people who already needed no help.

The fix is to grade on a percentage crossing a threshold: *what share of users reached a level we believe is meaningful?* That metric cannot be moved by making your heaviest users heavier. The only way up is to move someone across the line.

## What Duolingo does

Source: blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22)

- While the goal was **Total Time Spent Learning**, improvements to competitive features (Leaderboards) grew the number **almost entirely through already-hyperactive learners** — a group Duolingo describes as already doing more than enough. The aggregate rose; the distribution did not.
- The goal was changed to increasing the **percentage of learners spending at least 15 minutes a day**.
- The **15-minute** bar was not picked by intuition. It came out of formal studies, discussion with internal learning and curriculum experts, and analysis of existing learner behavior.
- Stated tension: choosing the threshold is a judgment call with no clean answer. It took studies plus expert consultation to land on a single number, and that number is a commitment the whole org then inherits.

A related hazard: the competitive feature that inflated the aggregate is also the one most worth manipulating. Duolingo monitors leaderboards for irregular XP activity and removes learners with illegitimate gains, while stating publicly that cheating is rare and that the outlier totals users report are usually genuine. Leaderboards can also be turned off through the profile-privacy toggle. Source: blog.duolingo.com/duolingo-leagues-leaderboards (Duolingo blog, 2023-05-03; accessed 2026-09-22)

## The transferable pattern

1. **Find the bar that means something.** Not a round number — the level of usage above which people get the outcome your product promises. Derive it from outcome data, not from where your current median sits.
2. **Grade on the share above it.** `users_above_bar / eligible_users`. A power user going from heavy to heavier contributes nothing, which is the point.
3. **Keep the aggregate as a read-only number.** It still tells you about load, cost and capacity. It just does not decide whether anyone did a good job.
4. **Publish the threshold's provenance.** Whoever inherits the metric will want to move the bar when it gets inconvenient; the derivation is your defense.
5. **Watch the bar's neighborhood for gaming.** Any visible scoreboard attracts both real manipulation and, far more often, unfounded suspicion. Monitor for anomalies, and say plainly how rare abuse actually is — suspicion alone erodes belief in the number.

Costs to accept: a threshold metric is deliberately blind above the line, so a genuine improvement for your best users registers as zero. And a badly placed bar is worse than no bar, because everything downstream now optimizes toward it.

## Apply to your product

- What is the usage level above which your users reliably get the result you sell, and how would you derive it from outcome data rather than from your current median?
- If your headline number went up 20% next quarter, could you prove it was not one heavy cohort doing more of what they already did?
- Who would object to your threshold, and what evidence would settle it?

## See also

[[put-the-weight-in-the-formula-not-the-memo]] · [[pair-every-growth-metric-with-a-quality-proxy]] · [[../duo-experimentation/SKILL]]
