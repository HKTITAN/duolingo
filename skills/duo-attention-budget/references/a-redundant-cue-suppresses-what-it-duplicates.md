---
name: duo-attention-budget-a-redundant-cue-suppresses-what-it-duplicates
summary: When two signals carry the same meaning the cheaper one absorbs all the processing, so a helpful redundant cue becomes a permanent crutch unless removal is scheduled.
metadata:
  internal: true
---

# A Redundant Cue Suppresses What It Duplicates

## Concept

Attention allocates to whatever is informative. When two signals in the same view carry the same meaning, the cheaper one wins — it is faster to process and it fully determines the answer, so the expensive one becomes redundant and is never encoded. The user gets the right answer every time and learns nothing about the signal you were trying to teach.

This is the failure mode of every helper, hint, and highlight. Added early, a redundant cue is genuine scaffolding: it keeps the user succeeding while the real signal is still too expensive to read. Left in, it is a crutch that guarantees the real signal is never attended. The cue is only scaffolding if its removal is scheduled.

## What Duolingo does

Source: blog.duolingo.com/common-mistakes-language-learners (Duolingo blog, 2023-08-22; accessed 2026-09-22)

- Duolingo names the exact case: learners' brains process the content word **"yesterday"** and ignore the **"-ed"** ending, because both mark past tense. The ending is redundant given the adverb, so it does not get attended.
- The design response is two-sided, and the second side is the part people skip: **more cues like "yesterday" appear in early lessons** when "-ed" is first taught — and then, in the post's own words, "eventually you have to get used to focusing on those endings alone."
- So the cue is added on purpose *and* withdrawn on purpose. Duolingo does not treat the scaffold as a permanent kindness.
- The honest cost: withdrawal makes the task visibly harder for a while, and users who were succeeding start failing. That dip is the thing being learned becoming visible, not a regression — but it will look like one in your metrics.

## The transferable pattern

- **Look for duplicated meaning in the same view.** A colour and a label that say the same thing. An icon and its tooltip. An inline hint and the field it explains. A summary sentence and the chart beneath it. Whichever is cheaper to read is the only one being processed.
- **Decide which signal the user must eventually read unaided.** That is the expensive one — the chart, the ending, the raw field. Everything that duplicates it is temporary by construction.
- **Schedule the withdrawal when you add the cue, not later.** "We will take the training wheels off eventually" never happens, because by then removal looks like a regression. Write the removal condition into the same change that adds the cue.
- **Expect a visible dip on removal.** Success rate drops, support questions rise. If you cannot tolerate that, you have decided the user never needs to read the real signal — which is a legitimate choice, but make it consciously rather than by drift.
- **Redundancy is not always harmful.** Where the user only needs the outcome and will never need to read the underlying signal unaided, duplicate freely. The cost only applies to signals you intend them to learn.

## Apply to your product

- Where in your interface do two elements carry exactly the same information? Which one is cheaper to read, and is that the one you wanted them to learn?
- Which of your hints, tooltips, and helper texts were added as temporary scaffolding and have now been there for years?
- If you removed your most-used hint tomorrow, what would break — and is that breakage the thing you have been failing to teach?

## See also

[[salience-is-a-budget-and-it-front-loads]] · [[hold-everything-but-the-target-constant]] · [[../duo-design/SKILL]]
