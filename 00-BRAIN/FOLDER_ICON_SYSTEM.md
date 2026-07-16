---
type: guide
timeline: reference
tags: [governance]
status: active
---

# Folder Icon System

## Purpose

Give Windows Explorer a stable visual vocabulary for `.ROOT`. Major realms have
distinct icons and colors; repeated folder roles such as notes, templates, raw
sources, code, stages, and logs reuse the same visual identity.

## Implementation

- Source: Tabler Icons PNG package `3.44.0`, MIT license.
- Generated local assets: `.folder-icons\v1\` (hidden and system-marked).
- Installer and repair tool: `00-BRAIN\scripts\folder_icons.ps1`.
- Windows metadata: each eligible folder's existing `desktop.ini` is preserved,
  then an absolute `IconResource` entry is added or replaced.
- First-run backups of original metadata are stored under
  `.folder-icons\v1\desktop-ini-backup\`; folders that originally had no
  `desktop.ini` are listed in `created-desktop-ini.txt`.
- Persistence: `desktop.ini` receives hidden/system attributes and its folder
  receives the read-only customization attribute required by Explorer.

## Commands

```powershell
# Regenerate icons and the visual preview from official Tabler sources.
pwsh -File 00-BRAIN\scripts\folder_icons.ps1 -Mode Build

# Apply or repair assignments without downloading assets.
pwsh -File 00-BRAIN\scripts\folder_icons.ps1 -Mode Apply -RefreshExplorer

# Verify every eligible folder and write the local CSV audit.
pwsh -File 00-BRAIN\scripts\folder_icons.ps1 -Mode Audit

# Rebuild, apply, audit, and refresh in one operation.
pwsh -File 00-BRAIN\scripts\folder_icons.ps1 -Mode All -RefreshExplorer
```

Preview: `.folder-icons\v1\folder-icon-preview.png`.

## Boundaries

- `.ROOT` itself keeps Chris's existing tree icon.
- `88-JOURNAL` is skipped because AI may not read or write the private journal.
- Any folder named `raw` and `.raw ARCHIVE` are skipped because raw sources are
  immutable without an explicit exception.
- Git, temporary, cache, IDE, and application-state folders are skipped.
- `.folder-icons\` and `desktop.ini` remain local/Drive-backed rather than Git-
  tracked. The script and this guide are the reproducible source of truth.

## Color Changes

Colors and Tabler glyph names live in `Get-IconDefinitions` near the top of the
script. Change one definition, run `-Mode Build`, then run `-Mode Apply
-RefreshExplorer`. If Explorer holds an old thumbnail after a redesign, increment
the asset version folder in the script before rebuilding.
