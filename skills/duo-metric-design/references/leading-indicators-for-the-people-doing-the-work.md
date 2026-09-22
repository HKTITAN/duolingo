---
name: duo-metric-design-leading-indicators-for-the-people-doing-the-work
summary: A metric that arrives after the work is finished cannot change the work — expose quality targets inside the authoring tool, while decisions are still cheap.
metadata:
  internal: true
---

# Leading Indicators for the People Doing the Work

## Concept

Most quality measurement is retrospective. You ship the thing, run the experiment, and weeks later a result lands — by which point the cost is sunk and the person who built it still cannot tell which of their thousand decisions caused the outcome. The verdict is accurate and useless.

The move is to take the metrics you would have reported afterward and expose them *during* production, inside the tool where the work is being made. The same number that was an after-the-fact grade becomes a steering signal, and the feedback loop shortens from weeks to seconds.

## What Duolingo does

Source: blog.duolingo.com/how-were-improving-duolingos-course-creation-process (Duolingo blog, 2019-09-09; accessed 2026-09-22)

- Duolingo built course-quality metrics, then built the **Tree Filter** for course contributors — a tool that color-codes every skill in a course by a chosen metric, so authors see problems **while the course is still being built** rather than after an A/B experiment concludes.
- It shipped concrete in-authoring targets derived from the data: **6–7 lexemes (vocabulary items) per lesson**, and **4–6 lessons per skill at level 0**.
- The Tree Filter became **one of the most-used course-creator tools** — adoption is the evidence that a leading indicator beats a retrospective report for the person holding the pen.
- Stated tension: **blanket recommendations backfired.** Authors already sitting at the sweet spot were being told to add more content, so the recommendations had to be personalized per course. A global target applied without context produces confident bad advice at scale.

Note the scope limit. Duolingo's course tooling is a specialized internal authoring environment; the pattern here is the placement of the signal, not the shape of that particular tool.

## The transferable pattern

1. **List the quality metrics you currently report after the fact.** Analytics dashboards, post-launch reviews, experiment readouts.
2. **Ask which of them could be computed from the draft.** Many can — they were only retrospective because that is where the dashboard happened to live.
3. **Put them in the authoring surface**, next to the work, updating as the work changes. The editor, the config screen, the PR, the campaign builder, whatever your producers actually sit in.
4. **Give a target, not just a number.** "6–7" is actionable; "6.2" is trivia. State the range and where it came from.
5. **Personalize before you recommend.** A target computed for the average case will tell your best producers to get worse. Check the current state before firing advice.
6. **Measure adoption of the indicator itself.** If producers do not open it voluntarily, it is a report, not a steering signal, and nothing has changed.

The cost is that in-authoring targets homogenize output. Everyone converges on the same range, including in the cases where deviation was correct — so hold the targets loosely and let producers override with a reason.

## Apply to your product

- Who in your org produces the artifacts whose quality you measure, and what do they see while producing them?
- Which number from your post-launch review could be computed from a draft and shown live in the editor?
- What target range would you give — and which of your producers is already past it and would be made worse by being told to hit it?

## See also

[[per-unit-quality-map-not-aggregate-score]] · [[score-the-feedback-queue-do-not-drain-it]] · [[../duo-expert-content-engine/SKILL]]
