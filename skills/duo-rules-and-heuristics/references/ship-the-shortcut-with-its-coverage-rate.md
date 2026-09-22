---
name: duo-rules-and-heuristics-ship-the-shortcut-with-its-coverage-rate
summary: Lead with the rule that resolves most cases, state its hit rate so users can bet calibrated, and quarantine the real mechanism behind an opt-in header.
metadata:
  internal: true
---

# Ship the Shortcut With Its Coverage Rate

## Concept

A user needs a procedure they can execute now. Precision they cannot act on is load without capability, so an accurate model taught first is strictly worse than a heuristic that resolves most cases. The move has three parts, and dropping any one of them breaks it: lead with the shortcut, **state its coverage rate** so the user can make a calibrated bet instead of guessing at chance, and put the real mechanism behind an explicitly labelled opt-in section. The coverage number is what lets a user be wrong occasionally without losing trust in the rule — they were told to expect it.

## What Duolingo does

- German plurals: open with the two invariants you can always count on (the nominative determiner is always "die"; the noun changes in exactly one of **4 ways**), then give the dominant pattern with a number — **an estimated 90% of feminine nouns form the plural with -n or -en** — and push the masculine and neuter defectors into a short, explicitly labelled memorise-these list. Source: blog.duolingo.com/german-plurals (Duolingo blog, 2025-01-29; accessed 2026-09-22)
- German gender: "**About two-thirds of one-syllable words are masculine**, so if you have to guess about a new, short word, masculine is a good guess." German has **3 genders x 4 cases but only 8 distinct article forms**. Source: blog.duolingo.com/german-gender-der-die-das (Duolingo blog, 2022-10-04; accessed 2026-09-22)
- Preterite vs imperfect: one rule of thumb up front — if you need a phrase to say it in English (was doing / would do / used to do), use the imperfect — stated to cover "the vast majority of scenarios," with the real aspectual mechanism behind a header literally titled **"an advanced course"** and the line "if you're interested in what to do the rest of the time... read on." Source: blog.duolingo.com/spanish-preterite-imperfect (Duolingo blog, 2021-08-10; accessed 2026-09-22)
- The b/v post states the safe default in bold — when in doubt, pronounce both like English "b" — and only then opens "For intermediate Spanish learners: behind the scenes" covering the two allophones. Source: blog.duolingo.com/pronounce-spanish-b-v (Duolingo blog, 2023-05-16; accessed 2026-09-22)
- Under the heading **"If it helps, try cheating,"** learners who cannot physically distinguish the vowels in "seat" and "sit" are told to exaggerate vowel length instead — a difference of milliseconds natives produce unconsciously — so they can be understood while still working on tongue position. Source: blog.duolingo.com/tips-for-english-pronunciation (Duolingo blog, 2023-05-02; accessed 2026-09-22)

**Tension.** Every one of these posts names the cost. The preterite shortcut fails and you must fall back to the deeper model. The gender heuristic misfires "even among the most common words" — the high-frequency items a beginner meets first are exactly where it is least reliable. The vowel trick is labelled cheating because it diverges from the real mechanism and can calcify. A shortcut buys speed at the price of an error class you will eventually have to unteach.

## The transferable pattern

Write the default first, in one sentence, with no hedging inside it. Hedging is what destroys a shortcut: a rule presented alongside its exceptions reads as having no rule, so the user abandons it and falls back to per-case lookup.

Then attach a number. "This is right about 90% of the time" is dramatically more useful than "this is usually right," because it tells the user what to do when it fails — try again with the default rather than discard it. If you have no measurement, say which cases it is known to break on instead.

Then quarantine the truth. A visibly separate, opt-in section titled for the next level up ("the full mechanism", "for advanced users") lets you be accurate without taxing the beginner. Anyone who needs it will open it.

Two guardrails. Track the error class the shortcut creates, because you own the unteaching. And check whether the shortcut misfires disproportionately on high-frequency cases — if so, list those as lookups rather than letting the rule fail on them repeatedly.

## Apply to your product

- What is the one-sentence default for your most common user decision, with no conditions attached?
- Can you put a number on how often it is right? If not, can you name the cases where it breaks?
- Where does your documentation interleave the rule with its exceptions — and could the exceptions move into a separate, labelled list?

## See also

[[turn-the-table-into-a-procedure]] · [[give-them-a-handle-they-can-hold-under-pressure]] · [[name-the-arbitrary-and-kill-the-folk-theory]]
