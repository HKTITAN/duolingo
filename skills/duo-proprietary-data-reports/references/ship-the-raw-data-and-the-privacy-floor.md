---
name: duo-proprietary-data-reports-ship-the-raw-data-and-the-privacy-floor
summary: A linked spreadsheet of the underlying rows plus a hard minimum-N-per-cell rule makes the report auditable enough to cite and keeps small cells unpublished.
metadata:
  internal: true
---

# Ship the raw data and the privacy floor

## Concept

Two artifacts do most of the work of turning a marketing document into a citable one, and they pull in the same direction. The first is a linked file of the underlying aggregated rows, so a reader can check a claim without asking you. The second is a hard minimum-count-per-cell rule, applied before publication, so no cell small enough to identify an individual ever reaches the file. The floor is usually framed as a privacy control, and it is one — but it is also what makes shipping the rows safe in the first place. You cannot responsibly do the first without the second.

## What Duolingo does

- The 2020 global edition ships an explicit "About the data" note — aggregation by country or language, **exclusion of any country with fewer than 5,000 learners** stated as a privacy measure — and links a public spreadsheet containing a subset of the underlying data. The report covers the window **1 October 2019 to 30 September 2020**, across **500M+ total users, roughly 40M monthly actives, all 194 countries, 98 courses teaching 39 languages**.
  Source: blog.duolingo.com/global-language-report-2020 (Duolingo blog, 2020-12-15; accessed 2026-09-22)
- The practice persists rather than being a first-edition flourish. The 2023 edition again publishes the **full country-by-language list as a spreadsheet**, excludes countries under **5,000 learners**, and excludes **under-13s** from all analyses.
  Source: blog.duolingo.com/2023-duolingo-language-report (Duolingo blog, 2023-12-04; accessed 2026-09-22)
- The 2025 edition links the full country and language spreadsheet alongside the narrative, flags age and motivation as self-reported, and republishes the whole report in local languages — so the auditable file and the localized editions travel together rather than the file being an English-only appendix.
  Source: blog.duolingo.com/2025-duolingo-language-report (Duolingo blog, 2025-12-01; accessed 2026-09-22)
- Tension: publishing the rows means somebody will re-analyse them and reach a conclusion you did not pick, including one that contradicts your headline. That is the cost of being citable, and it is the correct trade — but it means the headline has to be defensible against the file you shipped, which is a real constraint on how you write the narrative. The floor has its own cost too: cells below the threshold are the smallest and often the fastest-moving segments, so the published file is structurally quiet about exactly the places where something new is happening.

## The transferable pattern

Decide the floor before you run the query, then publish what survives it.

1. **Set a minimum count per published cell and apply it in the pipeline, not in review.** A rule enforced by a human at the end is a rule that will be waived for one interesting number.
2. **Publish the aggregated rows as a plain file — a spreadsheet or CSV — at a stable URL.** Not a chart image, not a PDF. Somebody has to be able to sort it.
3. **Publish the rows that did not make the narrative.** The credibility comes precisely from the reader finding a row you did not highlight.
4. **State what the floor removed.** "N segments fell below the threshold and are excluded from rankings" is a one-line disclosure that stops the floor from looking like curation.
5. **Translate the file, not only the prose.** If you publish regional or translated editions, the underlying table has to be reachable from every one of them, or those editions are strictly less citable than the original.
6. **Write the headline so it survives the file.** Before publishing, have someone try to contradict your lead using only the rows you are about to ship.

## Apply to your product

- What is the smallest cell count you are willing to publish, and is that number enforced in code or in a review meeting?
- If you shipped your underlying aggregated rows tomorrow, which of your own headline claims would be the easiest to argue with?
- Which segments would your floor silently delete, and are those the segments where your most interesting movement is happening?

## See also

[[publish-the-exclusions-with-the-findings]] · [[cut-data-to-a-unit-people-belong-to]] · [[fixed-window-repeated-forever]]
