---
name: duo-return-triggers-answer-the-exit-not-the-dialog
summary: At the moment someone abandons, address why they are leaving instead of confirming the mechanics of leaving.
metadata:
  internal: true
---

# Answer The Exit, Not The Dialog

## Concept

The standard abandon prompt asks the user to ratify a decision it has already treated as settled. "Are you sure you want to quit?" contains no argument; it is a confirmation step wearing the costume of a question, and its only function is to catch misclicks. But a mid-task exit is rarely a misclick and rarely a settled decision — it is usually a person who has hit something they found discouraging. Naming that reason out loud reopens the decision, and gives them something to stay for that the neutral version never offered.

## What Duolingo does

Source: blog.duolingo.com/copy-testing-experiments (Duolingo blog, 2022-01-14; accessed 2026-09-22)

- Duolingo changed the Spanish quit-lesson prompt from the plain "Do you want to end this session?" to **"Don't give up! Do you really want to end this session?"**
- The change came from a stated hypothesis about a specific audience — that Spanish-speaking learners would respond to a warmer, more direct tone — not from a general preference for friendly copy.
- The result — it **reduced the number of people who quit sessions and increased time spent learning**. No percentage was published, which is worth holding in mind. The direction is reported; the magnitude is not.
- Note the mechanics of the winning line. It adds an encouragement and an intensifier ("really") while leaving the exit exactly where it was. Nothing was hidden, moved, or made harder to click.
- Note also that this was a localised test. The tone that won for one audience is not automatically the tone that wins for another, which is the whole reason Duolingo ran it per-language rather than shipping one global string.

## The transferable pattern

Treat the abandon prompt as your last piece of persuasion rather than your last piece of plumbing.

- **Say why they might be leaving.** Discouraged, stuck, out of time, in the wrong place. Guessing out loud gives them something to disagree with, and disagreement is engagement.
- **Offer the smaller option instead of the binary.** Save and come back, switch to something easier, do a shorter version. Many exits are a rejection of the current size of the task, not of the task.
- **Do not make leaving harder.** Dark-pattern exit friction buys one session and costs trust permanently. The lever is the copy, not the button placement.
- **Test it per audience, and log the reason.** Abandon prompts are cheap to test and are one of the few places you can ask a churning user a question while they are still present.
- **Accept unpublished magnitudes carefully.** "It worked" from someone else's test is a hypothesis for yours, not a number you can plan against.

## Apply to your product

- What does your product say at the exact moment a user abandons something mid-flow, and does it contain any reason to stay?
- What are the top three real reasons people quit that flow, and does your prompt name any of them?
- Is there a smaller version of the task you could offer instead of a yes-or-no exit?

## See also

[[process-framing-beats-outcome-framing]] · [[re-entry-resumes-it-does-not-restart]] · [[../duo-experimentation/SKILL]]
