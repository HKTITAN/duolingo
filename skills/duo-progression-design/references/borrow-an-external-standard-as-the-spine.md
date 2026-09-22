---
name: duo-progression-design-borrow-an-external-standard-as-the-spine
summary: Align progression to a third-party standard instead of levels you invented, because invented levels are unfalsifiable.
metadata:
  internal: true
---

# Borrow an External Standard as the Spine

## Concept

Levels you invent cannot be wrong. You can always redefine Level 5, and you will — quietly, under deadline, when the content for it turns out to be expensive. That is the problem. An internal ladder can only be compared to itself, so it cannot tell a user whether they are ready for the real-world task they came for, and it gives your team a bar it can move without anyone noticing. An external standard supplies capability statements the user can check against their own goal, and converts arguments about taste into arguments about coverage, which are settleable.

## What Duolingo does

Source: blog.duolingo.com/how-are-duolingo-courses-evolving (Duolingo blog, 2019-04-03; accessed 2026-09-22)

- Duolingo rebuilt its most popular courses **from scratch** against the CEFR — an external, government-and-institution-recognized framework it did not control — resequencing existing material to follow published "Can Do" statements rather than its own intuition.
- Coverage became measurable: about **800 words at each of A1 and A2**, **over 800 new words** added to the Spanish, French and English courses, with B1 planned to add about **2,000 more words per course**. Those are audit numbers, not marketing numbers — they exist because the standard defines what "complete" means.
- Course sections map to levels, so a user's position in the product has an external meaning: **end of Section 3 = A1, Section 4 = A2, Section 6 = B1, Section 8 = B2**, with end of A2 described as comparable to **4 semesters of university study** (blog.duolingo.com/how-weve-improved-the-duolingo-learning-experience-this-year-and-a-sneak-peek-toward-2020 (Duolingo blog, 2019-12-11; accessed 2026-09-22)).
- Adopting the standard forced product work rather than just relabeling: Duolingo built **new exercise types specifically to reach B1**, because the standard demanded capabilities the existing exercise inventory could not produce.
- Volunteer contributors were pushed to apply the same standard, which is the real cost — a borrowed spine constrains everyone who touches the content, including the people who were happiest improvising.

## The transferable pattern

Before inventing a progression, look for a standard your users are already measured against elsewhere: a certification, a regulatory tier, a competency framework, a published rubric, an industry maturity model, a benchmark suite.

What you gain:

1. **Falsifiability.** "Level 4" means whatever you say. "Meets the standard's tier 3" is checkable by someone who does not work for you.
2. **A coverage audit.** Gaps surface as missing coverage against an external list rather than as a disagreement between two senior people.
3. **Portability of the user's progress.** Achievement inside your product becomes a claim they can make outside it, which is worth more to them than any badge you mint.
4. **A bar you cannot quietly lower.** This is the one your team will resist, and the main reason to do it.

The costs are real: you inherit the standard's blind spots and its pace of revision, you may have to rebuild rather than remap, and a standard that is a poor fit for your domain is worse than none. If no standard fits, publish your own capability statements in the standard's *form* — observable "can do X unaided" claims — so at least the bar is stated in public and moving it is visible.

## Apply to your product

- Is there an external certification, rubric, or benchmark your users already care about? What would it take to map your stages onto it rather than onto your feature set?
- Write the capability statement for each of your current levels as "the user can do X, unaided, in a real situation." Which levels turn out to have no honest statement?
- If you rebuilt your progression against that standard, what content would be revealed as missing — and what existing content would be revealed as ungated indulgence?

## See also

[[sequence-by-task-not-by-taxonomy]] · [[rank-what-you-teach-by-cost-of-getting-it-wrong]] · [[structured-coverage-catches-what-use-never-surfaces]] · [[../duo-product/references/raise-the-bar]]
