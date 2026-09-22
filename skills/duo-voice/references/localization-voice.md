---
name: duo-voice-localization-voice
summary: Keeping the voice consistent across 40+ languages where the joke doesn't always translate.
metadata:
  internal: true
---

# Localization Voice

## Concept

Most consumer products lose all voice the moment they're localized — strings get translated literally, jokes are softened or removed, and what was a brand becomes a generic UI in 40 languages. Duolingo's challenge is harder: the voice is half of the product, the user base is global, and *unhinged* doesn't always translate.

The discipline: localize the *register*, not the words.

## What Duolingo does

Source: blog.duolingo.com/copy-testing-experiments (Duolingo blog, 2022-01-14; accessed 2026-09-22)

The actual mechanism is not "rewrite from scratch" — it is *adapt, then measure per language*. In-app copy is written in English, localized into learners' **22 primary languages**, and then A/B-tested locale by locale with an in-house tool (Expurrimenter, built into their CopyCAT translation system).

- **The register is the variable being tested, not the words.** In Spanish, the plain "Do you want to end this session?" was replaced with "Don't give up! Do you really want to end this session?" — fewer people quit sessions, more time spent learning.
- **A winning line in one language does not transfer.** Rewriting the German notification opt-in ask to say notifications "are proven to foster learning success" lifted opt-in **8%** for German learners. The same test run in Spanish had **no significant impact**.
- **Language shape changes what copy can do.** Chinese characters are compact enough that the Plus feature list could be expanded from "Unlimited Hearts" to "No heart loss on errors" — a change "not feasible in any of our longer languages" — and it raised free-trial sign-ups.
- **The tooling is the enabler.** Before Expurrimenter, every copy test needed engineering time. Within its first three months the team more than doubled their all-time volume of copy tests.

## The transferable pattern

Three rules for localizing voice:

1. **Translate intent, not strings.** A literal translation of a joke kills the joke. Document *why* the line works, then let local writers find a local equivalent.
2. **Make the per-language copy test cheap.** Duolingo's unlock wasn't hiring — it was removing engineering from the loop so a localization team could run its own A/B test. Until a test costs a ticket, the English line is the only one anyone will ever tune.
3. **Never generalize a locale's winning copy.** Treat every lift as local until it replicates. The German 8% did not replicate in Spanish.
4. **Some surfaces translate, some get rewritten.** Settings labels: translate. Brand voice copy: rewrite.

Anti-pattern: machine translation for brand-bearing copy, even with human review. The joke *was* the brand; if it goes flat in translation, the brand goes flat.

## Apply to your product

- Does your product ship localized? If yes, who writes the localized copy — translators or writers?
- For your top three markets after the home market, is the voice as strong as in English? How would you know?
- Is there a written voice brief that can be interpreted, or only a string database?

## See also

[[wholesome-unhinged]] · [[character-archetypes]] · [[one-name-per-entity]] · [[unmarked-framing]] · [[../duo-growth/references/localization-as-growth]]
