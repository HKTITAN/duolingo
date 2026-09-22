---
name: duo-experiment-velocity-build-tools-that-can-embarrass-you
summary: An analytics tool earns its keep by disconfirming beliefs, which requires cheap arbitrary cohorting and at least one method that can return a category nobody hypothesised.
metadata:
  internal: true
---

# Build Tools That Can Embarrass You

## Concept

Teams generate hypotheses far faster than they can test them, and every hypothesis arrives attached to a person who wants it to be true. That asymmetry decides what your tooling is actually for. If slicing an arbitrary group of users and checking a relationship is expensive, the only findings that ever surface are the ones somebody deliberately went looking for — which means the tool returns a filtered stream of confirmations and feels extremely useful while doing it. A tool is worth its cost when it can cheaply show that a feature the team was proud of made things worse. The same logic indicts the analytical framework you use to organise the business, because a framework can only return categories you already thought of.

## What Duolingo does

Source: blog.duolingo.com/how-cohorts-and-correlations-help-us-better-understand-our-learners (Duolingo blog, 2019-09-19; accessed 2026-09-22)

- Duolingo added cohorting and correlation analysis to its internal analytics dashboard, and states plainly that these tools are equally or more important for checking and correcting the team's misconceptions about what makes the product better — because a feature the team expects to help can do the opposite.
- The worked example shows the shape of an unlooked-for finding. Users of the Stories feature had streaks that were **7 days longer on average**, and the correlation with still using Stories a month later was **maximised at four or more stories in the first week**.
- The post then attacks its own number. Correlation is not causation, so doing four stories does not mean a user is more likely to continue — the threshold is **a flag for further analysis, not an activation target to optimise**. A team that skipped that sentence would have shipped a campaign to push everyone to four.
- The structural version of the same problem — Duolingo framed its move toward unsupervised methods as moving the organisation away from analytical frameworks that can foster confirmation bias, in order to reach insights beyond the path most taken (blog.duolingo.com/growth-model-duolingo (Duolingo blog, 2023-02-17; accessed 2026-09-22)).
- What this node does not cover — whether any surfaced relationship is causal, and what design would let you believe it. That belongs to [[../duo-measurement-validity/SKILL]] and [[../duo-experimentation/references/ladder-of-evidence]]. This node is about whether the finding can surface at all.

## The transferable pattern

- **Define an arbitrary group in seconds, or you will only ever check the groups someone argued for.** Cohorting cost is the real gate on disconfirmation, and it is invisible because nobody files a ticket for a check they did not think to run.
- **Point the tool at your own recent shipped work first.** Run the segments around a feature you are proud of. If the tool cannot possibly produce a bad answer there, it is a reporting layer, not an analysis tool.
- **Treat a sharp threshold as a hypothesis generator.** A number where a correlation peaks is a starting point for a test. Turning it directly into a target optimises the proxy and usually selects for the users who were already going to stay.
- **Pair every top-down framework with a bottom-up method.** Segments you defined will keep confirming the model that produced them, so run at least one method that can return a grouping nobody proposed.
- **Log the disconfirmations somewhere visible.** The value of the tool is the beliefs it killed, and that record is the only defence against the version of the team that re-proposes the same idea next year.
- **Expect the finding to be unwelcome, and decide in advance who it goes to.** A tool that can embarrass the team only works if the embarrassing output reaches a decision rather than a drawer.

## Apply to your product

- What is the strongest belief your team holds about why users stay, and what query would show it is wrong? How long would running that query take today?
- Which of your standard segments were designed by the same people who designed the product strategy they are used to evaluate?
- Name a recent finding that changed someone's mind. If you cannot, is that because your beliefs are correct or because your tooling cannot challenge them?

## See also

[[self-serve-adoption-is-the-tooling-metric]] · [[curate-the-report-per-experiment-type]] · [[../duo-growth-model/SKILL]]
