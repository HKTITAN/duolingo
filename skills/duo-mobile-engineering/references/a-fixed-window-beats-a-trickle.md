---
name: duo-mobile-engineering-a-fixed-window-beats-a-trickle
summary: For a broad mechanical migration, halt feature work and concentrate everyone for a fixed window to collapse the dual-maintenance period — but do not freeze releases while you do it.
metadata:
  internal: true
---

# A Fixed Window Beats a Trickle

## Concept

A migration done gradually forces the team to maintain two architectures simultaneously for as long as it lasts, and every partially-migrated area is a merge-conflict surface. The dual-maintenance period is the real cost, and it scales with duration, not with scope. Concentrating everyone for a fixed window ends that period fastest, and has a second effect that is easy to undervalue: it becomes a shared project with a visible end, instead of a chore everyone is behind on.

The near-universal mistake is to freeze releases at the same time, on the reasoning that nothing user-facing is changing anyway. That is precisely when regressions accumulate unseen, until one enormous release exposes them all at once.

## What Duolingo does

Source: blog.duolingo.com/duolingo-android-reboot-2021 (Duolingo blog, 2021-10-27; accessed 2026-09-22)

- Duolingo gathered **all ~30 Android developers for 2 months**, halted feature development, and organized into **5 squads by product area**, each with a designated lead managing that squad's backlog and reporting progress.
- Result: **ANR rate improved 41%** and the frame-rate metric **28%** — about **80% of the way toward their yearly goal**, from a two-month push.
- Duolingo names two real costs. They **paused weekly releases**, which made the eventual single release **arduous with accumulated regressions** and reinforced their dependence on the beta programme. And because a sweeping architectural change cannot be A/B tested normally, they **used app versions as experimental conditions**, which "didn't work perfectly" and left them with **less rigorous metrics comparisons than usual**.
- On the design choice itself: with two options that both fixed the problem, they took the **repository pattern** — splitting a monolithic single source of truth into distinct pieces — over the **selector pattern**, because a filter suppresses the symptom while leaving the coupling that produced it, whereas splitting the source removes the coupling. They weighted the choice further toward the pattern the platform vendor officially recommends, since the ecosystem keeps building tooling, libraries and hiring familiarity around it for free.

## The transferable pattern

1. **Concentrate mechanical migrations; do not trickle them.** The cost you are minimizing is time spent maintaining two of everything. A fixed window with a named end date and everyone on it is the shortest path through.
2. **Keep shipping while you do it.** Freezing releases hides regressions until they arrive together. If you must reduce release frequency, invest in a staged channel with real users, because that becomes your only signal.
3. **Squads with named leads, not one big pool.** Thirty people on one backlog is not a plan. Partition by product area, give each partition an owner accountable for its progress.
4. **Accept that you cannot cleanly experiment on a sweeping change, and say so.** Using build versions as conditions is a legitimate fallback and a weaker instrument. Decide in advance what evidence would count, rather than discovering afterwards that your comparison is not rigorous.
5. **Between two fixes, prefer the one that makes recurrence structurally impossible** over the one that filters the symptom. And where two structures are otherwise equal, take the one your platform vendor recommends — you are buying future tooling for free.

## Apply to your product

- What are you currently maintaining two of, and how much longer is the gradual plan going to take? Multiply that duration by the cost of the duplication before defending it.
- If you concentrated your team for a fixed window, what would have to keep shipping anyway — and do you have a release channel that would catch regressions during the push?
- For the fix you are about to make: does it prevent the problem from recurring, or does it filter the symptom while leaving the cause?

## See also

[[mandate-new-code-first-backfill-on-evidence]] · [[prove-the-shape-in-the-hardest-part-first]] · [[../duo-experimentation/references/ab-test-structure]]
