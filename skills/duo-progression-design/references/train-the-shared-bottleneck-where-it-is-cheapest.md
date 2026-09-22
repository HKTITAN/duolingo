---
name: duo-progression-design-train-the-shared-bottleneck-where-it-is-cheapest
summary: When two skills stall on the same underlying resource, drill that resource in whichever context is easiest.
metadata:
  internal: true
---

# Train the Shared Bottleneck Where It Is Cheapest

## Concept

Skills that look independent frequently stall on the same underlying resource. When that is true, the fastest way to improve the hard skill is not to practise the hard skill — it is to find the shared subcomponent and train it in whichever context costs least. Attack a bottleneck where the surrounding load is low and the gain transfers to every context that shares it, including the one where practice was previously unbearable. The failure this fixes is the user grinding away at the hard version, failing for a reason they cannot see, and concluding they lack talent.

The same logic changes how you recommend practice material: index it by which sub-skill it trains and what support it carries, not by how good it is.

## What Duolingo does

Source: blog.duolingo.com/covering-all-the-bases-duolingos-approach-to-listening-skills (Duolingo blog, 2026-05-05; accessed 2026-09-22)

- Duolingo's position, stated plainly: **reading improves listening**, because the faster the brain can retrieve related vocabulary, the easier real-time listening becomes. Lexical retrieval is the shared bottleneck; reading exercises it **without real-time pressure**, so the cheap context trains the resource that the expensive one is starved of.
- The same split applied to production: writing and speaking are both productive skills requiring retrieval, but writing "gives you the time to think carefully about what you want to say" and to go back and edit — framed as "a safe space to help you train your brain for situations where you need to speak." One cost is removed so the other can be trained alone (blog.duolingo.com/covering-all-the-bases-duolingos-approach-to-writing-skills (Duolingo blog, 2026-07-02; accessed 2026-09-22)).
- The recommendation corollary: Duolingo sorts **15 films into 3 buckets by sub-skill**, and every entry states its mechanism rather than its quality. Teen movies train unaided listening because simple plots plus first-person narration mean "you can't rely on the visual aid of watching people's mouths" while there is no complicated story to track. Sci-fi and period pieces build vocabulary because they "revolve around a specific theme that uses it repeatedly" — built-in spaced repetition of domain terms. Comedies train speech because the dialogue is "straightforward and natural, rather than textbook-like" (blog.duolingo.com/movies-for-learning-english (Duolingo blog, 2026-01-22; accessed 2026-09-22)).

## The transferable pattern

When a skill is stuck, decompose it before adding reps. Ask what resource the failing task is starved of, then find every other task in your domain that exercises that same resource and rank them by how much *other* load they carry. Train in the cheapest one.

The usual shapes of a shared bottleneck: speed of lookup or recall; holding several items in working memory at once; pattern recognition over noisy input; the decision procedure itself, separate from executing it. Each of these appears in multiple tasks, and usually at least one of those tasks is far easier than the one the user is failing.

Two practical consequences:

- **Prescribe the adjacent drill and explain why.** Users will resist practising X to get better at Y unless you name the shared component. Without the explanation it reads as a detour and they skip it.
- **Recommend material by mechanism, not by quality.** "This is excellent" gives a user with a training goal nothing to choose on. "This trains unaided pattern recognition because the usual visual crutch is absent" does. Every recommendation should say which sub-skill it exercises and what support it carries or withholds — those two facts are the whole basis for choosing.

The caution: a shared bottleneck is a hypothesis, not a given. If training the cheap context does not move the expensive one, the components were not shared and you have spent the user's time on a theory.

## Apply to your product

- Where users are stuck, what resource is the failing task starved of — and which easier task in your product exercises that same resource?
- When you recommend practice material, does each item say which sub-skill it trains and what support it carries? Or does it just say the item is good?
- What would tell you the bottleneck was not actually shared, and are you measuring it?

## See also

[[recognition-then-guided-then-production]] · [[do-the-real-thing-badly-on-day-one]] · [[scaffold-and-fade-on-a-schedule]] · [[rank-what-you-teach-by-cost-of-getting-it-wrong]]
