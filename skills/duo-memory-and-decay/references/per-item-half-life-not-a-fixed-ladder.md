---
name: duo-memory-and-decay-per-item-half-life-not-a-fixed-ladder
summary: Retention decays exponentially with a half-life that differs per item and per person; schedule where lag approximates half-life instead of walking a universal interval ladder.
metadata:
  internal: true
---

# Per-Item Half-Life, Not a Fixed Ladder

## Concept

A fixed interval ladder — show it again after 1 day, then 3, then 7, then 30 — treats every item and every person as the same. They are not. Some items are nearly free because they resemble something the user already has; others are fragile and rot in hours. Two users who saw identical content carry different residues.

Model retention instead as an exponential decay with a per-item, per-person half-life: the probability of recall is roughly `p = 2^(-lag / h)`, where `lag` is time since last exposure and `h` is that item's half-life for that person. Retrieval effort — and therefore the strengthening effect — is greatest when `lag` is close to `h`. Scheduling at that point is the whole algorithm. A rigid ladder either wastes repetitions on items already secure, or arrives after the memory is already gone, and cannot tell which.

## What Duolingo does

Source: blog.duolingo.com/how-we-learn-how-you-learn (Duolingo blog, 2016-12-14; accessed 2026-09-22)

- Duolingo models **every word a learner has ever seen** with its own forgetting curve and picks practice timing where lag is close to half-life. The student model holds **billions of entries** and is updated about **3,000 times per second**.
- This replaced two hand-tuned heuristics: the **Pimsleur** schedule (fixed intervals of 5s, 25s, 2min, 10min and so on, from the 1960s) and the **Leitner** box system (roughly double the interval on success, halve it on failure, from the 1970s), which Duolingo shipped with from **2012**. The underlying forgetting curve goes back to Ebbinghaus in **1885**.
- The replacement is **half-life regression (HLR)**: fit `h = 2^(Θ·x)` over learning-history features plus the lexical items themselves, trained and evaluated on **more than 12 million practice sessions**.
- Accuracy and outcome: HLR reached **mean absolute error 0.13**, roughly **half** the error of the Leitner heuristic. The A/B test returned **+9.5% daily retention on practice sessions**, **+1.7% on lessons**, and **+12% overall activity**. The code and data were open-sourced (`github.com/duolingo/halflife-regression`; paper Settles & Meeder, ACL 2016, pp. 1848–1858).

**The tension.** Duolingo did not benchmark HLR against SuperMemo- or Anki-style algorithms, citing practical reasons. The comparison set was its own predecessors, not the best available. A result that beats the thing you already shipped is a real result — it is not evidence you reached the frontier, and a fitted model can still be worse than a good published one.

## The transferable pattern

Whenever you own population-scale interaction logs, a hand-tuned schedule is a designer's single guess sitting where a fitted model could be.

1. **Fit the model to the logs, not to intuition.** Aggregate error patterns contain regularities nobody enumerated: which items are intrinsically hard, which are nearly free, which users decay fast. "Double on success, halve on failure" discards all of it by treating every item as identical.
2. **Estimate per item and per person.** The unit of the model is the pair, not the person and not the item.
3. **Target the point of maximum effort, not maximum safety.** Resurfacing something the user still comfortably holds is a wasted slot; resurfacing after it is gone is a re-teach. Aim at the edge.
4. **Publish your baseline honestly.** State what you compared against. "Better than our old heuristic" and "state of the art" are different claims and only one of them is usually true.

## Apply to your product

- What is your current resurfacing rule, and is it a ladder someone picked in a meeting? What would it cost to fit it to the last year of your own interaction logs?
- Do you have a per-user, per-item state at all, or only a per-user state? Which of your items are nearly free for most users, and are you still charging them a slot?
- When you replace the heuristic, what is the baseline you will report — the thing you shipped, or the best known alternative?

## See also

[[spacing-beats-massing-at-equal-cost]] · [[delay-the-retry-and-weight-the-queue]] · [[../duo-experimentation/references/metric-selection]]
