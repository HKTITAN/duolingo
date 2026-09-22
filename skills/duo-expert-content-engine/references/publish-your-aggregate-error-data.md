---
name: duo-expert-content-engine-publish-your-aggregate-error-data
summary: What users get wrong most often is a byproduct you already own and a competitor cannot replicate — published, it is credible because derived and useful because it targets the real failure mode.
metadata:
  internal: true
---

# Publish Your Aggregate Error Data

## Concept

Every system that grades, validates, or corrects its users accumulates a record of what they get wrong. Most teams treat that record as an internal quality signal and nothing else.

It is also the rarest kind of content asset: a claim that is credible because it was derived rather than asserted, useful because it targets the reader's actual failure mode instead of a generic best practice, and effectively unreplicable, because a competitor cannot produce the same ranking without your volume. Generic advice is available from anyone. A frequency-ranked list of the real mistakes is available only from whoever owns the logs.

## What Duolingo does

Source: blog.duolingo.com/mistakes-in-french-for-learners (Duolingo blog, 2026-05-28; accessed 2026-09-22)

- Duolingo analyzed its own learner data to publish the **top 5 most common mistakes** early French learners make, ranked by observed frequency rather than by editorial judgement: verb conjugation, gender agreement, number agreement, adjective agreement, word order.
- Each ranked error is paired with **the underlying pattern that causes it**, so the piece explains the failure rather than just listing it — the same tactic-plus-mechanism discipline that makes crowdsourced tips teachable.
- The ranking doubles as a demonstration of data scale: publishing a frequency order implies a corpus large enough to produce a stable one, without needing to state a user count.
- Because it is derived from behavior rather than from opinion, the piece is defensible under a credentialed byline in a way that a "five tips" post is not (blog.duolingo.com/study-tips-from-learners (Duolingo blog, 2023-03-07; accessed 2026-09-22)).

**Tension.** An error ranking describes your users on your surface, not the world. What people get wrong inside a system is partly a fact about the people and partly a fact about the system's design — a confusing interface manufactures errors that would not exist elsewhere. Publishing the list without that caveat invites readers to treat an artifact of your product as a universal truth about the domain, and it quietly advertises your own rough edges to anyone reading carefully.

## The transferable pattern

1. **Inventory the byproducts you already log** — failed validations, abandoned steps, retried actions, rejected inputs, most-corrected fields. Any of them is a frequency table waiting to be published.
2. **Rank by observed frequency, not by editorial instinct.** The ranking is the whole value; a list your team ordered by intuition is indistinguishable from every other list.
3. **Pair each entry with its cause.** The frequency makes it credible; the mechanism makes it useful.
4. **Publish the aggregate only.** Individual records belong to individual people; a ranked distribution does not identify anyone.
5. **Separate what the data says about your users from what it says about your design.** Some entries on the list are your fault, and naming which ones is more credible than pretending none are.
6. **Re-derive it on a schedule.** A frequency table is a snapshot, and a stale one presented as current is a liability.

## Apply to your product

- What does your system already record about user failure that nobody has ever aggregated?
- If you published your top five most common user errors next week, which of them would be embarrassing because they are really design defects — and would fixing those be worth more than the post?
- Who else could produce the same ranking? If the answer is nobody, why are you not publishing it?

## See also

[[solicit-tactics-credit-them-add-the-mechanism]] · [[define-the-unit-and-recut-by-frequency]] · [[../duo-experimentation/SKILL]]
