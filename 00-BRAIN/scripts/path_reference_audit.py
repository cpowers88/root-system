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


def link_scope(root: Path, source: Path) -> Path:
    """Use a hub's wiki root for Obsidian-style vault-relative links."""
    parts = source.relative_to(root).parts
    if "wiki" in parts:
        index = parts.index("wiki")
        if index >= 1 and (parts[0] == "03-WIKIS" or parts[:2] == ("00-BRAIN", "CASTLE")):
            return root.joinpath(*parts[: index + 1])
    return root


def issue(kind: str, source: Path, line: int, target: str, root: Path, **extra: object) -> dict[str, object]:
    value: dict[str, object] = {
        "kind": kind,
        "source": rel(root, source),
        "line": line,
        "target": target,
    }
    value.update(extra)
    return value


def load_baseline(path: Path | None) -> tuple[Path | None, list[dict[str, object]]]:
    if path is None:
        return None, []
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    return path.resolve(), list(data.get("rules", []))


def baseline_match(item: dict[str, object], rules: list[dict[str, object]]) -> dict[str, str] | None:
    source = str(item["source"]).replace("\\", "/")
    target = str(item["target"])
    for rule in rules:
        source_prefix = rule.get("source_prefix")
        target_prefix = rule.get("target_prefix")
        target_exact = rule.get("target_exact", [])
        if source_prefix and not source.startswith(str(source_prefix)):
            continue
        if target_prefix and not target.startswith(str(target_prefix)):
            continue
        if target_exact and target not in target_exact:
            continue
        return {
            "rule": str(rule.get("id", "unnamed")),
            "classification": str(rule.get("classification", "baselined")),
        }
    return None


def audit(root: Path, include_archive: bool,
          baseline_path: Path | None = None) -> dict[str, object]:
    files = markdown_files(root, include_archive)
    file_set = set(files)
    index_cache: dict[Path, dict[str, list[Path]]] = {}
    issues: list[dict[str, object]] = []
    cache: dict[Path, set[str]] = {}

    for source in files:
        try:
            text = source.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            issues.append(issue("unreadable_source", source, 0, "", root, detail=str(exc)))
            continue
        scope = link_scope(root, source)
        if scope not in index_cache:
            scope_files = files if scope == root else [path for path in files if path.is_relative_to(scope)]
            scoped_index: dict[str, list[Path]] = {}
            for path in scope_files:
                scoped_index.setdefault(path.name, []).append(path)
            index_cache[scope] = scoped_index
        name_index = index_cache[scope]
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in WIKILINK_RE.finditer(line):
                target = match.group("target").strip()
                anchor = None
                if "#" in target:
                    target, anchor = target.split("#", 1)
                resolved, matches = resolve_wikilink(scope, source, target, name_index)
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

    baseline_path, baseline_rules = load_baseline(baseline_path)
    baseline_counts: dict[str, int] = {}
    for item in issues:
        match = baseline_match(item, baseline_rules)
        if match:
            item["baseline_rule"] = match["rule"]
            item["classification"] = match["classification"]
            baseline_counts[match["classification"]] = baseline_counts.get(match["classification"], 0) + 1
        else:
            item["classification"] = "unbaselined"
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
        "baseline": str(baseline_path) if baseline_path else None,
        "files_scanned": len(files),
        "issue_counts": counts,
        "baseline_counts": baseline_counts,
        "baselined_count": sum(baseline_counts.values()),
        "unbaselined_count": len(issues) - sum(baseline_counts.values()),
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--include-archive", action="store_true")
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    report = audit(root, args.include_archive, args.baseline)
    if args.as_json:
        json.dump(report, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print(f"Scanned {report['files_scanned']} Markdown files under {root}")
        print(f"Issues: {sum(report['issue_counts'].values())}")
        print(f"Baselined: {report['baselined_count']}")
        print(f"Unbaselined: {report['unbaselined_count']}")
        for kind, count in sorted(report["issue_counts"].items()):
            print(f"  {kind}: {count}")
    return 1 if report["unbaselined_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
