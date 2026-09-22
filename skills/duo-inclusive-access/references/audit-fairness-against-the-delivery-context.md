---
name: duo-inclusive-access-audit-fairness-against-the-delivery-context
summary: On a self-administered product the environment is part of the instrument — device, screen size and connection belong in the fairness audit alongside demographics.
metadata:
  internal: true
---

# Audit Fairness Against the Delivery Context

## Concept

When your product is used in a controlled room you supply, the environment is a constant and you can ignore it. When it is self-administered — at home, on whatever device the person owns, over whatever connection they have — the environment stops being a constant and becomes part of the instrument. Two people with identical ability can produce different results because one of them was reading a small image on a small screen.

The dangerous part is the attribution. Unless you explicitly test for that variance, it gets attributed to the person. Your system records it as an ability difference, and your dashboards report a hardware gap as a capability gap. Fairness audits that only stratify by demographics will not catch this, because the variable doing the damage is not a demographic — it is a delivery condition that happens to correlate with several.

## What Duolingo does

Source: blog.duolingo.com/fairness (Duolingo blog, 2021-06-30; accessed 2026-09-22)

- Duolingo analyses **differential item functioning** (DIF) beyond traditional demographic groupings, explicitly checking image-based items for variance across **screen size**.
- The worked illustration: two test takers who both score **125** overall — matched ability — answer one image item differently. If the split tracks screen size, that item was partly measuring the ability to read a small screen rather than the construct it was written for.
- Consequence, not just a flag: any item flagged for DIF is **retired from the item bank** and sent to a **panel of content experts** for further analysis. The statistical signal triggers a human review rather than an automatic verdict, and the item does not quietly stay in circulation while the review runs.
- The audit runs continuously against the live bank rather than once at authoring time, which is the only way to catch a condition — a new device class, a new default screen size — that did not exist when the item was written.

## The transferable pattern

Write down the delivery conditions your product does not control — screen size, input device, operating system version, connection speed, ambient noise, whether the person is standing up — and add them to whatever fairness or quality audit you already run. Then, for any component where a result is produced, test whether outcomes differ across those conditions *among users you have reason to believe are equivalent*. That last clause is what makes it an audit rather than a correlation hunt: you are looking for cases where matched people diverge.

Two implementation details carry most of the value. First, the flag has to have a consequence — a component that fails the check comes out of circulation, rather than getting a note attached. Second, the review is human. A statistical signal tells you something is off; it does not tell you what the component is accidentally measuring, and that judgement is the part you cannot automate.

The failure this prevents is subtle and expensive: a model, a score or a ranking that has learned a delivery condition and is reporting it as a property of the person. Once that number leaves your system and gets used for a decision, nobody downstream can tell the two apart.

## Apply to your product

- List the delivery conditions you do not control. Which of them plausibly changes an outcome your product records about a person?
- Do you have any way to compare matched users across those conditions today? If not, what is the cheapest version of that comparison you could stand up this quarter?
- When something is flagged as unfair, what happens next in your process — does it get pulled, or does it get a ticket?

## See also

[[never-penalise-what-you-are-not-measuring]] · [[strip-every-demand-you-are-not-measuring]] · [[../duo-experimentation/SKILL]]
