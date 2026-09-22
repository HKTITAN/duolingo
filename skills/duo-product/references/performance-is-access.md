---
name: duo-product-performance-is-access
summary: Treat speed on the worst hardware in your user base as an access problem, and staff a team against it.
metadata:
  internal: true
---

# Performance Is Access

## Concept

Engineers build on flagship devices and fast networks, so the experience of the users at the bottom of the hardware distribution is structurally invisible to the people who could fix it. Framing that gap as *polish* guarantees it loses every prioritization round to a feature. Framing it as **access** — as the product failing to be available to a whole class of users — is what justifies a standing team, a guardrail, and a place on the roadmap.

## What Duolingo does

Source: blog.duolingo.com/android-app-performance (Duolingo blog, 2025-06-11; accessed 2026-09-22)

- The trigger was a measured abandonment problem, not a complaint. In **early 2024, 39% of users on entry-level Android devices waited over 5 seconds** for the app to start — and those users were disproportionately in emerging markets, the same markets carrying growth.
- The framing was explicit: slow startup on cheap hardware **undermines the mission of universal accessibility**. That framing is what turned a cleanup backlog into a funded, **dedicated Android performance team** rather than an occasional sprint.
- Ownership is concentrated rather than diffuse — a named team owns the number, instead of "everyone should think about performance" ([[ownership-clarity]]).
- It compounds with the long view: the users who abandon over load time never enter the retention curve at all, so the payoff shows up as growth rather than as a satisfaction metric ([[take-the-long-view]]).

Tensions to carry over honestly. A dedicated team is real headcount spent on work that ships no visible feature, and its wins are invisible to everyone whose device was already fast — including every executive reviewing it. And a startup-time target can be gamed by deferring work past the measured moment, so the guardrail has to be defined against what the user can actually do, not against when the first frame appears.

## The transferable pattern

1. **Measure at the bottom of the distribution, not the median.** A p50 number describes a user who was never at risk. Publish the p90 or the entry-tier cohort instead, and make that the number the team owns.
2. **Name the harm, not the metric.** "Load time is 5.2s" loses to a feature. "39% of our cheapest-device users wait over five seconds before they can start" is an access failure, and access failures get funded.
3. **Give it a standing owner.** Work that belongs to everyone regresses continuously, because every individual change is individually defensible.
4. **Test on the hardware your users have.** Buy the cheap devices. The experience that is invisible to your team is the one deciding whether a growing segment stays ([[dogfooding]]).

## Apply to your product

- What is your slowest-decile experience right now, and who on the team has personally sat through it this month?
- Is your performance guardrail expressed as an average? What changes if you restate it for your worst-served cohort?
- Which growth segment is currently buying your least-capable experience?

## See also

[[dogfooding]] · [[take-the-long-view]] · [[ownership-clarity]] · [[raise-the-bar]]
