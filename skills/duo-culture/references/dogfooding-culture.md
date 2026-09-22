---
name: duo-culture-dogfooding-culture
summary: The cultural commitment behind the product practice — leaders use the product, ship the bug fix, set the example.
metadata:
  internal: true
---

# Dogfooding (Culture)

## Concept

The product version ([[../duo-product/references/dogfooding]]) describes the practice. The cultural version describes the *why-it-survives*: leaders dogfood publicly, bug reports from internal users get treated as legitimate, and "I would never tolerate this as a user" is a respected reason to push back on a ship.

Dogfooding only works when culture rewards it. Without that, it dies in the first sprint where someone is too busy.

## What Duolingo does

- **More than 70% of the company dogfoods the internal build** — everyone is encouraged to, not only people shipping user-facing features. The CEO dogfoods daily, across multiple courses and multiple device types. Source: blog.duolingo.com/dogfooding-app (Duolingo blog, 2024-03-01; accessed 2026-09-22)
- **Duolingo pays for it.** A twice-yearly Language Challenge gives employees a financial incentive to keep up language courses across a 6-month window — because a habit product fails in ways only visible over weeks, which nobody does voluntarily on top of their real job.
- **Internal reports get first-class tooling.** Shake-to-Report auto-attaches a screenshot, device and app version, the experiments the reporter is treated in, course and lesson state, a log file and a session recording. Internal and external feedback flow into the same aggregator (Jeeves).
- **It is a release gate, not a suggestion box.** Monday mornings QA reviews the weekend's dogfooding bugs, and rollout does not begin while any bug is blocking or significantly degrades the experience.

## The transferable pattern

Three rules:

1. **Leaders set the floor.** If executives don't dogfood, no one will. The behavior is set at the top, even if the practice happens at the bottom.
2. **Internal bug reports are first-class.** Treat them with the same routing, triage, and feedback that external bugs get.
3. **Reward catching the small stuff.** A culture that thanks people for surfacing minor friction will surface more of it. A culture that responds with "is that really a priority" suppresses it.

Anti-patterns:
- "Dogfooding launched" as a one-time program. Half-life of two weeks.
- Internal accounts with privileged paths that bypass the user experience.
- Leadership delegating dogfooding to interns.

## Apply to your product

- Do your executives dogfood? When was the last bug they surfaced?
- Are internal bug reports routed differently from external ones? Should they be?
- Is "I'd never tolerate this as a user" a respected pushback in your team?

## See also

[[../duo-product/references/dogfooding]] · [[talent-density]] · [[managers-keep-practising-the-craft]] · [[quirky-by-design]] · [[../duo-product/references/raise-the-bar]]
