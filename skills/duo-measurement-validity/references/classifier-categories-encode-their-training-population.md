---
name: duo-measurement-validity-classifier-categories-encode-their-training-population
summary: A group the training data never contained gets filed under its nearest surface match, and the misfiling will be read as a finding.
metadata:
  internal: true
---

# Classifier Categories Encode Their Training Population

## Concept

A classifier learns the surface markers that separated the groups it was shown. It does not learn the causal structure that produced those markers, and it has no label meaning "this is a fourth thing I have never seen." So when a population the training data never contained happens to share surface features with one it did — by a different route entirely — the model files it under that label with full confidence. The output looks like a measurement of the person. It is a measurement of the training set. The damage is that the misfiling gets quoted downstream as a discovery about the misfiled group.

## What Duolingo does

- A Duolingo post on Black Spanish dialects opens with a widely shared MIT quiz built to guess a test taker's US English dialect and native language. Many Spanish speakers found their English classified as **"U.S. Black Vernacular/Ebonics"** — a category the quiz had markers for, applied to speakers it was never built to distinguish.
- Dr. Aris Clemons treats the misclassification as an entry point rather than as data. The surface convergence is not random — there is genuine historical contact between Afro-Latino and African American varieties, plus parallel phonological processes that produce similar markers by independent routes. But the quiz cannot tell those apart, so its output is evidence about its own label set, not about the speakers.
- Scale matters to why the category was missing in the first place — roughly **25% of Latin America's population is Afro-descendant, versus about 12% of the U.S.** A population that large being absent from a model's categories is a fact about who built the model (blog.duolingo.com/black-spanish-dialects (Duolingo blog, 2024-01-25; accessed 2026-09-22)).
- The complementary move, when the boundary of a category is genuinely contested, is to stop adjudicating membership. Music researchers, per Duolingo's explainer, avoid ruling on what is and is not music — Islamic and Jewish liturgical chanting is recitation to practitioners and musical to outsiders — and instead catalogue **features that recur in most places most of the time**, such as beat subdivisions of two or three and asymmetrical scales (blog.duolingo.com/is-music-a-universal-language (Duolingo blog, 2024-01-31; accessed 2026-09-22)).
- The tension between the two halves is real. A feature catalogue is more honest and much harder to act on — you cannot route, price, or alert on "has 6 of 9 properties" as easily as on a label. Definitions are operationally cheap and epistemically expensive; feature sets are the reverse.

## The transferable pattern

- **A label set is a map of the data that trained it.** Before trusting an assignment, ask which populations the training set could not have contained. Those are the ones that will be confidently mislabelled.
- **Give every classifier an "unlike anything I know" output** with a real threshold, and monitor its rate. A model that never abstains is not confident, it is uninstrumented.
- **Audit the cases the model is most confident about.** Confidence is computed inside the label set, so the most confident misfilings are the ones nobody reviews.
- **Distinguish shared cause from shared appearance.** Two populations can converge on the same markers by different routes. The classifier cannot see the route; you can, from domain knowledge, and it changes what the output means entirely.
- **When a boundary is culturally or politically contested, ship features instead of membership.** A definition forces a binary call on every instance, turns every disputed case into a blocking argument, and quietly installs the builders' assumptions as the criterion. A feature catalogue describes an instance by which properties it has and survives instances that fit no existing category.
- **Check the assignment rate against the population you believe exists.** A category absorbing far more cases than its real-world share is the signature of a missing label next door to it.
- **Never let a model's output re-enter as ground truth.** A misfiling that gets logged, aggregated and charted becomes a finding about the world within one quarter.

## Apply to your product

- Which segment, tier or category in your system has no "none of these" option — and what happens to an account that genuinely is none of them?
- Where did your category labels come from, and which populations were absent from the data that produced them?
- Is there a classification you currently report as a fact about users that is really a fact about your label set? What would it cost to report the confidence and the abstention rate next to it?

## See also

[[audit-bias-at-intersections]] · [[resemblance-is-not-lineage]] · [[../duo-inclusive-access/SKILL]]
