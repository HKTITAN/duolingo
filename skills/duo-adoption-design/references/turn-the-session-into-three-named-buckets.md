---
name: duo-adoption-design-turn-the-session-into-three-named-buckets
summary: Make each finished session a reviewable artifact sorting decisions into what worked, what you missed and what cost you — and surface only the few moments that changed the outcome.
metadata:
  internal: true
---

# Turn the Session into Three Named Buckets

## Concept

A finished session usually leaves the user with one undifferentiated fact: it went well, or it didn't. That fact carries no instruction. Sorting the same session's decisions into a small number of named categories tells the user which *kind* of correction to make, and replaying the decision point — rather than describing it — puts them back at the exact position where their model failed. The second half of the move is restraint: an analysis engine that can annotate everything must deliberately show almost nothing.

## What Duolingo does

- Chess Game Review saves **every completed match** to a history and walks the player through it move by move, highlighting moments in **three buckets**: good moves, missed opportunities, and mistakes.
- The buckets are not symmetric in treatment. **Missed opportunities become interactive retry exercises** or short sequences to think through; **mistakes** are explained with the underlying concept — a pinned piece, a missed threat. Reviewing earns XP, so the review is inside the reward loop rather than beside it.
- It launched on **iOS and Android**.
- The engineering account is explicit that the scope was a deliberate subtraction. Games run **40-plus moves**; Game Review was designed from the start to surface **only key takeaways**, specifically to avoid the information overload improving players hit with standard engine analysis.
- The selection also carries a reframe Duolingo wanted: you do not need to be perfect, only better than the alternative available at that moment. Exhaustive annotation buries that lesson.

Source: blog.duolingo.com/chess-game-review (Duolingo blog, 2026-08-11; accessed 2026-09-22)

Source: blog.duolingo.com/engineering-game-review (Duolingo blog, 2026-09-08; accessed 2026-09-22)

## The transferable pattern

Three properties make a session review actually get used:

1. **Named categories, and few of them.** "What worked / what you missed / what cost you" is a complete taxonomy for most decision-heavy sessions. The name is the instruction: a missed opportunity means look wider next time, a mistake means you had a wrong model. An undifferentiated list of errors means nothing.
2. **Replay, don't narrate.** Put the user back at the decision with the same information they had and let them choose again. Reading about a decision is recognition; re-making it is retrieval. Reserve narration for the cases where the user could not have known — those need the concept, not another attempt.
3. **Selection is the feature.** Completeness of feedback is not thoroughness; it is a refusal to prioritise, and it hands the ranking problem back to the person least able to solve it. If your system can annotate forty things, show three.

Put the review inside the existing reward loop, not in a separate analytics area. A review users have to navigate to is a review users do not do.

## Apply to your product

- What does a user of yours have at the end of a session? If it is one aggregate outcome, what would the three named buckets be?
- Which of your feedback items could be replayed as a decision instead of described as a note?
- If your system can flag forty things, what is your rule for picking the three that change the outcome — and who currently does that ranking, you or the user?

## See also

[[structure-the-session-and-let-them-ask-for-the-explanation]] · [[be-generous-at-the-threshold-when-you-show-someone-their-record]] · [[../duo-experimentation/references/metric-selection]]
