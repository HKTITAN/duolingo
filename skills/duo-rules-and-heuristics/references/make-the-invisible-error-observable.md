---
name: duo-rules-and-heuristics-make-the-invisible-error-observable
summary: Users cannot correct an error they cannot perceive — convert the imperceptible signal into a visible one, and have someone name one focus per review.
metadata:
  internal: true
---

# Make the Invisible Error Observable

## Concept

Some mistakes cannot be fixed by explanation, because the user has no way to tell whether they just made one. Two mechanisms produce this. First, the signal itself is below the threshold of perception. Second, production and self-monitoring compete for the same attention, so while someone is performing, working memory is fully occupied producing the output and errors go unregistered. Both have the same remedy shape: convert the imperceptible into something the user can sense, or separate production from evaluation in time. And both come with the same catch — an instrument alone does not produce change, because the gaps that caused the error also govern what the user notices in playback.

## What Duolingo does

- To stop English speakers aspirating p/t/k in Spanish and French, Duolingo has learners **hold a tissue or hand in front of their mouth** and compare "pan" (puff), "ban" (no puff) and "span" (no puff), then practise target words until the tissue stops moving. The timing difference that produces the puff is **under 100 milliseconds** between larynx vibration and the mouth sound — imperceptible to the person producing it, obvious once it moves paper. Source: blog.duolingo.com/spanish-english-pronunciation-trick (Duolingo blog, 2022-09-20; accessed 2026-09-22)
- Duolingo calls recording yourself "one of the most powerful tools for improving pronunciation" — and immediately qualifies it: "you won't always be the best judge of your own pronunciation," so a trusted expert should point out **one key sound to focus on at a time**. Source: blog.duolingo.com/improve-pronunciation-in-new-language-tips (Duolingo blog, 2025-04-09; accessed 2026-09-22)
- A learning scientist and hyperpolyglot (**21 languages studied**) gives the full protocol: record monologues, phone calls and conversations with consent, review afterwards to find where you got stuck or failed to understand, and learn one specific fix for next time. Source: blog.duolingo.com/language-tips-from-a-hyperpolyglot (Duolingo blog, 2023-08-30; accessed 2026-09-22)
- The same attention economics govern review. Intermediate chess players are told to run games through an engine and focus on **a couple of the biggest mistakes per game** — specifically the largest shifts in the engine's evaluation, the moments where one side went from winning to losing — and to have the engine play out its recommendation for comparison. Source: blog.duolingo.com/how-to-get-better-at-chess (Duolingo blog, 2026-03-24; accessed 2026-09-22)

**Tension.** The instrument is explicitly insufficient on its own. Self-review needs an external party to set the focus, which is the expensive part and the part most products skip — shipping the recording feature and calling it a feedback loop. Duolingo also scopes the fix rather than chasing perfection: correct the habit only as far as it improves communication.

## The transferable pattern

When users repeatedly do something wrong and your explanation has not helped, ask whether they can perceive the thing at all. If they cannot, no wording will work and the job is instrumentation, not copy.

**Make the signal sensible.** Find the cheapest external indicator that moves when the behaviour happens. Cheap and physical beats accurate and abstract — the value is in the immediacy of the feedback loop, not the fidelity of the measurement.

**Separate doing from judging.** Give users a record of their own work — a replay, a diff, a log, a session recording — so they can spend full attention on diagnosis while the specific moment of failure is still concrete. During execution that attention simply was not available.

**Then rank, and set the focus.** Exhaustive review exhausts the reviewer and flattens signal: small errors vastly outnumber decisive ones. Rank moments by magnitude of state change, review the two or three biggest, and let the user compare their choice against the recommended one. Have someone name **one** thing to work on per review — that constraint is what turns a recording into a change in behaviour, and it is the part that costs real human time.

## Apply to your product

- Which user error is invisible to the person making it? What is the cheapest indicator that would make it visible?
- Do your users have any way to review their own past work, or only to do more of it?
- If you already have replay or logs, does anything in the product rank moments by importance and name one thing to fix — or does it just hand over everything that happened?

## See also

[[mistakes-are-the-signal-not-the-defect]] · [[a-second-representation-does-what-more-practice-cannot]] · [[explanation-lands-at-the-moment-of-the-error]]
