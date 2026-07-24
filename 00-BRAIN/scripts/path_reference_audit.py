#!/usr/bin/env python3
"""Read-only baseline audit for Markdown file links and anchors.

This first-pass prototype writes nothing. It scans the vault and emits a
machine-readable report to stdout when --json is supplied, or a concise
human-readable summary otherwise.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote


WIKILINK_RE = re.compile(r"!?(\[\[(?P<target>[^\]|]+)(?:\|[^\]]+)?\]\])")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)(?P<full>\[[^\]]*\]\((?P<target>[^)]+)\))")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
SKIP_DIRS = {".git", ".obsidian", ".trash", ".tmp.driveupload", "88-JOURNAL",
             ".venv", "venv", "node_modules", "__pycache__"}
ARCHIVE_DIR = "99-ARCHIVE"


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def slugify(heading: str) -> str:
    heading = re.sub(r"[`*_~]", "", heading).strip().lower()
    heading = re.sub(r"[^\w\s-]", "", heading, flags=re.UNICODE)
    return re.sub(r"\s+", "-", heading)


def headings(path: Path) -> set[str]:
    found: set[str] = set()
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError):
        return found
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            found.add(slugify(match.group(1)))
    return found


def markdown_files(root: Path, include_archive: bool) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        relative_parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in relative_parts):
            continue
        if not include_archive and ARCHIVE_DIR in relative_parts:
            continue
        files.append(path)
    return sorted(files)


def candidate_paths(root: Path, source: Path, target: str) -> list[Path]:
    target = unquote(target.strip()).replace("\\", "/")
    if target.startswith(".ROOT/"):
        target = target[len(".ROOT/") :]
    raw = Path(target)
    candidates: list[Path] = []
    if raw.is_absolute():
        candidates.append(raw)
    else:
        candidates.extend((source.parent / raw, root / raw))
    if raw.suffix == "":
        candidates.extend(path.with_suffix(".md") for path in list(candidates))
    return list(dict.fromkeys(path.resolve() for path in candidates))


def resolve_wikilink(root: Path, source: Path, target: str,
                     name_index: dict[str, list[Path]]) -> tuple[Path | None, list[Path]]:
    target = target.strip().replace("\\", "/")
    direct = [path for path in candidate_paths(root, source, target) if path.is_file()]
    if direct:
        return direct[0], direct
    name = Path(target).name
    matches = list(name_index.get(name, []))
    if not Path(name).suffix:
        matches += name_index.get(f"{name}.md", [])
    matches = list(dict.fromkeys(matches))
    if len(matches) == 1:
        return matches[0], matches
    return None, matches


def issue(kind: str, source: Path, line: int, target: str, root: Path, **extra: object) -> dict[str, object]:
    value: dict[str, object] = {
        "kind": kind,
        "source": rel(root, source),
        "line": line,
        "target": target,
    }
    value.update(extra)
    return value


def audit(root: Path, include_archive: bool) -> dict[str, object]:
    files = markdown_files(root, include_archive)
    file_set = set(files)
    name_index: dict[str, list[Path]] = {}
    for path in files:
        name_index.setdefault(path.name, []).append(path)
    issues: list[dict[str, object]] = []
    cache: dict[Path, set[str]] = {}

    for source in files:
        try:
            text = source.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            issues.append(issue("unreadable_source", source, 0, "", root, detail=str(exc)))
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in WIKILINK_RE.finditer(line):
                target = match.group("target").strip()
                anchor = None
                if "#" in target:
                    target, anchor = target.split("#", 1)
                resolved, matches = resolve_wikilink(root, source, target, name_index)
                if resolved is None and len(matches) > 1:
                    issues.append(issue("ambiguous_wikilink", source, line_no, target, root,
                                        candidates=[rel(root, item) for item in matches]))
                    continue
                if resolved is None:
                    issues.append(issue("unresolved_wikilink", source, line_no, target, root))
                    continue
                if anchor:
                    cache.setdefault(resolved, headings(resolved))
                    if slugify(anchor) not in cache[resolved]:
                        issues.append(issue("broken_anchor", source, line_no, f"{target}#{anchor}", root,
                                            resolved=rel(root, resolved), anchor=slugify(anchor)))

            for match in MARKDOWN_LINK_RE.finditer(line):
                target = match.group("target").strip().strip("<>")
                if not target or re.match(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|//)", target):
                    continue
                path_target, anchor = (target.split("#", 1) + [None])[:2] if "#" in target else (target, None)
                if not path_target:
                    candidates = [source]
                else:
                    candidates = [path for path in candidate_paths(root, source, path_target)
                                  if path in file_set or path.is_file()]
                if not candidates:
                    issues.append(issue("unresolved_markdown_link", source, line_no, target, root))
                elif anchor:
                    resolved = candidates[0]
                    cache.setdefault(resolved, headings(resolved))
                    if slugify(anchor) not in cache[resolved]:
                        issues.append(issue("broken_anchor", source, line_no, target, root,
                                            resolved=rel(root, resolved), anchor=slugify(anchor)))

    counts: dict[str, int] = {}
    for item in issues:
        kind = str(item["kind"])
        counts[kind] = counts.get(kind, 0) + 1
    return {
        "schema_version": "0.1",
        "tool": "path_reference_audit.py",
        "mode": "read-only-baseline-link-integrity",
        "root": str(root),
        "include_archive": include_archive,
        "files_scanned": len(files),
        "issue_counts": counts,
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--include-archive", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    report = audit(root, args.include_archive)
    if args.as_json:
        json.dump(report, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print(f"Scanned {report['files_scanned']} Markdown files under {root}")
        print(f"Issues: {sum(report['issue_counts'].values())}")
        for kind, count in sorted(report["issue_counts"].items()):
            print(f"  {kind}: {count}")
    return 1 if report["issues"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
