---
name: duo-mobile-engineering-verify-the-harness-and-route-around-vendors
summary: A harness that performs production's steps in a different order returns green for an artifact that is inert in production — file the vendor bug, ship your own workaround anyway.
metadata:
  internal: true
---

# Verify the Harness, Then Route Around Vendors

## Concept

Correctness of a build artifact often depends on the *order* of transformation steps, not merely their presence. A test harness that performs the same steps in a different order validates a different artifact than the one you ship. This failure is silent in the worst way: the test passes, you ship, and the metric simply does not move — which reads as "the optimization didn't help" rather than "the optimization was never present."

The second half is about whose backlog you are sitting in. When a third-party bug blocks you, maintainers triage by breadth of impact. A bug that only affects unusual configurations is *correctly* low-priority for them and blocking for you. Waiting converts your timeline into their roadmap.

## What Duolingo does

Source: blog.duolingo.com/slashed-android-startup-time-baseline-profiles (Duolingo blog, 2025-05-02; accessed 2026-09-22)

- Duolingo **side-loaded baseline profiles for testing, saw great results, shipped — and metrics did not move at all.**
- Google's baseline-profile experts found the profiles were **entirely invalid**. In side-loading, dex files are modified *before* profile conversion; in the real build, *after*. Same steps, different order, inert artifact.
- The same class of bug then **recurred between APK and App Bundle builds** after being fixed for APKs, and **two separate third-party libraries independently invalidated the profiles**. This was not a one-off.
- When one library's maintainers deemed the bug low-priority because it only affected niche setups, Duolingo **added a build step that regenerates the profile from the already-modified dex files** and shipped that while waiting.
- They also note that escalating to the platform vendor's experts early was decisive — without direct vendor support, diagnosis would have taken far longer.

Source: blog.duolingo.com/flipping-duolingo-filling-a-gap-in-support-for-right-to-left-languages (Duolingo blog, 2016-09-13; accessed 2026-09-22)

- Where a platform gap blocked a market they cared about, Duolingo fixed it in the ecosystem and published it: **RtlViewPager, released on GitHub as their first open-source project** — in the same post announcing they were hiring Android developers.

## The transferable pattern

1. **Validate the artifact, not the process.** Before trusting any optimization, confirm that the thing you measured is byte-for-byte the thing that reaches users. If the test path takes a shortcut, the shortcut is where the lie lives.
2. **Suspect your harness first when a shipped change moves nothing.** "No effect" and "not actually applied" look identical in a dashboard, and the second is far more common than teams assume.
3. **Escalate to the vendor early, and workaround in parallel.** The bug report and the workaround are not alternatives. One fixes it for everyone eventually; the other unblocks you this week.
4. **When the gap is in the ecosystem and the gap blocks a market, fix it upstream and publish.** A private patch must be re-merged forever and helps nobody; publishing costs little extra and attracts maintenance from others hitting the same wall.

The tension: every workaround you ship is a piece of infrastructure you now own. A regeneration step bolted onto the build to dodge a library defect is permanent maintenance created by someone else's mistake. Log these, and delete them when the upstream fix lands — otherwise your build grows a layer of archaeology nobody can safely remove.

## Apply to your product

- Is there anything in your pipeline where the test environment assembles the artifact differently from production? Name it, then go check it.
- When one of your optimizations "didn't work," did you confirm it was actually present in the shipped build, or did you accept the null result?
- Which third-party bug are you currently waiting on, and what would an ugly local workaround cost compared to another month of waiting?

## See also

[[fix-the-diagnostic-loop-before-the-bug]] · [[cold-start-is-a-retention-metric]] · [[../duo-experimentation/references/ab-test-structure]]
