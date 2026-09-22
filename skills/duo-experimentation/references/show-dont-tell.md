---
name: duo-experimentation-show-dont-tell
summary: When people disagree, the experiment is the answer. The handbook principle that puts metrics over titles.
metadata:
  internal: true
---

# Show Don't Tell

## Concept

The Duolingo Handbook's Principle #4 *Show Don't Tell* puts metrics over hierarchy: when two people disagree about a product change, the answer is to test it, not to escalate. The principle has three parts in the handbook:

1. *We lead with the results of our work, not the story of its effort.*
2. *Our products don't have to explain themselves — they should be intuitive to everyone.*
3. *When we disagree, we test ideas and let the metrics decide.*

This skill mostly extends the third one, but the first two come up too.

## What Duolingo does

"Test everything" is one of Duolingo's named operating principles, and the volume is what makes it more than a slogan: **a few hundred experiments running simultaneously** in a typical week, **over 2,000** through the internal experiments service in its first three years, and thousands of A/B tests a year — covering everything from updating a single button to launching Leaderboards. Source: blog.duolingo.com/improving-duolingo-one-experiment-at-a-time (Duolingo blog, 2020-01-10; accessed 2026-09-22)

- **The evidence is everyone's, which is what takes the title out of the argument.** PMs form and test hypotheses for anything from a copy change to an entirely new app section, and *everyone has access to past experiment data* — so the counter to a senior opinion is a query, not an escalation. Source: blog.duolingo.com/why-i-interned-at-duolingo-rebecca-hu-product-management-intern (Duolingo blog, 2022-08-26; accessed 2026-09-22)
- **Self-serve tooling is the enabling condition.** Duolingo builds its own segmentation, dashboard, retention, funnel and A/B analysis tools; an analyst who arrived from Spotify and Facebook found them as powerful and flexible as those, and easier to use. A culture where only analysts can run the query is a culture that decides by title. Source: blog.duolingo.com/duolingos-secret-weapon-our-beautiful-and-powerful-analytics-tools (Duolingo blog, 2021-03-22; accessed 2026-09-22)
- Experiments are reviewed on a fast cadence ([[experiment-cadence]]); decisions that fall out are committed quickly.

**Where Duolingo says the principle stops.** Writing up the streak milestone redesign, the team states that they test everything *but* recognize some wins are hard to measure quantitatively — and counted that launch a success on two channels at once: early iOS and Android metrics showing more people keeping streaks alive, plus overwhelmingly positive reception on Reddit, Twitter and elsewhere. A team that only ships what it can measure systematically under-invests in craft. Source: blog.duolingo.com/streak-milestone-design-animation (Duolingo blog, 2022-01-21; accessed 2026-09-22)

## The transferable pattern

Three rules:

1. **Disagreement is not a bug.** Two competent people will disagree often; the system question is whether the resolution is by experiment or by escalation. Experiments scale; escalation doesn't.
2. **The experiment must actually be the decision.** If the result can be overruled by anyone's intuition, you don't have a *Show Don't Tell* culture, you have a theater of one.
3. **Some decisions are too small to test.** Build a fast lane for those. Tests are expensive; not everything justifies one.

Anti-pattern: testing decisions that everyone already agrees on. Tests are decision-resolution mechanisms; using them on consensus is just bureaucracy.

## Apply to your product

- The next time two people on your team disagree on a feature change, can it be tested? Will the test actually decide?
- Has anyone in your org overruled an experiment with intuition? What was the cost?
- Are you running enough experiments — or so many that the system is overhead instead of leverage?

## See also

[[hypothesis-design]] · [[ab-test-structure]] · [[ladder-of-evidence]] · [[../duo-product/references/ship-it]] · [[../duo-culture/references/candor-what-not-who]]
