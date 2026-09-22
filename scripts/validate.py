#!/usr/bin/env python3
"""
Validate the duolingo skill graph.

Checks:
  1. SKILL.md frontmatter is spec-compliant (agentskills.io) and skills.sh-installable.
  2. references/*.md carry name, summary, and a real boolean metadata.internal: true.
  3. Every wikilink [[...]] resolves to an existing file.
  4. Concept nodes carry the four body-contract sections and cite a source URL.
  5. No orphan nodes — every node is reachable from a SKILL.md via wikilink traversal.
  6. The router reaches every skill in the repo, and names no skill that doesn't exist.

Frontmatter is parsed with a real YAML parser. The previous hand-rolled line parser
silently mis-read block scalars (`>-` made a 900-char description measure as 2 chars),
so length and type checks passed without checking anything.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERR  PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
ROUTER = "duolingo"

WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]+`|```.*?```", re.DOTALL)
URL = re.compile(r"(?:https?://|\b)(?:blog|handbook|design)\.duolingo\.com[^\s)\]`]*")
BLOG_CITE = re.compile(r"blog\.duolingo\.com/([a-z0-9][a-z0-9-]*)")
# Non-post paths on the blog (section landing pages), which have no sitemap slug.
NON_POST = {"hub", "archive", "author", "tag", "rss"}

# A node that defers to the live site is a node that breaks when the site changes.
# design.duolingo.com already 301s to a four-post hub, so this is not hypothetical:
# the substance belongs inline, and the URL is provenance only.
SEND_TO_SITE = re.compile(
    r"(?i)\b(?:see|read|visit|check|refer to|full details?(?: at| in)?)\s+"
    r"(?:the\s+)?(?:full\s+)?(?:post|article|blog|page|write-?up)?[^.\n]{0,40}?"
    r"(?:blog|handbook|design)\.duolingo\.com"
)

# The bibliography of every post the pack was distilled from. A cited slug that is not
# in here never existed in the corpus, so it is fabricated or mistyped — and because the
# skills must work without network access, a wrong URL would never be caught at runtime.
_BIB_PATH = ROOT / "scripts" / "sources.json"
KNOWN_SLUGS: set[str] = set()
if _BIB_PATH.exists():
    try:
        KNOWN_SLUGS = set(json.loads(_BIB_PATH.read_text(encoding="utf-8"))["posts"])
    except (ValueError, KeyError):
        pass

# Ground truth read from the skills CLI bundle (vercel-labs/skills v1.7.0):
#   isValidSkillName: 1-64 chars, ^[a-z0-9-]+$, no leading/trailing '-', no '--'
SKILL_NAME = re.compile(r"^[a-z0-9-]+$")

# The router's references are procedural (routing tables, handoff contracts), not
# concept nodes, so they are exempt from the Concept/What-Duolingo-does contract.
PROCEDURAL = {ROUTER}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def strip_code_spans(text: str) -> str:
    return INLINE_CODE.sub(lambda m: " " * len(m.group(0)), text)


def parse_frontmatter(text: str, where: Path) -> dict:
    m = FRONTMATTER.match(text)
    if not m:
        err(f"{rel(where)}: no YAML frontmatter block")
        return {}
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        err(f"{rel(where)}: frontmatter is not valid YAML — {str(e).splitlines()[0]}")
        return {}
    if not isinstance(data, dict):
        err(f"{rel(where)}: frontmatter must be a mapping")
        return {}
    return data


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(p)


def check_name(name: object, expected: str, where: Path) -> None:
    if not isinstance(name, str) or not name:
        err(f"{rel(where)}: 'name' missing or not a string")
        return
    if name != expected:
        err(f"{rel(where)}: name '{name}' does not match directory '{expected}'")
    if len(name) > 64:
        err(f"{rel(where)}: name exceeds 64 characters")
    if not SKILL_NAME.match(name):
        err(f"{rel(where)}: name '{name}' must match ^[a-z0-9-]+$ (skills.sh rule)")
    if name.startswith("-") or name.endswith("-"):
        err(f"{rel(where)}: name must not start or end with a hyphen")
    if "--" in name:
        err(f"{rel(where)}: name must not contain consecutive hyphens")


def resolve_wikilink(target: str, source_file: Path) -> Path:
    skill_dir = source_file.parent
    if skill_dir.name == "references":
        skill_dir = skill_dir.parent

    t = target.strip()
    if t.startswith("../"):
        path = SKILLS / t[3:]
    elif t.startswith("references/"):
        path = skill_dir / t
    elif "/" in t:
        path = skill_dir / t
    else:
        path = skill_dir / "references" / t

    if not path.suffix:
        path = path.with_suffix(".md")
    return path


def check_links(text: str, source: Path) -> set[Path]:
    found: set[Path] = set()
    for m in WIKILINK.finditer(strip_code_spans(text)):
        resolved = resolve_wikilink(m.group(1), source)
        if not resolved.exists():
            err(f"{rel(source)}: broken wikilink [[{m.group(1)}]] -> {rel(resolved)}")
        else:
            found.add(resolved.resolve())
    return found


def check_skill_md(skill_md: Path) -> set[Path]:
    skill_name = skill_md.parent.name
    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text, skill_md)
    if not fm:
        return set()

    check_name(fm.get("name"), skill_name, skill_md)

    desc = fm.get("description")
    if not isinstance(desc, str) or not desc.strip():
        err(f"{rel(skill_md)}: 'description' missing, empty, or not a string")
    elif len(desc) > 1024:
        err(f"{rel(skill_md)}: description is {len(desc)} chars (max 1024)")
    elif len(desc) < 120:
        warn(f"{rel(skill_md)}: description is only {len(desc)} chars — weak trigger surface")

    compat = fm.get("compatibility")
    if compat is not None and (not isinstance(compat, str) or len(compat) > 500):
        err(f"{rel(skill_md)}: 'compatibility' must be a string of at most 500 chars")

    if fm.get("license") != "MIT":
        warn(f"{rel(skill_md)}: license is not MIT")

    for key in ("version", "homepage", "author"):
        if key in fm:
            err(f"{rel(skill_md)}: '{key}' is not a spec field — nest it under metadata")

    body_lines = text.split("\n---\n", 2)[-1].count("\n")
    if body_lines > 500:
        err(f"{rel(skill_md)}: body is {body_lines} lines (spec recommends under 500)")

    return check_links(text, skill_md)


def check_node(node_md: Path, procedural: bool) -> None:
    text = node_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text, node_md)
    if not fm:
        return

    if not isinstance(fm.get("name"), str) or not fm.get("name"):
        err(f"{rel(node_md)}: missing 'name'")
    if not isinstance(fm.get("summary"), str) or not fm.get("summary"):
        err(f"{rel(node_md)}: missing 'summary'")

    meta = fm.get("metadata")
    if not isinstance(meta, dict) or meta.get("internal") is not True:
        # Strict: the skills CLI tests `metadata?.internal === true`, so the string
        # "true" does NOT hide the node. It must be a real YAML boolean.
        err(f"{rel(node_md)}: needs metadata.internal: true (unquoted boolean)")

    body = text.split("\n---\n", 2)[-1]

    if not procedural:
        for marker in (
            "## Concept",
            "## What Duolingo does",
            "## The transferable pattern",
            "## Apply to your product",
        ):
            if marker not in body:
                err(f"{rel(node_md)}: missing required section '{marker.strip('# ')}'")
        if not URL.search(body):
            err(f"{rel(node_md)}: cites no duolingo.com source URL")

    # Anti-fabrication: every cited blog slug must exist in the crawled corpus.
    if KNOWN_SLUGS:
        for slug in set(BLOG_CITE.findall(body)):
            if slug in NON_POST:
                continue
            if slug not in KNOWN_SLUGS:
                err(
                    f"{rel(node_md)}: cites blog.duolingo.com/{slug}, which is not in "
                    f"scripts/sources.json — fabricated or mistyped"
                )

    # The pack must stand alone: a node may not send the agent to the live site.
    for m in SEND_TO_SITE.finditer(body):
        err(
            f"{rel(node_md)}: tells the reader to go to the live site "
            f'("{m.group(0).strip()[:60]}"). Sources rot — inline the substance and '
            f"keep the URL as provenance only."
        )

    check_links(text, node_md)


def check_router_coverage(skill_dirs: list[Path]) -> None:
    router_dir = SKILLS / ROUTER
    if not router_dir.exists():
        err(f"router skill '{ROUTER}' not found at {rel(router_dir)}")
        return

    leaves = {d.name for d in skill_dirs if d.name != ROUTER}
    routed: set[str] = set()

    for p in sorted(router_dir.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        routed |= set(re.findall(r"\.\./(duo-[a-z0-9-]+)/", text))

        # A skill named in prose or a code span is still a routing instruction, but it
        # is invisible to the wikilink checker. Two whole router files once pointed at a
        # taxonomy that had been split apart, and nothing caught it, because the names
        # were written as `duo-old-name` rather than as links.
        for name in set(re.findall(r"\bduo-[a-z0-9-]+\b", text)):
            if name not in leaves:
                err(
                    f"{rel(p)}: names '{name}', which is not a skill in this repo — "
                    f"a stale routing target"
                )

    for missing in sorted(leaves - routed):
        err(f"router does not route to '{missing}' — every skill must be reachable from /{ROUTER}")


def main() -> int:
    if not SKILLS.exists():
        err(f"skills/ directory not found at {rel(SKILLS)}")
        return 1

    all_referenced: set[Path] = set()
    all_nodes: set[Path] = set()

    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    print(f"Found {len(skill_dirs)} skills")

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            err(f"{rel(skill_dir)}: missing SKILL.md")
            continue

        all_referenced.update(check_skill_md(skill_md))

        refs_dir = skill_dir / "references"
        if not refs_dir.exists():
            err(f"{rel(skill_dir)}: missing references/ directory")
            continue

        procedural = skill_dir.name in PROCEDURAL
        for node in sorted(refs_dir.glob("*.md")):
            all_nodes.add(node.resolve())
            check_node(node, procedural)

    check_router_coverage(skill_dirs)

    reachable = set(all_referenced)
    changed = True
    while changed:
        changed = False
        for node in list(reachable):
            try:
                t = strip_code_spans(node.read_text(encoding="utf-8"))
            except OSError:
                continue
            for m in WIKILINK.finditer(t):
                target = resolve_wikilink(m.group(1), node)
                if target.exists():
                    r = target.resolve()
                    if r not in reachable:
                        reachable.add(r)
                        changed = True

    for o in sorted(all_nodes - reachable):
        err(f"orphan node (unreachable from any SKILL.md): {rel(o)}")

    print(f"  total nodes: {len(all_nodes)}")
    print(f"  reachable:   {len(reachable & all_nodes)}")
    print()

    if warnings:
        print(f"Warnings: {len(warnings)}")
        for w in warnings:
            print(f"  WARN  {w}")
    if errors:
        print(f"Errors:   {len(errors)}")
        for e in errors:
            print(f"  ERR   {e}")
        return 1

    print(f"OK — {len(all_nodes)} nodes across {len(skill_dirs)} skills, no errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
