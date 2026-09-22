---
name: duo-voice-one-name-per-entity
summary: Keep proper names identical in every locale, because shared references are what let user culture compound.
metadata:
  internal: true
---

# One Name Per Entity

## Concept

A name accrues social value only if everyone recognises it as the same name. Translate a character or feature name per market and you have not localized it — you have fragmented the shared reference that user-generated culture needs in order to compound. A post saying "I'm such a Bea" is legible to everyone or to a fraction, depending on a decision made years earlier, and the fraction version never produces a cross-market network effect; each market just builds a smaller, separate culture of its own.

## What Duolingo does

Source: blog.duolingo.com/duolingo-female-character-origin-stories (Duolingo blog, 2022-03-08; accessed 2026-09-22)

Duolingo kept its cast's names near-identical across every locale rather than adapting them per market. The screening that makes this possible is the expensive part:

- **Every candidate name was cross-referenced in many languages** to rule out odd or unfortunate meanings, while staying close to the English form.
- **Pronounceability was checked for all users**, not just the home market — a name nobody can say out loud cannot be passed around.
- **Meaning that could not survive the constraint was encoded structurally instead.** Lin and Lucy share an initial to signal that they are related, because a name cannot carry that hint once it has to be the same everywhere.

**Tension.** The constraint is genuinely costly. It required a lot of cross-referencing work and it narrows the usable name set sharply — every market gets veto power, so the best-sounding name in the home market is frequently unavailable. The payoff is a single shared reference, and it is only worth the price if your users actually talk to each other across markets.

## The transferable pattern

1. **Decide once, early, whether a name is a shared reference or a label.** Shared references — characters, mascots, named rituals, named tiers — stay identical everywhere. Labels — settings, menu items, descriptions — get adapted freely.
2. **Budget for the screening pass.** Cross-market meaning and pronounceability checks belong in the naming process, not in a post-launch incident.
3. **Accept a narrower name set as the price** of the shared reference, and do not reopen the decision per market later — a rename after culture has formed destroys the thing you paid for.
4. **Encode relationships structurally** (shared initials, shared shapes, shared suffixes) since that meaning cannot ride in a translated word.

## Apply to your product

- Which of your names are meant to be said by users to other users, and are those identical in every market?
- If a name were adapted in one market today, what would break — and would anyone notice?
- What screening does a new name go through before it ships?

## See also

[[localization-voice]] · [[character-archetypes]] · [[screenshot-bait]] · [[../duo-growth/references/localization-as-growth]]
