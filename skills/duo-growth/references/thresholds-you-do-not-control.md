---
name: duo-growth-thresholds-you-do-not-control
summary: A platform limit turns steady growth into a step change in acquisition at an arbitrary moment — alert on headroom to the threshold, not on the trend.
metadata:
  internal: true
---

# Thresholds You Do Not Control

## Concept

Between your product and a new user sits a platform that gets to set rules: a download size, a rate cap, a store warning, a policy limit. A trend line invites you to read steady growth as benign. A threshold turns that same steady growth into a step function in user-visible behaviour on an arbitrary day — acquisition degrades overnight with no change to your product and no bug to find. Worse, the people affected are usually invisible in your metrics, because the friction is applied before they ever become a user. So the thing to monitor is not direction but distance to the limit.

## What Duolingo does

- **Learned about the limit from the platform, after crossing it.** Duolingo received a surprise email from Apple that its release candidate had crossed the **200MB** download threshold and would now warn users downloading over cellular — a warning shown to a population that matters, since **about a third of new Duolingo users install on cellular networks**. Nothing in the product had changed for the worse; the size had simply drifted up until it hit someone else's line. Source: blog.duolingo.com/emerge-tool-app-size (Duolingo blog, 2023-07-14; accessed 2026-09-22)
- **Refused to treat it as a regression to revert.** Duolingo's stated reasoning was that "focusing on the latest regression would be shortsighted" — the last commit was not the cause, the absence of a budget was. They attacked the whole size problem instead, cutting the app by **20%**. Same source.

Tension: alerting on headroom means building an alert around a number owned by a third party who can move it, deprecate it, or apply it differently by region without telling you. And the population it protects is exactly the one you cannot see in your funnel, so the alert can never be validated against your own conversion data — you are instrumenting a harm you have to take on faith.

## The transferable pattern

1. **Enumerate the limits between you and a new user.** Size caps, rate limits, warning thresholds, policy ceilings, quota tiers. Most teams have never written the list down.
2. **Alert on distance, not direction.** "We are at 91% of the cap" is actionable. "Growing 2% per release" is not, because it reads as healthy right up until it isn't.
3. **The last change is not the cause.** When you cross a limit, reverting the most recent increase buys a release and rebuilds nothing. The absence of a budget is the defect.
4. **Assume the damage is invisible.** Users gated before signup never appear in your metrics, so absence of a dip is not evidence of absence of harm.

## Apply to your product

- What third-party limits sit between a prospective user and their first successful session, and how much headroom do you have on each right now?
- Is any of that headroom monitored, or would you learn about it from the platform's email?
- Which of your acquisition losses would be invisible in your own funnel because they happen before signup?

## See also

[[displace-an-accredited-incumbent]] · [[../duo-product/references/performance-is-access]] · [[localization-as-growth]]
