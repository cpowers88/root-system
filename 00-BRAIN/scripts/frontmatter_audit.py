#!/usr/bin/env python3
"""frontmatter_audit.py — Tag Standard enforcement.

Checks every live .md in .ROOT against WHERE_IT_GOES.md § Tag Standard:

  - frontmatter block present
  - `type:` present
  - exactly ONE timeline tag: now | next | later | parked | reference
    (or `log` for history files; wikis may use native equivalents:
    priority/*, stage-*, phase-*)

Read-only: prints a Markdown report to stdout.
Usage (from .ROOT):  python 00-BRAIN/scripts/frontmatter_audit.py
"""

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED = {"99-ARCHIVE", "raw", ".git", ".obsidian", "Report Archive",
            "77-INBOX", "88-JOURNAL", ".claude", ".agents", "SKILLS"}
TIMELINE = {"now", "next", "later", "parked", "reference", "log"}
NATIVE = re.compile(r"^(priority/\w+|stage-\d+|phase-(\d+|all)|stage-all)$")


def parse_frontmatter(text: str):
    if not text.lstrip().startswith("---"):
        return None
    body = text.lstrip()[3:]
    end = body.find("\n---")
    if end == -1:
        return None
    return body[:end]


def tags_from(fm: str):
    tags = []
    inline = re.search(r"^tags:\s*\[([^\]]*)\]", fm, re.M)
    if inline:
        tags = [t.strip().strip("'\"") for t in inline.group(1).split(",") if t.strip()]
    else:
        block = re.search(r"^tags:\s*\n((?:\s+-\s+.+\n?)+)", fm, re.M)
        if block:
            tags = [ln.strip().lstrip("- ").strip().strip("'\"")
                    for ln in block.group(1).splitlines() if ln.strip()]
    return tags


def main() -> int:
    missing_fm, missing_type, timeline_bad = [], [], []
    checked = 0

    for p in sorted(ROOT.rglob("*.md")):
        if EXCLUDED.intersection(p.relative_to(ROOT).parts):
            continue
        checked += 1
        rel = p.relative_to(ROOT)
        fm = parse_frontmatter(p.read_text(encoding="utf-8", errors="replace"))
        if fm is None:
            missing_fm.append(str(rel))
            continue
        if not re.search(r"^type:\s*\S+", fm, re.M):
            missing_type.append(str(rel))
        tags = tags_from(fm)
        tl = [t for t in tags if t in TIMELINE or NATIVE.match(t)]
        if len(tl) != 1:
            timeline_bad.append((str(rel), tl or ["<none>"]))

    print("# FRONTMATTER / TAG AUDIT")
    print(f"\nFiles checked: {checked}\n")
    print(f"## Missing frontmatter ({len(missing_fm)})")
    for f in missing_fm or []:
        print(f"- `{f}`")
    if not missing_fm:
        print("- none")
    print(f"\n## Missing `type:` ({len(missing_type)})")
    for f in missing_type or []:
        print(f"- `{f}`")
    if not missing_type:
        print("- none")
    print(f"\n## Timeline tag ≠ exactly one ({len(timeline_bad)})")
    for f, tl in timeline_bad or []:
        print(f"- `{f}` — has: {', '.join(tl)}")
    if not timeline_bad:
        print("- none")
    total = len(missing_fm) + len(missing_type) + len(timeline_bad)
    print(f"\n**Total findings: {total}** — "
          f"{'CLEAN' if total == 0 else 'fix at reviews per Tag Standard'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
