---
name: duo-prior-knowledge-transfer-difficulty-is-distance-from-what-they-already-know
summary: Difficulty is not a property of your product but the distance between it and the model each user already carries.
metadata:
  internal: true
---

# Difficulty Is Distance, Not a Property

## Concept

Difficulty is not a property of the thing being learned. It is the distance between that thing and the model the person already carries. Anything resembling a known model transfers almost free; anything unfamiliar has to be built from scratch. Two people meeting identical material therefore meet genuinely different difficulty, and a single "beginner" path will be trivial for one of them and impossible for the other. Distance is also uneven across dimensions — the same thing can be easy on one axis and brutal on another for the same person — so averaging it into one rating discards exactly the information that would have told the user where they will struggle.

## What Duolingo does

Source: blog.duolingo.com/hardest-languages-to-learn (Duolingo blog, 2025-01-21; accessed 2026-09-22)

- Asked to name the objectively hardest language, Duolingo's linguist refuses the premise. There is no single hardest language, even for English speakers, because difficulty depends on the languages you already know. The four factors she names — writing system, sound inventory, grammatical structure, cultural distance — are each measured as distance from the learner's existing system, never as an absolute score.
- The examples are concrete distances, not adjectives: Japanese has **three writing systems and three politeness levels**; Zulu has **15–19 noun classes** plus clicks and tone; Georgian layers **two case systems**; !Xóõ has roughly **100–170 sounds including up to 80 clicks**, against English's **~44**.
- The companion post refuses the mirror-image framing — "No one language is objectively easier than the rest" — then decomposes by axis. Japanese has relatively familiar sounds for English speakers and no tones, but three scripts and very different word order; Chinese has a hard sound system and **no verb tenses at all**. English is genetically closer to German yet shares more vocabulary with French, so "related" and "feels familiar" come apart. The same post counts **over 100 language isolates worldwide** — systems with no near neighbour for anyone (blog.duolingo.com/whats-the-easiest-language-to-learn (Duolingo blog, 2026-08-20; accessed 2026-09-22)).
- The template a user reaches for is the nearest structural neighbour, not the system they know best. A less-proficient second language can exert more influence on a third than the more proficient one, when it is the more similar one: an Italian speaker with strong English leans on Italian while learning Spanish. The post's own summary is "language similarity matters a lot" (blog.duolingo.com/is-learning-a-third-language-easier (Duolingo blog, 2024-01-24; accessed 2026-09-22)).
- Tension worth keeping: that same post admits the mechanism is unsettled. The brain may copy an entire existing system wholesale at the outset, or transfer piecemeal over time, and "the research says either might be possible." The prediction — similarity drives transfer — holds either way; the timing does not.

## The transferable pattern

1. **Difficulty is a relation, not a label.** Ask "hard for whom, arriving from what?" before you accept any claim that a feature is hard or easy.
2. **Decompose by axis.** Rate the distance separately on each dimension your product has — the concept model, the terminology, the workflow, the permissions model, the data shape. A single number hides that one axis carries all the pain.
3. **Segment onboarding by what people arrive knowing**, not by an abstract complexity tier. "Beginner / advanced" is the wrong cut when the real variable is which prior system they used.
4. **Find the nearest structural neighbour, not the dominant tool.** Pattern-matching runs on structural overlap before it runs on familiarity, so the weakly-held but near-identical prior gets recruited as the template. Design defaults and docs against that one.
5. **Watch for the split between "related" and "feels familiar."** A system can be genealogically close to yours and still feel alien, or distant and feel obvious. Only measured confusion tells you which.

## Apply to your product

- List the three or four axes on which your product could be far from a newcomer's prior tool. Which one actually accounts for most of your support volume?
- For your last five churned trials, what was each user's *nearest* prior tool — not the market-leading one they also had open?
- If you ship one "getting started" path today, who is it secretly written for, and which arriving cohort does it insult or drown?

## See also

[[interference-clusters-among-near-neighbours]] · [[write-the-path-for-their-source-system]] · [[../duo-product/SKILL]]
