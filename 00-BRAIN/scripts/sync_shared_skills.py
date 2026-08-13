#!/usr/bin/env python3
"""Check or synchronize `.ROOT` canonical skills and product mirrors.

Mirrors whole skill *directories*, not `SKILL.md` alone, and fails when a
`SKILL.md` references a file that is absent from a mirror.

Before 2026-08-13 this script copied only `SKILL.md`. A skill whose `SKILL.md`
linked to a companion file therefore mirrored as a document with a dead link,
and `--check` returned PASS over it — `root_health.py` inherited that PASS.
Worse, `--sync`, the documented remedy, exited 0 without copying the missing
file. That was flag #99: a validator certifying a defect its own repair tool
could not repair. The reference check below is the part that makes the fix
real; mirroring directories alone would have moved the defect, not closed it.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "00-BRAIN" / "SKILLS"
MIRRORS = (ROOT / ".agents" / "skills", ROOT / ".claude" / "skills")

# Windows folder-appearance files. Local presentation, never skill content.
SKIP_NAMES = {"desktop.ini"}

# Markdown link targets: [text](target). Reference-style and bare paths are not
# matched on purpose — an over-eager matcher that flags prose would get muted,
# and a muted check is the defect this script exists to prevent.
LINK = re.compile(r"\]\(\s*<?([^)>\s]+)>?\s*\)")


def is_local_reference(target: str) -> bool:
    """True for a link that names a file shipped beside the skill."""
    if target.startswith(("#", "/")):
        return False
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):  # http:, mailto:, ...
        return False
    return "." in Path(target.split("#", 1)[0].split("?", 1)[0]).name


def referenced_files(text: str) -> set[str]:
    """Relative paths a SKILL.md points at, as posix strings."""
    found: set[str] = set()
    for target in LINK.findall(text):
        if not is_local_reference(target):
            continue
        clean = target.split("#", 1)[0].split("?", 1)[0]
        found.add(Path(clean).as_posix().lstrip("./"))
    return found


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


def skill_payload(base: Path) -> dict[str, str]:
    """Every mirrorable file in one skill directory, keyed by relative path."""
    payload: dict[str, str] = {}
    if not base.exists():
        return payload
    for path in sorted(base.rglob("*")):
        if not path.is_file() or path.name in SKIP_NAMES:
            continue
        payload[path.relative_to(base).as_posix()] = normalized(path)
    return payload


def stray_skills(root: Path, known: set[str]) -> list[str]:
    """SKILL.md files below the canonical tree that validation never sees.

    `00-BRAIN\\skills\\_staged\\handoff\\` is tracked in git, differs from the
    live `handoff` skill, and is invisible to a `*/SKILL.md` glob. Reported as
    a warning rather than an error: it needs Chris's disposition (promote,
    delete, or move out of the canonical tree), and a validator should not
    fail a gate over a question nobody has answered yet.
    """
    if not root.exists():
        return []
    strays = []
    for path in sorted(root.rglob("SKILL.md")):
        rel = path.relative_to(root)
        if len(rel.parts) != 2 or rel.parts[0] not in known:
            strays.append(rel.as_posix())
    return strays


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

    canonical_payload: dict[str, dict[str, str]] = {}
    for name in sorted(canonical_names):
        path = CANONICAL / name / "SKILL.md"
        errors.extend(validate_skill(path))
        payload = skill_payload(CANONICAL / name)
        canonical_payload[name] = payload
        # A reference the canonical skill itself cannot satisfy is a broken
        # skill, not a broken mirror. Catch it here so --sync never propagates
        # a dead link into two mirrors and calls it done.
        for ref in sorted(referenced_files(payload.get("SKILL.md", ""))):
            if ref not in payload:
                errors.append(
                    f"00-BRAIN/SKILLS/{name}/SKILL.md: references '{ref}', "
                    "which does not exist in the canonical skill directory"
                )

    if errors:
        print("# SHARED SKILL VALIDATION — FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.sync:
        for mirror in MIRRORS:
            for name, payload in canonical_payload.items():
                for rel, text in payload.items():
                    target = mirror / name / rel
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
            canonical_files = canonical_payload[name]
            mirror_files = skill_payload(mirror / name)
            errors.extend(validate_skill(mirror / name / "SKILL.md"))

            for rel in sorted(set(canonical_files) - set(mirror_files)):
                errors.append(f"{mirror.relative_to(ROOT)}/{name}: missing file '{rel}'")
            for rel in sorted(set(mirror_files) - set(canonical_files)):
                errors.append(
                    f"{mirror.relative_to(ROOT)}/{name}: unexpected file '{rel}' "
                    "— not in the canonical skill; remove it by hand"
                )
            for rel in sorted(set(canonical_files) & set(mirror_files)):
                if mirror_files[rel] != canonical_files[rel]:
                    errors.append(
                        f"{mirror.relative_to(ROOT)}/{name}/{rel}: mirror "
                        f"{digest(mirror_files[rel])} != canonical {digest(canonical_files[rel])}"
                    )

            # The flag #99 condition itself, checked against the mirror the
            # agent actually reads rather than against the canonical tree.
            for ref in sorted(referenced_files(mirror_files.get("SKILL.md", ""))):
                if ref not in mirror_files:
                    errors.append(
                        f"{mirror.relative_to(ROOT)}/{name}/SKILL.md: references "
                        f"'{ref}', which is absent from this mirror"
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
        payload = canonical_payload[name]
        extra = len(payload) - 1
        suffix = f" (+{extra} file{'s' if extra != 1 else ''})" if extra else ""
        print(f"- {name}: {digest(payload['SKILL.md'])}{suffix}")

    for stray in stray_skills(CANONICAL, canonical_names):
        print(f"! WARNING: '{stray}' carries a SKILL.md but is not a canonical skill")
        print("  Not mirrored and not validated. Needs disposition: promote, delete, or move out.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
