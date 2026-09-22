---
name: duo-mobile-engineering-fix-the-diagnostic-loop-before-the-bug
summary: When adding one trace point costs a 20-minute rebuild, automating instrumentation changes which problems are findable at all — and build the shared trace viewer before you start optimizing.
metadata:
  internal: true
---

# Fix the Diagnostic Loop Before the Bug

## Concept

A slow observation cycle does more than waste time. It forces you to guess where to look, because each guess is expensive, so you only instrument the places you already suspect — which means you only ever confirm hypotheses you already had. Cheap, blanket instrumentation surfaces the costs nobody predicted, and those are where the large wins live.

The second bottleneck is social. On a performance project, velocity is set by how quickly a team can form and reject hypotheses together. If only the person who captured the trace can interpret it, every idea in the building has to route through one human. Making the evidence legible to many people is an optimization on the project, not a nicety.

Both of these are build-the-tool-first arguments, and both are habitually deferred because the tool is not the deliverable.

## What Duolingo does

Source: blog.duolingo.com/android-app-performance (Duolingo blog, 2025-06-11; accessed 2026-09-22)

- Hand-adding `Trace.beginSection` markers required an app rebuild of **up to 20 minutes per trace point**. At that price, instrumentation is rationed and you only measure what you already suspect.
- Instead they used **bytecode manipulation via an ASM transform plus regex filtering** to automatically trace entire categories of methods — **all ViewModels, Activities, Fragments and Repositories** — with no source changes at all. The implementation was published as a public gist.
- This is what made **200+ performance A/B tests in 2024** affordable; the discoveries in [[defer-everything-the-first-screen-doesnt-need]] came out of traces nobody would have paid 20 minutes each to collect.

Source: blog.duolingo.com/unique-engineering-problems (Duolingo blog, 2024-05-15; accessed 2026-09-22)

- Duolingo built an internal tool, **MethodTrace**, to make Perfetto system traces easier to annotate and interpret — explicitly to **increase experiment velocity** — and credits *looking at traces together* as the reason the team moved fast.

The cost to name: blanket instrumentation is not free at runtime, and a trace that covers everything can bury the signal under volume. Duolingo's regex filtering is the concession — you are choosing categories, not literally everything.

## The transferable pattern

- **Price your observation cycle before you start.** Minutes per hypothesis multiplied by hypotheses is the real budget of an investigation. If that number is large, the first ticket is the tooling ticket.
- **Automate instrumentation at the category level.** Instrument by architectural role — every handler, every repository, every job — rather than by hand at suspected hot spots. You are buying the ability to be surprised.
- **Make the evidence shareable and annotatable.** A raw dump readable by one expert is a single-threaded project. Annotation turns a trace into an artifact a group can argue over.
- **Publish the tooling where you can.** It costs little beyond what you already built, and it attracts fixes from others hitting the same wall.

## Apply to your product

- How long does it take you, today, to add one measurement and see its result? Multiply that by twenty and ask whether you would run a twenty-hypothesis investigation.
- Can anyone on your team read your profiling output, or does every performance question route through one person?
- What class of thing in your codebase — handlers, jobs, queries — could be instrumented wholesale by role instead of one call site at a time?

## See also

[[verify-the-harness-and-route-around-vendors]] · [[treat-the-build-loop-as-a-shipped-feature]] · [[optimize-against-conversion-not-milliseconds]]
