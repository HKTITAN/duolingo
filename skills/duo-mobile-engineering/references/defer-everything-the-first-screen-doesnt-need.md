---
name: duo-mobile-engineering-defer-everything-the-first-screen-doesnt-need
summary: Startup is bounded by the first meaningful screen, not total work — push everything else past first render and turn the fix into a shared utility.
metadata:
  internal: true
---

# Defer Everything the First Screen Doesn't Need

## Concept

Startup is a contended window. Every subsystem initializes at once, so a unit of work placed there costs far more than the identical unit placed thirty seconds later when the cores are idle and nobody is waiting. The budget you are managing is not total work — it is work serialized in front of the user before the screen they came for.

Two failure modes follow. First, third-party SDKs initialize eagerly at launch for features that will not be used for minutes, if ever. Second, "non-blocking" background requests are treated as free; the word describes their relationship to your code, not to the device's finite radio and cores.

And the one-off fix decays. You remove the blocking initializer, and next quarter another team adds the next one, because nothing about the codebase made deferral the easy path.

## What Duolingo does

Source: blog.duolingo.com/android-app-performance (Duolingo blog, 2025-06-11; accessed 2026-09-22)

- Traces showed the **ads library initializing a WebView on the main thread at launch, eating over 1 second** — despite ads only being shown *after* a lesson completes. Deferring it cut **~1.5 seconds from startup**, which Duolingo counted as **20,000 learners a day** saved from quitting before entering the app.
- They then built **`HomeLoadedStartupTask`**, a utility for running startup logic after the home page loads, and made it the standard for all non-critical startup work — so the next engineer gets deferral by default rather than by heroism.
- On session start, non-blocking background requests refreshed leaderboards and quest progress. **Delaying those by 5 seconds** to reduce contention significantly improved session start latency and DAUs — they were competing for the same radio and cores as the requests the user was waiting on.

Source: blog.duolingo.com/unique-engineering-problems (Duolingo blog, 2024-05-15; accessed 2026-09-22)

- Duolingo profiled startup on Perfetto, split the flow into key steps, and deferred **lesson prefetching, ads-SDK initialization, and creation of not-yet-visible UI elements** until after the home screen loaded.
- Combined effect: **Android app startup 40% faster in roughly five months** (January to May 2024).

## The transferable pattern

1. **Enumerate everything that runs before first render.** Not what you think runs — what a trace says runs. Third-party dependencies are the usual offenders because their init cost is invisible in your own source.
2. **For each item ask: does the first screen need this?** If the feature it serves cannot be reached for at least one user action, it does not belong before first render.
3. **Count background work against the budget too.** Fire-and-forget requests issued alongside critical ones contend for the same finite resources. A deliberate few-second delay on the non-critical ones is a real, cheap win.
4. **Codify the fix as a named primitive.** A utility called something like "run after the main view is ready" makes the correct behaviour the path of least resistance. Without it, you will re-fight this every two quarters.

The tradeoff to name: deferral moves cost, it does not delete it. Push too much past first render and you trade a slow launch for a janky first interaction. Measure the second moment as well as the first.

## Apply to your product

- What initializes in your startup path today that serves a feature the user cannot reach in their first ten seconds?
- Which of your background jobs fire at the same moment as the work the user is waiting on, and what happens to the foreground if you delay them by a few seconds?
- Is there a named, discoverable place in your codebase for "do this later"? If not, your next fix will be a one-off that the next engineer undoes.

## See also

[[cold-start-is-a-retention-metric]] · [[measure-from-your-worst-region-and-device]] · [[fix-the-diagnostic-loop-before-the-bug]]
