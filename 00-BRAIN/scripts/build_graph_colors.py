#!/usr/bin/env python3
"""build_graph_colors.py — generate .obsidian/graph.json colorGroups from COLOR_MAP.yaml.

The canonical color registry is 00-BRAIN/COLOR_MAP.yaml. This script:
  1. Reads COLOR_MAP.yaml (no PyYAML needed — parses the file's restricted schema).
  2. Reads the existing .obsidian/graph.json and PRESERVES every key it does not
     own. It only replaces `colorGroups` and appends missing exclude terms to
     `search` (never removing terms a human added).
  3. Converts each color_hex to Obsidian's decimal RGB integer ((R<<16)+(G<<8)+B).
  4. Runs a drift check: any top-level folder (or 03-WIKIS subfolder) that has
     neither a color group nor an excluded_from_graph entry is reported as an
     action item. It is NEVER auto-assigned a color — add it to COLOR_MAP.yaml
     yourself so taxonomy changes stay deliberate.

Idempotent: running twice with an unchanged COLOR_MAP.yaml produces a
byte-identical graph.json.

Usage:  python build_graph_colors.py
(Paths are resolved relative to this file: 00-BRAIN/scripts/ → vault root.)
"""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent          # 00-BRAIN/scripts
BRAIN_DIR = SCRIPT_DIR.parent                          # 00-BRAIN
VAULT_ROOT = BRAIN_DIR.parent                          # .ROOT
COLOR_MAP = BRAIN_DIR / "COLOR_MAP.yaml"
GRAPH_JSON = VAULT_ROOT / ".obsidian" / "graph.json"

# Infrastructure folders the drift check never reports.
DRIFT_IGNORE = {".obsidian", ".claude", ".agents", ".git", ".trash", ".DS_Store"}


def parse_color_map(path: Path) -> dict:
    """Parse COLOR_MAP.yaml's restricted schema without PyYAML.

    Understands: top-level scalars, `groups:` (list of dicts with string/bool/
    inline-list values), `excluded_from_graph:` (list of strings). Comments and
    blank lines are ignored. Raises on anything it doesn't understand rather
    than guessing.
    """
    data = {"groups": [], "excluded_from_graph": []}
    section = None      # None | "groups" | "excluded_from_graph"
    current = None      # dict being built inside groups

    def strip_comment(s: str) -> str:
        out, in_str = [], False
        for ch in s:
            if ch == '"':
                in_str = not in_str
            if ch == "#" and not in_str:
                break
            out.append(ch)
        return "".join(out).rstrip()

    def parse_scalar(s: str):
        s = s.strip()
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1]
        if s in ("true", "false"):
            return s == "true"
        if s.startswith("[") and s.endswith("]"):
            inner = s[1:-1].strip()
            return [parse_scalar(x) for x in inner.split(",")] if inner else []
        return s

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = strip_comment(raw)
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        text = line.strip()

        if indent == 0:
            current = None
            if text == "groups:":
                section = "groups"
            elif text == "excluded_from_graph:":
                section = "excluded_from_graph"
            elif ":" in text:
                section = None
                key, _, val = text.partition(":")
                data[key.strip()] = parse_scalar(val)
            else:
                raise ValueError(f"COLOR_MAP.yaml: unrecognized line: {raw!r}")
            continue

        if section == "excluded_from_graph":
            if not text.startswith("- "):
                raise ValueError(f"COLOR_MAP.yaml: expected list item: {raw!r}")
            data["excluded_from_graph"].append(parse_scalar(text[2:]))
        elif section == "groups":
            if text.startswith("- "):
                current = {}
                data["groups"].append(current)
                text = text[2:]
            if current is None or ":" not in text:
                raise ValueError(f"COLOR_MAP.yaml: unrecognized line: {raw!r}")
            key, _, val = text.partition(":")
            current[key.strip()] = parse_scalar(val)
        else:
            raise ValueError(f"COLOR_MAP.yaml: unrecognized line: {raw!r}")

    return data


def hex_to_obsidian_rgb(color_hex: str) -> int:
    h = color_hex.lstrip("#")
    if len(h) != 6:
        raise ValueError(f"color_hex must be #RRGGBB, got {color_hex!r}")
    return (int(h[0:2], 16) << 16) + (int(h[2:4], 16) << 8) + int(h[4:6], 16)


def build_color_groups(groups: list) -> list:
    out = []
    for g in groups:
        query = f'path:"{g["path"]}"'
        for sub in g.get("exclude_subpaths", []):
            query += f' -path:"{sub}"'
        out.append({
            "query": query,
            "color": {"a": 1, "rgb": hex_to_obsidian_rgb(g["color_hex"])},
        })
    return out


def merge_excludes(search: str, excluded: list) -> str:
    """Append missing -path:"X" terms; never remove or reorder existing terms."""
    for folder in excluded:
        term = f'-path:"{folder}"'
        if term not in search:
            search = f"{search} {term}" if search else term
    return search


def drift_check(groups: list, excluded: list) -> list:
    """Report folders with neither a color group nor an exclusion. Never assigns."""
    group_paths = [g["path"] for g in groups]
    candidates = []
    for p in sorted(VAULT_ROOT.iterdir()):
        if p.is_dir() and p.name not in DRIFT_IGNORE:
            candidates.append(p.name)
    wikis = VAULT_ROOT / "03-WIKIS"
    if wikis.is_dir():
        for p in sorted(wikis.iterdir()):
            if p.is_dir() and p.name not in DRIFT_IGNORE:
                candidates.append(f"03-WIKIS/{p.name}")

    gaps = []
    for folder in candidates:
        colored = any(gp == folder or gp.startswith(folder + "/") for gp in group_paths)
        excl = any(folder == e or folder.startswith(e + "/") for e in excluded)
        if not (colored or excl):
            gaps.append(folder)
    return gaps


def main() -> int:
    cmap = parse_color_map(COLOR_MAP)
    groups, excluded = cmap["groups"], cmap["excluded_from_graph"]

    first_run = not GRAPH_JSON.exists()
    if first_run:
        graph = {"search": "", "colorGroups": []}
    else:
        graph = json.loads(GRAPH_JSON.read_text(encoding="utf-8"))

    graph["colorGroups"] = build_color_groups(groups)
    graph["search"] = merge_excludes(graph.get("search", ""), excluded)

    GRAPH_JSON.parent.mkdir(parents=True, exist_ok=True)
    GRAPH_JSON.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8", newline="\n")

    print(f"graph.json: {len(graph['colorGroups'])} color groups written "
          f"(from {COLOR_MAP.name}, updated {cmap.get('updated', '?')})")
    print(f"excluded from graph: {', '.join(excluded)}")
    if first_run:
        print("WARNING: graph.json did not exist — created fresh (first run). "
              "Open Obsidian's graph view once so it fills in display settings.")

    gaps = drift_check(groups, excluded)
    if gaps:
        print("\nDRIFT CHECK — folders with no color and no exclusion "
              "(action item for Chris/Operator — add to COLOR_MAP.yaml by hand):")
        for g in gaps:
            print(f"  - {g}")
    else:
        print("\nDRIFT CHECK — clean: every folder is either colored or excluded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
