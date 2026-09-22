---
name: duo-progression-design-pick-one-variant-and-name-the-choice
summary: Teach one canonical default, accept the alternatives as correct, and say out loud that you chose.
metadata:
  internal: true
---

# Pick One Variant and Name the Choice

## Concept

Domains with legitimate variation put you in a trap. Present the fuzzy thing as a clean rule set and the user's trust dies the first time reality contradicts you. Present every variant at once and the thing is unlearnable — there is no working hypothesis to start from. The way out is three moves that have to be made together: teach one canonical default so there is something to hold; accept the alternatives as correct so the system never punishes a user for being right in a different context; and state in public that the default is a choice you made, not a truth you discovered. Skip the third move and the first two curdle into a product that is confidently wrong.

## What Duolingo does

Source: blog.duolingo.com/what-is-spanish-vosotros (Duolingo blog, 2026-05-26; accessed 2026-09-22)

- The Spanish course teaches **"ustedes" and not "vosotros"**, even though "vosotros" is the only second-person-plural form used in Spain, because far more dialects use "ustedes" and Spain understands it too. Same logic in Korean: the **Seoul-based standard only, out of 6 major dialects**. The post states the principle directly — no single course, app, instructor or textbook can teach everything for one city, age group and context.
- **The cost is conceded in the same post:** you will not sound like you are from Spain, and the learner who prompted the post — **a 365-day streak, reading Spanish books** — hit a wall precisely because the course omitted it. The omission generated the complaint that generated the post.
- Alternatives are accepted, not just tolerated. The course teaches the "Some le" pattern most common in Latin America but **explicitly marks other leísmo varieties correct**, and publishes a comparison table of **4 documented varieties** so learners can see the default is a choice. **The post admits the table is simplified** and that speakers switch for more reasons and in different ways than shown (blog.duolingo.com/spanish-dialects-differences-le-lo (Duolingo blog, 2022-11-15; accessed 2026-09-22)).
- **The sharpest version of the conflict.** Duolingo teaches Modern Standard Arabic — official in **22+ countries**, part of a language with **300 million+ speakers** — and says in the same post that MSA "is not a dialect that people learn at home," being acquired through formal or religious education. It then documents how far Moroccan, Egyptian and Syrian Arabic diverge in greeting, grammar and pronunciation. Its dialect post opens on the same admission: "the language people use in everyday life often differs from what's formally taught" (blog.duolingo.com/arabic-dialects (Duolingo blog, 2023-11-09; accessed 2026-09-22)).
- **The tension is unresolvable and Duolingo says which side it picked.** The reason MSA is teachable is the reason it is useless at home: none of the spoken dialects have been standardized, so there is usually more than one way to spell things. Teachability and field usefulness point in opposite directions. Duolingo chose teachability.

## The transferable pattern

Where your domain has real variation — competing conventions, regional practice, several valid architectures, house styles that disagree — do all three of these, not one:

1. **Teach one default.** Pick the variant with the widest reach rather than the one that is locally optimal. A user with the broadly-understood version can pick up the local variant in context later; the reverse is not true. Attention is a fixed budget and you are spending it.
2. **Accept the alternatives as correct.** Anywhere you validate, check for a set, not a string. Punishing a user for being right somewhere else is the fastest way to teach them your product does not know the domain.
3. **Publish the choice and its cost.** One line: here is what we teach, here is what else exists, here is where ours will not serve you. This is the move that preserves trust when the user meets the boundary, and it is the one that gets cut for space.

Where only one variant has a stable specification, teach that one and name the gap explicitly — a documented standard is teachable at scale precisely because it has been standardized, which is often the same reason it is not what people actually use.

## Apply to your product

- Where does your product present a contested convention as the single right answer? What would the one-line disclosure say?
- Does your validation accept the alternatives as correct, or only the default? Check the actual comparison, not the documentation.
- Are you optimizing for the variant that is most teachable or the one that is most useful in the field? You cannot have both — which did you pick, and have you told anyone?

## See also

[[make-the-scaffold-removable-by-the-user]] · [[structured-coverage-catches-what-use-never-surfaces]] · [[sequence-by-frequency-and-declare-the-tail-optional]] · [[../duo-voice/SKILL]]
