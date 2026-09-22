# AGENTS.md

Guidance for AI coding agents working in this repository. Format: [agents.md](https://agents.md).

## What this repo is

A library of [Agent Skills](https://agentskills.io/specification) that extract Duolingo's public playbook — the [Duolingo Handbook](https://handbook.duolingo.com) and 750 English posts from the [Duolingo Blog](https://blog.duolingo.com/archive/) — into reusable thinking tools for **anyone** building a brand, product, system, or culture.

This is not "skills about Duolingo." Duolingo is the case study and source. The user's product is the target. Every node ends with an "Apply to your product" section.

This repo contains **only Markdown** — no source code to compile, no runtime to ship. The deliverable is the skill graph itself.

## Project layout

```
.
├── AGENTS.md                       # this file
├── README.md                       # human-facing intro + install
├── LICENSE                         # MIT
├── .gitignore
├── .markdownlint.jsonc
└── skills/
    └── <skill-name>/
        ├── SKILL.md                # Map of Content, spec-compliant frontmatter
        └── references/             # spec-standard subdirectory for atomic nodes
            └── *.md                # one concept per file, with [[wikilinks]]
```

The closest `AGENTS.md` to the file you're editing wins; only this top-level one exists today.

## The skills

44 skills plus a router. `skills/duolingo/` is the **router** — `/duolingo` — and every
other skill is a leaf it dispatches to. Run `python scripts/validate.py` to see the current
count; the router is CI-checked to reach every leaf, and to name no leaf that doesn't exist.

The leaves are grouped into eight families, defined in
`skills/duolingo/references/map.md` (generated from what is on disk):

| Family | Covers |
|---|---|
| They stop coming back | retention, streaks, return triggers, perceived progress, attachment |
| They are here but flat | gamification, learner motivation |
| The product has to teach them something | memory and decay, progression, rules, difficulty, prior knowledge, attention, efficacy |
| The words and the face | voice, characters, naming, design rationale, inclusive access |
| Deciding and measuring | product, metrics, score credibility, adoption, monetization, category entry, growth model, experimentation |
| Reaching people | growth, localization, data reports, timely publishing, segmentation, validity, expert content |
| Building it | backend, mobile, reliability, infra cost, ML, agent platform, LLM features, AI strategy |
| The team | culture |

**UI craft is deliberately out of scope for the whole pack.** Easing curves, contrast ratios,
token values and component props route out to
[design-engineering](https://github.com/AgentsORG/design-engineering) via
`skills/duolingo/references/design-handoff.md`. This pack owns *why* an interface should
behave a certain way; it must never invent a token value or an easing curve.

### Adding a skill

A new skill needs enough evidence to stand up: roughly **13+ extracted claims, at least 4 of
them load-bearing**, which supports 6-13 nodes. Below that bar it belongs as nodes on an
existing skill, not as a skill of its own. Padding a thin skill to look substantial is the
failure this bar exists to prevent.

Every new skill must also be added to a family in `skills/duolingo/SKILL.md` — CI fails if a
skill is unreachable from the router.

## Authoring rules

When adding or editing a skill, follow these rules — CI enforces the spec ones.

### `SKILL.md` frontmatter (Agent Skills spec)

- `name` (required) — lowercase letters, digits, hyphens; ≤ 64 chars; **must match the parent directory name**; no leading/trailing/consecutive hyphens.
- `description` (required) — ≤ 1024 chars, non-empty, describes *what* the skill does *and when* to use it. Include trigger phrases users would actually say.
- `license` — keep `MIT` unless deliberately changing.
- `metadata.author`, `metadata.version`, `metadata.graph: true` — local convention.

### Skill graph structure (local convention)

Each skill is a **graph**, not a monolithic file. Inspired by [Akshay Pachaar's "Skill Graphs > SKILL.md"](https://x.com/akshay_pachaar/status/2024848778415755327).

- `SKILL.md` is a **Map of Content**: short descriptions plus `[[wikilinks]]`. Don't dump prose here.
- `references/*.md` files are **atomic concepts** — one complete thought per file, ≤ ~60 lines. Add YAML frontmatter (`name`, `summary`, `metadata.internal: true`) so the skills.sh CLI doesn't surface them as separate skills.
- Cross-skill links use `[[../<other-skill>/references/<node>]]`.
- Keep `SKILL.md` under 500 lines per the spec; aim for under 100 in this repo.

### Node body contract (this repo's invariant)

Every reference node delivers four sections, in this order:

1. **Concept** — one paragraph, the idea in plain English.
2. **What Duolingo does** — the actual move, with the real numbers, and a dated citation.
3. **The transferable pattern** — the rule, separated from Duolingo specifics.
4. **Apply to your product** — 2–3 prompts the reader can answer about their own thing.

If a node only has #1 and #2, it's a content dump, not a skill. Reject in review.

### Self-containment (non-negotiable)

**A node must be fully useful with no network access.** Never write "see the full post at
blog.duolingo.com/x" or otherwise defer the substance to the live site. Sources rot:
`design.duolingo.com` already 301-redirects to a four-post blog hub, which silently turned
every citation pointing at it into a dead end.

So:

- **Inline the substance.** The figure, the mechanism, the tradeoff, the reason it worked —
  in the node. The URL is provenance, not a pointer to go read.
- **Keep the numbers.** `+0.38% relative DAU`, `400 gems`, `two freezes`, `weekend DAU falls
  5–10%`. Numbers are the part an agent cannot invent and the part that makes a claim
  checkable. A node that drops them to stay short has thrown away its evidence.
- **Stamp the citation with a date**, so a future reader knows when it was true:

  ```text
  Source: blog.duolingo.com/friend-streak (Duolingo blog, 2024-08-05; accessed 2026-09-22)
  ```

  `python scripts/stamp_citations.py --write` applies this format mechanically.

- **Never invent a URL.** Every cited blog slug must exist in `scripts/sources.json`, the
  bibliography of all 842 crawled English posts. CI fails the build otherwise — a
  plausible-but-wrong citation is worse than none, because it survives review.
- **Mark retired systems.** Duolingo has replaced hearts with energy and the tree with the
  path. A node presenting a retired system as current is a liability; say what changed.

### Wikilink conventions

- `[[references/foo]]` — same-skill link.
- `[[../duo-voice/references/foo]]` — cross-skill link.
- `[[../duo-voice/SKILL]]` — link to a sibling skill's MoC.
- `[[references/foo|display text]]` — alias form when the target slug isn't ideal prose.

Don't introduce a new wikilink target without creating the corresponding file.

## Adding a new skill — the procedure

Clear the evidence bar in "Adding a skill" above first, then:

1. Create `skills/<name>/SKILL.md` with valid frontmatter (`name` matching the directory).
2. Add `skills/<name>/references/` with at least six nodes.
3. Add a row for it to the right family table in `skills/duolingo/SKILL.md`, with a real
   phrase a user would type — not a topic label. CI fails if the router can't reach it.
4. Cross-link it from at least one sibling skill's MoC.
5. Regenerate the README (it is generated from what is on disk, never hand-edited).

## Adding a new node to an existing skill

1. Create `skills/<skill>/references/<topic>.md` with frontmatter (`name`, `summary`, `metadata.internal: true`).
2. Add a `[[references/<topic>]]` line to the skill's `SKILL.md` MoC under the right section.
3. Add inbound links from at least one related node so it's discoverable through traversal.

## Validation

Run the local validator before opening a PR. CI runs the same script on every PR and push to `main`.

```bash
python scripts/validate.py
```

```bash
pip install pyyaml
python scripts/validate.py
python scripts/stamp_citations.py          # report; --write to apply
```

The validator checks:

- Every `SKILL.md` has spec-compliant frontmatter, parsed with a **real YAML parser**
  (`name` matches dir, `description` ≤ 1024 chars, `compatibility` ≤ 500, no top-level
  `version`/`homepage`/`author` — those belong under `metadata`).
- Every `references/*.md` has `name`, `summary`, and `metadata.internal: true` as an
  **unquoted boolean** — the skills CLI tests `=== true`, so the string `"true"` silently
  fails to hide the node.
- Every wikilink `[[...]]` resolves (code-span wikilinks in prose are ignored — which also
  means a backticked `` `[[link]]` `` is NOT part of the graph).
- Every concept node has the four body sections **and** cites a duolingo.com source.
- Every cited blog slug exists in `scripts/sources.json`. A fabricated or mistyped URL
  fails the build.
- No node defers substance to the live site ("see the full post at…").
- No orphan nodes — everything is reachable from a `SKILL.md` by traversal.
- **The router reaches every skill**, and names no skill that doesn't exist.

CI workflow lives at `.github/workflows/validate.yml`.

## Style

- Use em-dash `—` (U+2014), not `--`.
- Don't add emojis to skill content unless the user asked.
- Code fences must specify a language.
- Keep node titles imperative or noun-phrase, not full sentences.
- One blank line between sections; no trailing whitespace.
- Cite sources concretely. "The Duolingo blog" is not a citation; `blog.duolingo.com/streak-society` is.
- Don't reproduce Duolingo brand assets, design tokens, or copy verbatim — describe the *pattern*. This makes the skills portable to non-language-learning products and avoids IP issues.

## Things NOT to do

- **Don't** add `nodes/` — the spec-standard directory is `references/`.
- **Don't** create hidden auto-generated files; everything is hand-authored.
- **Don't** rewrite the skill-graph structure into single monolithic SKILL.md files — the graph layout is intentional.
- **Don't** introduce a build step or `package.json` — this repo is pure Markdown by design.
- **Don't** ship a node without an "Apply to your product" section. The whole point is utility, not trivia.
- **Don't** treat Duolingo's choices as gospel. Where the handbook acknowledges tension (e.g. monetization vs. retention), the node should too.

## Commit / PR conventions

- Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`.
- One skill / one concern per PR. Cross-skill renames are fine in a single PR.
- PR description should mention which skills were touched and link to any external sources cited.

## License

MIT. By contributing, you agree your contributions are MIT-licensed.
