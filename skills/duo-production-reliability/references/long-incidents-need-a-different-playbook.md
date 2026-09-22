---
name: duo-production-reliability-long-incidents-need-a-different-playbook
summary: Past roughly one shift, informal incident handling becomes a liability and you need a dedicated commander, explicit decision ownership, a written narrative, and visible task ownership.
metadata:
  internal: true
---

# Long incidents need a different playbook

## Concept

Most incident practice is tuned for the common case: a handful of people, under an hour, resolved by whoever knows the subsystem. That informality is efficient and it does not scale past about one shift. In a long incident, complexity grows faster than the underlying problem — each decision creates second-order effects, information fragments across channels, and the population of responders turns over. The limiting factor stops being technical skill and becomes the cognitive load on whoever is coordinating. Past that threshold you are running a different activity, and it needs a different structure: someone whose only job is coordination, and enough written state that a handover does not reset the investigation.

## What Duolingo does

Source: blog.duolingo.com/incident-management-lessons (Duolingo blog, 2026-03-25; accessed 2026-09-22)

- A Duolingo engineer who volunteers with **Allegheny Mountain Rescue** took a **Managing Lost Person Incidents** course in **Badlands National Park** and mapped its structure onto how Duolingo handles rare, high-impact incidents. Search and rescue has been running multi-day, high-stakes, high-uncertainty operations for far longer than software has.
- The transferred structure: **an incident commander whose only job is coordination** (not debugging), **explicit decision ownership** so no decision is everyone's and therefore nobody's, **a written narrative of what has been tried and why** rather than a scrollback, and **task ownership visible at a glance** so the commander can see progress without asking.
- Also transferred: search and rescue's practice of maintaining **one shared map artifact** that grounds every responder in the same reality. See [[agree-the-shared-artifact-before-the-incident]].
- Tension, and the post is direct about it: **being good at fixing things does not transfer to orchestrating people and uncertainty.** Your strongest debugger is often the wrong incident commander — and putting them in that role costs you twice, because you lose them from the investigation too.
- Worth noting this is an analogy from another discipline rather than a measured result. It is a structure to adopt deliberately, not a benchmark.

## The transferable pattern

1. **Define the threshold that changes the mode.** Pick a duration or an impact level at which informality stops and the structured roles start. Without a stated trigger, nobody escalates, because escalating always feels premature.
2. **Separate coordination from investigation.** The commander is not the best debugger and should not be debugging. Their output is allocation, sequencing, and a current picture.
3. **Make decision ownership explicit and named.** In a long operation the expensive failure is a decision everyone assumed someone else had made.
4. **Keep a narrative, not a transcript.** What has been tried, what was ruled out, and why. A chat log is not a state record; a person joining at hour six cannot read one.
5. **Make ownership visible without asking.** If the coordinator has to ask for status, the coordinator is the bottleneck and every question costs an investigator their context.
6. **Plan handover from the start.** Long means shift changes. If the state lives only in someone's head, your incident restarts every eight hours.

## Apply to your product

- What is your longest incident in the last two years, and what actually broke down in hour four — the technical work, or the coordination around it?
- Who would you name as commander, and is that the same person you would want debugging? If so, you have one person doing two jobs badly.
- If everyone currently on your incident had to hand over right now, what would the next shift read?

## See also

[[agree-the-shared-artifact-before-the-incident]] · [[the-kill-switch-must-fail-open]] · [[../duo-culture/SKILL]]
