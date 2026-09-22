---
name: duo-metric-design-score-the-feedback-queue-do-not-drain-it
summary: Past the volume you can review, rank reports by predicted validity and work top-down — and treat the rejected majority as a map of where users were taught wrong.
metadata:
  internal: true
---

# Score the Feedback Queue, Do Not Drain It

## Concept

Every feedback channel eventually outgrows the people reading it. The default response is to work the queue in order and accept a growing backlog. That is the worst available allocation: review capacity is fixed and report quality is wildly skewed, so first-in-first-out spends your scarcest resource at the *base rate* of validity.

Scoring the queue instead — ranking each report by predicted validity from cheap signals, then reviewing top-down — concentrates reviewers on the tail where real defects live and multiplies effective throughput without adding headcount. The second, less obvious half: the reports you reject are not waste. A confident-but-wrong report is a precise address for a place your product taught someone the wrong model.

## What Duolingo does

Source: blog.duolingo.com/how-user-reports-improve-course-content (Duolingo blog, 2022-03-29; accessed 2026-09-22)

- Volume: roughly **200,000 user reports per day**. The mix is highly concentrated — **72% "my answer should have been accepted," 10% "the audio does not sound correct," 5% "the hints are wrong or missing."**
- Duolingo built a **Report Quality Estimation Tool**: an ML model producing a report-quality score used to prioritize which of the day's reports get human review first. Signals include the reporter's history, how many other users reported the same thing, and how far the submission sits from known-good answers.
- Validity really is skewed: only about **15% of reviewed "should have been accepted" reports are judged correct** and become new accepted answers.
- The other **~85% are not discarded.** Duolingo treats them as a signal of concepts learners are not grasping, and surfaces **reports per session** to course creators at **course, section, skill and individual-exercise granularity**, so they can change the teaching approach or prioritize an inline explanation at that exact spot.

Tension worth naming: a validity model trained on past review decisions will inherit those decisions' blind spots, and a reporter-history signal systematically down-ranks first-time reporters — exactly the population whose confusion is most diagnostic. Ranking is an allocation policy, not a verdict; the low-ranked tail still has to be sampled.

## The transferable pattern

1. **Measure the skew before you build anything.** What fraction of reports in each category turn out actionable? If validity is near-uniform, ordering buys you nothing and you have a capacity problem instead.
2. **Score with cheap signals first.** Reporter track record, duplicate count, and distance from a known-good state usually get most of the lift. A heuristic ranking shipped this month beats a model shipped next year.
3. **Review top-down, sample the bottom.** Reserve a slice of capacity for randomly drawn low-ranked reports — that is your only check on whether the ranker is wrong.
4. **Aggregate the rejections by location.** A rejected report says the product is working and the user's mental model is not. That is the only signal that finds comprehension failures rather than functional ones, and bug trackers throw it away by design.
5. **Route that map to whoever owns the content**, at the granularity they can edit. Reports-per-unit, normalized by traffic, pointed at the person who can rewrite the confusing thing.

## Apply to your product

- What is your actual validity rate per feedback category — and if you cannot answer, what would it take to sample 100 reports and find out?
- Which three cheap signals could rank your queue tomorrow, before anyone builds a model?
- Where do your rejected reports go, and who would benefit from seeing them clustered by the screen that produced them?

## See also

[[leading-indicators-for-the-people-doing-the-work]] · [[per-unit-quality-map-not-aggregate-score]] · [[../duo-measurement-validity/SKILL]]
