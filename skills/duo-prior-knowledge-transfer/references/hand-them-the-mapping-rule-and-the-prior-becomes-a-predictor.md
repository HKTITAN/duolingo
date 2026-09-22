---
name: duo-prior-knowledge-transfer-hand-them-the-mapping-rule-and-the-prior-becomes-a-predictor
summary: You cannot delete the prior model, so state the mapping rule and redirect its activation into correct guesses about things the user has never seen.
metadata:
  internal: true
---

# State the Mapping, Get a Prediction Engine

## Concept

Prior knowledge cannot be deleted. Its connections are strong precisely because they have been reinforced for years, and they fire first by default. Suppression is therefore the expensive strategy and redirection is the cheap one: give the user the explicit correspondence rule between the old system and yours, and the same activation that was producing errors starts producing correct guesses about parts of your product they have never opened. One stated rule can cover hundreds of individual cases, because the user re-derives each one instead of storing it.

## What Duolingo does

Source: blog.duolingo.com/transfer-from-first-language (Duolingo blog, 2023-01-10; accessed 2026-09-22)

- Duolingo teaches first-language transfer as an **asset**, not only as interference. A Spanish speaker who is told that Spanish **‑ción** corresponds to Portuguese **‑ção** can then correctly guess Portuguese words they have never studied. The rule is one line; the coverage is a whole word class.
- The underlying model in the same post is Neil Kirk's volume-control analogy — both systems are always on, and effort goes into turning one down. That is the argument for redirection over suppression: the activation is happening anyway, so the only question is where it lands.
- The same move makes an arbitrary-looking rule stick. Duolingo teaches the Spanish **y → e** switch (*divertido e interesante*, *padres e hijos*) by mapping it onto an English rule readers already obey without thinking — "we say *a banana* but *an apple*." Both exist to stop two identical vowel sounds colliding. It then reuses that single anchor twice more: for **o → u** (*siete u ocho*, *plata u oro*), and for *el agua* — feminine, but taking *el*, because *la agua* would stack two stressed a's. Three rules become one principle the reader already owned (blog.duolingo.com/what-does-y-mean-in-spanish (Duolingo blog, 2026-08-25; accessed 2026-09-22)).
- Tension: transfer is genuinely double-edged. The same strong connections that let a Spanish speaker predict ‑ção also push Portuguese words into their Spanish word order. Duolingo's stated position is that you would not remove transfer even if you could — the prediction is worth the leakage.
- Corollary from the same post: an isolated arbitrary rule has no retrieval hook and decays. Attached to an existing unconscious competence it gains both a hook and a justification, so the user stores one generalization instead of two exceptions and can re-derive it when memory fails.

## The transferable pattern

1. **Write the correspondence rules down and ship them as product surface** — not as a migration appendix. "Everything the old system called X is called Y here, and the pattern holds everywhere" is worth more than a hundred individually documented renames.
2. **Prefer a rule with coverage to a table of instances.** A table is memorized; a rule is applied to cases you never listed, including features you ship next quarter.
3. **Anchor arbitrary rules to something they already do without thinking.** A rule that looks arbitrary gets forgotten; the same rule presented as an instance of a principle they already obey gets re-derived rather than recalled.
4. **Reuse one anchor across several rules.** If the same underlying reason drives three of your conventions, say so once and point at it three times. Three exceptions collapse into one generalization.
5. **Accept the leakage.** The connection that generates good guesses also generates the occasional wrong import. You do not get one without the other, and the trade is usually worth taking — but say out loud which direction leaks, so it is a known cost rather than a surprise.

## Apply to your product

- What is the single correspondence rule between your product and the tool most of your users arrive from? If you cannot state it in one sentence, your users cannot generalize from it either.
- Pick your most arbitrary-looking convention. What rule do your users already follow elsewhere for the same underlying reason, and does your documentation make that connection?
- Where does redirecting the old model leak wrong guesses into your product, and is that leak visible to you or only to your users?

## See also

[[anchor-to-a-reflex-they-already-execute]] · [[the-old-model-is-suppressed-not-erased]] · [[analogy-plus-its-exception-clause]]
