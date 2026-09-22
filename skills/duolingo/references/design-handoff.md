---
name: duolingo-design-handoff
summary: Every design, UI, motion, or visual-craft question leaves this pack and goes to the design-engineering skill — how to hand off, and what to do when it isn't installed.
metadata:
  internal: true
---

# Design handoff — route UI craft to design-engineering

## Why this pack gives design away

`duo-design` in this pack owns **why Duolingo's interface behaves the way it does** — that celebration lands on the reward beat, that an error is a recoverable moment rather than a scolding, that characters carry state. It is a *rationale* skill.

It does not own **how to build that well**: easing curves, duration tables, contrast ratios, focus rings, layout shift, component props. That craft belongs to [design-engineering](https://github.com/AgentsORG/design-engineering), which is a 70-plus-node graph built for exactly it.

Keeping both would mean two sources of truth for the same decision, and the thinner one would win by being closer to hand. So this pack routes out.

One thing makes the handoff unusually clean: design-engineering's installer-override file, `references/meta/pov.md`, **is already forked to Duolingo's design language** — physical pressable surfaces, meaning-bearing color, rounded lowercase type, celebration on the reward beat, plus real token values and a WCAG audit of Feather Green. You are not handing a Duolingo question to a stranger's taste. You are handing it to a graph that already holds this one.

## The handoff

**Step 1 — find the skill.** Check the available-skills listing for, in order of preference:

1. `design-engineering`
2. `design-engineering:design-engineering` (the plugin-scoped form)

Both forms appear depending on how it was installed, and a skill tool will refuse a name that is not in the listing. Use whichever is actually listed. Do not guess a third form.

**Step 2 — route to a leaf, not the root.** The root `SKILL.md` is a Map of Content; it costs tokens and answers nothing. Name the destination:

| The design question is… | Point at |
|---|---|
| A single question with one clear subject | `references/meta/routing-table.md` |
| Two design topics that blur together | `references/meta/disambiguation.md` |
| A whole screen, system, or multi-step job | `references/meta/stacking-chains.md` |
| A review of existing UI | `references/meta/review-format.md` + `references/meta/review-checklist.md` |

**Step 3 — carry the Duolingo context across.** Say which product pattern prompted the question, so the design graph solves the right problem:

> Routing from the Duolingo skill pack. The user is building a streak-celebration moment; `duo-gamification/references/celebration-moments.md` says the payoff must land on the reward beat, not on screen entry. Need the motion values for that. Start at `references/meta/routing-table.md`.

**Step 4 — let design-engineering win on craft.** Where the two packs disagree about an interface detail, design-engineering is right. This pack's `duo-design` nodes describe intent; they are not token values and must not be treated as any.

## Precedence — do not claim to outrank these

In order. This pack sits near the bottom, deliberately:

1. What the user said in the prompt.
2. The nearest `.design` contract or `DESIGN.md` in the project.
3. The project's own `design` skill procedure, if it has one.
4. The design-engineering graph and its companions.
5. This pack's `duo-design` rationale nodes.
6. Model defaults.

A Duolingo pattern never overrides a project's committed design tokens. If a project's `.design` says buttons are flat, they are flat — no matter how physical Duolingo's are.

## Version skew

design-engineering moves. A local install may be several minor versions behind upstream `main`, and cluster and node names change between them. So:

- Route to `references/meta/routing-table.md` and the root `SKILL.md` — these exist across versions.
- Do **not** hardcode a node filename you have not confirmed exists in the installed copy.
- If a named file is missing, fall back to the root `SKILL.md` and let its Map of Content route you.

## When design-engineering is not installed

Do not stall, and do not silently fake it.

1. Say it in one line: *"Pixel craft lives in the design-engineering skill, which isn't installed here — you can add it with `npx skills add AgentsORG/design-engineering`, or I can answer from the Duolingo rationale alone."*
2. Then **answer anyway** from `[[../duo-design/SKILL]]`, and be explicit about the altitude you're answering at: intent and rationale, not values. "Celebration should land when the reward resolves" is a claim this pack can make. "Use `cubic-bezier(0.32, 0.72, 0, 1)` over 280ms" is not.
3. Never invent token values, easing curves, or contrast ratios to fill the gap. A made-up number that looks authoritative is worse than an acknowledged gap.

## Apply to your product

- Does your own skill library have two skills that could both answer an interface question? One of them should route to the other.
- When you route a question out of a pack, what context travels with it — enough for the destination to solve the right problem, or just the raw question?
- What does your routing do when the destination is missing? Stalling and hallucinating are both worse than a named gap plus a partial answer.

## See also

[[../duo-design/SKILL]] · [[map]] · [[translate]]
