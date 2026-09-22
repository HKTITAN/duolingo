---
name: duo-rules-and-heuristics-explanation-lands-at-the-moment-of-the-error
summary: The same explanation is inert before the mistake and sticky immediately after it; ship it at the point of failure and name the rule that fired.
metadata:
  internal: true
---

# Explanation Lands at the Moment of the Error

## Concept

Timing decides whether an explanation is absorbed or discarded. Read before the attempt, it has nothing to attach to and is stored as inert trivia. Delivered right after a specific mistake, it arrives with a live discrepancy the person is already motivated to resolve, and it binds to a concrete instance — their own wrong answer. The second half of the move matters as much as the timing: the feedback should name the rule that governed the outcome, not just mark the outcome. "Wrong" carries one bit and leaves the user to reverse-engineer why, and if they infer the wrong rule, their next correct answer reinforces it.

## What Duolingo does

- **Smart Tips** are short explanations that fire after a specific mistake, explain the pattern, and then practise it in context. Duolingo reserves explicit instruction for this moment while teaching implicitly the rest of the time. Source: blog.duolingo.com/language-rules-learning-grammar-on-duolingo (Duolingo blog, 2020-10-02; accessed 2026-09-22)
- In experiments, learners who saw these explanations **made fewer subsequent errors** than learners who did not. Grammar Skills were added to **20 units across the four biggest courses** in 2021, and learners cited the content as "rewarding." Source: blog.duolingo.com/duolingo-grammar-skills-improvements-2021 (Duolingo blog, 2021-10-15; accessed 2026-09-22)
- Personalised grammar tips fire **inside lessons, on the topics that particular learner finds hardest**, while per-unit Guidebooks stay opt-in rather than gating. Source: blog.duolingo.com/tips-for-learning-spanish-on-duolingo (Duolingo blog, 2021-01-29; accessed 2026-09-22)
- The answer keys never say just "correct." Each one restates which rule fired — "Estas (a form of estar) because we are talking about someone's Condition"; "D (Duration): we use por when talking about how long something lasted." The posts carry **2 challenges of 5 items each**, every answer annotated with its governing rule, and one challenge requires justifying the choice and the conjugation separately. Source: blog.duolingo.com/ser-vs-estar (Duolingo blog, 2026-08-13; accessed 2026-09-22)

**Tension.** Duolingo does not apply this absolutely. Dedicated Grammar Lessons deliberately front-load the tip, keeping it reachable mid-lesson via a lightbulb. "Explain only after failure" is the default, not a law — when a feature is genuinely un-inferable from exposure, up-front is right ([[where-explicit-instruction-earns-its-place]]).

## The transferable pattern

Move your explanation from where it is convenient to write to where it is cheap to absorb — the instant after the user gets it wrong. A manual is written in one place and read in none; an error-triggered explanation is delivered to exactly the person who just proved they need it, at the one moment they care.

Three requirements make it work:

1. **Trigger on the specific failure**, not on the category. A generic help panel that opens on any error is the manual again, relocated.
2. **Name the governing rule, not the verdict.** Convert an outcome into a decision procedure the user can run next time. Error text that only says what happened teaches nothing transferable.
3. **Let it practise, not just tell.** The explanation should be followed immediately by another instance of the same decision, while attention is still on the gap.

The corollary: an escalation in documentation is usually the wrong response to a recurring mistake. The text may already be correct. It is arriving at the wrong moment.

## Apply to your product

- What is your single most common user error, and where does your explanation of it currently live — in a doc, a tooltip, or the failure itself?
- Do your error messages name the rule that fired, or only report that something went wrong?
- After a user recovers from an error, do they get another chance to make the same decision while it is still fresh, or does the flow move on?

## See also

[[mistakes-are-the-signal-not-the-defect]] · [[where-explicit-instruction-earns-its-place]] · [[make-the-invisible-error-observable]]
