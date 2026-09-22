---
name: duo-ml-in-production-shallow-features-let-new-segments-inherit-performance
summary: Surface features let one pooled model serve every segment, so a brand-new segment with almost no data inherits the performance of all the others.
metadata:
  internal: true
---

# Shallow Features Let New Segments Inherit Performance

## Concept

Every feature that depends on an external resource — a parser, an embedding model, a labelled corpus, a vendor API — forces you to build the system once per segment, and quietly excludes every segment where that resource does not exist. The richer feature wins the offline benchmark on your biggest segment and loses the long tail entirely.

Features computable from the raw input alone have the opposite property. Because they mean the same thing everywhere, one model trains across all segments at once, and a segment that launched last week inherits the statistical strength of every segment that came before it. That is not a convenience. It is the difference between a cold-start segment having a working system on day one and having nothing until it accumulates its own history.

## What Duolingo does

Source: blog.duolingo.com/how-machine-learning-helps-duolingo-prioritize-course-improvements (Duolingo blog, 2019-12-16; accessed 2026-09-22)

- The report-ranking model uses **unigrams and bigrams from the submitted answer**, plus **edit-style features** comparing that answer to the already-accepted ones. Nothing else.
- They deliberately avoided NLP libraries and outside data, which "are often themselves limited to a few of the most widely spoken languages" — the resource-rich feature would have served the head and abandoned the tail.
- **One model, trained across all courses simultaneously.**
- The prior baseline was wisdom-of-the-crowd ranking by report count, which scored **AUC-ROC of about 0.59** against 0.5 for random. The ML system **beat it on every single course**.
- It worked on the data-scarce courses — **Navajo, Hawaiian, Klingon and High Valyrian** — where per-segment tooling does not exist at any price.
- **Arabic, Latin and Scottish Gaelic reached the low report rates of mature courses within weeks of launch**, with near-zero training data of their own.
- **The tension is stated by the authors themselves:** the design is dated, and they expect to revisit it with multilingual contextual embeddings for "much higher accuracy." Cheap-and-general was the right launch decision, not the ceiling.

## The transferable pattern

Ask of every candidate feature: *what does this require that not all of my segments have?* Anything needing a per-segment artifact buys accuracy on your largest segment and pays for it with total coverage on your smallest — and the smallest segments are exactly the ones with no other way to get a working system.

The payoff is pooled training. If the features carry the same meaning everywhere, all the data becomes one training set, and the model a new segment gets on day one is the model every other segment already validated. Sharding per segment throws that away and makes cold start unsolvable by construction.

Keep an honest baseline. The naive ordering here — sort by how many people complained — is the one most teams would ship and never question. Measuring it at 0.59 is what turned "we beat it everywhere" into a claim rather than a feeling.

Name the expiry date. Resource-free features are a launch decision, not a permanent architecture. Write down what you would switch to once your important segments have their own data, so the shortcut does not calcify into a constraint nobody remembers choosing.

## Apply to your product

- Which of your model's features silently require a resource only your biggest segments have?
- If you pooled every segment into one training set today, which segment would gain most — and is that the one you currently cannot serve at all?
- What is the dumbest ordering heuristic a reasonable person would try first, and have you actually measured it?

## See also

[[rank-the-noise-dont-filter-it]] · [[../duo-inclusive-access/SKILL]] · [[../duo-rules-and-heuristics/references/ship-the-shortcut-with-its-coverage-rate]]
