---
name: duo-retention-retention-vs-revenue
summary: The explicit tradeoff between monetization aggressiveness and long-term retention; how Duolingo bounds it.
metadata:
  internal: true
---

# Retention vs. Revenue

## Concept

The cleanest version of the *long view* shows up in monetization decisions. Every ad, every paywall, every "upgrade" prompt extracts short-term revenue and pays a long-term retention cost. The question is not whether to monetize — it's where the line is.

Most teams do not draw this line explicitly. Duolingo does.

## What Duolingo does

- Free product is genuinely usable; the paid product (Super Duolingo) removes ads and adds convenience, not core access.
- Ad density is capped, not maximized — the handbook describes deliberately accepting lower per-session revenue to protect long-term retention.
- Paywalls exist but rarely block first value. Users hit them after they're invested, not before.
- The decision rule: if a monetization move improves quarter revenue but degrades cohort retention, it doesn't ship — even if the math says short-term net positive.

## The transferable pattern

A useful frame for any monetization decision:

1. **Estimate both numbers.** What's the revenue lift? What's the retention cost?
2. **Convert retention cost into revenue.** A 1% drop in 6-month retention is worth $X in lifetime revenue. Compare like-for-like.
3. **Default to the long-view answer.** Short-term wins compound less than long-term retention.
4. **Accept that the line is qualitative too.** A move that hits the math but feels coercive (dark patterns, fake urgency) is still a long-term brand cost.

Tension: this requires that the company can afford the long view. Bootstrapped or runway-constrained teams sometimes have to choose short-term. The discipline is to mark it as a temporary choice, not normalize it.

## Apply to your product

- Have you ever quantified the retention cost of a monetization decision, or only the revenue lift?
- Where is your line on coercive monetization? Have you written it down so the next team member knows?
- If you removed your worst monetization touchpoint tomorrow, what would it cost in revenue, and what would it return in retention?

## See also

[[forever-product]] · [[notification-discipline]] · [[../duo-product/references/take-the-long-view]] · [[../duo-product/references/raise-the-bar]]
