---
name: duo-motivation-segmentation-size-of-other-is-a-taxonomy-diagnostic
summary: A spike in the catch-all bucket for one segment means your category list is wrong there — read it as a diagnostic, not a rounding error.
metadata:
  internal: true
---

# The Size of "Other" Is a Taxonomy Diagnostic

## Concept

A forced-choice list encodes the researcher's prior. Every option you offer is a guess about what motivates people, and the catch-all at the bottom is where users go when none of your guesses fit. So the size of "other" is not noise to be dropped from the chart — it is a measurement of how wrong your model is, segment by segment. Where "other" spikes, your product assumptions are least tested, and the people in that bucket are receiving an experience designed around a motive they do not have.

## What Duolingo does

Duolingo watched the catch-all rate vary by segment instead of averaging it away.

- Roughly **10% of English, Spanish, and French learners choose "other"** — but **about 20%, double the rate, for indigenous and endangered languages**. Duolingo's read is that these learners are driven by media, entertainment, and music specifically: a motive finer-grained than the "culture" bucket on offer.
- Adjacent evidence supported the diagnosis rather than the bucket. **34% of U.S. Yiddish learners cite culture as their primary reason — three times the English/Spanish/French rate — and 54% cite family or culture combined.** In a Duolingo–DKC Analytics survey, **70% of pandemic-era new learners tied their learning to heritage, ancestry, or culture; 27% had a family member from an endangered, indigenous, or understudied language community, and 90% of those were interested in learning it. 69% practised via TV and streaming, 69% via social media.**
  Source: blog.duolingo.com/understudied-language-motivations-2021 (Duolingo blog, 2021-12-08; accessed 2026-09-22)

**Tension.** A reported category is a readout of the respondent's own schema, not a description of the thing being categorised. Duolingo makes this point about perceived similarity: one of five reasons unrelated languages sound alike is that "they're not as similar as you think" — an unfamiliar language is channelled through the ones you already know, so what feels similar to you "could be totally different from what speakers of other languages perceive as similar." The post is careful, though: four of its five explanations are real properties of the artifacts. Rule those out before blaming the observer, and rule the observer out before believing the comparison (blog.duolingo.com/why-unrelated-languages-can-be-similar (Duolingo blog, 2025-07-08; accessed 2026-09-22)). Practically: a big "other" tells you your list is wrong, but the free-text explanations inside it are still filtered through the respondent's categories, not yours.

## The transferable pattern

Instrument the catch-all and put it on the dashboard with the named options.

1. **Report "other" per segment, never pooled.** The global rate is stable and boring. The per-segment rate is where the finding is.
2. **Set a threshold in advance.** Pick a rate — say, double your baseline — at which the taxonomy gets revisited rather than defended.
3. **Always allow free text alongside it,** and read it in bulk. Recurring phrasing in that box is the name of the category you failed to offer.
4. **Expect the fix to be finer-grained, not broader.** The usual cause is a bucket that is technically correct but too coarse to be actionable. Splitting one category beats adding a sixth.
5. **Re-ask after you change the list.** A taxonomy revision invalidates the trend line; say so rather than plotting the old and new mixes on one axis.

## Apply to your product

- What is your catch-all rate broken out by segment, and which segment is twice the rest?
- Do you store the free text next to the choice, or throw it away at collection time?
- When did you last change your category list, and would a chart of that field across the change be misleading?

## See also

[[name-the-unplanned-motive-then-interview-it]] · [[collect-a-declared-why-at-signup]] · [[../duo-measurement-validity/SKILL]]
