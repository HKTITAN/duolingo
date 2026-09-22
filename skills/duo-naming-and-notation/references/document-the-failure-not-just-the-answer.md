---
name: duo-naming-and-notation-document-the-failure-not-just-the-answer
summary: Enumerate what actually happens when the user gets it wrong, attach every shortcut's limit inline, and name the false belief generating the error rather than the correct answer.
metadata:
  internal: true
---

# Document the Failure, Not Just the Answer

## Concept

Three moves, one mechanism: users are reasoning from a model, and documentation that only supplies correct answers leaves the model untouched.

**Name the consequence.** Users default to assuming an unknown failure is catastrophic and respond by not acting at all. Enumerating the actual downside recalibrates the risk; naming the recovery cue turns a feared dead end into a handled path.

**Attach the limit to the shortcut, inline.** A heuristic taught without its boundary gets applied outside it, and the misfire lands on the user, usually in public.

**Correct the generator, not the instance.** A user holding a wrong model regenerates the error in every situation the model covers. Fixing the output patches one case; naming the belief lets them retract it and all its consequences at once.

## What Duolingo does

- The tú/usted guide devotes a whole section to "What if I use the wrong pronoun?" and walks **3 distinct failure modes** — too formal, too informal, and wrong regional variant — giving the recovery signal for each: if they say *"Puedes tutearme"* you may switch to *tú*; if they keep calling you *usted*, switch back. The feared social catastrophe is replaced by three small, cued, recoverable events. Source: blog.duolingo.com/tu-vs-usted (Duolingo blog, 2026-07-09; accessed 2026-09-22)
- The Spain slang guide attaches a warning directly to each entry that flips meaning by context — **4 of 8 entries** carry one: *molar* implies romantic interest when used about a person; *chulo* means cocky and arrogant about people rather than cool; *flipar* can reference drug use; *guiri* can be derogatory depending on intent. The warnings sit **beside the example sentences**, not in a caveats section at the end, because that is where the reader is standing when they decide to use the word. Source: blog.duolingo.com/slang-words-in-spain (Duolingo blog, 2024-05-21; accessed 2026-09-22)
- The object-pronoun guide gives **2 worked error diagnoses** that name the belief, not the fix. *"Lo está lloviendo"* is diagnosed as **"*lo* is not a perfect substitute for 'it'"** — the learner is using a direct-object pronoun as a subject. *"Vi él"* is diagnosed as "we can't trust English word order to know the role of a noun in Spanish." Each retracts a whole class of future errors. Source: blog.duolingo.com/direct-indirect-objects-spanish (Duolingo blog, 2022-04-12; accessed 2026-09-22)
- **The tension:** naming consequences is only de-escalating when the consequences really are small. If a mistake in your system is genuinely expensive or irreversible, enumerating it honestly will — correctly — make users more cautious, and you should treat that as a signal to change the system rather than the copy.

## The transferable pattern

1. **Write a "what if I get this wrong" section for every consequential choice**, and enumerate the failure modes separately. One combined paragraph reads as a general warning; three named modes read as three bounded, survivable events.
2. **Give each failure mode its recovery signal.** The observable cue that tells the user they are in it, and the specific move that gets them out. Without the cue, the enumeration is just a longer list of things to fear.
3. **Put the limit where the shortcut is, never in a footnote.** Physical adjacency does the work. The user reading the shortcut at the moment of use will not scroll to a caveats section, and both of you know it.
4. **Mark only the entries that need it.** If every entry carries a warning, none of them do — the selectivity argument from [[mark-only-what-deviates-and-force-the-unambiguous-form]] applies to hazards too.
5. **Diagnose the belief.** Write "X is not a substitute for Y" rather than "the answer is Z." The first form is testable by the user against cases you never listed; the second is a lookup they must repeat.
6. **If honest consequences frighten people off, fix the system.** Rewriting the copy to sound gentler while the downside stays real is how you get users who trust the docs once.

Where the question is what the interface *says back* in the moment of failure — the tone and wording of the live error — that is copy work; [[../duo-voice/references/error-copy]] owns it. This node owns the reference material that prevents the error and explains the model behind it.

## Apply to your product

- Pick the choice your users hesitate on most. Is the actual downside of getting it wrong documented anywhere — with its recovery path — or are they imagining it?
- Take one shortcut or rule of thumb in your docs. Where is its boundary written, relative to where the shortcut is read?
- Read your last five support answers. Did they give the right answer, or name the wrong belief? How many of those tickets are the same model regenerating?

## See also

[[split-one-overloaded-primitive-into-named-senses]] · [[ship-a-labelled-default-with-named-exceptions]] · [[teach-a-choice-with-a-minimal-contrast]]
