---
name: duo-rules-and-heuristics-mistakes-are-the-signal-not-the-defect
summary: Error is the mechanism, not the failure — and if a task can be passed with a plausibility shortcut, users will take it and learn nothing.
metadata:
  internal: true
---

# Mistakes Are the Signal, Not the Defect

## Concept

Getting something wrong produces a prediction error, which spikes attention across the whole pattern and forces the person to revise their model. That makes the moment of being wrong the cheapest possible moment to deliver a correction — and it makes an interface that prevents mistakes (heavy hand-holding, disabled wrong options, pre-emptive hints) a machine for removing the very signal that drives learning. There is a sharper version of the same argument. The brain solves any task by the cheapest available route. If a task can be passed with a plausibility heuristic, users will use the heuristic and learn nothing, and your success metric will not notice.

## What Duolingo does

- Courses are explicitly designed so learners **make mistakes from the first lesson**, on the grounds that an error is the brain testing a possible rule, and that being wrong heightens attention to the pattern so the next hypothesis is better. Source: blog.duolingo.com/what-is-implicit-learning (Duolingo blog, 2023-08-03; accessed 2026-09-22)
- The much-mocked silly sentences are a deliberate defeat of the shortcut. Learners lean on real-world plausibility — "The cat was chased by the mouse" gets misread because cats chase mice — so implausible sentences force attention onto word order and endings. Duolingo states the intent plainly: "We have to drag your brain away from just relying on that tempting real-world knowledge and skipping the grammar!" Source: blog.duolingo.com/common-mistakes-language-learners (Duolingo blog, 2023-08-22; accessed 2026-09-22)

**Tension, and it is a real one.** The cost is reputational. The strange sentences get screenshotted as evidence that the product is unserious and is not teaching real language. Duolingo pays that price on purpose: an item where the shortcut and the signal agree measures and trains only the shortcut, so it is an unscored item wearing the costume of a real one. If you copy this move, budget for looking silly to people who are not your users.

## The transferable pattern

Two design rules fall out.

**Stop protecting users from being wrong.** Guardrails that make the wrong action impossible also make the right action unlearnable — the user completes the flow without ever forming the judgement it was supposed to teach. Reserve hard prevention for the irreversible and the expensive; everywhere else, let the attempt fail cheaply, fast, and with the correction attached ([[explanation-lands-at-the-moment-of-the-error]]).

**Audit your tasks for the cheap route.** For any check, certification, onboarding step or evaluation you run, ask what the laziest strategy that passes it is. If context, formatting, position or common sense gets a user through without engaging the thing you are teaching, you are measuring the shortcut. Build items where the shortcut and the correct answer disagree — the correct answer must be unavailable to anyone using the cheap route.

This applies just as hard to how you evaluate an automated system as to how you teach a person: any benchmark passable by surface correlation is measuring the correlation.

The uncomfortable part is that both rules make your numbers look worse before they look better. Completion rate falls when you stop preventing errors, and pass rate falls when you remove the cheap route. Decide in advance which metric you are willing to let drop, or the change gets reverted by whoever owns the dashboard.

## Apply to your product

- Where have you disabled, pre-filled or hidden a wrong option? What judgement did the user stop developing when you did?
- Take your onboarding checklist or certification. What is the laziest strategy that passes it, and would a user who used that strategy be competent?
- What is the cheapest, safest place in your product for a user to be wrong — and is your correction actually delivered there?

## See also

[[explanation-lands-at-the-moment-of-the-error]] · [[two-memory-systems-explanation-loads-the-wrong-one]] · [[let-them-induce-it-from-volume-then-confirm]]
