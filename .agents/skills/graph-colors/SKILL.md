---
name: graph-colors
description: Update the Obsidian graph's categorical colors after adding or changing a tag/path filter. Use when Chris asks to change graph colors, add a new color group, or after a new top-level tag/section needs its own graph color.
---

# Graph Color Maintenance

Categorical graph colors live in `.obsidian\graph.json`, generated from
`00-BRAIN\COLOR_MAP.yaml`. Sequential priority uses tag and path filters in
graph search.

## Steps

1. Never hand-edit `.obsidian\graph.json`'s `colorGroups` directly.
2. Edit `00-BRAIN\COLOR_MAP.yaml` instead.
3. Run `00-BRAIN\scripts\build_graph_colors.py` to regenerate `graph.json`.
