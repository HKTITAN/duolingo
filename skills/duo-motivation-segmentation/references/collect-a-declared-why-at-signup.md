---
name: duo-motivation-segmentation-collect-a-declared-why-at-signup
summary: Telemetry tells you what changed; a declared motive collected at signup is the only field that tells you why — and it has known failure modes.
metadata:
  internal: true
---

# Collect a Declared Why at Signup

## Concept

Usage counts are ambiguous. The same rise in a metric can mean obligation, curiosity, or fandom — three populations that look identical in behaviour and need three different products. No amount of event instrumentation reconstructs intent, because intent is not a behaviour; it is the reason behind one. A single self-reported field, asked once at signup and stored as a first-class dimension alongside plan, geography, and cohort, converts a correlation into an explanation you can act on and defend in a roadmap argument.

## What Duolingo does

Duolingo asks new learners to pick a primary reason and then uses that field everywhere — to explain divergences between populations that behave alike.

- In its 2024 report: a third of South Koreans studied English to connect with people, with education second at 23%; connecting with people was also the top U.S. reason at 35%. 32% of Japanese learners in China and 29% of Korean learners in Japan chose "just for fun." Travel was the top reason (22%) for Argentinians studying Portuguese. Earlier cuts: over 18% of new Japanese learners cited culture in 2021 against 8% of English, 9% of Spanish, and 10% of French learners.
  Source: blog.duolingo.com/2024-duolingo-language-report (Duolingo blog, 2024-12-02; accessed 2026-09-22)
- The same product, segmented by declared motive, produces sharply different profiles: 26% of new Japanese learners say "just for fun," while English learners cite school and Spanish learners cite connecting with people. 86% of Japanese learners are under 30 and 70% are 13–22. Japanese was #5 globally, #4 in the U.S., #2 in China, #4 in Japan, across 17M+ learners in two courses.
  Source: blog.duolingo.com/who-studies-japanese-on-duolingo (Duolingo blog, 2023-04-25; accessed 2026-09-22)

**Tensions.** Duolingo's own reports flag the field as self-reported, and two other posts show exactly how self-report breaks. First, low-status labels get declined: speakers of Dundonian Scots "behave just like bilinguals" on switch-cost measures but "do not often consider themselves as anything other than monolingual speakers of English," so any segmentation built on the label misses a population your instrumentation would detect — blog.duolingo.com/languages-vs-dialects-in-your-brain (Duolingo blog, 2022-09-05; accessed 2026-09-22). Second, users report group associations as properties of the artifact: the meme mocking German "Schmetterling" is an attitude aimed at German speakers, not at the sounds — every phoneme in it already exists in English — blog.duolingo.com/butterfly-in-german (Duolingo blog, 2023-04-20; accessed 2026-09-22).

## The transferable pattern

Ask one question at signup — why are you here — and treat the answer as a stored dimension, not an onboarding formality you discard.

1. **Keep the list short and mutually exclusive.** Four or five options people recognise instantly. A long list turns the question into a survey and depresses completion.
2. **Join it to everything.** Retention, conversion, feature adoption, support volume. The value is not the distribution; it is the cross-tab.
3. **Hold it loosely.** A declared reason is a claim about identity, and claims about identity are edited for status. Where the label carries prestige or stigma, the declared mix will diverge from the behavioural mix — and the gap itself is a finding.
4. **Never treat a reported judgment of your product as a property of your product.** "It feels cheap" is often a report about who the user thinks uses it. Re-test the same thing stripped of its group cue before you redesign it.

## Apply to your product

- If you had to explain last quarter's retention change to your board in one sentence, could you say why, or only what moved?
- What single question could you add to signup that would still be worth joining against usage two years from now?
- Which of your declared segments carries status, and would you notice if people were under-reporting into it?

## See also

[[largest-segment-is-not-most-engaged]] · [[size-of-other-is-a-taxonomy-diagnostic]] · [[../duo-measurement-validity/SKILL]]
