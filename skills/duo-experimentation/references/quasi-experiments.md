---
name: duo-experimentation-quasi-experiments
summary: Causal reads without randomization — habitual users as their own control, matched cohorts, and scoring variants only within comparable audiences.
metadata:
  internal: true
---

# Quasi-Experiments

## Concept

Plenty of the things you most want to understand cannot be randomized: optional features nobody will be forced into, behaviors users choose, variants that eligibility rules restrict to a subset. The naive move is to compare users who did the thing against users who did not, which confounds the action with the kind of person who takes it — adopters of any optional feature are more motivated by default. Three constructions get you a defensible read anyway, all built on the same idea: hold the person-type constant and let only the action vary.

## What Duolingo does

**The habitual user as their own control.** To isolate the effect of completing one optional extra level, Duolingo used a regression discontinuity design: instead of doers versus non-doers, it compared learners who *normally* complete that level against those same-profile learners on occasions they happened to skip it. The habit holds motivation constant; the only thing varying is whether they did it this time. Source: blog.duolingo.com/review-exercises-help-measure-learner-recall (Duolingo blog, 2021-12-02; accessed 2026-09-22)

**Matched cohorts on recent exposure.** For the Video Call study, Duolingo compared beginner French and Spanish learners who used the feature against those who did not — but only among learners who had *just completed the same units*, so both groups had recently covered identical material. Both were then tested on producing target phrases aloud. The users scored higher. Source: blog.duolingo.com/falstaff-calls-research (Duolingo blog, 2026-03-10; accessed 2026-09-22)

**Scoring only within a comparable audience.** Eligibility rules quietly manufacture confounded comparisons. Duolingo found that many learners complete a session no matter which notification arrives — long-streak users especially — so a template only eligible for that group gets an unearned win rate. The fix was a scoring method that compares each template only against other templates sent to the same type of user. Source: blog.duolingo.com/hi-its-duo-the-ai-behind-the-meme (Duolingo blog, 2020-09-03; accessed 2026-09-22)

Tensions: the Video Call study publishes direction only — "scored higher" — with no effect size or sample size, which caps how much weight it can carry. And self-as-own-control still cannot rule out that whatever caused the skip (a bad day, a busy week) also caused the outcome.

## The transferable pattern

Before comparing two groups you did not randomize, ask what else differs between them, then remove it structurally:

| Construction | Holds constant | Use when |
|---|---|---|
| Habitual doers, split on whether they did it this time | The kind of person | The action is optional and self-selected |
| Cohorts matched on stage and recent exposure | Where they are in the journey | Adoption is voluntary but stage is recorded |
| Within-stratum scoring | The audience a variant could reach | Eligibility rules restrict some variants |

Two rules. State the construction and its residual confound in the same sentence as the result — a matched comparison presented as an A/B test is worse than no result. And check eligibility before reading any leaderboard of variants: if one option could only ever be shown to your best users, its score is measuring them.

## Apply to your product

- Which of your optional features has never been evaluated because "we can't randomize it"? Which construction above would fit?
- Do any of your message, offer or layout variants have eligibility rules that restrict them to a specific segment — and are they ranked against each other anyway?
- For your most-cited correlational finding, what is the residual confound, and is it written down next to the number?

## See also

[[ab-test-structure]] · [[design-the-population]] · [[probes-inside-the-product]] · [[unmeasurable-wins]]
