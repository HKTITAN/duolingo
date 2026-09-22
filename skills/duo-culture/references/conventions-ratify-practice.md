---
name: duo-culture-conventions-ratify-practice
summary: A standards body codifies what practitioners already do; to get a convention adopted, win working practice first.
metadata:
  internal: true
---

# Conventions Ratify Practice

## Concept

A committee has authority over a document, not over behaviour. Practitioners converge on conventions through repeated coordination under real constraints, and a written standard that codifies that convergence is adopted instantly because everyone already complies. One that contradicts it is simply ignored, and the result is a widening gap between the documented system and the real one — at which point the documentation stops being consulted at all.

So the order of operations for anyone who wants a convention adopted is the reverse of the intuitive one: get it into working practice among the people doing the work, then write it down.

## What Duolingo does

- **It traces standardization histories in which the institution arrives late.** English printers "had largely settled on certain spelling and grammar conventions" by the mid-17th century, and Johnson's 1755 dictionary solidified rather than created those norms; English never had an academy at all. The formal bodies and their dictionaries: Accademia della Crusca founded 1583, dictionary 1612; Académie française 1635, dictionary 1694; Real Academia Española 1713, Diccionario de autoridades 1726–1739; Webster 1783 and 1828; Duden 1880; An Caighdeán Oifigiúil 1958. Source: blog.duolingo.com/history-of-standardization (Duolingo blog, 2025-12-23; accessed 2026-09-22)
- **The failed attempts are the load-bearing detail.** Academy foundings "weren't the actual starting point. They were preceded by many earlier efforts that simply didn't stick."
- **It states the limit of mandates after walking through 200 years of change**: such mandates "might slow progress or spark debates, but language serves its users — not the other way around." Source: blog.duolingo.com/how-language-has-changed-in-the-last-200-years (Duolingo blog, 2022-06-27; accessed 2026-09-22)
- **The corpus contains hard counterexamples to its own optimism.** An Caighdeán Oifigiúil was written for government use and spread outward into education — a body can seed a standard where there is no established practice to ratify. And a mandate backed by control of a venue does sometimes win outright: the 6th-century bishop Martin of Braga forced Portuguese off the planetary day names onto Church Latin numerals, and the change has held for 1,400 years. Source: blog.duolingo.com/why-do-languages-change (Duolingo blog, 2023-06-13; accessed 2026-09-22)
- **In its own engineering, it used credit rather than mandate to move a migration.** Expecting product teams to deprioritize a Java-to-Kotlin conversion nobody was rewarded for, Duolingo ran a conversion contest with a daily leaderboard and a trophy mug. Product-team developers ended up doing about **50% of all file conversions**. A temporary "Kotlin checker" reviewer role spread the new practice, and membership grew until it contained every Android developer and the role was retired. Source: blog.duolingo.com/migrating-duolingos-android-app-to-100-kotlin (Duolingo blog, 2020-04-06; accessed 2026-09-22)

## The transferable pattern

1. **Pilot the convention with the people who will live under it before it becomes a rule.** Adoption is decided at the point of use, where your authority does not reach.
2. **For work whose benefit is diffuse and whose credit is invisible, supply the missing credit.** A public scoreboard and a trivial trophy cost nothing and can substitute for winning the prioritization argument on every team, one team at a time.
3. **Make the enforcement role temporary by design.** A specialist reviewer exists to transfer knowledge; its value hits zero when the transfer completes, and keeping it past that point adds queueing delay and turns a teaching mechanism into a status marker.
4. **When the documented system and the real one diverge, update the document first.** Otherwise you lose the document, and the real system goes unrecorded.

Tensions worth naming. A convention that wins working practice is not automatically the right one, and a body writing a standard where no practice exists yet is a different case entirely (see the counterexamples above). A scoreboard has its own failure mode: it counts what is easy to count, so it rewards volume and needs a separate quality guard beside it. And credit-based adoption only reaches work that can be made visible — the genuinely invisible tasks stay undone.

## Apply to your product

- Which of your written standards describe something your team was already doing, and which were imposed from a document?
- Name a piece of necessary work no team is rewarded for. What would a visible scoreboard for it cost you to build?
- Which reviewer or approver role in your process was created to teach something that has since been learned?

## See also

[[audit-the-inherited-standard]] · [[no-process-without-purpose]] · [[ownership-clarity-culture]] · [[clock-speed]]
