---
name: duo-measurement-validity-ship-a-subscore-only-if-it-adds-information
summary: A component score earns its place only by passing three tests — structure, reliability, and information the total does not already carry.
metadata:
  internal: true
---

# Ship a Subscore Only If It Adds Information

## Concept

Splitting a headline number into parts feels like generosity — more detail, more transparency, more for the user to act on. It is usually the opposite. A component that merely restates the total adds noise and false precision, and invites decisions the data cannot support. Two questions decide whether a breakdown is real. First, are you cutting along the lines the capability is actually used on, or along the lines that were convenient to collect? Second, does each component carry information the composite does not already contain? If it does not, it is a decoration on a dashboard.

## What Duolingo does

Source: blog.duolingo.com/subscores-improving-how-we-report-duolingo-english-test-results-2 (Duolingo blog, 2020-06-08; accessed 2026-09-22)

- The Duolingo English Test reports four integrated subscores — Literacy, Conversation, Comprehension, Production — instead of the conventional four-channel split the industry ships. The reasoning is that real situations combine channels, so the report should too. Seven question types feed the four subscores, each type feeding two of them.
- Before shipping, they checked the structure empirically rather than assuming it. Non-metric multidimensional scaling on **n=47,654** test takers returned **Stress-1 = 0.026**, meaning the assumed grouping matched how performance actually clustered.
- Reliability, internal consistency: Literacy **.89**, Conversation **.93**, Comprehension **.95**, Production **.76**. Reliability, 30-day test-retest: **.82 / .80 / .78 / .83**. A component that does not reproduce on a second sitting is not a measurement.
- The decisive gate was proportional reduction in mean squared error against the total score. All four subscores beat the total — most dramatically Production, at **.76 versus .45**. Shipped July 2020.
- The tension is in that same pair of numbers. Production has the *weakest* internal consistency (.76) and by far the *largest* added value over the total (.76 vs .45). The dimension your instrument measures least well is the one the composite hides most, so the noisiest component is often the one most worth reporting — and the one most likely to be cut for looking unreliable.

## The transferable pattern

Run any proposed breakdown through three gates, in order:

1. **Structure.** Does the data cluster the way your proposed components assume? Cut along how the thing is actually used in the world, not along the systems that happened to emit the events. A breakdown that mirrors your data pipeline is a diagram of your pipeline.
2. **Reliability.** Does each component reproduce when the same subject is measured again a month later? A component that moves on re-measurement is reporting sampling noise with a confident label on it.
3. **Added information.** Does the component predict the outcome better than the total already does? If the total explains it, the component is a restatement — and every restatement you publish invites someone to make a decision on it.

Report the weakest-measured surviving component anyway, with its reliability stated next to it. Suppressing it hands the composite a flattering average and hides the exact place you are worst.

## Apply to your product

- Take the headline number on your main dashboard. Are its components the way customers experience the product, or the way your event schema happens to be shaped?
- For each component you already publish, can you show it predicts anything the total does not? If not, what would break if you deleted it this week?
- Which of your components would survive a re-measurement of the same accounts 30 days later, and do you know, or are you assuming?

## See also

[[publish-the-component-where-you-lose]] · [[benchmark-on-an-instrument-you-did-not-build]] · [[../duo-experimentation/references/metric-selection]]
