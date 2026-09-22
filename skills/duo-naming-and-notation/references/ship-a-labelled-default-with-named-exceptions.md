---
name: duo-naming-and-notation-ship-a-labelled-default-with-named-exceptions
summary: Give an explicit default labelled as a default plus its named exceptions — a false universal destroys trust in all your guidance, and a hedge gives the user nothing to act on.
metadata:
  internal: true
---

# Ship a Labelled Default with Named Exceptions

## Concept

There are three ways to document a rule that has exceptions, and two of them are bad. A universal-sounding rule that fails in the field teaches users your guidance is unreliable — and they do not discount that one rule, they discount all of it. A hedged non-answer ("it depends on context") preserves your accuracy and gives the user nothing to act on.

The third way is to **label the coverage boundary**: state the default, say out loud that it is a default and roughly what it covers, then name the specific cases where it does not hold. That preserves usability and credibility at once, and it converts "your docs were wrong" into "I hit one of the named cases."

The same labelling move solves tiering. Material a user has not reached reads as a deficit and stalls them; the same material labelled "not yet relevant to you" is permission to proceed.

## What Duolingo does

- The tú/usted guide gives one table explicitly covering "*most* situations," then names **3 specific counterexamples**: Costa Rican Spanish uses *usted* even between spouses, Spain skews toward *tú* (except the Canary Islands and Andalucía), and parts of Colombia use *usted* as an intimacy marker. The reader gets a decision for the common case and knows exactly which three places to distrust it. Source: blog.duolingo.com/tu-vs-usted (Duolingo blog, 2026-07-09; accessed 2026-09-22)
- When the default itself is contested, Duolingo splits the decision **by dimension** rather than picking one authority for everything. The Yiddish course teaches **YIVO-standardised grammar** — matching what a university course would use, for interoperability and credibility — but uses the **Hasidic Hungarian accent** for pronunciation, because that is the variety learners are most likely to actually hear. Standard and most-encountered optimise for different failure modes, so a single source for both guarantees you fail one of them. Yiddish speakers fell from as many as **13 million** historically to around **600,000** today; it was Duolingo's **40th** course. Source: blog.duolingo.com/yiddish-is-now-on-duolingo (Duolingo blog, 2021-04-06; accessed 2026-09-22)
- On tiering inside one document: the Spanish pronunciation column closes with "Level up: Two tips for advanced learners" and tells beginners explicitly to "Start with the vowel sounds and 'c' and 'g,' and move on to the other tips once you're comfortable." The German plurals guide does the same structurally, splitting itself into "101" and "201." Source: blog.duolingo.com/spanish-pronunciation-tips (Duolingo blog, 2022-06-28; accessed 2026-09-22)
- **The tension:** naming exceptions has a cost. Each named case invites the reader to wonder how many unnamed ones exist, and a long exception list starts to read as a rule that does not work. Three named cases clarify; fifteen mean the default is wrong and should be re-cut.

## The transferable pattern

1. **Never ship a rule with no stated scope.** "Usually", "in most cases", "unless you are on the enterprise plan" — the qualifier is what makes the rule survive its first failure.
2. **Name the exceptions specifically enough to self-identify.** "Some regions differ" is a hedge. "Costa Rica, Spain outside the Canaries and Andalucía, parts of Colombia" lets a reader check whether they are in one.
3. **When the default is genuinely contested, split by dimension.** Ask which failure each candidate protects against — compatibility with other systems, or matching what the user will actually encounter first. Take the standard for the first and the common variant for the second, and say which you took where.
4. **Tier inside the document, not across documents.** Splitting into separate pages loses the user. Not splitting at all paralyses them. An explicit "skip this for now" label converts unread material from deficit into permission.
5. **Count your exceptions as a diagnostic.** Past roughly three or four, the default is mis-cut. Re-draw the boundary rather than lengthening the list.

## Apply to your product

- Take the rule in your docs that support answers most often override. Is it written as a universal? What is its real coverage, and which three named cases break it?
- Where have you picked one authority for an entire area of your product? Are compatibility and day-one usability actually pulling in different directions there?
- Which of your documentation pages has no "you can skip this for now" marker — and how much of it is a user reading as things they should already know?

## See also

[[teach-the-invariant-the-exception-preserves]] · [[mark-only-what-deviates-and-force-the-unambiguous-form]] · [[document-the-failure-not-just-the-answer]]
