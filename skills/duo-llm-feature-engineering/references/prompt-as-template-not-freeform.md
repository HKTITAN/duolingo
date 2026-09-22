---
name: duo-llm-feature-engineering-prompt-as-template-not-freeform
summary: Split a production prompt into a fixed constraint zone and per-instance slots, so operators supply judgement and never format.
metadata:
  internal: true
---

# Prompt as Template, Not Freeform

## Concept

A prompt that ships is not a message someone writes each time. It is a template with two zones. The **fixed zone** holds the constraints that never vary for this output type — the format, the length ceiling, the number of items, the shape the downstream system expects. The **variable zone** holds the handful of decisions that genuinely differ per instance, exposed as named slots.

The split exists because the fixed zone is where your quality and format guarantees live. If every operator can rewrite the whole prompt, consistency degrades with each new author, and the failure shows up as output that is individually fine and collectively incoherent. Isolating the slots means the operator supplies only the judgement that is actually theirs; everything else is enforced by construction, not by discipline.

## What Duolingo does

Source: blog.duolingo.com/large-language-model-duolingo-lessons (Duolingo blog, 2023-06-22; accessed 2026-09-22)

- Duolingo describes its exercise-generation prompt as working **"kind of like a Mad Lib"** — a fixed frame with blanks.
- **Fixed rules, identical on every call**: exactly **two answer options**, and **fewer than 75 characters** per item. These are never exposed to the person triggering the generation.
- **Variable slots, filled per instance**: the target word, the language, the **CEFR level** (for example A2), the **grammar focus** (for example preterite plus imperfect), and the theme.
- Ownership of the slots is split — some are **auto-filled by engineering** from the course data, others are **chosen by the Learning Designer** at the moment of authoring.
- **Tension.** Duolingo says they are "constantly adjusting the instructions we give the model." The fixed zone is fixed relative to an instance, not permanently. It is a centrally-owned artifact under continuous revision, not a frozen one.
- The same post offers Duolingo's own metaphor for the model underneath — **"a wind up toy"** that will certainly move, and needs guardrails to move in the right direction. The template is one of those guardrails.

## The transferable pattern

Take any prompt you are about to put behind a button and sort every line into one of two buckets.

1. **Invariant for this output type** — schema, field count, length caps, tone floor, forbidden constructions, the contract the consuming system relies on. This goes in the fixed zone, lives in version control, and is owned by one team.
2. **Genuinely per-instance** — the subject, the audience tier, the difficulty band, the one dimension the operator knows and the system does not. This becomes a named, typed slot with a default.

Two follow-on rules. **Pre-fill every slot you can derive** from data you already hold; a slot the operator must fill but could not get wrong is a slot you should have computed. And **treat the fixed zone as a versioned artifact** — when you change it, you change every future output, so that edit deserves a review and a changelog, not a hotfix.

If you find yourself adding a slot for something that is really a constraint, you are letting the operator negotiate your quality bar.

## Apply to your product

- Take your most-used prompt. Which lines would be wrong to change for any instance, and which genuinely vary? Can you name the second set on one hand?
- Who is allowed to edit the fixed zone today, and would you notice if they did?
- Which of the slots you expose could be derived from data you already have, so the operator never has to supply it?

## See also

[[find-the-context-optimum]] · [[examples-from-your-corpus-beat-more-instructions]] · [[../duo-ai-agent-platform/SKILL]]
