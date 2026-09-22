---
name: duo-naming-and-notation-teach-the-invariant-the-exception-preserves
summary: Find what an exception is protecting and teach that — a rule plus its purpose regenerates the fact on demand and predicts exceptions the user has not met yet.
metadata:
  internal: true
---

# Teach the Invariant the Exception Preserves

## Concept

Most exceptions are not arbitrary. They exist because something else in the system has to stay constant, and the surface rule had to bend to keep it constant. Presented as a list of special cases, they must be brute-force memorised and will be forgotten. Presented as "here is what this is protecting," the irregularity becomes regularity one level down: the user stores a rule plus a purpose, regenerates the fact on demand, and can **predict exceptions they have never encountered**.

The same logic explains a design preference that surprises people: a consistent surface-to-behaviour mapping beats a smaller but arbitrary rule set. Consistent mappings generalise to inputs the user has never seen, so their cost is paid once. Arbitrary exceptions cannot be extrapolated, so their cost scales with the size of your system, not with the number of rules.

## What Duolingo does

- The Spanish preterite guide does not list the spelling changes as irregularities. It explains that **-car→-qu-, -gar→-gu- and -zar→-c-** in the *yo* form exist specifically "to keep the pronunciation the same in all the forms of the preterite," and that *leer→leyó* exists to avoid three vowels in a row. **3 spelling-change classes plus the *leer* case**, all reframed as one invariant being defended.
- **The tension, conceded in the same post:** there is a residue with no such reason — "there are some irregular forms in the preterite that you'll just have to memorize." Not every exception protects something. Claiming a reason where there is none is worse than admitting the arbitrary remainder, because the user will test your explanation against the first counterexample they meet. Source: blog.duolingo.com/preterite-tense-spanish (Duolingo blog, 2023-03-15; accessed 2026-09-22)
- On consistency beating brevity: Duolingo's Italian pronunciation guide notes that Italian's letter-to-sound correspondence is consistent enough that once you have the basics you can pronounce **any** Italian word, including words you have never seen — each written vowel has only **1 or 2** possible pronunciations. English, with arguably fewer stated rules in circulation, generalises far worse. Source: blog.duolingo.com/italian-pronunciation-guide (Duolingo blog, 2026-04-02; accessed 2026-09-22)

## The transferable pattern

1. **For every exception in your system, ask what it is protecting.** A special case in a pricing tier, a validation rule, a keyboard shortcut, an API default — usually something upstream must stay invariant and this is the bend that keeps it so. Write the invariant, not the bend.
2. **Test whether the user can now predict an unseen case.** That is the whole payoff. If your explanation lets someone correctly guess a special case you did not document, it is an invariant. If it only re-describes the cases you listed, it is still a list.
3. **Prefer a consistent mapping over a short one.** A larger rule set that always applies the same way costs less over a system's life than a compact set riddled with exceptions, because the first generalises to everything you ship next year and the second does not.
4. **Name the arbitrary residue as arbitrary.** Say which items have no reason. This protects the credibility of every explanation you *did* give — otherwise the first unexplained case makes the user suspect all of them.
5. **Check whether the invariant should be the surface rule.** If the thing being protected is the one users actually care about, expose it directly and let the mechanics follow from it, rather than documenting a surface rule plus the bends that keep the real rule intact.
6. **Treat a growing exception list as a design signal.** Exceptions that protect nothing are debt. Exceptions that protect something valuable are a hint that the invariant should have been the surface rule in the first place.

## Apply to your product

- Take the three most-asked-about special cases in your system. For each, what stays constant because of it? If nothing does, why does it exist?
- Rewrite one of your exception lists as an invariant plus consequences. Hand it to someone and ask them to predict a case you left out. Can they?
- Which of your special cases has no protective reason at all, and does your documentation say so — or does it imply a logic that does not exist?
- Where have you kept a rule set small by making it inconsistent? Count how many individual items your users must memorise as a result — that is the real number, and it grows with your product.

## See also

[[ship-a-labelled-default-with-named-exceptions]] · [[mark-only-what-deviates-and-force-the-unambiguous-form]] · [[motivated-form-and-one-symbol-one-thing]]
