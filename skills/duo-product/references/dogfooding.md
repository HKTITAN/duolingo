---
name: duo-product-dogfooding
summary: Use the product daily; the cheapest, most honest source of polish.
metadata:
  internal: true
---

# Dogfooding

## Concept

Dogfooding is the practice of the people building a product being heavy users of it. Done seriously, it's a quality forcing function — bugs surface, friction surfaces, missing polish surfaces, because the people who can fix them are stubbing their toes daily. Done as ritual, it's theater.

## What Duolingo does

Source: blog.duolingo.com/dogfooding-app (Duolingo blog, 2024-03-01; accessed 2026-09-22)

- **More than 70% of the company dogfoods**, including the CEO, who uses the internal build every day across multiple courses on multiple device types. Employees run the latest internal build on Android, iOS, and Web.
- Internal bug reports have their own tooling: **Shake-to-Report** (shake the phone, get a form) auto-attaches a screenshot, the user's active experiments, device, app version, course and lesson state, a log file, and a Fullstory recording of what happened just before the bug.
- A **Release Dashboard** reads telemetry (ANR, crashes, OOM, frame rates) from each dogfooding build and produces a reliable signal within a few hours; **Jeeves** clusters dogfooding and external feedback into trending "spikes."
- The gate is real: on Monday mornings QA reviews weekend dogfooding bugs and **rollout does not begin while any blocking or significant-UX bug is open**.
- A twice-yearly Language Challenge pays a financial incentive for employees to dogfood language courses consistently over a 6-month period.
- It catches real launch risk. Weeks before Math and Music shipped on iOS, persistent dogfooding reports plus elevated Crashlytics numbers led the team to add targeted logging and find the root cause: an edge case from pausing songs in a specific pattern.

Dogfooding also carries early product bets. The first internal Friend Streak build was entirely on-device — if you started a streak with someone, they were never told. The team calls it an "uber prototype"; Duos loved even that hacky version, and that engagement won leadership buy-in (blog.duolingo.com/product-lessons-friend-streak (Duolingo blog, 2024-09-20; accessed 2026-09-22)).

## The transferable pattern

Three rules:

1. **Use the product, not the demo.** A staging instance and a demo account aren't dogfooding. Real account, real data, real consequences.
2. **Leaders dogfood publicly.** Engineers won't if execs don't. The behavior is set at the top.
3. **Friction beats heroics.** A small daily annoyance fixed early is worth more than a big quarterly polish push.

Anti-patterns:
- "We don't have time to use it." That's a leadership problem, not a calendar problem.
- Dogfooding only at launch. The half-life of a launch dogfood program is two weeks.
- Internal users with privileged accounts that bypass the user experience.

## Apply to your product

- Do you use your own product daily, with a real account, on the same platform as your users?
- When was the last bug you reported from your own use?
- What's a daily friction point you've worked around so long you forgot it was there?

## See also

[[raise-the-bar]] · [[polish]] · [[intuitive-by-default]] · [[performance-is-access]] · [[../duo-culture/references/dogfooding-culture]]
