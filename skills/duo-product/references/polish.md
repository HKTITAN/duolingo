---
name: duo-product-polish
summary: What "polished" actually means in review, with concrete tests.
metadata:
  internal: true
---

# Polish

## Concept

"Polish" gets used as a vague honorific — "this needs more polish" — without anyone agreeing what they mean. Concretely, polish is the absence of visible seams: the things that don't appear unless you go looking for them, and the things that *would* appear if you didn't. A polished feature handles its edges, errors, and edge-cases as if they were the main path.

## What Duolingo does

Source: blog.duolingo.com/core-tabs-redesign (Duolingo blog, 2026-02-04; accessed 2026-09-22)

Duolingo calls this *craft*, and the 2026 core-tabs refresh is the clearest worked example:

- **The trigger was accumulation, not breakage.** Each tab "worked fine on their own," but headers varied in size, typography lacked hierarchy, and spacing was inconsistent. "Eventually, these small details added up to an experience that didn't feel polished and cohesive."
- **The pass was its own project.** A divergent sprint produced **four distinct directions** (Punchy, Soft, Modular, Flat), each pushing consistency and simplicity to an extreme, prototyped and tested on real phones before any of it was built.
- **Polish was given QA machinery.** Designers and engineers built shared QA processes including **self-QA with design overlays**, on top of the existing dogfooding culture across languages and devices ([[dogfooding]]).
- **It was measured.** Post-launch: higher engagement across tabs **while holding core learning metrics flat** — the polish pass had to prove it cost nothing, not just that it looked better.
- Motion gets the same treatment. The streak milestone redesign went through **multiple passes of rough animation** purely to tune rhythm and timing — "these variables are as important to the success of Duo's transformation as the design itself" — and the fire metaphor was rebuilt around a phoenix because "keeping the flame alive" is not a universally shared image (blog.duolingo.com/streak-milestone-design-animation (Duolingo blog, 2022-01-21; accessed 2026-09-22)).
- Error states, empty states, and sound get the same intent ([[../duo-voice/references/error-copy]], [[../duo-voice/references/empty-states]], [[../duo-design/references/juicy-motion]], [[../duo-design/references/sound-as-ux]], [[../duo-design/references/accessibility-default]]).

Two tradeoffs the post states rather than hides: **consistency has to be balanced against purpose** (artwork in every header is consistent and often useless), and **simplicity has to be balanced against clarity**. Polish is not maximizing either axis; it is knowing what to remove and what to keep.

## The transferable pattern

A useful checklist for "is this polished":

| Test | Pass condition |
|---|---|
| Error state | Has illustration + voice copy + clear next action |
| Empty state | Has illustration + voice copy + clear next action |
| Loading state | Designed, not just a spinner |
| Network failure | Recovery path explained |
| Edge data (very long names, zero items, max items) | All handled visually |
| Accessibility | Color-not-only, keyboard nav, screen-reader path |
| Motion | Specified easing, specified duration, respects motion-reduce |
| Sound | Optional, calibrated, doesn't fire at wrong moments |

Three rules:

1. **Polish is plural.** It's not one big check; it's a list of small ones. Make the list explicit.
2. **The polish review is its own pass.** Bundling polish into "design review" means polish gets cut for time.
3. **Polish is leadership's responsibility too.** Engineers and designers know what isn't polished; the question is whether anyone has time for it.

## Apply to your product

- Run the checklist above against your last shipped feature. How many pass?
- Does "polish" have a defined list in your team, or is it a vibe?
- What's the quickest polish item you could fix this week?

## See also

[[raise-the-bar]] · [[dogfooding]] · [[quality-tiers-by-reversibility]] · [[../duo-design/references/error-as-delight]] · [[../duo-design/references/accessibility-default]] · [[../duo-voice/references/error-copy]]
