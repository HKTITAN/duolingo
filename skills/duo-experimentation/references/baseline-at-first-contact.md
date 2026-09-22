---
name: duo-experimentation-baseline-at-first-contact
summary: Capture a self-reported starting level once, at first contact, or you cannot separate what you taught from who you attracted.
metadata:
  internal: true
---

# A Baseline Taken at First Contact

## Concept

Aggregate outcome scores are confounded by acquisition. If your numbers go up after a marketing push, you cannot tell whether the product got better at producing capable users or better at attracting people who were already capable. The fix is cheap and has exactly one valid moment: ask users to self-report their starting level the first time you measure anything, before the product has changed them. Bucket the answer, then compare outcomes *within* buckets at a matched point of progress. The gap you closed between the low-prior bucket and the high-prior bucket is the part attributable to you.

## What Duolingo does

The first time a learner sees the Learning Quiz, they self-report prior knowledge on a 0-10 scale. Duolingo buckets that into four ranges — 0-2 (little), 3-5 (intermediate), 6-8 (substantial), 9-10 (expert) — and then only ever compares scores within a bucket, among users at the same point of course progress. Source: blog.duolingo.com/how-does-duolingo-measure-learning (Duolingo blog, 2018-08-10; accessed 2026-09-22)

The result that matters is the convergence. Among users two-thirds or further through a course, scores on a 0-1 scale ran roughly 0.6 for the little-prior bucket, 0.7 for intermediate and 0.8 for substantial — a gap of about two questions on a ten-question assessment between someone who started from nothing and someone who arrived already competent. A raw average across all buckets would have reported one number that moved with the acquisition mix and nothing else.

The instrument is deliberately harmless. The Learning Quiz has no impact on the user's progress and pays a small reward for taking it. That combination is doing real work: anything that affects standing gets gamed, retried or avoided, and the remaining sample skews toward the confident. Decoupling the measurement from consequences removes the incentive to game it; the reward buys the completion rate that makes the sample representative.

Tension: self-report is a weak instrument. It is unvalidated, subject to over- and under-claiming, and captured exactly once. It is defensible only because it is used to *stratify* a comparison, never as an outcome in its own right.

## The transferable pattern

1. **Ask once, at first contact.** Later is contaminated by the product. A re-ask measures confidence drift, not starting state.
2. **Bucket coarsely.** Three or four ranges. Finer buckets buy false precision from a noisy self-report and shrink each cell below usable size.
3. **Compare within bucket, at matched progress.** Two variables held constant: where they started and how far they have come.
4. **Make the instrument non-punitive and pay for it.** If a measurement can affect someone's standing, you are measuring their strategy, not their state.

## Apply to your product

- Do you know the starting competence of the users your outcome numbers are built from, or only the outcome?
- If your acquisition mix shifted next quarter toward more sophisticated users, would any metric on your dashboard tell you apart from "the product improved"?
- Does any measurement you run affect a user's standing, score or access — and therefore give them a reason to game it?

## See also

[[design-the-population]] · [[probes-inside-the-product]] · [[metric-selection]] · [[ladder-of-evidence]]
