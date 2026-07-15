#!/usr/bin/env python3
"""Classified monthly wiki lint for the eight hubs plus CASTLE.

Default mode reports findings without failing. --strict exits 1 only for
blockers: missing frontmatter or an index that links to a nonexistent page.
Expected selective-index omissions, planned PHYSICS links, and code examples
are separated from actionable review debt.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[2]
HUB_NAMES = (
    "AI_AUTOMATION_SYSTEMS", "BUSINESS", "EDUCATION", "PHYSICS",
    "PYTHON", "REVENUE_LAB", "SYSTEMS", "TECHNOLOGY",
)
HUBS = [ROOT / "03-WIKIS" / h for h in HUB_NAMES] + [
    ROOT / "00-BRAIN" / "CASTLE"
]
EXCLUDED_DIRS = {
    "raw", "99-ARCHIVE", ".git", ".obsidian", "Report Archive",
    "88-JOURNAL",
}
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FENCED = re.compile(r"(^|\n)(```|~~~).*?(\n\2)(?=\n|$)", re.S)
INLINE_CODE = re.compile(r"`[^`\n]+`")
SELECTIVE_INDEX_HUBS = {"BUSINESS", "PYTHON", "PHYSICS"}
PHYSICS_PLANNED_FOLDERS = {
    "concepts", "equations", "calculus-links", "problem-types",
    "worked-examples", "drills", "glossary", "flashcards", "diagrams",
    "common-errors", "parked-advanced",
}


def visible_text(text: str) -> str:
    return INLINE_CODE.sub("", FENCED.sub("\n", text))


def links(text: str):
    return WIKILINK.findall(visible_text(text))


def stem(target: str) -> str:
    return re.sub(
        r"\.md$", "", target.strip().split("/")[-1].strip(), flags=re.I
    ).lower()


def wiki_pages(hub: Path):
    wiki = hub / "wiki"
    if not wiki.is_dir():
        return []
    return [
        p for p in wiki.rglob("*.md")
        if not EXCLUDED_DIRS.intersection(p.relative_to(hub).parts)
    ]


def with_md(path: Path) -> Path:
    return path if path.suffix.lower() == ".md" else path.with_suffix(".md")


def target_exists(root: Path, hub: Path, source: Path, target: str,
                  known_stems: set[str]) -> bool:
    """Resolve qualified wikilinks as paths; use stem lookup only for bare links."""
    normalized = target.strip().replace("\\", "/")
    if not normalized:
        return True
    if "/" not in normalized:
        return stem(normalized) in known_stems

    if normalized.startswith("/"):
        candidates = [root / normalized.lstrip("/")]
    else:
        candidates = [
            source.parent / normalized,
            hub / "wiki" / normalized,
            hub / normalized,
            root / normalized,
        ]
    return any(with_md(candidate).resolve().is_file() for candidate in candidates)


def current_physics_stage(hub: Path) -> int | None:
    path = hub / "wiki" / "current-position.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"\bStage\s+(\d+)\b", text, re.I)
    return int(match.group(1)) if match else None


def is_active_physics_page(page: Path, text: str,
                           current_stage: int | None) -> bool:
    if page.name in {"current-position.md", "index.md"}:
        return True
    frontmatter = text.split("---", 2)[1] if text.lstrip().startswith("---") else ""
    if re.search(r"(?:^|[\s,\[])now(?:$|[\s,\]])", frontmatter, re.I):
        return True
    stage_match = re.search(r"stage-(\d+)", page.stem, re.I)
    return bool(stage_match and current_stage is not None
                and int(stage_match.group(1)) == current_stage)


def is_physics_planned(hub: Path, page: Path, target: str, text: str,
                       current_stage: int | None) -> bool:
    if hub.name != "PHYSICS":
        return False
    if is_active_physics_page(page, text, current_stage):
        return False
    parts = {p for p in target.replace("\\", "/").split("/") if p not in (".", "..")}
    return bool(parts & PHYSICS_PLANNED_FOLDERS)


def print_group(title: str, items, limit: int = 80):
    print(f"## {title} ({len(items)})")
    for line in items[:limit]:
        print(f"- {line}")
    if len(items) > limit:
        print(f"- ... {len(items) - limit} more (run against the named hub for detail)")
    if not items:
        print("- none")
    print()


def self_test() -> int:
    """Exercise both prior false-pass classes without filesystem writes."""
    root = Path("Z:/__root_wiki_lint_self_test__")
    hub = root / "03-WIKIS" / "PHYSICS"
    page = hub / "wiki" / "stages" / "stage-3-vectors.md"
    text = (
        "---\ntype: stage\ntags: [now, physics]\n---\n"
        "[[../concepts/vector-additoin]]\n"
    )
    # The misspelled stem exists "elsewhere" in the simulated vault index. A
    # path-qualified resolver must still reject it because the intended path does
    # not exist.
    known_stems = {"vector-additoin", page.stem.lower()}
    caught_path_typo = not target_exists(
        root, hub, page, "../concepts/vector-additoin", known_stems)
    active_not_planned = not is_physics_planned(
        hub, page, "../concepts/vector-additoin", text, 3)
    if caught_path_typo and active_not_planned:
        print("# WIKI LINT SELF-TEST - PASS")
        print("- qualified-path typo did not pass via unrelated matching stem")
        print("- active PHYSICS typo classified as blocker, not planned debt")
        return 0
    print("# WIKI LINT SELF-TEST - FAIL")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 when blocker-class findings exist")
    parser.add_argument("--fail-on-review", action="store_true",
                        help="also exit 1 when review debt exists")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable results")
    parser.add_argument("--self-test", action="store_true",
                        help="test path and active-PHYSICS classification in temp files")
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    all_md = [
        p for p in ROOT.rglob("*.md")
        if not EXCLUDED_DIRS.intersection(p.relative_to(ROOT).parts)
    ]
    known_stems = {p.stem.lower() for p in all_md}

    inbound = set()
    for page in all_md:
        text = page.read_text(encoding="utf-8", errors="replace")
        inbound.update(stem(t) for t in links(text) if stem(t))

    groups = defaultdict(list)

    for hub in HUBS:
        pages = wiki_pages(hub)
        if not pages:
            continue
        hub_rel = str(hub.relative_to(ROOT))
        physics_stage = current_physics_stage(hub) if hub.name == "PHYSICS" else None

        for page in pages:
            raw_text = page.read_text(encoding="utf-8", errors="replace")
            clean_targets = links(raw_text)
            raw_targets = WIKILINK.findall(raw_text)
            rel = str(page.relative_to(ROOT))

            if not raw_text.lstrip().startswith("---"):
                groups["blocker_missing_frontmatter"].append(f"`{rel}`")

            clean_unknown = {
                t for t in clean_targets
                if stem(t) and not target_exists(ROOT, hub, page, t, known_stems)
            }
            raw_unknown = {
                t for t in raw_targets
                if stem(t) and not target_exists(ROOT, hub, page, t, known_stems)
            }
            for target in sorted(raw_unknown - clean_unknown):
                groups["expected_code_false_positive"].append(
                    f"`{rel}` -> `[[{target}]]`"
                )
            for target in sorted(clean_unknown):
                item = f"`{rel}` -> `[[{target}]]`"
                if page.name == "log.md":
                    groups["expected_historical_log_link"].append(item)
                elif (hub.name == "PHYSICS"
                      and is_active_physics_page(page, raw_text, physics_stage)):
                    groups["blocker_active_physics_link"].append(item)
                elif is_physics_planned(
                        hub, page, target, raw_text, physics_stage):
                    groups["expected_planned_physics_link"].append(item)
                else:
                    groups["review_dead_link"].append(item)

        for page in pages:
            if page.name in ("index.md", "log.md"):
                continue
            text = page.read_text(encoding="utf-8", errors="replace")
            if not links(text) and page.stem.lower() not in inbound:
                bucket = ("expected_inactive_physics_draft"
                          if hub.name == "PHYSICS" else "review_orphan")
                groups[bucket].append(f"`{page.relative_to(ROOT)}`")

        index = hub / "wiki" / "index.md"
        if not index.exists():
            groups["blocker_missing_index"].append(f"`{hub_rel}`")
            continue

        index_text = index.read_text(encoding="utf-8", errors="replace")
        index_lower = index_text.lower()
        for page in pages:
            if page.name in ("index.md", "log.md"):
                continue
            if page.stem.lower() not in index_lower:
                item = (
                    f"`{hub_rel}` — missing from index: "
                    f"{page.relative_to(hub)}"
                )
                if hub.name in SELECTIVE_INDEX_HUBS:
                    groups["expected_selective_index"].append(item)
                else:
                    groups["review_index_omission"].append(item)

        for target in set(links(index_text)):
            if (stem(target)
                    and not target_exists(ROOT, hub, index, target, known_stems)):
                groups["blocker_dead_index_link"].append(
                    f"`{hub_rel}` -> `[[{target.strip()}]]`"
                )

    blockers = (
        len(groups["blocker_missing_frontmatter"])
        + len(groups["blocker_missing_index"])
        + len(groups["blocker_dead_index_link"])
        + len(groups["blocker_active_physics_link"])
    )
    review = (
        len(groups["review_dead_link"])
        + len(groups["review_orphan"])
        + len(groups["review_index_omission"])
    )
    expected = sum(
        len(groups[name]) for name in (
            "expected_code_false_positive",
            "expected_historical_log_link",
            "expected_planned_physics_link",
            "expected_selective_index",
            "expected_inactive_physics_draft",
        )
    )

    result = {
        "status": "BLOCKER" if blockers else ("REVIEW" if review else "PASS"),
        "scanned_hubs": len(HUBS),
        "vault_pages": len(all_md),
        "blockers": blockers,
        "review_debt": review,
        "expected": expected,
        "groups": {name: groups[name] for name in sorted(groups)},
    }
    if args.json:
        print(json.dumps(result, indent=2))
        return 1 if ((args.strict and blockers)
                     or (args.fail_on_review and review)) else 0

    print("# CLASSIFIED WIKI LINT REPORT")
    print(
        f"\nScanned hubs: {len(HUBS)} | vault pages: {len(all_md)} | "
        f"blockers: {blockers} | review debt: {review} | expected: {expected}\n"
    )

    print_group("BLOCKER — missing frontmatter",
                groups["blocker_missing_frontmatter"])
    print_group("BLOCKER — missing hub index",
                groups["blocker_missing_index"])
    print_group("BLOCKER — index links to nonexistent page",
                groups["blocker_dead_index_link"])
    print_group("BLOCKER — active PHYSICS links to nonexistent page",
                groups["blocker_active_physics_link"])
    print_group("REVIEW — unresolved dead links",
                groups["review_dead_link"])
    print_group("REVIEW — index omissions in exhaustive hubs",
                groups["review_index_omission"])
    print_group("REVIEW — orphan pages",
                groups["review_orphan"])
    print_group("EXPECTED — planned PHYSICS links",
                groups["expected_planned_physics_link"])
    print_group("EXPECTED — selective navigation indexes",
                groups["expected_selective_index"])
    print_group("EXPECTED — inactive PHYSICS drafts",
                groups["expected_inactive_physics_draft"])
    print_group("EXPECTED — code-fence false positives",
                groups["expected_code_false_positive"])
    print_group("EXPECTED — historical log links",
                groups["expected_historical_log_link"])

    print(
        f"**Classified totals:** blockers={blockers}; review={review}; "
        f"expected={expected}."
    )
    if (args.strict and blockers) or (args.fail_on_review and review):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
