#!/usr/bin/env python3
"""
Validate the duolingo skill graph.

Checks:
  1. Every SKILL.md has spec-compliant frontmatter (name matches dir, etc.)
  2. Every references/*.md has internal-flag frontmatter
  3. Every wikilink [[...]] resolves to an existing file
  4. Every reference node has the 4 body-contract sections
  5. No orphan nodes (every node is reachable from at least one SKILL.md)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

# Wikilink regex: [[target]] or [[target|display]]
WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
# Inline code spans: `...` and ```...``` — wikilinks inside these are prose, not links
INLINE_CODE = re.compile(r"`[^`\n]+`|```.*?```", re.DOTALL)


def strip_code_spans(text: str) -> str:
    """Replace inline code spans with whitespace of equal length so offsets stay valid."""
    return INLINE_CODE.sub(lambda m: " " * len(m.group(0)), text)

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            out[k.strip()] = v.strip().strip('"')
    return out


def resolve_wikilink(target: str, source_file: Path) -> Path | None:
    """Resolve [[target]] from source_file to an absolute Path."""
    skill_dir = source_file.parent
    if skill_dir.name == "references":
        skill_dir = skill_dir.parent

    t = target.strip()

    if t.startswith("../"):
        # cross-skill: ../duo-other/references/foo  or  ../duo-other/SKILL
        rel = t[3:]
        path = SKILLS / rel
    elif t.startswith("references/"):
        # same-skill explicit
        path = skill_dir / t
    elif "/" in t:
        # other relative form
        path = skill_dir / t
    else:
        # bare: refers to a sibling node in the same skill's references/
        path = skill_dir / "references" / t

    if not path.suffix:
        path = path.with_suffix(".md")
    return path


def check_skill_md(skill_md: Path) -> set[Path]:
    """Validate a SKILL.md and return the set of nodes it references."""
    skill_name = skill_md.parent.name
    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if not fm.get("name"):
        err(f"{skill_md}: missing 'name' in frontmatter")
    elif fm["name"] != skill_name:
        err(f"{skill_md}: name '{fm['name']}' does not match dir '{skill_name}'")
    if not fm.get("description"):
        err(f"{skill_md}: missing 'description' in frontmatter")
    elif len(fm["description"]) > 1024:
        err(f"{skill_md}: description exceeds 1024 chars")
    if fm.get("license") != "MIT":
        warn(f"{skill_md}: license is not MIT")

    referenced: set[Path] = set()
    scannable = strip_code_spans(text)
    for m in WIKILINK.finditer(scannable):
        resolved = resolve_wikilink(m.group(1), skill_md)
        if resolved is None:
            continue
        if not resolved.exists():
            err(f"{skill_md}: broken wikilink [[{m.group(1)}]] -> {resolved}")
        else:
            referenced.add(resolved.resolve())

    return referenced


def check_node(node_md: Path) -> None:
    text = node_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if not fm.get("name"):
        err(f"{node_md}: missing 'name' in frontmatter")
    if not fm.get("summary"):
        err(f"{node_md}: missing 'summary' in frontmatter")

    # Check internal flag (string match — simple parser doesn't handle nested keys)
    if "internal: true" not in text[: text.find("---", 4) + 4 if text.startswith("---") else 0] and "internal: true" not in text.split("---", 2)[1]:
        err(f"{node_md}: missing 'metadata.internal: true'")

    # Body contract — look for the four required sections
    body = text.split("---", 2)[-1]
    required_sections = [
        ("## Concept", "Concept"),
        ("## What Duolingo does", "What Duolingo does"),
        ("## The transferable pattern", "The transferable pattern"),
        ("## Apply to your product", "Apply to your product"),
    ]
    for marker, label in required_sections:
        if marker not in body:
            err(f"{node_md}: missing required section '{label}'")

    # Validate wikilinks (ignoring code spans)
    scannable = strip_code_spans(text)
    for m in WIKILINK.finditer(scannable):
        resolved = resolve_wikilink(m.group(1), node_md)
        if resolved is None:
            continue
        if not resolved.exists():
            err(f"{node_md}: broken wikilink [[{m.group(1)}]] -> {resolved}")


def main() -> int:
    if not SKILLS.exists():
        err(f"skills/ directory not found at {SKILLS}")
        return 1

    all_referenced: set[Path] = set()
    all_nodes: set[Path] = set()

    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    print(f"Found {len(skill_dirs)} skills")

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            err(f"{skill_dir}: missing SKILL.md")
            continue

        referenced = check_skill_md(skill_md)
        all_referenced.update(referenced)

        refs_dir = skill_dir / "references"
        if not refs_dir.exists():
            err(f"{skill_dir}: missing references/ directory")
            continue

        for node in sorted(refs_dir.glob("*.md")):
            all_nodes.add(node.resolve())
            check_node(node)

    # Reachability: every node should be referenced from at least one SKILL.md
    # OR be reachable through transitive node-to-node wikilinks. Since we want
    # the agent to find every node via traversal, we check direct SKILL.md
    # reach first, then expand via node outlinks.
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
                if target and target.exists():
                    r = target.resolve()
                    if r not in reachable:
                        reachable.add(r)
                        changed = True

    orphans = all_nodes - reachable
    for o in sorted(orphans):
        err(f"orphan node (not reachable from any SKILL.md): {o.relative_to(ROOT)}")

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

    print(f"OK — {len(all_nodes)} nodes, {len(skill_dirs)} skills, no errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
