#!/usr/bin/env python3
"""Convert four confirmed-clean legacy tag families into proper frontmatter
properties, per the 2026-07-21 tag-taxonomy audit:

  priority/{now,next,later}  -> timeline: {value}      (skip if timeline: already set)
  status/wiki-only           -> status: wiki-only       (skip if status: already set)
  stage-NN  (when stage: property ALREADY holds the same value) -> just drop
             the now-redundant tag (verified duplicate, no property write)
  phase-N / phase-all        -> phase: {value}          (new property; BUSINESS
             roadmap phase, deliberately kept separate from PYTHON/PHYSICS
             `stage:` — different concept, not the same field)

Anything that doesn't cleanly match one of these four exact shapes is left
untouched and reported, never guessed.

Usage:
    python convert_legacy_tag_families.py --check
    python convert_legacy_tag_families.py --apply
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import frontmatter_audit as audit  # noqa: E402

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
STAGE_TAG_RE = re.compile(r"^stage-(\d+)$")
PHASE_TAG_RE = re.compile(r"^phase-(\d+|all)$")


def remove_tag_lines(lines: list, tags_idx: int, remove_tag: str):
    """Remove one tag (inline-list or block-list form). Returns (new_lines, ok)."""
    line = lines[tags_idx]
    inline = re.match(r"^(tags\s*:\s*)\[(.*)\]\s*$", line)
    if inline:
        prefix, inner = inline.groups()
        items = [t.strip() for t in inner.split(",") if t.strip()]
        if remove_tag not in items:
            return lines, False
        items.remove(remove_tag)
        lines[tags_idx] = f"{prefix}[{', '.join(items)}]"
        return lines, True

    removed = False
    j = tags_idx + 1
    kept = []
    while j < len(lines) and re.match(r"^\s*-\s*", lines[j]):
        item = re.sub(r"^\s*-\s*", "", lines[j]).strip()
        if item == remove_tag and not removed:
            removed = True
        else:
            kept.append(lines[j])
        j += 1
    if not removed:
        return lines, False
    return lines[: tags_idx + 1] + kept + lines[j:], True


def find_tags_index(lines: list):
    for i, line in enumerate(lines):
        if re.match(r"^tags\s*:", line):
            return i
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    changed = 0
    skipped_ambiguous = 0

    for path in sorted(audit.ROOT.rglob("*.md")):
        rel = path.relative_to(audit.ROOT)
        if audit.EXCLUDED.intersection(rel.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm_match = FRONTMATTER_RE.match(text)
        if not fm_match:
            continue
        fm_block = fm_match.group(1)
        fm_str = audit.parse_frontmatter(text)
        tags = audit.tags_from(fm_str) if fm_str is not None else []
        if not tags:
            continue

        controls = [t for t in tags if t.startswith("priority/") or t.startswith("status/")
                    or STAGE_TAG_RE.match(t) or PHASE_TAG_RE.match(t)]
        if not controls:
            continue

        # Group by TARGET property so independent conversions on the same file
        # (e.g. priority/now -> timeline, status/wiki-only -> status) both
        # proceed; only a genuine collision on the SAME target is ambiguous.
        by_target = {"timeline": [], "status": [], "stage": [], "phase": []}
        for t in controls:
            if t.startswith("priority/"):
                by_target["timeline"].append(t)
            elif t.startswith("status/"):
                by_target["status"].append(t)
            elif STAGE_TAG_RE.match(t):
                by_target["stage"].append(t)
            elif PHASE_TAG_RE.match(t):
                by_target["phase"].append(t)

        has_timeline_prop = re.search(r"(?m)^timeline\s*:", fm_block) is not None
        has_status_prop = re.search(r"(?m)^status\s*:", fm_block) is not None
        has_phase_prop = re.search(r"(?m)^phase\s*:", fm_block) is not None
        existing_stage_match = re.search(r"(?m)^stage\s*:\s*['\"]?(\S+?)['\"]?\s*$", fm_block)

        actions = []  # list of (tag, kind, value_or_None)
        file_ambiguous = False

        if len(by_target["timeline"]) == 1 and not has_timeline_prop:
            value = by_target["timeline"][0].split("/", 1)[1]
            if value in {"now", "next", "later"}:
                actions.append((by_target["timeline"][0], "timeline", value))
        elif len(by_target["timeline"]) > 1:
            file_ambiguous = True

        if len(by_target["status"]) == 1 and not has_status_prop:
            value = by_target["status"][0].split("/", 1)[1]
            if value == "wiki-only":
                actions.append((by_target["status"][0], "status", value))
        elif len(by_target["status"]) > 1:
            file_ambiguous = True

        if len(by_target["stage"]) == 1:
            tag = by_target["stage"][0]
            num = STAGE_TAG_RE.match(tag).group(1)
            if existing_stage_match and existing_stage_match.group(1).lstrip("0") == num.lstrip("0"):
                actions.append((tag, "drop", None))
            else:
                file_ambiguous = True
        elif len(by_target["stage"]) > 1:
            file_ambiguous = True

        if len(by_target["phase"]) == 1 and not has_phase_prop:
            value = PHASE_TAG_RE.match(by_target["phase"][0]).group(1)
            actions.append((by_target["phase"][0], "phase", value))
        elif len(by_target["phase"]) > 1:
            file_ambiguous = True

        if file_ambiguous or not actions:
            print(f"  SKIP ({controls}): {rel}")
            skipped_ambiguous += 1
            continue

        if args.check:
            for tag, kind, value in actions:
                if kind == "drop":
                    print(f"  WOULD DROP duplicate tag {tag!r}: {rel}")
                else:
                    print(f"  WOULD CONVERT {tag!r} -> {kind}: {value!r}: {rel}")
            changed += 1
            continue

        lines = fm_block.split("\n")
        new_props = []
        ok_all = True
        for tag, kind, value in actions:
            tags_idx = find_tags_index(lines)
            if tags_idx is None:
                ok_all = False
                break
            lines, ok = remove_tag_lines(lines, tags_idx, tag)
            if not ok:
                print(f"  SKIP (could not remove tag {tag!r} mechanically): {rel}")
                ok_all = False
                break
            if kind != "drop":
                new_props.append(f"{kind}: {value}")
        if not ok_all:
            skipped_ambiguous += 1
            continue

        lines.extend(new_props)
        new_fm = "\n".join(lines)
        new_text = FRONTMATTER_RE.sub(f"---\n{new_fm}\n---\n", text, count=1)
        path.write_text(new_text, encoding="utf-8", newline="\n")
        changed += 1

    verb = "would be changed" if args.check else "changed"
    print(f"\n{changed} files {verb}; {skipped_ambiguous} skipped (ambiguous/manual).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
