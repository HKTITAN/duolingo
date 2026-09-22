---
name: duo-difficulty-calibration-read-error-rate-with-completion-rate
summary: Errors rising while completion holds flat is productive difficulty; errors rising with completion falling is a broken experience — and the error metric alone cannot tell them apart.
metadata:
  internal: true
---

# Read Error Rate With Completion Rate

## Concept

A spike in errors after a change is the most commonly misread signal in product work. It arrives looking like a regression, and the reflex is to soften whatever caused it. But an error-rate number on its own is genuinely ambiguous: the user who is struggling productively and the user who is suffering produce the same line on that chart.

The disambiguator is a second metric measured over the same population: whether people still finish. Completion rate is the behavioral proxy for frustration — a user who is overwhelmed, bored or defeated leaves, and leaving is observable. Error rate is a proxy for effort. Held together they separate two cases that are indistinguishable apart: **errors up, completion flat** means the work got harder and people are still willing to do it; **errors up, completion down** means you broke something. Never read one without the other, and never let a single-metric alert decide whether to roll back a difficulty change.

## What Duolingo does

Source: blog.duolingo.com/language-rules-learning-grammar-on-duolingo (Duolingo blog, 2020-10-02; accessed 2026-09-22)

- When Duolingo shipped Grammar Lessons, learners made **almost twice as many mistakes** as in a regular lesson — and completed them at **the same rate**.
- Duolingo read that pair as confirmation that the underlying learning science was right, not as a difficulty defect, and shipped the feature.
- **The tension.** The stated goal is to "balance some healthy mistake-making with good progress" — not to maximize errors. The flat completion rate is what bounds how far the difficulty can be pushed. Remove that bound and the same reasoning justifies any amount of failure.

Source: blog.duolingo.com/common-mistakes-language-learners (Duolingo blog, 2023-08-22; accessed 2026-09-22)

- A second reason a raw accuracy drop can be healthy: Duolingo documents **U-shaped learning**, where measured performance gets worse mid-way through acquiring a rule. English-learning toddlers go from a correct memorized "I went" to "I goed" to "I wented" and back to "I went." Spanish learners go from a correct chunked "Me llamo" through "yo llamo," "mi llamo," "mi llamo es," and back.
- The mechanism: early competence comes from storing whole chunks. Acquiring the underlying rule means those chunks get re-derived, and the intermediate hypotheses are wrong in new ways — so accuracy falls before it exceeds the chunk-based ceiling.
- **The tension Duolingo's own data carries.** This makes an accuracy metric on an intermediate user genuinely ambiguous. A drop could be a broken step or a healthy restructuring, and in aggregate the two look identical. An optimizer that smooths the dip away will hold users at the shortcut, permanently.

## The transferable pattern

Never ship a difficulty decision off a single metric.

1. **Pair every effort metric with an abandonment metric**, measured on the same cohort over the same window. Effort up with abandonment flat is the signature you are looking for. Effort up with abandonment up is a defect.
2. **Decide the pairing before the experiment runs.** Read after the fact, a flat abandonment rate is a rationalization; declared in advance it is a real acceptance criterion.
3. **Expect a transient dip when users change strategy.** When a system teaches a general rule that replaces memorized special cases, measured performance gets worse before it gets better. Optimizing continuously against short-window accuracy quietly selects for the shortcut.
4. **Distinguish the dip from the defect by shape, not by level.** A restructuring dip recovers and then exceeds the prior ceiling; a defect does not recover. That takes a longer measurement window than most dashboards default to.

## Apply to your product

- Which of your dashboards would fire an alert on an error spike that is actually a feature working? What second metric would have to be on the same chart to stop that?
- What is your abandonment proxy — the thing a frustrated user does that you can see? How long after the frustration does it show up?
- Is there a point in your product where users trade a memorized shortcut for a general method? Would your metrics tell you, or would that look like a regression?

## See also

[[the-narrow-band-between-bored-and-lost]] · [[fifty-percent-success-is-the-honest-signal]] · [[../duo-experimentation/references/guardrail-metrics]] · [[../duo-experimentation/references/metric-selection]]
