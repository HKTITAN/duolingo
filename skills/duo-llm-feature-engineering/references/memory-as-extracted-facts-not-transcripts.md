---
name: duo-llm-feature-engineering-memory-as-extracted-facts-not-transcripts
summary: Give a long-lived AI experience memory by extracting a compact list of facts after each session and injecting that, never by replaying raw transcripts.
metadata:
  internal: true
---

# Memory as Extracted Facts, Not Transcripts

## Concept

The obvious way to give an AI feature memory across sessions is to keep the transcripts and paste them back in. It is the wrong shape in three ways at once. A transcript **grows without bound**, so cost and latency climb forever. It **dilutes attention** — the current instructions compete with hundreds of lines of old small talk. And it is **unauditable**, because nobody can tell you what the system believes about a user without reading everything.

Extract instead. When a session ends, run one call that asks what is worth remembering, and append the answer to a **persistent list of facts** that gets injected into the next session's system prompt. The list is bounded, readable, and cheap to carry. The extraction step is also where you get to **decide what is worth remembering** — a decision that replaying raw history never lets you make.

## What Duolingo does

Source: blog.duolingo.com/ai-and-video-call (Duolingo blog, 2025-04-22; accessed 2026-09-22)

- After a Video Call with the character Lily ends, Duolingo **shows the transcript to the model and asks what important information was learned about the user**.
- The answer is **appended to a persistent List of Facts**, which is then used in the **next call's system prompt**.
- The transcript itself is not what travels forward between sessions. Within a single session the transcript is passed turn to turn (see [[one-narrow-prompt-per-move]]); across sessions, only the extracted list survives.
- This is one more separate, single-purpose call in a feature built from them — prep, turn generation, memory extraction — each with its own job, consistent with [[isolate-the-high-stakes-generation]].
- **Tension.** Extraction is lossy by construction, and the model decides what is important, so anything it judges unimportant is gone permanently. A fact list also accumulates staleness — a preference stated once is carried as though it were still true, with nothing in the mechanism to expire it.

## The transferable pattern

- **Summarise at the session boundary, not at the next session's start.** The end of a session is when you have the full context and the user is not waiting.
- **Extract into a schema, not into prose.** Typed slots — preference, constraint, stated goal, thing already covered — are filterable, expirable and diff-able. A paragraph of remembered impressions is none of those.
- **Cap the list and decide the eviction rule up front.** Least-recently-confirmed, or a hard item limit, or an age cut. Unbounded memory is the problem you were escaping.
- **Make it inspectable, and ideally editable, by the user.** "Here is what this remembers about you" is both a trust feature and your best debugging tool for wrong behaviour that looks inexplicable.
- **Timestamp every fact.** Something true six months ago and asserted as current today is a specific and embarrassing failure mode.
- **Treat the list as user data with a real lifecycle** — deletable, exportable, and covered by the same retention rules as the rest of your user record, because that is what it is.

## Apply to your product

- What would your AI feature need to remember across sessions for the second session to be better than the first — stated as five or fewer typed fields?
- What is your eviction rule, and what happens to a remembered fact that stops being true?
- Could a user see, correct and delete what your system remembers about them today?

## See also

[[one-narrow-prompt-per-move]] · [[isolate-the-high-stakes-generation]] · [[../duo-ai-agent-platform/SKILL]]
