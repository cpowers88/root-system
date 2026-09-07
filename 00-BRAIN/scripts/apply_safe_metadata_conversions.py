#!/usr/bin/env python3
"""Apply ONLY the `safe_complete_conversions` from a metadata_migration_plan.py
dry-run report: move a single plain timeline tag (now/next/later/parked/
reference) into the `timeline:` frontmatter property and remove it from `tags`.

Nothing else in the file is touched. Refuses to run against a plan whose
recomputed hash does not match (the plan must describe the live tree exactly).

Usage:
    python apply_safe_metadata_conversions.py --plan <dry_run.json> --check
    python apply_safe_metadata_conversions.py --plan <dry_run.json> --apply
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import metadata_migration_plan as planner  # noqa: E402

ROOT = planner.audit.ROOT
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def rewrite_file(path: Path, timeline_value: str, remove_tag: str) -> bool:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FRONTMATTER_RE.match(text)
    if not m:
        print(f"  SKIP (no frontmatter block matched): {path}")
        return False
    fm_block = m.group(1)
    lines = fm_block.split("\n")
    out_lines = []
    tags_line_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^tags\s*:", line):
            tags_line_idx = i
        out_lines.append(line)

    if tags_line_idx is None:
        print(f"  SKIP (no tags: line found): {path}")
        return False

    tags_line = out_lines[tags_line_idx]
    # Inline list form: tags: [a, b, c]
    inline = re.match(r"^(tags\s*:\s*)\[(.*)\]\s*$", tags_line)
    if inline:
        prefix, inner = inline.groups()
        items = [t.strip() for t in inner.split(",") if t.strip()]
        if remove_tag not in items:
            print(f"  SKIP (tag {remove_tag!r} not found inline): {path}")
            return False
        items.remove(remove_tag)
        new_tags_line = f"{prefix}[{', '.join(items)}]"
        out_lines[tags_line_idx] = new_tags_line
    else:
        # Block list form: tags:\n  - a\n  - b
        removed = False
        new_block = []
        j = tags_line_idx + 1
        while j < len(out_lines) and re.match(r"^\s*-\s*", out_lines[j]):
            item = re.sub(r"^\s*-\s*", "", out_lines[j]).strip()
            if item == remove_tag and not removed:
                removed = True
                j += 1
                continue
            new_block.append(out_lines[j])
            j += 1
        if not removed:
            print(f"  SKIP (tag {remove_tag!r} not found in block list): {path}")
            return False
        out_lines = out_lines[: tags_line_idx + 1] + new_block + out_lines[j:]

    # Insert or set timeline: right after the tags block (simple, safe placement:
    # only insert if a timeline: key doesn't already exist — the planner already
    # guarantees it doesn't, via property_from(fm, "timeline") is None).
    out_lines.append(f"timeline: {timeline_value}")

    new_fm = "\n".join(out_lines)
    new_text = FRONTMATTER_RE.sub(f"---\n{new_fm}\n---\n", text, count=1)
    path.write_text(new_text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="list what would change, write nothing")
    mode.add_argument("--apply", action="store_true", help="perform the safe conversions")
    args = parser.parse_args()

    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    recomputed = planner.build_plan()
    if recomputed["plan_sha256"] != plan["plan_sha256"]:
        print("REFUSING: the live tree no longer matches this plan's hash.")
        print("Regenerate the plan with metadata_migration_plan.py first.")
        return 1

    conversions = plan["safe_complete_conversions"]
    print(f"Plan verified against live tree. {len(conversions)} safe conversions queued.\n")

    changed = 0
    skipped = 0
    for item in conversions:
        path = ROOT / item["path"]
        timeline_value = item["set"]["timeline"]
        remove_tag = item["remove_tags"][0]
        if args.check:
            print(f"  WOULD CONVERT: {item['path']}  (tag {remove_tag!r} -> timeline: {timeline_value})")
            changed += 1
            continue
        ok = rewrite_file(path, timeline_value, remove_tag)
        if ok:
            changed += 1
        else:
            skipped += 1

    mode_word = "would be changed" if args.check else "changed"
    print(f"\n{changed} files {mode_word}; {skipped} skipped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
