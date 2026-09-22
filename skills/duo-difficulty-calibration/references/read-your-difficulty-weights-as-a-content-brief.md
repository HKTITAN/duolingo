---
name: duo-difficulty-calibration-read-your-difficulty-weights-as-a-content-brief
summary: The learned weights of a difficulty model separate hard-because-unfamiliar from hard-because-irregular, which makes them a redesign brief rather than only a scheduling input.
metadata:
  internal: true
---

# Read Your Difficulty Weights as a Content Brief

## Concept

A fitted difficulty model is usually treated as a black box with one job: emit a number, feed the scheduler, done. That wastes most of what it knows. The model was fit across millions of interactions on your actual content, which makes its per-item parameters the only unbiased ranking of your own material you will ever get — unbiased in the specific sense that no author, reviewer or stakeholder had a say in it.

Read that ranking and a second distinction appears. Some items are hard because the user has not met them often enough — a familiarity problem, which more exposure fixes. Others are hard because of something structural in the item itself: it breaks the pattern the rest of the material taught, or it carries more moving parts than its neighbors. That is not a scheduling problem and no amount of extra repetition will resolve it. It is a design defect in the content, and the weights just told you where the defects are.

## What Duolingo does

Source: blog.duolingo.com/how-we-learn-how-you-learn (Duolingo blog, 2016-12-14; accessed 2026-09-22)

- Duolingo's half-life regression model fits a weight for each lexical item alongside its learning-history features. Inspecting those weights produced an interpretable split.
- **Positive weights (easier, longer-lived)** went to cognates and to short, regular, high-frequency forms: English **"camera" +0.77**, German **"Baby" +0.87**, French **"visite" +0.94**.
- **Negative weights (harder, faster-decaying)** went to items that were rare, irregular, or carried extra grammatical machinery such as participles and imperfective aspect: English **"writing" −0.81**, German **"war" −1.10**, French **"fallait" −0.91**.
- The same model reached **mean absolute error 0.13**, roughly half the error of the hand-tuned heuristic it replaced — so the weights are not incidental noise attached to a weak model.
- **The tension.** These weights are population averages, fit on the people who stayed. An item that is hard enough to drive users away early will look easier than it is, because the users it defeated are not in the data. Survivorship runs straight through any per-item difficulty estimate, and it biases exactly the items you most want to find.

## The transferable pattern

Turn the model's parameters into a work queue for the people who make the content.

1. **Rank your items by fitted difficulty and actually read both tails.** The easy tail tells you which things resemble something users already hold, so you can teach faster there. The hard tail is the brief.
2. **Split the hard tail by cause.** Hard-because-unfamiliar is a scheduling and exposure problem. Hard-because-structural — it violates the pattern its neighbors set, or it bundles several new things into one step — is a rewrite, and shipping more repetitions of it is the wrong response.
3. **Look for items that are outliers against their own neighborhood.** An item much harder than everything around it is either misplaced in the sequence or under-scaffolded; either way the fix is upstream of the scheduler.
4. **Correct for who is missing.** Difficulty fit on retained users understates the items that caused people to leave. Cross-check the hard tail against where abandonment happens before you trust the ranking.

## Apply to your product

- If you have any fitted per-item parameter — difficulty, decay, completion probability — has anyone on the content side ever looked at its ranked output? What would the top and bottom fifty items tell them?
- Which of your hardest items are hard because they are unfamiliar, and which are hard because of how they are built? What is the ratio?
- Which items sit right where users abandon? Do they look easy in your model, and if so, who is missing from the fit?

## See also

[[model-the-item-and-the-user-jointly]] · [[read-error-rate-with-completion-rate]] · [[the-narrow-band-between-bored-and-lost]] · [[../duo-memory-and-decay/references/per-item-half-life-not-a-fixed-ladder]]
