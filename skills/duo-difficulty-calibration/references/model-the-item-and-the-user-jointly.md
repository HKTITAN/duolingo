---
name: duo-difficulty-calibration-model-the-item-and-the-user-jointly
summary: Difficulty is a property of the item-user pairing, not of the item, so estimate content difficulty and user ability in one model or you cannot target anyone.
metadata:
  internal: true
---

# Model the Item and the User Jointly

## Concept

Most products carry a difficulty label baked into the content: this task is "advanced," that one is "beginner." The label is a guess made once, by an author, about an average person who does not exist. It cannot tell you whether this specific item is a stretch or a bore for the person in front of you right now.

Difficulty is not a property of an item. It is a property of the pairing — item crossed with user. A system that knows only how hard the content is, or only how capable the user is, has one of the two curves and cannot find where they meet. Both quantities can be learned from the same interaction stream: every attempt is simultaneously evidence about the item's difficulty and about that user's ability, and fitting both at once is what makes "pick the right next thing" a computable question rather than an editorial one.

## What Duolingo does

Source: blog.duolingo.com/learning-how-to-help-you-learn-introducing-birdbrain (Duolingo blog, 2020-10-07; accessed 2026-09-22)

- Duolingo built **Birdbrain**, a machine-learning model that continuously estimates **both** how proficient each learner is **and** how difficult each piece of content is for them. Its output — the predicted probability that this learner gets this item right — is fed into the Session Generator, which assembles each session at that learner's difficulty.
- Rollout was gradual and measured: personalized lessons went from roughly **0% in March 2020 to over 20% by October 2020**. A/B tests showed learners both learned more and returned more often.
- It complemented, rather than replaced, an older per-word knowledge model — Birdbrain extended ability estimates from single vocabulary items to all facets of the skill.

Source: blog.duolingo.com/duolingo-technology-innovations (Duolingo blog, 2022-06-13; accessed 2026-09-22)

- Trained on data from more than **500 million exercises completed daily**. Duolingo built it in-house rather than adopting an existing model, and described it at launch as the largest-scale student model in its field.

Source: blog.duolingo.com/duolingo-teaching-method (Duolingo blog, 2023-02-02; accessed 2026-09-22)

- The published method makes this the second of its principles: the model tracks what the learner knows and adjusts **order and difficulty** — advancing faster past aced concepts, inserting foundational practice where the estimate is weak.

**The tension.** A joint model needs volume. At 500 million events a day the estimates are sharp; on a product with a thousand daily events, the same architecture returns confident noise. The pattern below is the target, not the day-one build.

## The transferable pattern

Two separate estimates, fit from one event stream:

1. **Per-item difficulty** — learned from how the whole population performs on it, not from the author's label.
2. **Per-user ability** — learned from that user's history across items, not from what they told you at signup.

Select the next item where those two meet. The unit you are modelling is the **pair**, and a system that stores only a per-user level or only a per-item tier has thrown away half the signal before it starts.

Two practical consequences. First, an authored difficulty tier is a prior, useful on a cold item and worth overwriting the moment real attempts arrive. Second, the model's own confidence matters: when the estimate for a pair is weak, the right move is an item that is informative rather than one that is comfortable.

## Apply to your product

- Do you store a difficulty value per item, a level per user, or an estimate for the pair? If it is one of the first two, what does the missing half currently cost you?
- Where do your current difficulty labels come from — measured behavior, or an author's judgment at authoring time? How stale are they?
- What is your daily event volume? Is it enough to fit anything, or should the first version be a simple ability estimate with authored difficulty as a prior?

## See also

[[the-narrow-band-between-bored-and-lost]] · [[fifty-percent-success-is-the-honest-signal]] · [[read-your-difficulty-weights-as-a-content-brief]] · [[../duo-memory-and-decay/references/per-item-half-life-not-a-fixed-ladder]]
