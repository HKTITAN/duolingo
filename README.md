# Duolingo Skills

Agent skills that extract the Duolingo playbook — the [Handbook](https://handbook.duolingo.com), the [Blog](https://blog.duolingo.com/archive/), and the [Design System](https://design.duolingo.com) — into reusable thinking tools for **anyone** building a brand, product, system, or culture.

Not "skills about Duolingo." Duolingo is the case study; the user's product is the target. Every node ends with **Apply to your product**.

## Install

```bash
npx skills add HKTITAN/duolingo
```

This uses the [skills.sh](https://skills.sh) CLI to install the skills into your detected agent (Claude Code, Cursor, etc.). The CLI will prompt for scope (project vs. global) and method (symlink vs. copy).

## Paste this into your coding agent

The fastest way to set up any coding agent — Claude Code, Cursor, Windsurf, Codex, Aider, Cline, or anything that reads project rules — is to drop the block below into your agent's instructions / `AGENTS.md` / `.cursorrules` / system prompt.

```text
You have access to Duolingo Skills — a library of reusable thinking tools
extracted from Duolingo's public playbook (Handbook, Blog, Design System).
Use them whenever the user is building, evaluating, or redesigning a
product, brand, system, or culture.

- Repo:           https://github.com/HKTITAN/duolingo
- Skills root:    https://github.com/HKTITAN/duolingo/tree/main/skills
- Install:        npx skills add HKTITAN/duolingo
- Authoring rules and conventions: AGENTS.md at the repo root.

Each skill is a graph:
- `skills/<skill>/SKILL.md` is a Map of Content — short descriptions plus
  [[wikilinks]] to atomic concept nodes.
- `skills/<skill>/references/<node>.md` are atomic concept files. Each one
  follows the same body contract: Concept → What Duolingo does → The
  transferable pattern → Apply to your product.
- Cross-skill wikilinks like `[[../duo-voice/references/push-notification-copy]]`
  let you traverse the whole library as one graph.

The eight skills:
- duo-retention       — habit loops, streaks, churn diagnostics, day-N hooks
- duo-gamification    — XP, juicy feedback, leagues, progression design
- duo-voice           — "wholesome but unhinged" copy, character archetypes
- duo-experimentation — A/B testing, hypothesis design, show-don't-tell
- duo-product         — take the long view, ship it, raise the bar
- duo-growth          — viral loops, brand-as-acquisition, earned media
- duo-culture         — the Green Machine, talent density, candor
- duo-design          — juicy motion, character system, design tokens

Rules:
1. The user is rarely building Duolingo. Always do the translation step:
   read the relevant node, then apply its pattern to the user's actual
   product. Don't just describe what Duolingo did.
2. Cite the node path you used (e.g.
   `skills/duo-retention/references/streak-mechanics.md`).
3. Prefer reading a specific `references/<node>.md` over the whole SKILL.md
   when you know the area — cheaper on context, the graph is built for it.
4. If multiple skills overlap (a retention question often touches voice and
   gamification too), follow the cross-skill `[[../...]]` wikilinks rather
   than re-deriving the connection.

Smoke test: name three things from
`skills/duo-retention/references/streak-freeze.md` that explain why the
streak freeze is a retention move, not a kindness. (Expected:
loss-aversion preservation, removes guilt-driven churn, increases
willingness to start a streak in the first place.)
```

## What's included

| Skill | Use it when… |
|---|---|
| `duo-retention` | Designing for habit and long-term return — streaks, leagues, day-1/7/30 drop-off, notification timing, churn debugging. |
| `duo-gamification` | Adding XP, levels, juicy feedback, celebration moments, hearts/energy, or anti-grind mechanics to any product. |
| `duo-voice` | Writing product copy that gets screenshotted — push notifications, error messages, onboarding, empty states, character-driven tone. |
| `duo-experimentation` | Running A/B tests properly — hypothesis design, metric selection, guardrails, sample size, kill criteria. |
| `duo-product` | Making product decisions — long view vs. short term, ruthless prioritization, dogfooding, the "intuitive by default" bar. |
| `duo-growth` | Acquisition that doesn't hurt retention — viral loops, brand-as-acquisition, marketing stunts, earned media. |
| `duo-culture` | Building the team — the Green Machine op model, talent density, candor protocol, hire-slow / fire-fast. |
| `duo-design` | UI patterns from the design system — juicy motion, character reactions, sound, accessibility, error-as-delight. |

## Structure: skill graphs, not flat files

Each skill is a **graph**, not a single file. The pattern (per [Akshay Pachaar's "Skill Graphs > SKILL.md"](https://x.com/akshay_pachaar/status/2024848778415755327)):

- **`SKILL.md`** is a *Map of Content* — short descriptions of every node in the graph, plus `[[wikilinks]]` to follow.
- **`references/*.md`** are atomic concept files — one complete thought each, with their own YAML frontmatter and outbound `[[wikilinks]]` to siblings (within the skill) and across skills. (`references/` is the [Agent Skills spec](https://agentskills.io/specification) standard directory for additional documentation.)
- The agent **scans descriptions and frontmatter first**, then follows only the links it needs. Most decisions happen before reading a single full node.
- Nodes are marked `metadata.internal: true` so the skills.sh CLI surfaces only the eight top-level skills, not every node.
- Cross-skill wikilinks (e.g. `[[../duo-voice/references/push-notification-copy]]`) make all eight skills navigable as one larger graph.

## Repository layout

```text
duolingo/
├── AGENTS.md
├── README.md
├── LICENSE
└── skills/
    ├── duo-retention/
    │   ├── SKILL.md
    │   └── references/  (forever-product, habit-loop, streak-mechanics,
    │                streak-freeze, loss-aversion, variable-reward, leagues,
    │                daily-quests, churn-diagnostics, notification-discipline,
    │                friction-as-stickiness, retention-vs-revenue)
    ├── duo-gamification/
    │   ├── SKILL.md
    │   └── references/  (juicy-feedback, xp-system, progression-design,
    │                celebration-moments, character-reactions, ramp-up-difficulty,
    │                hearts-and-energy, power-ups, combo-multipliers, anti-grind)
    ├── duo-voice/
    │   ├── SKILL.md
    │   └── references/  (wholesome-unhinged, character-archetypes,
    │                push-notification-copy, error-copy, onboarding-copy,
    │                empty-states, celebration-copy, threat-copy,
    │                localization-voice, screenshot-bait)
    ├── duo-experimentation/
    │   ├── SKILL.md
    │   └── references/  (show-dont-tell, hypothesis-design, ab-test-structure,
    │                metric-selection, guardrail-metrics, sample-size,
    │                novelty-effects, ship-and-iterate, kill-criteria,
    │                experiment-cadence)
    ├── duo-product/
    │   ├── SKILL.md
    │   └── references/  (take-the-long-view, raise-the-bar, ship-it,
    │                intuitive-by-default, ruthless-prioritization, dogfooding,
    │                ownership-clarity, polish, hundred-year-brand,
    │                kill-criteria-product)
    ├── duo-growth/
    │   ├── SKILL.md
    │   └── references/  (viral-loops, social-mechanics, referrals,
    │                localization-as-growth, brand-as-acquisition,
    │                marketing-stunts, duo-tiktok, gen-z-positioning,
    │                earned-media, founder-mode-marketing)
    ├── duo-culture/
    │   ├── SKILL.md
    │   └── references/  (green-machine, talent-density, candor-what-not-who,
    │                hire-slow-fire-fast, no-process-without-purpose,
    │                clock-speed, dogfooding-culture, async-vs-meetings,
    │                quirky-by-design, ownership-clarity-culture)
    └── duo-design/
        ├── SKILL.md
        └── references/  (juicy-motion, character-system, color-tokens,
                     type-system, sound-as-ux, accessibility-default,
                     error-as-delight, celebration-design, progress-bars,
                     bottom-bar-navigation)
```

## Sources

- The Duolingo Handbook (2025) — <https://handbook.duolingo.com>
- The Duolingo Blog archive — <https://blog.duolingo.com/archive/>
- The Duolingo Design System — <https://design.duolingo.com>

## See also

- [skills.sh](https://skills.sh) — the CLI and registry
- [Agent Skills spec](https://agentskills.io/specification)
- [agents.md](https://agents.md) — the AGENTS.md format
- Skill-graph idea: [@akshay_pachaar](https://x.com/akshay_pachaar/status/2024848778415755327)

## License

MIT
