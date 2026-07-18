#!/usr/bin/env python3
"""Check or synchronize `.ROOT` canonical skills and product mirrors."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "00-BRAIN" / "SKILLS"
MIRRORS = (ROOT / ".agents" / "skills", ROOT / ".claude" / "skills")


def normalized(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = normalized(path)
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return [f"{path}: invalid YAML frontmatter boundary"]
    frontmatter = text.split("---\n", 2)[1]
    fields = re.findall(r"^([a-zA-Z0-9_-]+):\s*(.+)$", frontmatter, re.M)
    values = dict(fields)
    extra = sorted(set(values) - {"name", "description"})
    if extra:
        errors.append(f"{path}: unsupported frontmatter fields {extra}")
    name = values.get("name", "").strip()
    if name != path.parent.name:
        errors.append(f"{path}: name '{name}' does not match folder")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append(f"{path}: invalid skill name '{name}'")
    if not values.get("description", "").strip():
        errors.append(f"{path}: missing description")
    return errors


def skill_names(root: Path) -> set[str]:
    if not root.exists():
        return set()
    return {p.parent.name for p in root.glob("*/SKILL.md")}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sync", action="store_true", help="write mirrors from canonical skills")
    parser.add_argument("--check", action="store_true", help="check only (default)")
    args = parser.parse_args()
    if args.sync and args.check:
        parser.error("choose --sync or --check")

    canonical_names = skill_names(CANONICAL)
    errors: list[str] = []
    if not canonical_names:
        errors.append("no canonical skills found")

    canonical_text: dict[str, str] = {}
    for name in sorted(canonical_names):
        path = CANONICAL / name / "SKILL.md"
        errors.extend(validate_skill(path))
        canonical_text[name] = normalized(path)

    if errors:
        print("# SHARED SKILL VALIDATION — FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.sync:
        for mirror in MIRRORS:
            for name, text in canonical_text.items():
                target = mirror / name / "SKILL.md"
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(text, encoding="utf-8", newline="\n")

    for mirror in MIRRORS:
        mirror_names = skill_names(mirror)
        missing = sorted(canonical_names - mirror_names)
        unexpected = sorted(mirror_names - canonical_names)
        if missing:
            errors.append(f"{mirror.relative_to(ROOT)}: missing {missing}")
        if unexpected:
            errors.append(f"{mirror.relative_to(ROOT)}: unexpected {unexpected}")
        for name in sorted(canonical_names & mirror_names):
            target = mirror / name / "SKILL.md"
            errors.extend(validate_skill(target))
            actual = normalized(target)
            if actual != canonical_text[name]:
                errors.append(
                    f"{target.relative_to(ROOT)}: mirror {digest(actual)} != "
                    f"canonical {digest(canonical_text[name])}"
                )

    if errors:
        print("# SHARED SKILL VALIDATION — FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    action = "SYNCED" if args.sync else "PASS"
    print(f"# SHARED SKILL VALIDATION — {action}")
    print(f"Canonical skills: {len(canonical_names)} | Mirrors: {len(MIRRORS)}")
    for name in sorted(canonical_names):
        print(f"- {name}: {digest(canonical_text[name])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
