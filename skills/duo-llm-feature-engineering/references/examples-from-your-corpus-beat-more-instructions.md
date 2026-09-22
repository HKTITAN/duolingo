---
name: duo-llm-feature-engineering-examples-from-your-corpus-beat-more-instructions
summary: When output quality is poor, add curated in-domain examples rather than more instructions — and source the prompt material from the same context as the output.
metadata:
  internal: true
---

# Examples From Your Corpus Beat More Instructions

## Concept

The reflex when generated output is bad is to explain the target better. That reflex is usually wrong, and it is wrong for a specific reason.

An instruction is a **lossy description of the target in a second language** — you translate a thing you can recognise into rules, and the model translates the rules back. Every hop loses something. Worse, instructions accumulate into conflicts, and a model resolves a conflict arbitrarily, which is why adding rules can make output *worse* in a way that looks random. A curated example from your own body of work does not describe the target; it **is** the target, and pattern-matching against in-domain exemplars is the thing generative models are genuinely reliable at. So when quality is poor, the first move is to add examples and delete instructions, not the reverse.

## What Duolingo does

Source: blog.duolingo.com/scaling-duoradio (Duolingo blog, 2025-03-11; accessed 2026-09-22)

- Duolingo's **first two attempts failed quality review**, and both were instruction-heavy. Attempt one generated scripts from scratch under **detailed prompts**. Attempt two **machine-translated existing English episodes** into the target language.
- The breakthrough was neither. It was feeding the prompts **real sentences and exercises written by Learning Designers for the corresponding curriculum** — material that already existed, already passed review, and already sat at the right level.
- The same principle governs the prompt's own language. For courses that do not teach English, **English-only prompt instructions were less effective**, so Duolingo switched to **language-specific content drawn from each course's own curriculum**. Instructions written in one language carry that language's structures into the output.
- This is the pipeline that later produced the numbers in [[the-filter-holds-the-bar-not-the-generator]] — **15,000-plus episodes**, **25-plus courses**, **99% cost reduction**. The unlock was the examples; the filter held the bar afterwards.
- **Tension.** This only works if you already have a curated corpus. Duolingo could reach for years of expert-authored material; a team without one has to build the exemplar set first, and that is real expert time spent before any leverage appears.

## The transferable pattern

- **Diagnose before you edit.** If output is wrong in a way you can *point at* in a good example, add the example. If it is wrong in a way no example demonstrates — a hard cap, a forbidden action, a schema — that is genuinely an instruction.
- **Prefer artifacts that already passed your review process.** Their value is that the bar has already been applied to them by a person who was accountable for it.
- **Match the example to the instance, not to the average.** Retrieve exemplars that share the instance's segment, tier or register rather than shipping one fixed set to every call.
- **Write the prompt in the register and idiom of the output.** A prompt composed in the terms of one context imports that context's assumptions; source the framing material from the same place the output has to live.
- **Delete an instruction every time you add an example.** Otherwise the prompt only grows, and you land in the problem described in [[find-the-context-optimum]].
- **Audit your exemplars on a schedule.** They are the specification now. A stale example is a stale spec that no one is reviewing.

## Apply to your product

- What body of already-reviewed work do you own that a prompt could be pointed at, and who curates it?
- Look at your longest prompt. How many of its rules are attempts to describe something you could show instead?
- If your output serves multiple segments, contexts or markets, are you prompting all of them with material drawn from one of them?

## See also

[[find-the-context-optimum]] · [[prompt-as-template-not-freeform]] · [[the-filter-holds-the-bar-not-the-generator]]
