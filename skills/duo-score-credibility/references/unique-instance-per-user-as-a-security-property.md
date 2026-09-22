---
name: duo-score-credibility-unique-instance-per-user-as-a-security-property
summary: Per-user instances cap a leak's blast radius at one person; anonymous recorded review and hired outside attackers keep the rest honest.
metadata:
  internal: true
---

# Unique Instance Per User As A Security Property

## Concept

When everyone receives identical content, a single disclosure invalidates the whole population's results. Assembling a distinct instance for each person is not personalization — it is blast-radius control. A leaked instance tells an attacker nothing about anyone else's, so a compromise is contained by construction rather than by policy. The same containment logic then applies to the humans who police abuse: remove co-location and identity linkage between reviewer and reviewed, record the session so judgement becomes reviewable evidence, and isolate each case so one bad actor cannot taint anyone else's outcome. And because the payoff to defeating you rises with every person you let in, you pay outsiders to break in on a schedule.

## What Duolingo does

- Each Duolingo English Test form is uniquely assembled for the individual taker, so leaked items cannot be shared usefully — unlike a paper exam where one leak can cancel scores for an entire session. Supervision is one session at a time rather than group invigilation.
- Source: blog.duolingo.com/digital-sat-future-of-testing (Duolingo blog, 2022-01-28; accessed 2026-09-22)
- Live proctoring was replaced by "proctoring plus": every session is recorded via computer, microphone, keyboard and mouse, then reviewed asynchronously by multiple trained proctors who are anonymous both to the test taker and to each other, with AI assistance. Each session is discrete.
- **Hundreds of proctors globally**, split into **3 tiers** by expertise — tier 1 for ID verification and behavioural flags, tier 2 applied-ESL professionals reviewing the interview portion, tier 3 senior experts on the most complex cases. Every tier completes **several weeks of training with 1:1 senior mentorship** before reviewing independently.
- Source: blog.duolingo.com/what-is-online-proctoring (Duolingo blog, 2022-07-21; accessed 2026-09-22)
- In 2021 Duolingo hired highly trained outside experts to break into its own systems in order to expose and eradicate weaknesses, and published that it had done so — in the same year the test was taken in **over 12,000 cities** and **over 10,000 fee waivers** were offered across **70+ countries**. Access and attack surface grew together, so the audit was framed as a recurring cost of that growth.
- Source: blog.duolingo.com/how-we-improved-the-duolingo-english-test-in-2021 (Duolingo blog, 2021-12-22; accessed 2026-09-22)

## The transferable pattern

- **Generate per-user instances wherever a shared artifact would be the single point of failure.** Ask what one disclosure costs you: the population, or one account. Containment by construction survives staff turnover and policy drift; secrecy does not.
- **Never let a reviewer and the reviewed be co-located or mutually identifiable.** Proximity creates both collusion opportunity and coercion risk, and identity linkage invites retaliation in either direction.
- **Record, then review asynchronously.** A recording converts one reviewer's unverifiable memory into evidence several independent reviewers can re-examine, which is the only way a disputed judgement can be appealed rather than merely re-asserted.
- **Tier your reviewers and pay for the training.** Routine verification and hard judgement calls are different jobs; running them through one undifferentiated queue means either over-paying for the easy cases or under-qualifying the hard ones.
- **Buy an outside attack on a cadence, and say publicly that you did.** Internal teams cannot find the holes they designed around, and the disclosure is itself part of the credibility you are selling.
- Cost to accept: this is a permanent operating line item, not a launch task, and it scales with reach. Budget it as such or it quietly degrades into a compliance checkbox.

## Apply to your product

- If one user's session content or evaluation artifact leaked publicly tomorrow, how many other users' results would you have to void?
- Who reviews flagged cases in your product, can the reviewed person identify them, and is there a recording that a second reviewer could independently re-judge?
- When did an outsider last attempt to defeat your verification, and what is the trigger — a date, a user-count threshold — for the next attempt?

## See also

[[a-large-item-bank-makes-leakage-structurally-irrelevant]] · [[design-so-cramming-cannot-move-the-score]] · [[../duo-inclusive-access/SKILL]]
