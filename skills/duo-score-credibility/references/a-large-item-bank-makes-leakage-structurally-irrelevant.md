---
name: duo-score-credibility-a-large-item-bank-makes-leakage-structurally-irrelevant
summary: A big randomized item bank shortens the assessment and kills leakage as a threat, which is what lets you give calibrated practice away free.
metadata:
  internal: true
---

# A Large Item Bank Makes Leakage Structurally Irrelevant

## Concept

A small fixed set of items has to be guarded, because one disclosure devalues every result derived from it. Guarding it means rationing access: no free practice, no unlimited retakes, a prep industry in the gap. A large randomized bank inverts that. Once no two people see the same sequence, a leaked set is worth almost nothing to the next person, and the reason to ration disappears. The security investment turns into a distribution advantage — you can hand out unlimited free practice. But the practice has to be calibrated to the real thing's output, not just its look, or you have replaced one anxiety with a false confidence.

## What Duolingo does

- The Duolingo English Test draws from an item bank of **over 10,000 questions** and adapts difficulty to each answer, so the certified test finishes in **60 minutes or less** where traditional exams run multiple hours.
- The same adaptivity is what makes the practice test free and takeable **as many times as you want** without people ever repeating questions — rationing would buy nothing.
- Duolingo then aligned the practice test's scoring algorithm more closely with the certified test so it returns a **narrower and more precise estimated score range**, and gave it the same question types and the same adaptive experience, on phone, tablet and desktop.
- Source: blog.duolingo.com/3-ways-we-improved-the-det-practice-test (Duolingo blog, 2023-10-16; accessed 2026-09-22)
- Alongside the free unlimited practice test sit a published official guide covering question types, scoring and the test experience, plus video walkthroughs, while the certified test stays **$49**.
- Source: blog.duolingo.com/duolingo-english-test-readiness (Duolingo blog, 2021-10-14; accessed 2026-09-22)
- Tension: Duolingo is explicit that the practice test cannot raise your score — there is no trick or class that moves it, only real proficiency. The preview is framed as format familiarization and deliberately not as coaching, which means it removes anxiety without promising an advantage it cannot deliver.

## The transferable pattern

- **Size the content pool as a security parameter.** Ask how many distinct instances the pool can generate, not how well you can keep it secret. Secrecy is a policy you have to enforce forever; scale is a property you buy once.
- **A pool big enough to randomize pays twice.** It removes leakage as a threat, and it lets you select adaptively, which shortens the session. The same investment funds both.
- **When leakage stops mattering, stop rationing.** Unlimited free practice at the format costs you almost nothing per attempt and removes a variance source — format unfamiliarity — that was corrupting your measurement and penalizing whoever could not afford preparation.
- **Calibrate the preview to the real output, not the real skin.** People commit time, money or a high-stakes attempt on the strength of a preview result. A preview scored more loosely than the real system manufactures confidence, and the gap gets discovered at the most expensive possible moment.
- **Say what the preview is for.** "This shows you the format" and "this will improve your result" are different promises. Claiming the second when you only built the first is how a free tier becomes a credibility liability.

## Apply to your product

- How many genuinely distinct instances can your content pool generate today, and what happens to every existing result if one instance becomes public?
- If leakage stopped mattering tomorrow, what would you stop charging for or stop rate-limiting — and would giving it away widen your funnel more than the fee it replaces?
- Does your free or trial tier return the same verdict the paid system would, and how would you know if it had drifted looser?

## See also

[[unique-instance-per-user-as-a-security-property]] · [[design-so-cramming-cannot-move-the-score]] · [[../duo-freemium-monetization/SKILL]]
