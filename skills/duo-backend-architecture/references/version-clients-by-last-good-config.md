---
name: duo-backend-architecture-version-clients-by-last-good-config
summary: Have the client cache the last config it could parse and the server send data-only partial responses to old clients, so server code never branches on client version.
metadata:
  internal: true
---

# Version Clients By Last Good Config

## Concept

The moment a server sends structure rather than just values, you inherit a compatibility problem: some installed clients are older than the structure you are sending. The obvious answer — branch on client version in server code — is a trap. Those conditionals accumulate without bound and are never deleted, because nobody can prove the last user on an old build is gone. The better answer inverts the direction: let the client cache the last configuration it could successfully parse, and when it cannot parse the current one, have the server omit the structure and send only the values. The compatibility decision is made by the one party that actually knows the answer, and old clients still receive fresh prices, strings and assets — only the layout is stale.

## What Duolingo does

Source: blog.duolingo.com/server-driven-ui (Duolingo blog, 2024-11-08; accessed 2026-09-22)

- Clients **cache the UI configuration** they last rendered successfully.
- When a client cannot parse the current server-driven response, the server sends a **partial response**: the UI config is omitted and only the **data model** is delivered. The client renders its cached layout with fresh data.
- Because the data model carries the per-user values — asset images, localized strings, prices, and the values conditions evaluate against — an out-of-date client is stale in appearance but correct in substance.
- The explicit rule that falls out: **server code never branches on client version**. There is one current config and one fallback path, not a growing ladder of per-release special cases.

Duolingo's linguists supply the matching warning about frozen representations. French spelling was standardized in **1635** and has had roughly **400 years** of sound change since — final consonants stopped being pronounced in the late 17th century, stranding the spellings — which is why so many distinct words now collapse into one written form. English froze in the **late 15th century** and shows the same accumulation. Freezing a representation does not stop the thing it represents from moving; ambiguity grows in proportion to time since the freeze. Their closing note is worth keeping: the drift was not pure cost, since the collisions became the raw material for wordplay (blog.duolingo.com/french-homophones-tiktok (Duolingo blog, 2023-05-11; accessed 2026-09-22)).

## The transferable pattern

1. **Never put a version conditional in shared server code.** It is write-only: additions are cheap, deletions are unprovable, and after two years the branch tree is the spec.
2. **Cache last-known-good on the consumer.** Whatever the consumer rendered successfully once, it can render again. That cached artifact is your compatibility fallback and it costs the producer nothing.
3. **Degrade structure, preserve values.** When the consumer cannot handle the new shape, strip the shape and keep the payload. Stale layout with live numbers is almost always acceptable; live layout with stale numbers almost never is.
4. **Budget for drift at the moment you freeze.** The day you pin a schema, a cached artifact or a wire format, start counting: every later change to the underlying domain adds one more case where two distinct things share one stored form. Plan the disambiguation mechanism then, not when the collisions start hurting.
5. **Expect a permanent long tail.** Old consumers never fully disappear, so design a policy that stays correct forever rather than one that assumes an end date.

## Apply to your product

- Where does your server code currently branch on which client, SDK or API version is calling — and who would be allowed to delete those branches?
- If a consumer of your API could not understand your latest response shape, is there a reduced response that still gives it correct values?
- What representation have you frozen — a cached schema, an enum, an event format — and how much has the underlying domain moved since?

## See also

[[move-the-ui-definition-to-the-server]] · [[predict-only-what-users-dont-care-about]] · [[instrument-the-failure-mode-you-traded-into]]
