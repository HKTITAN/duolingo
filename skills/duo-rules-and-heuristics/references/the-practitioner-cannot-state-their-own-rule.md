---
name: duo-rules-and-heuristics-the-practitioner-cannot-state-their-own-rule
summary: Expertise compiles rules out of conscious reach, so never build a spec by asking an expert to describe what they do — extract it from behaviour and check it with them.
metadata:
  internal: true
---

# The Practitioner Cannot State Their Own Rule

## Concept

Skill proceduralises with use. The rule stops being retrieved as a fact and starts running as a reflex, so the output stays correct while the introspective report degrades. That makes an expert simultaneously the best source of behaviour and the worst source of description — and it makes the standard method for writing documentation, training material or a specification ("ask the person who does it") structurally unreliable. The gap is not carelessness. It is what competence looks like from the inside.

## What Duolingo does

- A Duolingo writer describes applying for her first English teaching job thinking "I speak English. What else would I need to know?" — then failing to explain the difference between simple past and present perfect, and not getting the job. **Roughly 20 years later**, with a master's in the subject and about a decade in the classroom, she describes only later discovering that every native speaker applies a fixed adjective order with **9 slots** (determiner, opinion, size, age, shape, colour, origin, material, purpose), which almost none can state — which is why "gigantic yellow spider" is fine and "yellow gigantic spider" is not. Source: blog.duolingo.com/teaching-your-own-language (Duolingo blog, 2026-02-03; accessed 2026-09-22)
- The same post names a second case she had "never given a single thought" while obeying perfectly: "chicken" is countable on the farm and uncountable on the plate.
- Where a large item set does have structure, Duolingo ships the generative rule rather than the list — **7 transformation patterns** (-tion → -ción, -ty → -dad/-tad, -ous → -oso, -ly → -mente, -ic → -ico, -ant/-ent → -ante/-ente, s+consonant → es+consonant) covering the **10,000 to 15,000 cognates** English and Spanish share — and pairs them with the false-friend list in the same breath so learners know where the patterns break. Source: blog.duolingo.com/cognates-in-spanish (Duolingo blog, 2026-06-11; accessed 2026-09-22)

**Tension.** The cognates post opens by admitting it uses a looser definition than linguists do: strict cognates like Spanish "ocho" and French "huit" share an ancestor but look nothing alike. The learner-useful rule is not the technically correct one, which is exactly the trade an extracted rule makes — it is optimised for running, not for being right in the seminar.

## The transferable pattern

Never write a spec, a runbook or a training document by asking a practitioner to describe what they do. You will get a plausible narrative that is not the rule they actually follow, and it will be wrong in the places that matter most — the judgement calls, which are the most proceduralised part.

Extract from behaviour instead:

1. **Watch them work, or collect their outputs.** Decisions, cases, artefacts, the calls they made and the ones they rejected.
2. **Infer the rule yourself** from what varies with what. You are looking for the thing that predicts their choices, not the thing they say predicts them.
3. **Take it back to them as a claim to falsify.** "It looks like you always do X when Y" gets a reliable answer — recognition survives when recall does not. Their counterexample is the most valuable output of the whole exercise.

The same asymmetry sets a rule for what you ship. Where a large set has structure, ship the generative rule, because a rule the user can run on unseen items is worth orders of magnitude more than the items themselves. But ship its known failure cases in the same breath: an unqualified rule is worse than no rule, because the user applies it confidently exactly where it misfires.

## Apply to your product

- Which of your documents was written by asking an expert what they do? What in it has never matched how the work actually goes?
- Pick your most experienced user. Could you infer their working rules from their last twenty decisions, and would they recognise the rule if you showed it to them?
- Where do you hand users a list that could be a rule — and do you know where that rule breaks?

## See also

[[two-memory-systems-explanation-loads-the-wrong-one]] · [[make-the-invisible-error-observable]] · [[fix-the-model-instead-of-memorising-the-exception]]
