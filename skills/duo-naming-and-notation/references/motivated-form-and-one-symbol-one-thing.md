---
name: duo-naming-and-notation-motivated-form-and-one-symbol-one-thing
summary: Make each element's form encode what it does, and hold one symbol to one meaning — a derivable element survives forgetting, an ambiguous one is re-resolved by every reader forever.
metadata:
  internal: true
---

# Motivated Form and One Symbol, One Thing

## Concept

Two design rules do most of the work in any notation you invent.

**Motivated form:** the shape of an element should encode what it does. An arbitrary mapping is a fact each user must store and rehearse separately; a motivated one is a fact they can reconstruct from first principles. The motivated system therefore survives forgetting, which is the normal state of a user who touches your system once a month.

**One symbol, one thing:** each distinct referent gets exactly one symbol, and each symbol means exactly one thing. Ambiguity in a shared notation removes no work — it moves work. The designer saves one decision; every reader downstream pays a disambiguation step, forever, and some fraction of them resolve it wrongly.

## What Duolingo does

- Duolingo's Hangeul explainer surfaces the design decisions rather than just the characters: **24 letters**, each making **exactly one sound** (contrast English "a" in *father* / *about* / *age*), and consonant shapes drawn to mimic the tongue's position — ㄱ is the shape the tongue makes for the "g" sound. The motive is stated: King Sejong commissioned it in the 1400s because the existing characters were hard to learn and "didn't even match up with how people actually spoke," explicitly so ordinary people could file claims, write letters and keep records. Published **1446** (*Hunminjeongeum*); popularly claimed learnable in a day; marked on **Hangeul Day, Oct 9**. Source: blog.duolingo.com/hangeul-fun-facts (Duolingo blog, 2022-05-26; accessed 2026-09-22)
- The one-to-one rule has its own worked example in the IPA. Existing writing systems use one letter for several sounds (English *u* in rule/put/cut) and several letters for one sound (ea/ee/ey/i all as /i/), so the IPA assigns a distinct symbol to each distinct sound and vice versa — and marks its own symbols with slashes so a reader always knows which system they are in. The chart holds **107 consonants and vowels**; US English uses about **44** of them, Spanish about **24**. Introduced in the late 1800s. Source: blog.duolingo.com/how-is-the-international-phonetic-alphabet-used (Duolingo blog, 2026-07-23; accessed 2026-09-22)
- **The tension, and it is the important part:** full disambiguation is not always worth it. English deliberately writes the two different "p" sounds in *pan* and *span* with one letter, because splitting them "would be more confusing for English speakers" who never need the distinction. Precision a user does not need is cost without benefit.
- **A second tension:** the Hangeul post concedes the one-sound rule has acquired exceptions and defers them ("we'll save those for another time"). Even the cleanest designed notation accretes special cases over five centuries of use. Design for that, don't assume you have escaped it.

## The transferable pattern

Applies to status icons, log levels, event names, API error codes, chart encodings, keyboard shortcuts, badge colours — anything where a compact token stands for a concept.

1. **Prefer a derivable form over a memorable one.** If severity is encoded by a shape that gets sharper as severity rises, a user who has forgotten the legend can still rank two items. If it is encoded by arbitrary colour, they cannot.
2. **Audit for overloading before you audit for count.** A set of 40 one-meaning tokens is cheaper to live with than 12 tokens where 4 are overloaded. Count is not the cost; resolution is.
3. **Apply the one-to-one rule only to distinctions your users act on.** Splitting a token in two is only a win if the two halves lead to different behaviour. Otherwise you have exported precision that nobody spends.
4. **Mark which system a token belongs to.** The IPA's slashes exist so a reader never mistakes a notation symbol for an ordinary character. Namespacing, sigils and prefixes do the same job — they stop your tokens being read under the wrong convention.
5. **Schedule the exception review.** Assume your set will drift; decide now who prunes it and how often.

## Apply to your product

- Pick the three tokens in your system a new user gets wrong most often. Is each one overloaded, or is each one simply arbitrary? Those are different fixes.
- Which of your symbols could a user reconstruct from its shape alone, having forgotten the legend? If the answer is none, your legend is load-bearing and it is not in the room when they need it.
- Where are you drawing a distinction your users never act on, and what would collapsing it buy?

## See also

[[redesign-the-notation-dont-scale-the-training]] · [[split-one-overloaded-primitive-into-named-senses]] · [[your-symbol-set-is-not-a-shared-language]]
