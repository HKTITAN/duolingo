---
name: duo-motivation-segmentation-motive-decides-the-lever-and-who-to-exclude
summary: Two cohorts with identical usage curves can need opposite interventions, and pooling in a structurally different segment corrupts the comparison you are making.
metadata:
  internal: true
---

# Motive Decides the Lever — and Who to Exclude

## Concept

Averaging across motives produces a persona that matches nobody. Someone here for enjoyment responds to delight, novelty, and streak pressure; someone here to communicate with a specific person responds to practical utility and cultural depth. Their usage curves can be indistinguishable, so behaviour alone will never tell you which lever to pull. Worse, some segments do not belong in the comparison at all: when a population's causal story is structurally different — insiders to a thing versus outsiders adopting it — pooling them does not add signal, it corrupts the question.

## What Duolingo does

Duolingo analysed learners of Japanese, Korean, and Chinese across Brazil, Germany, India, Mexico, the U.S., and the U.K. — **deliberately excluding Japan, Korea, and China**, because domestic motivations differ structurally from foreign-learner motivations and would have poisoned the cross-country comparison.

- The #1 stated motivation varied by country *and* by language pair: "just for fun" in Germany and India; family and heritage for Chinese learners in Brazil, the U.S., and the U.K.; "spend time productively" for all three languages in Mexico; travel for Brazilians studying Korean.
- **Korean grew 75% year-over-year in India.** In Brazil, India, and Mexico, at least **70% of learners of these languages are 13–22**; **47% of Korean learners in Brazil are 13–17**. Japanese learners spend more time studying daily than Korean or Chinese learners in all six countries.
  Source: blog.duolingo.com/which-countries-study-japanese-korean-chinese (Duolingo blog, 2023-09-13; accessed 2026-09-22)
- The same market-boundedness shows up in engagement metrics themselves. For Year-in-Review, **Japan had the highest view rate and the highest email open rate but the lowest share rate**, while **India and Brazil had below-average open rates and the highest share rates**. Country marketing managers explained both: modesty about effort in one market, pride in achievement in another. Pooling share rate globally would have averaged two opposite social norms into a meaningless middle and hidden the market where the feature worked best.
  Source: blog.duolingo.com/duolingo-2020-year-in-review (Duolingo blog, 2021-05-03; accessed 2026-09-22)

**Tension.** Exclusion is a judgment call you make before you see the result, which makes it hard to distinguish from cherry-picking. The defence is to state the structural reason in writing up front and to report the excluded segment separately rather than deleting it.

## The transferable pattern

Motive selects the lever. Before you ship an intervention, ask which motive it serves and what it does to the others.

1. **Match lever to motive.** Enjoyment-driven users respond to delight and social pressure. Utility-driven users respond to evidence of progress toward the outside goal. The same feature can be a gift to one and noise to the other.
2. **Exclude, don't pool, when the causal story differs.** A segment whose relationship to your product is structurally different is not a noisy version of your other segments — it is a different question. Run it separately.
3. **Write the exclusion rule before the analysis.** Say what makes the segment structurally different, not that its numbers looked odd.
4. **Treat social metrics as market-bound.** Anything that requires a public act — sharing, reviewing, referring, posting — is governed by local norms about self-promotion, not by how much people liked the thing. Segment it by market before declaring a feature failed.

## Apply to your product

- Which of your segments is in your headline numbers only because excluding it felt like cheating?
- Name a feature you judged on a sharing or referral metric. Would that verdict survive a per-market split?
- For your two largest motives, what is one intervention that would help one and actively annoy the other?

## See also

[[split-by-cohort-before-concluding-what-users-want]] · [[in-a-shock-the-motive-mix-moves-first]] · [[../duo-experimentation/SKILL]]
