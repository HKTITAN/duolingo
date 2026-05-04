---
name: duo-experimentation-guardrail-metrics
summary: Metrics that must not go down even if the primary goes up; the safety net for an experimentation culture.
metadata:
  internal: true
---

# Guardrail Metrics

## Concept

A guardrail metric is a metric an experiment is *not* trying to move, but must not break. A test optimizing for engagement might shouldn't crater notification mute rate. A revenue test must not destroy retention. Without explicit guardrails, experimentation cultures slowly degrade the product on dimensions nobody is watching — each experiment locally rational, the cumulative effect bad.

## What Duolingo does

- Most retention experiments carry monetization guardrails (revenue must not drop materially) and vice versa.
- Notification experiments carry mute-rate guardrails — a notification can lift open rate but lose the right to send the next one.
- Engagement experiments carry "user-reported satisfaction" or proxies for it — short-term lifts that come from coercive design fail this guardrail.
- Guardrails are pre-registered, not picked after the fact, and breach is sufficient to block ship.

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

## Apply to your product

- Pick your last shipped experiment. What guardrails were defined? Were they breached?
- Do you have a holdout cohort that catches cumulative drift?
- What's a metric your product has been silently regressing on while individual tests "won"?

## See also

[[metric-selection]] · [[ab-test-structure]] · [[show-dont-tell]] · [[../duo-retention/references/retention-vs-revenue]]
