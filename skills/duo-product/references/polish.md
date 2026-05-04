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

- Error states are designed, not defaulted ([[../duo-voice/references/error-copy]], [[../duo-design/references/error-as-delight]]).
- Empty states have characters, voice, and a clear next action ([[../duo-voice/references/empty-states]]).
- Motion is calibrated, not stock ([[../duo-design/references/juicy-motion]]).
- Sound has design intent ([[../duo-design/references/sound-as-ux]]) — present, calibrated, mute-respectful.
- Accessibility is the default, not an afterthought ([[../duo-design/references/accessibility-default]]).

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

[[raise-the-bar]] · [[dogfooding]] · [[../duo-design/references/error-as-delight]] · [[../duo-design/references/accessibility-default]] · [[../duo-voice/references/error-copy]]
