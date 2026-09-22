---
name: duo-production-reliability-reassurance-is-load-shedding
summary: Telling users during an outage that their earned state is safe is capacity management, not courtesy, because anxious users retry and their retries keep you down.
metadata:
  internal: true
---

# Reassurance is load shedding

## Concept

During an outage, the message you show is usually treated as a communications decision made by whoever owns the status page. It is also a traffic decision. A user who believes something valuable is about to be lost will retry, hard, and keep retrying — reloading, force-quitting, reinstalling, hitting the action from three devices. Those retries are not noise around the incident; in a consumer product at scale they are a meaningful share of the load that is keeping the system down. A credible, specific, in-product promise that the valuable thing is protected removes the reason to retry. Vague reassurance does not, because the user has no way to price it.

## What Duolingo does

Source: blog.duolingo.com/protecting-streaks-from-site-issues (Duolingo blog, 2021-11-01; accessed 2026-09-22)

- When the Big Red Button is active, learners get a **maintenance page that tells them the app is paused** rather than an ambiguous error or a hanging spinner. The failure is legible, which is the first thing that stops frantic retrying.
- The promise behind the message is real and mechanical: BRB logs who was affected and **retroactively applies a streak freeze** for the affected day once systems recover. The reassurance is backed by tooling, not by intent.
- Traffic is **brought back online in controlled subsets** using multiple S3 files rather than reopening to everyone at once — an explicit acknowledgment that a recovering system meets a queue of pent-up demand, not a normal load curve.
- Numbers give the promise its weight: the same tooling has **protected over 2 million streaks** to date, so the claim on the maintenance page is describing a mechanism with a track record rather than an intention.
- Tension: the honesty only works if the mechanism exists. A message claiming state is safe without the repair behind it buys quiet for one incident and costs trust on the next one, when people check and find it was not true.

## The transferable pattern

1. **Treat the outage message as a lever on load, not only on sentiment.** Ask what behavior the current message produces. A spinner produces retries; a bare 500 produces reinstalls.
2. **Name the specific thing people fear losing.** Generic apology text does not reduce anxiety because it does not answer the question the user actually has. "Your progress from today is saved" does.
3. **Only promise what a mechanism enforces.** Write the reassurance copy and the repair path in the same change, so nobody can ship the sentence alone.
4. **Make the failure legible.** An explicit pause tells the user the retry is pointless. An ambiguous timeout tells them the retry might work, which is why they run it forty times.
5. **Plan the return like a second incident.** Everyone who was blocked arrives at once. Return in subsets you can throttle or abort.

## Apply to your product

- What does a user see today when your core action fails, and what does that message make them do in the next sixty seconds?
- What is the one thing your users would be most afraid of losing in an outage, and can you promise it is safe without lying?
- When you recover, does traffic return gradually or all at once? If all at once, what is the plan for the queue that formed while you were down?

## See also

[[repair-earned-state-in-the-incident-tooling]] · [[the-kill-switch-must-fail-open]] · [[../duo-voice/SKILL]]
