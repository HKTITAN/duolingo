---
name: duo-return-triggers-resurrected-users-are-their-own-cohort
summary: Users returning after a long absence retain worse than new users and need their own definition, metric and re-onboarding.
metadata:
  internal: true
---

# Resurrected Users Are Their Own Cohort

## Concept

Most analytics stacks recognise two kinds of active user — new and existing. The person who left for two months and came back this morning is silently filed under one or the other, and served the default experience either way. They are in fact a third cohort with worse odds than a brand-new user, because they return with decayed skill and lost status, and the default flow greets them with the accumulated consequences of their absence at the exact moment their commitment is lowest. A new user has nothing to confront. A returning one has a pile of it.

## What Duolingo does

Source: blog.duolingo.com/back-from-the-brink-what-duolingo-learned-about-its-resurrected-users (Duolingo blog, 2017-08-30; accessed 2026-09-22)

- Duolingo wrote down an explicit definition first — a **resurrected user is one who was inactive for 30 days or more and then returned**. Until the definition existed the cohort was invisible.
- They then measured it manually and found it **far larger than expected** — about **5% of daily active users on any given day are resurrected users**.
- The retention gap is the reason it matters. Resurrected users are roughly **20% less likely than a new user to still be active at both 7 days and 14 days**.
- Having sized it, they built a **dedicated re-onboarding experience** for that cohort rather than routing it into the new-user flow or the existing-user home screen.
- Tension the post concedes — the better play is upstream. Predicting who is about to go inactive and holding onto them would "eliminate the need to resurrect" at all. Resurrection work is remedial by nature; do not let a good win-back funnel disguise a churn problem you could have prevented.

## The transferable pattern

Make the cohort real before you try to serve it.

1. **Write the definition down.** Pick an inactivity threshold that fits your natural usage cadence — 30 days suits a daily product, a week might suit a high-frequency one, a quarter suits a B2B tool. The number matters less than having one.
2. **Measure the size as a share of daily actives**, not as a raw count. A percentage tells you whether to staff it.
3. **Measure their retention separately from new users.** If it is worse — it usually is — you have been under-serving a cohort you did not know you had.
4. **Give them their own entry path.** Not the first-run tour, which insults them, and not the default home, which confronts them.
5. **Report the upstream number next to it.** Win-back volume looks like success and is partly a measure of failure. Track predicted-churn saves alongside it.

## Apply to your product

- What is your inactivity threshold, and what share of today's actives crossed back over it?
- Do returning users in your product retain better or worse than first-timers, and have you ever actually split the chart?
- Is anyone on your team accountable for preventing the churn that your win-back campaign is paid to reverse?

## See also

[[re-entry-resumes-it-does-not-restart]] · [[new-content-beats-a-guilt-nudge]] · [[../duo-retention/references/churn-diagnostics]]
