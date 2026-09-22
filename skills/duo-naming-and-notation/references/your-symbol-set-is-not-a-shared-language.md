---
name: duo-naming-and-notation-your-symbol-set-is-not-a-shared-language
summary: Symbol meaning is set by community of use, not designer intent — a large minority reads any given symbol with a different or opposite valence, so never let one carry consequential meaning alone.
metadata:
  internal: true
---

# Your Symbol Set Is Not a Shared Language

## Concept

Designers ship a symbol believing it has a meaning. It does not. It has a **distribution** of meanings, set by communities of use — region, age, gender, workplace — and the reader has no way to know which convention the sender was using. In a low-stakes channel that produces mild friction. In a confirmation, a status indicator or an alert, it produces confident misreading, and the misreader has no signal that anything went wrong.

The counterweight matters as much as the warning: any medium that strips a channel of meaning grows a substitute whether or not you design one. Remove face, voice and rhythm from communication and the load transfers to whatever is available, which becomes a real grammar with real conventions. So the answer is never "remove the symbols."

## What Duolingo does

- Duolingo partnered with Slack on an **11-country** survey of emoji use and published the disagreements rather than a style guide. The slightly-smiling face means happy to **37%** of US respondents, general positivity to **24%**, and "deep exasperation or mistrust" to **20%**. The loudly-crying face splits **25/25** between tears of joy and crying from being upset. Nail-polish and laughing-face use vary sharply by race and gender.
- Cross-border valence flips outright: money-with-wings reads as **loss** to 27% globally and **59% in Japan**, but as **influx** to 31% globally. The kissing face is romantic for **52% in India** and platonic for **30% in Japan**. **74%** of respondents have had an emoji misunderstanding.
- **The tension, from the same survey, and it is not a footnote:** **71% of Americans** (57% globally) feel a message is incomplete without an emoji, and **two of three** say emoji help them communicate faster and with more nuance and make them feel closer and more bonded. The ambiguity is the price of the nuance, not a defect to design out. Source: blog.duolingo.com/emoji-language-trends (Duolingo blog, 2022-07-13; accessed 2026-09-22)
- Duolingo also analysed emoji as a system that took over the functions of gesture (thumbs-up, shrug), facial expression (smirk, eye-roll), prosody and emphasis, and even punctuation (a repeated raised-hands symbol used as a terminal mark after "Yes") — in written channels that had removed body language and tone. **58%** of surveyed global employees said emoji at work let them communicate more nuance with fewer words; **54%** said it speeds up workplace communication.

## The transferable pattern

1. **Never let a symbol carry consequential meaning alone.** If misreading it changes what the user does — destructive versus safe, approved versus blocked, on versus off — pair it with a word. The symbol can carry scanning speed; the word carries the meaning.
2. **Assume a 20-40% minority reads it differently**, including with opposite valence, and that they will not notice they did. This is not an edge case you can test your way out of with a single-market sample.
3. **Test valence across your actual population, not your team.** Your team shares a convention precisely because it is a community of use. That is the one group whose agreement proves nothing.
4. **Design the substitute channel deliberately.** If you strip tone, hierarchy or emphasis out of a surface, your users will improvise a replacement you cannot interpret and cannot control. A sanctioned, documented set beats an emergent one.
5. **Do not solve ambiguity by deleting expressiveness.** Most users report that the expressive layer makes communication faster, more nuanced and warmer. Stripping it back to plain text removes the misreads and the bonding together, and users will rebuild the layer anyway.

Where the symbol's visual style and personality are the question rather than its meaning, that belongs with the character and iconography work in [[../duo-design/SKILL]] — this node owns what a symbol means, not how it is drawn.

## Apply to your product

- Which symbols in your interface change what a user does? For each, is there a word next to it — and if not, what happens to the 20% who read it the other way?
- Has anyone outside your team, and outside your home market, been asked what your status icons mean, with no legend and no context?
- What tone or emphasis has your product's main surface removed, and what have users invented to replace it? Is that invention something you can read?

## See also

[[motivated-form-and-one-symbol-one-thing]] · [[mark-only-what-deviates-and-force-the-unambiguous-form]] · [[../duo-design/references/accessibility-default]]
