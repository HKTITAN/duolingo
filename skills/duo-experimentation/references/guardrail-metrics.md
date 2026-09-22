---
name: duo-experimentation-guardrail-metrics
summary: Metrics that must not go down even if the primary goes up; the safety net for an experimentation culture.
metadata:
  internal: true
---

# Guardrail Metrics

## Concept

A guardrail metric is a metric an experiment is *not* trying to move, but must not break. A test optimizing for engagement shouldn't crater notification mute rate. A revenue test must not destroy retention. Without explicit guardrails, experimentation cultures slowly degrade the product on dimensions nobody is watching — each experiment locally rational, the cumulative effect bad.

## What Duolingo does

The clearest published case: Duolingo ran a promo letting non-subscribers tap into locked skills while offline, then showed a Duolingo Plus upsell when they tried to start the lesson. The experiment group subscribed at a **much higher rate**. Duolingo shut it down anyway — retention fell and daily active users dipped, because the way the promo was presented discouraged those learners from using the app offline at all. The write-up says it plainly: the experiment "was successful from a revenue standpoint," and they killed it and iterated instead. Source: blog.duolingo.com/improving-duolingo-one-experiment-at-a-time (Duolingo blog, 2020-01-10; accessed 2026-09-22)

- **Guardrails live in the report template, not in anyone's memory.** Each experiment type has a template carrying a curated metric list *plus* universal metrics that always apply — the standing commitment being that they never launch experiments that hurt learning or lower engagement.
- **A guardrail only counts if it can veto a win.** The person running a revenue test has no incentive to go looking for the retention damage. The template goes looking for them.
- Guardrails are pre-registered, not picked after the fact, and breach is sufficient to block ship.
- **Cannibalization is a guardrail, not a footnote.** A new surface and the core loop draw on the same fixed attention, so a feature that merely relocates existing usage looks identical to one that creates new usage on every dashboard except the one comparing them. After finding that Duolingo Stories users had longer streaks and strong week-to-week retention, the team ran one final correlation — Stories lessons against regular lessons — specifically to confirm Stories were additive rather than supplanting the core lesson. They were. The same post flags the reverse-causation risk on its own headline stat: the most committed learners may simply be the ones who chose to try Stories. Source: blog.duolingo.com/how-cohorts-and-correlations-help-us-better-understand-our-learners (Duolingo blog, 2019-09-19; accessed 2026-09-22)

The uncomfortable part, and the reason this is a leadership commitment rather than an analytics feature: the revenue number was real. Killing it only works if the veto was agreed before anyone saw the chart.

## The transferable pattern

Three rules:

1. **Every experiment names guardrails up front.** Picking them after the fact lets winners-on-primary slip through with damage on dimensions you'd have caught.
2. **Guardrails are *thresholds*, not directions.** "Don't break X" needs a specific tolerance. Otherwise the discussion devolves into "well, only a tiny bit."
3. **Cumulative breach matters too.** Many experiments individually within tolerance can collectively drift a guardrail. Use a holdout cohort to detect this.

Common useful guardrails:
- Long-term retention (for revenue/short-term experiments)
- Revenue (for retention/engagement experiments)
- Notification mute / unsubscribe rate (for any messaging change)
- Crash rate / error rate (for any code change)
- Latency / load time (for any UI change)
- Core-loop volume per user (for any new surface — the cannibalization check)

## Apply to your product

- Pick your last shipped experiment. What guardrails were defined? Were they breached?
- Do you have a holdout cohort that catches cumulative drift?
- What's a metric your product has been silently regressing on while individual tests "won"?
- For the newest surface in your product, have you checked whether its usage is additive to the core loop or drawn from it?

## See also

[[metric-selection]] · [[ab-test-structure]] · [[show-dont-tell]] · [[quasi-experiments]] · [[invariant-metric-for-redesigns]] · [[../duo-retention/references/retention-vs-revenue]]
