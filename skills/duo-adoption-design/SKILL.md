---
name: duo-adoption-design
description: Design a shipped feature so it actually gets used — lower the cost of starting, give one obvious next step, and plan for the moment the user stalls, is embarrassed, is in the wrong place, or gets it wrong. Draws the pattern library from Duolingo's public record (path redesign, guided calls, Game Review, Practice Hub, Friends Quests, Year in Review migration) and restates each move for any product. Use when you hear "we shipped it and nobody uses it", "users say they're not sure they're doing it right", "should this be free choice or a fixed order", "our activation is bad", "people open the feature and bounce", "how do we onboard without a tutorial", "should we gate the recap", "nobody finishes the session", "users are abusing this feature", or "power users keep asking for a way to skip ahead".
license: MIT
metadata:
  author: HKTITAN
  version: "2.0.0"
  graph: true
---

# Adoption Design

Shipping is not adoption. This skill covers the gap between a feature existing and a feature being used: what you remove so the first attempt happens, what you put in front of the user so the next step is never a question, and what you build for the predictable moments where people stall, freeze, or quietly route around you.

It assumes the feature was worth building and that it cleared the launch bar — those are questions for [[../duo-product/SKILL]]. It also does not own the metric that proves adoption moved; see [[../duo-experimentation/references/metric-selection]].

## Remove the choice, then relieve it

- [[one-ordered-path-beats-a-branching-surface]] — when users ask whether they are using it "correctly," the fix is one ordered sequence, not better docs.
- [[the-progression-selects-give-a-test-out-and-a-side-door]] — the system picks the item; the user skips by demonstrating, and self-diagnosed gaps get their own surface.
- [[build-for-the-user-your-ladder-skips]] — the segment that is advanced on one axis and novice on another needs a separate track, not a middle rung.

## Lower the cost of starting

- [[lower-the-exposure-before-you-lower-the-difficulty]] — people avoid the witness, not the work; teach inside a task they already want to finish.
- [[ship-a-coached-variant-of-the-thing-people-avoid]] — a guided version beside the open-ended one, and do not price it out of reach of the users it was built for.
- [[social-features-die-in-empty-boxes-and-one-way-relationships]] — write the message for them, and make sure both sides of a pairing give and receive.

## Design for the moment it goes wrong

- [[every-context-gated-step-needs-a-skip-and-a-fallback]] — a step that needs quiet, a camera or two hands becomes a daily abandonment point without a no-penalty skip.
- [[script-the-repair-path]] — supply the exact words for the predictable failure, with the condition under which the script should be dropped.
- [[workarounds-are-unshipped-requirements]] — misuse is usually rule-governed expertise, and reuse of an existing affordance beats a new primitive.

## Close the loop so they come back

- [[turn-the-session-into-three-named-buckets]] — what worked, what you missed, what cost you; replay the decision instead of narrating it, and show three things, not forty.
- [[structure-the-session-and-let-them-ask-for-the-explanation]] — a narrator opens, steers and closes an open-ended session; explanation is a tap, offered on success too.
- [[be-generous-at-the-threshold-when-you-show-someone-their-record]] — gate the recap behind a minimum, and publish a rounding rule that favours the user on migration.

## Sibling skills

- [[../duo-product/SKILL]] — whether the thing was worth building and whether it clears the launch bar.
- [[../duo-retention/SKILL]] — what keeps the habit alive once adoption has happened.
- [[../duo-experimentation/SKILL]] — how you prove an adoption change actually moved something.
- [[../duo-gamification/SKILL]] — progression, difficulty ramps and the reward loop these patterns sit inside.

## Sources

All claims trace to dated posts on blog.duolingo.com, cited inline in each node; slugs are verified against `scripts/sources.json`.
