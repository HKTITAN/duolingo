---
name: duo-experimentation-unmeasurable-wins
summary: Some changes cannot be A/B tested by construction — decide the second evidence channel in advance, or the roadmap drifts toward whatever is easy to measure.
metadata:
  internal: true
---

# Unmeasurable Wins

## Concept

An experiment needs two concurrent populations differing only in the treatment. Some changes make that split impossible by construction — the treatment is applied at install time, below the application layer, or it is a diffuse emotional effect that will never clear a significance bar on a single launch. A team that only ships what it can measure does not become more rigorous; it quietly reallocates its roadmap toward changes that are easy to instrument. The discipline is not to abandon evidence. It is to decide, before you build, what your second channel of evidence is, and to grant it equal standing when it arrives.

## What Duolingo does

**The change that cannot be split.** Android baseline profiles are compiled at install, so a company that A/B tests almost everything could not run an experiment on them. Duolingo validated the gain with macrobenchmark tests instead — a controlled lab benchmark rather than a production split — and only after the benchmarking library itself had to be fixed first. Their stated cost, published plainly: this makes it difficult to identify how much of the improvement in their metrics comes from baseline profiles. They never fully attributed the production gain. Source: blog.duolingo.com/slashed-android-startup-time-baseline-profiles (Duolingo blog, 2025-05-02; accessed 2026-09-22)

**The change whose value is diffuse.** For the streak milestone redesign, Duolingo states outright that some wins are hard to measure quantitatively, and counts the launch a success on two channels at once: early iOS and Android metrics showing more people keeping streaks alive, *plus* overwhelmingly positive reception across Reddit, Twitter and other social media. Source: blog.duolingo.com/streak-milestone-design-animation (Duolingo blog, 2022-01-21; accessed 2026-09-22)

Tension worth preserving: this is a live argument inside Duolingo's own experimentation culture, not a reconciliation. The second post is arguing against its own organization's default. Qualitative reception is also the easiest evidence to abuse — a team that reaches for it whenever the numbers disappoint has not found a second channel, it has found an excuse. The protection is declaring the channel before the result, not after.

## The transferable pattern

1. **Classify before you build.** Is this splittable? Changes below the application layer, applied at install or provisioning time, or affecting every user simultaneously are not.
2. **For unsplittable mechanics, use a controlled benchmark.** A repeatable measurement in a fixed environment. It trades production realism for attribution, and you must say which you gave up.
3. **For diffuse effects, name the qualitative channel and the bar in advance.** Where you will read reception, over what window, and what counts as positive.
4. **Report what you could not attribute.** "Metrics improved and we cannot say how much of it was this" is a legitimate, honest result. Silently claiming the whole delta is not.
5. **Watch the portfolio, not the launch.** If everything shipped last quarter happened to be easy to instrument, measurability has started choosing your roadmap.

## Apply to your product

- What improvements has your team deprioritized because there was no clean way to measure them?
- For work that cannot be split, do you have a repeatable benchmark, or only a before-and-after production chart with everything else moving in it?
- When you claim a launch was a success on qualitative reception, was that channel named before the launch or after the numbers came in flat?

## See also

[[quasi-experiments]] · [[ladder-of-evidence]] · [[ship-and-iterate]] · [[kill-criteria]]
