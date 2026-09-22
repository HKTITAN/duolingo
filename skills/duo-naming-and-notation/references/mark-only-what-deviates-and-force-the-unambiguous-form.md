---
name: duo-naming-and-notation-mark-only-what-deviates-and-force-the-unambiguous-form
summary: Flag exactly the unreliable rows and nothing else — and where two conventions collide, refuse to render the ambiguous form at all.
metadata:
  internal: true
---

# Mark Only What Deviates, and Force the Unambiguous Form

## Concept

Readers infer confidence from format, not from content. A reference table where every row looks the same transfers your uncertainty to the user as **false certainty**: they trust the weak rows exactly as much as the strong ones, and the failure surfaces later somewhere they cannot trace it back.

The fix is selectivity. A signal's information content comes from where it is *absent*. A badge on every item is ignored and the user must still evaluate each one; a badge reserved for deviations says *stop and look*, and its absence safely means *proceed as usual*.

The hard version of the same problem is when two conventions collide irreconcilably. There, marking is not enough — you have to refuse to emit the ambiguous form.

## What Duolingo does

- Duolingo's table of Spanish verb endings by grammatical person marks exactly **3 of 6 rows** as unreliable with a siren marker: *yo* and *él/ella/usted* (whose endings look alike) and *ellos/ellas/ustedes* (where *-n* covers both "they" and "you all"). The other three get **no marker at all** and are stated as consistent across all tenses — *tú* always *-s*, *nosotros* always *-mos*, *vosotros* always *-is/-ís*. The unmarked rows are a promise, which is what makes the marked ones a warning. Source: blog.duolingo.com/how-to-find-the-subject-in-spanish (Duolingo blog, 2025-01-02; accessed 2026-09-22)
- Spanish written accents are the same principle built into the notation itself: **every** word has stress, but only exceptions to the **2 default stress rules** carry a written mark (ends in -n, -s or a vowel means stress the second-to-last syllable; any other consonant means stress the last). The same mark does **3 distinct jobs** — marking exceptional stress, disambiguating **5 common homograph pairs** (mi/mí, tu/tú, el/él, se/sé, que/qué), and separating the letter *o* from the digit *0*. Source: blog.duolingo.com/spanish-accent-marks (Duolingo blog, 2025-05-29; accessed 2026-09-22)
- On irreconcilable conventions, Duolingo's calendar guide **refuses to pick a winner** for DD/MM versus MM/DD and prescribes the ritual instead: "07/01 ... could mean either the first day of July or the seventh day of January. You'll have to do what English speakers do — ask for clarification. To be sure, you can also write out the month to make it clear what you mean." DD/MM/YYYY is used across most of the English-speaking world, MM/DD/YYYY in the U.S. — and the U.S. still says "the 4th of July" in the other order, so even one population is not internally consistent. Source: blog.duolingo.com/calendar-in-english (Duolingo blog, 2025-09-29; accessed 2026-09-22)
- **The tension:** a marker set that starts selective drifts toward universal. Each new caveat feels worth adding, and once most rows carry one the marker has quietly become decoration. Selectivity is a budget that has to be defended, not a decision made once.

## The transferable pattern

1. **Grade your own reference material before publishing it.** For each row, ask whether you would stake a production incident on it. The ones you would not are the ones that get marked.
2. **Mark deviations only.** If you find yourself marking a majority of rows, your default is wrong — re-cut the default rather than badging everything.
3. **Treat the unmarked rows as a commitment.** The warning only carries information if silence is a guarantee. An unmarked row that turns out to be unreliable destroys the whole scheme, not just that row.
4. **Where two conventions collide, do not silently choose.** A rendering that parses successfully under both conventions produces **no error signal at the point of entry** — sender, reader and system all believe they agree, and the disagreement is discovered downstream where it cannot be traced back. Force the unambiguous form: emit the long form, require the explicit qualifier, reject the ambiguous input.
5. **Let one marker do several jobs only if its meaning stays "this deviates."** Reusing a mark for related disambiguation work is efficient; reusing it for an unrelated job re-overloads the very primitive you were disambiguating.

Note the boundary: this node is about marking in reference material and stored form. What the interface does at the moment a user enters something wrong is a live-response question, not a notation one.

## Apply to your product

- In your main reference table or schema doc, which rows would you not bet on? Are they visually distinguishable from the ones you would?
- What percentage of your rows currently carry a caveat? Above about a third, your caveat has stopped being a signal.
- Which values in your system parse correctly under two different conventions — dates, units, timezones, ordering, precision, currency? What would forcing the unambiguous form cost, compared with the downstream incident you cannot trace?

## See also

[[ship-a-labelled-default-with-named-exceptions]] · [[teach-the-invariant-the-exception-preserves]] · [[your-symbol-set-is-not-a-shared-language]]
