# AGENTS.md

Guidance for AI coding agents working in this repository. Format: [agents.md](https://agents.md).

## What this repo is

A library of [Agent Skills](https://agentskills.io/specification) that extract Duolingo's public playbook — the [Duolingo Handbook](https://handbook.duolingo.com), the [Duolingo Blog](https://blog.duolingo.com/archive/), and the [Duolingo Design System](https://design.duolingo.com) — into reusable thinking tools for **anyone** building a brand, product, system, or culture.

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

## The eight skills

| Skill | Domain |
|---|---|
| `duo-retention` | habit loops, streaks, churn, day-N hooks |
| `duo-gamification` | XP, juicy feedback, leagues, progression |
| `duo-voice` | "wholesome but unhinged" copy, character archetypes, push notification patterns |
| `duo-experimentation` | A/B testing, hypothesis design, "show don't tell" |
| `duo-product` | take the long view, ship it, raise the bar |
| `duo-growth` | viral loops, brand-as-acquisition, marketing stunts |
| `duo-culture` | the Green Machine, talent density, candor |
| `duo-design` | juicy motion, character system, design tokens |

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
2. **What Duolingo does** — the actual move, with a citation (handbook page, blog URL, or design system page).
3. **The transferable pattern** — the rule, separated from Duolingo specifics.
4. **Apply to your product** — 2–3 prompts the reader can answer about their own thing.

If a node only has #1 and #2, it's a content dump, not a skill. Reject in review.

### Wikilink conventions

- `[[references/foo]]` — same-skill link.
- `[[../duo-voice/references/foo]]` — cross-skill link.
- `[[../duo-voice/SKILL]]` — link to a sibling skill's MoC.
- `[[references/foo|display text]]` — alias form when the target slug isn't ideal prose.

Don't introduce a new wikilink target without creating the corresponding file.

## Adding a new skill

1. Create `skills/<name>/SKILL.md` with valid frontmatter (`name` matching the directory).
2. Add `skills/<name>/references/` with at least three nodes.
3. Cross-link the new skill from at least one existing skill's MoC.
4. Update the skill table and tree in `README.md`.

## Adding a new node to an existing skill

1. Create `skills/<skill>/references/<topic>.md` with frontmatter (`name`, `summary`, `metadata.internal: true`).
2. Add a `[[references/<topic>]]` line to the skill's `SKILL.md` MoC under the right section.
3. Add inbound links from at least one related node so it's discoverable through traversal.

## Validation

Run the local validator before opening a PR. CI runs the same script on every PR and push to `main`.

```bash
python scripts/validate.py
```

The validator checks:

- Every `SKILL.md` has spec-compliant frontmatter (`name` matches dir, `description` ≤ 1024 chars).
- Every `references/*.md` has `name`, `summary`, and `metadata.internal: true`.
- Every wikilink `[[...]]` resolves to an existing file (code-span wikilinks like `` `[[wikilinks]]` `` in prose are ignored).
- Every reference node has all four required body sections (`## Concept`, `## What Duolingo does`, `## The transferable pattern`, `## Apply to your product`).
- No orphan nodes — every reference is reachable from at least one `SKILL.md` via wikilink traversal.

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
