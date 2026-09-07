---
name: graph-colors
description: Update the Obsidian graph's categorical colors after a tag or path filter changes. Use when Chris asks to change graph colors, add a color group, or give a new section its own graph color.
---

# Maintain Graph Colors

1. Never hand-edit `.obsidian\graph.json` color groups.
2. Edit `00-BRAIN\COLOR_MAP.yaml`.
3. Run `python 00-BRAIN\scripts\build_graph_colors.py`.
4. Confirm the generated graph configuration contains the intended filter and
   that the boot validator still passes.
