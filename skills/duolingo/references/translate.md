---
name: duolingo-translate
summary: The pack's one non-negotiable rule — the user is not building Duolingo, so every answer has to land in their product, not end at Duolingo's.
metadata:
  internal: true
---

# Translate — the rule that makes this pack useful

## Concept

This pack is a case study, not a catalogue. Duolingo is the worked example; the user's product is the target. An answer that explains what Duolingo did and stops has failed, even when every fact in it is correct.

The failure is seductive because Duolingo's moves are *vivid* — a passive-aggressive owl, a 3,000-day streak, a leaderboard that demotes you. Vivid detail reads as insight. It isn't. The user cannot ship an owl.

## What Duolingo does

Duolingo's own writing does the translation constantly. The engineering posts explain the *constraint* before the solution — "our release cycle limited how many experiments we could run" — so the reader can check whether they share the constraint. The learning-science posts name the mechanism (the spacing effect, the forgetting curve) before the feature that exploits it. The growth posts are explicit that a tactic worked *because of* a specific audience and would not generalize.

Source: `blog.duolingo.com/time-spent-learning-well (Duolingo blog, 2024-06-13; accessed 2026-09-22)` states the metric formula *and* the reason the previous metric failed, which is the part that transfers.

## The transferable pattern

Three moves, in order, every time:

**1. Name the mechanism, not the feature.** The streak is not the insight. Loss aversion applied to a daily counter is. A user building a B2B analytics tool cannot use a streak; they can use loss aversion.

**2. Check whether the user shares the precondition.** Almost every Duolingo pattern has one, and it is usually unstated. Streaks assume a genuinely daily use case — imposing one on a weekly product manufactures guilt and churns people faster. Leagues assume enough concurrent users to fill a bracket. Say the precondition out loud, then ask whether it holds.

**3. End in their product.** The last thing you write should be about *their* thing, in their words, with their constraints. If you can delete the final paragraph and the answer still reads complete, you never translated.

**And when it doesn't transfer, say so.** "Duolingo does this, and you shouldn't, because your users open this twice a month" is one of the most valuable answers in this pack. A skill that only ever says yes is a cheerleader.

## Apply to your product

- What is the mechanism under the Duolingo pattern you just cited — stated so it contains no language-learning words at all?
- What precondition does it need, and does the user's product actually meet it?
- If you deleted every proper noun from your answer, would there still be advice left?

## See also

[[map]] · [[overlaps]] · [[sources]]
