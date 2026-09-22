---
name: duo-llm-feature-engineering-dont-collapse-the-candidate-set
summary: Models are good at satisfying constraints and bad at taste, so generate N compliant candidates and put a human — or the end user — at the ranking step.
metadata:
  internal: true
---

# Don't Collapse the Candidate Set

## Concept

A generative model is reliably good at constraint satisfaction and unreliable at taste. So never let the system silently pick one answer. Ask for **N candidates that all satisfy the constraints**, and hand the choice to whoever actually holds the intent.

This has two layers, and they are the same mechanism. **Inside your org**, over-generating converts an expensive authoring task into a cheap ranking task, which is where expert judgement is fastest and most valuable. **Facing your users**, a tool that returns one confident answer has resolved an ambiguity without telling anyone — and the user cannot catch the error, because they asked precisely because they did not know. Collapsing the candidate set hides the decision at the exact moment the person is least equipped to audit it.

## What Duolingo does

Source: blog.duolingo.com/large-language-model-duolingo-lessons (Duolingo blog, 2023-06-22; accessed 2026-09-22)

- A Learning Designer clicks once and gets **ten exercises back in seconds**, picks their **three favourites**, and **edits them before they ship**.
- The raw output follows every rule and is still not shippable — the post says some of it sounds **"stilted or unnatural."** The edits are for naturalness, teaching value and word choice, none of which the constraints capture.
- Duolingo states the boundary as a policy, not a preference — its **teaching experts always have the final say**. Model failure modes never reach users unfiltered.

Source: blog.duolingo.com/how-to-use-online-translators-and-dictionaries (Duolingo blog, 2021-08-25; accessed 2026-09-22)

- Written in 2021, before the current model era, and it states the user-facing half exactly. A **translator returns one confident output**; a **dictionary returns ranked senses** with example sentences and register and region labels (*coloquial*; ES, AR, PR, MX).
- The worked failure — asking for "I don't have any dough" returns **"No tengo masa"**, which is bread dough rather than money, **with no signal that a choice was made**.
- The fix for ambiguity is more input, not a better guess — typing **"can"** alone leaves the tool guessing both the sense and the person, while **"we can"** narrows it to *podemos*.
- Duolingo's stated rule of thumb — dictionaries for single words and regional variation, translators for full sentences and conjugation, and never run slang through a translator.

## The transferable pattern

- **Generate more than you need.** If one candidate is worth generating, five are worth generating; the marginal cost is a rounding error against the cost of a human authoring one from scratch.
- **Put the human at the ranking-and-editing step, not the authoring step.** Keep the edit right explicit — the reviewer must be able to change the artifact, not only accept or reject it, or you have built an approval queue and called it review.
- **Constraints are not quality.** Expect compliant-but-wrong output as the normal case, and design the review around what the constraints cannot express.
- **When the output goes to an end user, show that a choice was made.** Ranked alternatives with a label explaining why each one might be right, and a visible confidence or a visible "this was ambiguous" state.
- **Or remove the ambiguity instead of hiding it** — widen the input so the system has enough context to not be guessing. A slightly longer input beats a silently-resolved one.
- **Publish the tool's own boundaries.** State in the product which inputs it handles well and which it does not. Telling people where your tool is unreliable buys more trust than pretending it is not.

## Apply to your product

- Where does your product return exactly one generated answer? What alternative did it discard, and would the user have picked differently?
- At what step does a human currently enter your pipeline — authoring, ranking, or approving? Can they edit, or only say yes?
- What extra input would let the system stop guessing, and what would it cost the user to supply it?

## See also

[[the-filter-holds-the-bar-not-the-generator]] · [[scope-generation-to-work-with-no-rhetorical-goal]] · [[../duo-rules-and-heuristics/SKILL]]
