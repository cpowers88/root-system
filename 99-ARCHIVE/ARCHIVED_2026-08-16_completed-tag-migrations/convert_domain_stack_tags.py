#!/usr/bin/env python3
"""Convert the SYSTEMS/TECHNOLOGY structured tag families into properties:

  domain/*        -> dropped entirely (inferable from 03-WIKIS/<hub> path)
  source-role/*   -> source_role: value   (scalar; list if a file genuinely
                     carries more than one — rare, checked before running)
  use-case/*      -> use_cases: [list]
  stack/*         -> stack: [list]

Nothing else in the file's tags/properties is touched.

Usage:
    python convert_domain_stack_tags.py --check
    python convert_domain_stack_tags.py --apply
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import frontmatter_audit as audit  # noqa: E402

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def find_tags_index(lines):
    for i, line in enumerate(lines):
        if re.match(r"^tags\s*:", line):
            return i
    return None


def remove_tags(lines, tags_idx, remove_set):
    line = lines[tags_idx]
    inline = re.match(r"^(tags\s*:\s*)\[(.*)\]\s*$", line)
    if inline:
        prefix, inner = inline.groups()
        items = [t.strip() for t in inner.split(",") if t.strip()]
        items = [t for t in items if t not in remove_set]
        lines[tags_idx] = f"{prefix}[{', '.join(items)}]"
        return lines
    j = tags_idx + 1
    kept = []
    while j < len(lines) and re.match(r"^\s*-\s*", lines[j]):
        item = re.sub(r"^\s*-\s*", "", lines[j]).strip()
        if item not in remove_set:
            kept.append(lines[j])
        j += 1
    return lines[: tags_idx + 1] + kept + lines[j:]


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    changed = 0
    for path in sorted(audit.ROOT.rglob("*.md")):
        rel = path.relative_to(audit.ROOT)
        if audit.EXCLUDED.intersection(rel.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        m = FRONTMATTER_RE.match(text)
        if not m:
            continue
        fm_block = m.group(1)
        fm_str = audit.parse_frontmatter(text)
        tags = audit.tags_from(fm_str) if fm_str is not None else []
        if not tags:
            continue

        domain_tags = [t for t in tags if t.startswith("domain/")]
        source_role_tags = [t for t in tags if t.startswith("source-role/")]
        use_case_tags = [t for t in tags if t.startswith("use-case/")]
        stack_tags = [t for t in tags if t.startswith("stack/")]

        if not (domain_tags or source_role_tags or use_case_tags or stack_tags):
            continue

        has_source_role_prop = re.search(r"(?m)^source_role\s*:", fm_block) is not None
        has_use_cases_prop = re.search(r"(?m)^use_cases\s*:", fm_block) is not None
        has_stack_prop = re.search(r"(?m)^stack\s*:", fm_block) is not None

        new_props = []
        remove_set = set(domain_tags)

        if source_role_tags and not has_source_role_prop:
            values = [t.split("/", 1)[1] for t in source_role_tags]
            if len(values) == 1:
                new_props.append(f"source_role: {values[0]}")
            else:
                new_props.append(f"source_role: [{', '.join(values)}]")
            remove_set.update(source_role_tags)
        elif source_role_tags and has_source_role_prop:
            print(f"  SKIP source-role (property already set): {rel}")

        if use_case_tags and not has_use_cases_prop:
            values = [t.split("/", 1)[1] for t in use_case_tags]
            new_props.append(f"use_cases: [{', '.join(values)}]")
            remove_set.update(use_case_tags)
        elif use_case_tags and has_use_cases_prop:
            print(f"  SKIP use-case (property already set): {rel}")

        if stack_tags and not has_stack_prop:
            values = [t.split("/", 1)[1] for t in stack_tags]
            new_props.append(f"stack: [{', '.join(values)}]")
            remove_set.update(stack_tags)
        elif stack_tags and has_stack_prop:
            print(f"  SKIP stack (property already set): {rel}")

        if not remove_set:
            continue

        if args.check:
            print(f"  WOULD CONVERT {rel}: remove {sorted(remove_set)}; add {new_props}")
            changed += 1
            continue

        lines = fm_block.split("\n")
        tags_idx = find_tags_index(lines)
        if tags_idx is None:
            continue
        lines = remove_tags(lines, tags_idx, remove_set)
        lines.extend(new_props)
        new_fm = "\n".join(lines)
        new_text = FRONTMATTER_RE.sub(f"---\n{new_fm}\n---\n", text, count=1)
        path.write_text(new_text, encoding="utf-8", newline="\n")
        changed += 1

    verb = "would be changed" if args.check else "changed"
    print(f"\n{changed} files {verb}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
