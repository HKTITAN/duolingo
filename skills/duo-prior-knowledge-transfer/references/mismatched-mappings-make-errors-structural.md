---
name: duo-prior-knowledge-transfer-mismatched-mappings-make-errors-structural
summary: When your model maps many-to-one onto the one users already have, their errors are in the mapping, not in them — so enumerate and name them.
metadata:
  internal: true
---

# Mismatched Mappings Make Errors Structural

## Concept

When your system splits a distinction the user's prior system merged, or merges one it split, the resulting errors are structural. If their old model collapsed a difference yours makes, they will keep collapsing it; if it split what yours merges, they will keep guessing which one applies. This is not carelessness and it is not random. The default that fires is deterministic, so the errors are too: every user arriving from source X makes roughly the same small set of mistakes. That makes them cheap to anticipate and expensive to ignore. Naming the mismatch out loud converts an unexplained recurring failure into a bounded, expected one — which is what stops the user concluding they are simply bad at your product.

## What Duolingo does

Source: blog.duolingo.com/prepositions-across-languages (Duolingo blog, 2025-04-01; accessed 2026-09-22)

- Duolingo maps, across **six languages**, which ones merge "to" and "at" and which split them: French, Italian and Greek merge; English, German, Spanish and Portuguese split. It then states the learner's position from each side — "If your language uses the same preposition in both contexts, you'll be surprised to have two different ones… And if your language uses two different prepositions, it's easy to forget which one to use."
- It closes by telling the learner the errors are expected: "remember that your mistakes are normal and they make sense." The attribution is moved from the person to the mapping.
- **Explain My Answer** personalizes feedback on two axes at once — it "takes into account the error you made and what about the pattern or rule can be challenging for learners like you." One axis alone yields either a generic rule or a bare correction. The worked case tailors grammatical-gender explanations specifically for speakers whose first system has no grammatical gender, and shows contrasting correct examples (*El niño y sus padres* / *La niña y sus padres*) beside the fix (blog.duolingo.com/explain-my-answer-now-free (Duolingo blog, 2026-01-01; accessed 2026-09-22)).
- A Duolingo hyperpolyglot catalogues her own persistent errors **by source system rather than by symptom**: Spanish tens come out as "-anta" instead of "-enta" because "-anta" is correct in Italian; she reaches for Italian *stare* to ask where things are because Spanish and Portuguese use *estar* that way. She names the mechanism — "a classic case of language interference" (blog.duolingo.com/5-mistakes-professional-language-learner-still-makes (Duolingo blog, 2024-01-10; accessed 2026-09-22)).
- Tension: some interference never resolves. After **20+ languages over 25 years**, she is still mixing English vowels after **30 years** of work on them — "I now get it right most of the time, but I still don't make these sounds as consistently… and I'm OK with that." Design for graceful handling of the residual errors, not for eliminating them.

## The transferable pattern

- **Cluster your error reports by source system, not by symptom.** Two users making the same-looking mistake for different prior reasons need different fixes, and one cohort's whole error class disappears with a single well-placed sentence.
- **Enumerate the mismatches ahead of the tickets.** For each prior system your users arrive from, write out where yours splits what theirs merged and merges what theirs split. That table is your predicted error list.
- **Personalize corrections on two axes** — what they just did wrong, and what is predictably hard for someone with their background. The correction alone gets re-learned on the next occurrence; the background explanation is what makes it stick.
- **Say the errors are expected.** One sentence telling the user the mistake is normal and structural prevents the far more expensive conclusion that the product is beyond them.
- **Show a correct contrasting case beside the fix**, not just the fix. The boundary is the thing being learned.
- **Accept a residual.** Some imported behaviour survives everything. Handle it gracefully — forgiving parsing, an undo, a confirm on the one destructive case — instead of budgeting for zero.

## Apply to your product

- Pick your top recurring user error. Does it split cleanly by which tool the user came from? If you cannot tell, you are not capturing prior system at signup.
- Where does your model split something a competitor's merged? What does your product currently say to a user who guesses wrong — is it a correction, or an explanation of why they guessed that?
- Which residual errors will never go away, and does your product handle them gracefully or punish them?

## See also

[[write-the-path-for-their-source-system]] · [[interference-clusters-among-near-neighbours]] · [[../duo-voice/SKILL]]
