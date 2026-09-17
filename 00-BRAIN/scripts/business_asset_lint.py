#!/usr/bin/env python3
"""Classified integrity lint for the reusable assets in ``05-BUSINESS``.

The wiki lint cannot cover this tree because it intentionally has no ``wiki``
subdirectory. This adapter checks the asset tree without reading private,
school, raw, or archived material.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[2]
ASSET_ROOT = ROOT / "05-BUSINESS"
TEMPLATE_INDEX = ASSET_ROOT / "TEMPLATE_INDEX.md"
CAPABILITY_ROOT = ASSET_ROOT / "06-Capability Library"
CAPABILITY_INDEX = CAPABILITY_ROOT / "CAPABILITY_LIBRARY_INDEX.md"
RESOLUTION_ROOTS = (
    "00-BRAIN",
    "01-NORTH_STAR",
    "02-LIBRARY",
    "03-WIKIS",
    "05-BUSINESS",
    "06-PROJECTS",
)
EXCLUDED_DIRS = {
    "raw",
    ".raw ARCHIVE",
    "99-ARCHIVE",
    ".git",
    ".obsidian",
    "Report Archive",
    "88-JOURNAL",
    "oracleJdk-26",
}
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FENCED = re.compile(r"(^|\n)(```|~~~).*?(\n\2)(?=\n|$)", re.S)
INLINE_CODE = re.compile(r"`[^`\n]+`")


def visible_text(text: str) -> str:
    return INLINE_CODE.sub("", FENCED.sub("\n", text))


def links(text: str) -> list[str]:
    return WIKILINK.findall(visible_text(text))


def stem(target: str) -> str:
    return re.sub(
        r"\.md$", "", target.strip().replace("\\", "/").split("/")[-1].strip(),
        flags=re.I,
    ).lower()


def markdown_pages(owner: Path) -> list[Path]:
    """Walk Markdown files without descending into excluded directories."""
    pages: list[Path] = []
    if not owner.is_dir():
        return pages
    for current, directories, files in os.walk(owner, topdown=True):
        directories[:] = [
            name for name in directories if name not in EXCLUDED_DIRS
        ]
        base = Path(current)
        pages.extend(
            base / name for name in files if name.lower().endswith(".md")
        )
    return pages


def asset_pages(asset_root: Path) -> list[Path]:
    return markdown_pages(asset_root)


def resolution_pages(root: Path) -> list[Path]:
    pages: list[Path] = []
    for name in RESOLUTION_ROOTS:
        owner = root / name
        if not owner.is_dir():
            continue
        pages.extend(markdown_pages(owner))
    return pages


def with_md(path: Path) -> Path:
    return path if path.suffix.lower() == ".md" else path.with_suffix(".md")


def target_exists(
    root: Path,
    asset_root: Path,
    source: Path,
    target: str,
    known_stems: set[str],
) -> bool:
    """Resolve qualified links as paths and bare links through allowed owners."""
    normalized = target.strip().replace("\\", "/")
    if not normalized:
        return True
    if "/" not in normalized:
        return stem(normalized) in known_stems
    candidates = (
        [root / normalized.lstrip("/")]
        if normalized.startswith("/")
        else [
            source.parent / normalized,
            asset_root / normalized,
            root / normalized,
        ]
    )
    return any(with_md(candidate).resolve().is_file() for candidate in candidates)


def frontmatter_type(text: str) -> str | None:
    if not (text.startswith("---\n") or text.startswith("---\r\n")):
        return None
    parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.M)
    if len(parts) < 3:
        return None
    match = re.search(r"^type:\s*([^#\n]+)", parts[1], re.M | re.I)
    return match.group(1).strip().lower() if match else None


def audit(root: Path, asset_root: Path) -> dict:
    groups: dict[str, list[str]] = defaultdict(list)
    pages = asset_pages(asset_root)
    known_stems = {page.stem.lower() for page in resolution_pages(root)}

    required_indexes = (
        asset_root / "TEMPLATE_INDEX.md",
        asset_root / "06-Capability Library" / "CAPABILITY_LIBRARY_INDEX.md",
    )
    for index in required_indexes:
        if not index.is_file():
            groups["blocker_missing_required_index"].append(
                f"`{index.relative_to(root)}`"
            )

    for page in pages:
        text = page.read_text(encoding="utf-8", errors="replace")
        rel = page.relative_to(root)
        if not (text.startswith("---\n") or text.startswith("---\r\n")):
            groups["blocker_frontmatter_not_at_byte_zero"].append(f"`{rel}`")
        for target in sorted(set(links(text))):
            if not stem(target) or target_exists(
                root, asset_root, page, target, known_stems
            ):
                continue
            item = f"`{rel}` -> `[[{target}]]`"
            bucket = (
                "blocker_dead_index_link"
                if page in required_indexes
                else "review_dead_link"
            )
            groups[bucket].append(item)

    if required_indexes[0].is_file():
        index_text = required_indexes[0].read_text(
            encoding="utf-8", errors="replace"
        ).lower()
        for page in pages:
            try:
                page.relative_to(asset_root / "06-Capability Library")
                in_capability = True
            except ValueError:
                in_capability = False
            if (
                not in_capability
                and page != required_indexes[0]
                and frontmatter_type(
                    page.read_text(encoding="utf-8", errors="replace")
                ) == "template"
                and page.stem.lower() not in index_text
            ):
                groups["review_template_index_omission"].append(
                    f"`{page.relative_to(root)}`"
                )

    if required_indexes[1].is_file():
        index_text = required_indexes[1].read_text(
            encoding="utf-8", errors="replace"
        ).lower()
        for page in pages:
            try:
                page.relative_to(asset_root / "06-Capability Library")
            except ValueError:
                continue
            if (
                page != required_indexes[1]
                and frontmatter_type(
                    page.read_text(encoding="utf-8", errors="replace")
                ) in {"asset", "template"}
                and page.name.lower() not in index_text
            ):
                groups["review_capability_index_omission"].append(
                    f"`{page.relative_to(root)}`"
                )

    blockers = sum(
        len(groups[name])
        for name in (
            "blocker_frontmatter_not_at_byte_zero",
            "blocker_missing_required_index",
            "blocker_dead_index_link",
        )
    )
    review = sum(
        len(groups[name])
        for name in (
            "review_dead_link",
            "review_template_index_omission",
            "review_capability_index_omission",
        )
    )
    return {
        "status": "BLOCKER" if blockers else ("REVIEW" if review else "PASS"),
        "asset_pages": len(pages),
        "blockers": blockers,
        "review_debt": review,
        "groups": {name: groups[name] for name in sorted(groups)},
    }


def write_fixture(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def self_test() -> int:
    """Prove typical, edge, and known failure classes in temporary trees."""
    with tempfile.TemporaryDirectory(prefix="root-business-asset-lint-") as temp:
        root = Path(temp)
        assets = root / "05-BUSINESS"
        fm = "---\ntype: {kind}\ntimeline: reference\n---\n\n"
        write_fixture(
            assets / "TEMPLATE_INDEX.md",
            fm.format(kind="map")
            + "[[01-Audit Templates/audit-template|Audit Template]]\n",
        )
        write_fixture(
            assets / "01-Audit Templates" / "audit-template.md",
            fm.format(kind="template") + "[[owner-method]]\n`[[code-example]]`\n",
        )
        write_fixture(
            assets / "06-Capability Library" / "CAPABILITY_LIBRARY_INDEX.md",
            fm.format(kind="map") + "`CAPABILITY_LIBRARY_INDEX.md`\n",
        )
        write_fixture(
            root / "03-WIKIS" / "BUSINESS" / "wiki" / "owner-method.md",
            fm.format(kind="method"),
        )
        clean = audit(root, assets)

        write_fixture(
            assets / "02-Field Notes" / "leading-space.md",
            " " + fm.format(kind="note"),
        )
        write_fixture(
            assets / "01-Audit Templates" / "unindexed-template.md",
            fm.format(kind="template") + "[[../methods/does-not-exist]]\n",
        )
        failed = audit(root, assets)
        groups = failed["groups"]
        checks = {
            "typical clean tree passes": clean["status"] == "PASS",
            "edge bare cross-owner link resolves": not clean["blockers"]
            and not clean["review_debt"],
            "leading-space frontmatter is blocked": len(
                groups.get("blocker_frontmatter_not_at_byte_zero", [])
            ) == 1,
            "dead relative method link is reported": len(
                groups.get("review_dead_link", [])
            ) == 1,
            "missing template row is reported": len(
                groups.get("review_template_index_omission", [])
            ) == 1,
        }
        if all(checks.values()):
            print("# BUSINESS ASSET LINT SELF-TEST - PASS")
            for name in checks:
                print(f"- {name}")
            return 0
        print("# BUSINESS ASSET LINT SELF-TEST - FAIL")
        for name, passed in checks.items():
            print(f"- {'PASS' if passed else 'FAIL'}: {name}")
        return 1


def print_group(title: str, items: list[str]) -> None:
    print(f"## {title} ({len(items)})")
    for item in items:
        print(f"- {item}")
    if not items:
        print("- none")
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--fail-on-review", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    result = audit(ROOT, ASSET_ROOT)
    exit_code = 1 if (
        (args.strict and result["blockers"])
        or (args.fail_on_review and result["review_debt"])
    ) else 0
    if args.json:
        print(json.dumps(result, indent=2))
        return exit_code

    print("# CLASSIFIED 05-BUSINESS ASSET LINT")
    print(
        f"\nAsset pages: {result['asset_pages']} | blockers: "
        f"{result['blockers']} | review debt: {result['review_debt']}\n"
    )
    groups = result["groups"]
    print_group(
        "BLOCKER — frontmatter not at byte zero",
        groups.get("blocker_frontmatter_not_at_byte_zero", []),
    )
    print_group(
        "BLOCKER — missing required index",
        groups.get("blocker_missing_required_index", []),
    )
    print_group(
        "BLOCKER — index links to nonexistent page",
        groups.get("blocker_dead_index_link", []),
    )
    print_group("REVIEW — unresolved links", groups.get("review_dead_link", []))
    print_group(
        "REVIEW — template index omissions",
        groups.get("review_template_index_omission", []),
    )
    print_group(
        "REVIEW — capability index omissions",
        groups.get("review_capability_index_omission", []),
    )
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
