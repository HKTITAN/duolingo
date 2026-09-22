#!/usr/bin/env python3
"""
Normalize every blog.duolingo.com citation in the skill graph to a dated form, and
flag any that don't resolve to a real post.

    blog.duolingo.com/friend-streak
    -> blog.duolingo.com/friend-streak (Duolingo blog, 2024-08-05; accessed 2026-09-22)

Why: the skills must stay useful when the source goes away. design.duolingo.com already
301-redirects to a four-post hub, so a bare URL is a promise the web may not keep. The
substance lives in the node; the URL is provenance, stamped with when it was true.

A slug that isn't in scripts/sources.json is a fabricated or mistyped citation — this
script reports those and does not rewrite them.

Usage:
    python scripts/stamp_citations.py            # report only
    python scripts/stamp_citations.py --write    # rewrite in place
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
ACCESSED = "2026-09-22"

BIB = json.loads((ROOT / "scripts" / "sources.json").read_text(encoding="utf-8"))
POSTS: dict[str, dict] = BIB["posts"]
# Section landing pages, not posts — they carry no publish date to stamp.
NON_POST = {"hub", "archive", "author", "tag", "rss"}

# A blog citation not already carrying a "(" stamp.
# The slug must be consumed whole: without the (?![a-z0-9-]) guard the engine
# backtracks into the slug to dodge the "already stamped" lookahead, producing a
# truncated slug that then looks fabricated.
CITE = re.compile(
    r"blog\.duolingo\.com/(?P<slug>[a-z0-9][a-z0-9-]*)/?"
    r"(?![a-z0-9-])"
    r"(?!\s*\((?:Duolingo blog|accessed))"
)


def stamp(slug: str) -> str:
    post = POSTS[slug]
    date = (post.get("d") or "").strip()
    when = f"{date}; " if date else ""
    return f"blog.duolingo.com/{slug} (Duolingo blog, {when}accessed {ACCESSED})"


def main() -> int:
    write = "--write" in sys.argv
    stamped = 0
    already = 0
    unknown: list[tuple[str, str]] = []
    touched: list[str] = []

    for md in sorted(SKILLS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        rel = str(md.relative_to(ROOT)).replace("\\", "/")
        changed = False

        def repl(m: re.Match) -> str:
            nonlocal changed, stamped
            slug = m.group("slug")
            if slug in NON_POST:
                return m.group(0)
            if slug not in POSTS:
                unknown.append((rel, slug))
                return m.group(0)
            changed = True
            stamped += 1
            return stamp(slug)

        new = CITE.sub(repl, text)
        already += len(re.findall(r"blog\.duolingo\.com/[a-z0-9-]+\s*\(Duolingo blog", text))

        if changed and new != text:
            touched.append(rel)
            if write:
                md.write_text(new, encoding="utf-8")

    print(f"citations stamped:   {stamped}")
    print(f"already stamped:     {already}")
    print(f"files touched:       {len(touched)}")

    if unknown:
        print(f"\nUNRESOLVED ({len(unknown)}) — not in the 842-post corpus, so likely fabricated:")
        seen = set()
        for rel, slug in unknown:
            key = (rel, slug)
            if key in seen:
                continue
            seen.add(key)
            print(f"  {rel}  ->  blog.duolingo.com/{slug}")

    if not write and touched:
        print("\n(report only — rerun with --write to apply)")
    return 1 if unknown else 0


if __name__ == "__main__":
    sys.exit(main())
