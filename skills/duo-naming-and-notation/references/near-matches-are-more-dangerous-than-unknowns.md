---
name: duo-naming-and-notation-near-matches-are-more-dangerous-than-unknowns
summary: An element that resembles something the user already knows but behaves differently causes worse, quieter, longer-lived errors than an element that looks entirely new.
metadata:
  internal: true
---

# Near-Matches Are More Dangerous Than Unknowns

## Concept

An unfamiliar token triggers a lookup. A familiar-looking token triggers a confident retrieval and no lookup at all. So the dangerous items in any new naming scheme or symbol set are not the alien ones — they are the near-misses, the things that resemble something the user already knows and behave differently.

The mechanism is that superficial similarity silently transfers an existing pattern **and** suppresses the uncertainty that would have made the user check. The user is not confused; they are confidently wrong. The error therefore survives until something external corrects it, which is usually the moment they act on it.

## What Duolingo does

- The Cyrillic guide deliberately splits the alphabet by risk rather than by frequency: letters that match Latin (А, K, M, T) in one group, then the **false friends** — В is /v/, Н is /n/, Р is /r/ — taught as the hard part, and the genuinely alien characters (Ш, Ч, Ж) treated as the **easier** group, precisely because a reader knows to look those up. Cyrillic is the official script for nearly **50 languages** and about **250 million speakers**. Source: blog.duolingo.com/what-is-the-cyrillic-alphabet (Duolingo blog, 2022-05-05; accessed 2026-09-22)
- The false-cognates post catalogues the same trap across languages — Spanish *embarazada* means pregnant, not embarrassed; *éxito* means success, not exit; French *librairie* is a bookstore, not a library; German *Gymnasium* is a high school; Dutch *braaf* means obedient. **9 worked pairs**, with **3 named causal mechanisms**: meanings drift apart, sounds drift together, or pure coincidence. Source: blog.duolingo.com/false-cognates (Duolingo blog, 2022-08-01; accessed 2026-09-22)
- **The tension is stated in the same post:** guessing from a familiar-looking form is a genuinely good strategy most of the time — "sometimes you can use your own language to your advantage and guess the meanings of new words." The heuristic that creates the trap is the same one that usually works. You cannot train it out of users, and you should not want to.
- Borrowed terms drift the same way. Japanese loanwords whose meanings moved from their sources: *manshon* (from "mansion") is an apartment; *arubaito* (German *Arbeit*, work) narrowed to part-time work; *piiman* (French *piment*, chili) is a mild bell pepper; *zubon* (French *jupon*, skirt) is trousers; *pantsu* means underpants only; *abekku* (French *avec*) means a romantic couple. **6 documented shifts across four source languages** — the framing being that you think you already know this one, and then reality hits. Source: blog.duolingo.com/surprising-japanese-loanwords (Duolingo blog, 2026-02-10; accessed 2026-09-22)

## The transferable pattern

When you introduce a set of names, statuses, flags or icons, sort them by **distance from what the user already holds**, not by how often they appear.

1. **Inventory the near-misses first.** Which of your tokens look or sound like a token in the system your users came from, and mean something else? That list is your highest-severity documentation, and it belongs at the top, not in a glossary.
2. **Flag them as traps, explicitly.** A near-miss taught as a neutral fact is filed alongside every other fact. Taught as "this one looks like X and is not X," it acquires the uncertainty that triggers a check.
3. **Teach the alien items second and worry about them less.** They cost more effort per item and generate almost no silent errors.
4. **Prefer a genuinely novel name over a near-miss name.** If you are choosing a label and the best candidate is one character or one connotation away from an established term with different behaviour, take the stranger option. Strangeness is a feature: it buys you the lookup.
5. **Make the divergence loud at first contact**, not at the point of failure. The cost of a wrong model is paid when the user acts, which is far downstream of when they read.

## Apply to your product

- List every term in your product that also exists in the tool your users most recently used. For each, does it mean the same thing? The ones that do not are your bug reports.
- Where are you reusing a well-known word for a subtly different concept because it "reads naturally"? What would the unfamiliar alternative cost you, and would it be cheaper than the misreads?
- How would a user currently discover that one of your near-miss terms is a near-miss — and would they discover it before or after acting on it?

## See also

[[users-snap-the-new-thing-to-categories-they-already-have]] · [[meaning-mutates-when-a-term-crosses-a-boundary]] · [[mark-only-what-deviates-and-force-the-unambiguous-form]]
