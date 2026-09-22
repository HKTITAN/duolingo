---
name: duo-production-reliability-agree-the-shared-artifact-before-the-incident
summary: Decide in advance which single place counts as agreed reality during a major incident, or capable people will quietly start solving different problems.
metadata:
  internal: true
---

# Agree the shared artifact before the incident

## Concept

In a disorienting situation each participant builds their own mental model from whatever partial information reached them, and those models drift apart without anyone noticing. Nobody is wrong and nobody disagrees out loud; they simply answer different questions and their work stops composing. A single shared artifact — one place that everyone accepts as the current picture — is the cheapest known mechanism for keeping those models converged. The critical detail is that it has to be chosen beforehand. Choosing it mid-incident is itself a coordination problem, arriving at the worst possible moment, and what you get instead is three competing documents and an argument about which one is current.

## What Duolingo does

Source: blog.duolingo.com/incident-management-lessons (Duolingo blog, 2026-03-25; accessed 2026-09-22)

- The observation comes from search and rescue, where teams rely on **a shared physical map** as the single grounding artifact. Every searcher marks it, every searcher reads it, and it is unambiguous which one is the map.
- The Duolingo engineer's stated takeaway was to ask what **the equivalent artifact should be during major Duolingo incidents**, and specifically **how intentional the company is about defining it ahead of time**.
- This is framed as an open question rather than a solved practice, which is the honest version — the post does not claim Duolingo has already standardized one.
- The structural point that makes it work: in rescue, the map is both the shared picture and the work assignment surface. Areas searched, areas not searched, and who is where all live in the same object. One artifact, not a status doc plus a task board plus a channel.

## The transferable pattern

1. **Pick the artifact now, while nothing is broken.** Name it in the runbook. "The incident doc, this template, linked in the channel topic" beats any decision made under load.
2. **One artifact, not a family of them.** The moment there are two places, reconciling them becomes someone's job and the drift you were preventing reappears as a merge conflict.
3. **It must hold both the picture and the assignments.** Separating "what we know" from "who is doing what" recreates the split-brain, because people read one and not the other.
4. **Someone owns keeping it current.** An artifact nobody is responsible for updating goes stale in twenty minutes and then actively misleads, which is worse than not having it.
5. **Chat is a transport, not a record.** A channel is a stream of partial views ordered by time. It cannot serve as agreed reality, because there is no current state in it, only history.
6. **Test it on a small incident.** If the artifact is only ever used during rare severe events, it will be unfamiliar exactly when familiarity matters.

## Apply to your product

- If a severe incident started in ten minutes, where would people look for the current picture — and would two of them name different places?
- Does your incident artifact show who is working on what, or only what has happened? If only the latter, how does the coordinator learn about duplicated work?
- Who updates it, and what happens to it when that person hands over at the end of their shift?

## See also

[[long-incidents-need-a-different-playbook]] · [[repair-earned-state-in-the-incident-tooling]] · [[../duo-culture/SKILL]]
