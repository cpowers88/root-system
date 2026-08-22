---
type: report
timeline: now
status: proposed
tags: [review, structure, migration, backup, challenger]
created: 2026-08-12
---

# Review Packet — 04-SCHOOL migration and backup second pass

**For an independent challenger (Codex). Commissioned by Chris, 2026-08-12.**
Two commits by Claude Code today are consequential and have had **no independent
review** — only my own deterministic checks, which is the exact "presence
mistaken for function" shape the 2026-08-11 council named as finding C1.

| Commit | What it did |
|---|---|
| `8cab756` | `.ROOT` PAUSED; `backup_to_d_drive.ps1` rewritten and scheduled; 3 stale docs corrected; flags #97/#98 |
| `3f78fa4` | `02-LIBRARY/00-school` → `04-SCHOOL`; 105 refs rewritten across 46 live files |

## What I verified

- Boot chain **PASS** — 31 boot files, 1,351 live pages
- `root_health.py` **PASS WITH DEBT, exit 0** — 4 pre-existing CASTLE items, 1,520 files, 0 findings
- Zero residual **tracked** references to `00-school`
- Git records 103 renames, so `git revert 3f78fa4` is a one-command undo
- `safe_shell.sh --selftest` passed all three probes *before* the migration ran, including the Aug 10 glob shape
- The rewrite was dry-run against copies (46 files, 105 refs, 0 problems) before touching the tree
- All 30 `desktop.ini` under `04-SCHOOL` carry no `IconResource` — no stranded icons
- Backup re-verified after the `.folder-icons` change: 478/478 files, 165/165 `desktop.ini`

## What I know is NOT verified — start here

1. **`git grep` only searches tracked files.** My residual check inherited that
   blindness. A follow-up filesystem scan found two untracked/ignored files still
   naming the old path:
   - `.folder-icons\v1\created-desktop-ini.txt` (records `02-LIBRARY\00-SCHOOL\...`)
   - `02-LIBRARY\.PROJECTS\MCP_Bootcamp\Docs\codex-adaptive-learning-evidence.md`

   I have **not** dispositioned either. See challenge 2.

2. **Nothing outside the repo was checked.** Obsidian workspace/config, VS Code
   workspaces, OneNote links, scheduled tasks, and any Google Drive copy may still
   point at `02-LIBRARY\00-school`. Drive matters more than it did yesterday —
   Chris ruled today that My Drive is the intended school↔home link.

3. **`folder_icons.ps1` was rewritten but never re-run.** Its output manifest is
   stale (item 1). Unknown whether re-running it does the right thing.

## Claims I want challenged

**Challenge 1 — the live/historical split.** I rewrote 46 files and deliberately
left 29 untouched under `00-BRAIN/Session_Logs/` and `99-ARCHIVE/`, on the rule
that *a log saying `00-school` was true when it was written, and editing it would
falsify the record.* Is that rule right? And is the boundary drawn correctly — are
any of those 29 actually live documents that happen to live under `Session_Logs/`?
`SYSTEM_FLAGS.md`-adjacent material and closed-flag files are the likely edge.

**Challenge 2 — the two untracked misses.** Is `created-desktop-ini.txt` a
*record* (leave it, by the rule above) or a *working manifest* (rewrite it, because
something reads it)? I can argue both and have done neither.

**Challenge 3 — the backup second pass.** The global `/XF desktop.ini` was
stripping all 165 `desktop.ini` under `.folder-icons\v1\desktop-ini-backup\` —
the one directory whose entire purpose is preserving them. I added a second
robocopy pass using `/E`, not `/MIR`, reasoning that robocopy never purges what it
excludes (the mechanism that keeps the sentinel alive), so the parent mirror won't
delete what the second pass adds. **The accepted trade: a `desktop.ini` deleted
from the source lingers in the mirror until a full re-seed.** Is that the right
trade, and is the no-purge reasoning actually correct?

**Challenge 4 — quarantine instead of delete.** `.tmp.driveupload` (1,403 files)
and the empty `.trash` were moved to `D:\BACKUPS\quarantine\2026-08-12\` rather
than deleted, because both were excluded from the backup and a hard delete would
have been unrecoverable. Is quarantine-on-the-backup-disk sound, or does it just
move dead weight onto the disk the backup depends on?

**Challenge 5 — the structural ruling itself.** The split now asserted is:
`02-LIBRARY` = reference shelves and projects; `03-WIKIS` = what the system
learned, AI-grown, Chris never files into it; `04-SCHOOL` = what he is graded on.
Does that survive contact with the actual tree? Specifically: `02-LIBRARY` still
holds `.PROJECTS` (dot-prefixed, sorting as machine layer, holding real project
work) and 10 `ref-*` shelves.

## Open, not yet done

- No output bay. `04-SCHOOL` fixes *buried*; it does not answer where a TCOM draft
  in progress lives versus the course material it came from. Classes begin **Aug 24**.
- `tmp\`, `outputs\`, `...projectSuccess\` reviewed but not dispositioned.
- `claude_and_chris_direction.md` (the July 26 interview, with Chris's Round One
  answers) still sits at the vault root, unmined.
- Graph drift check now names `.vs` and `outputs` as uncolored and unexcluded.

## Load pattern — measured today, not yet acted on

Always-loaded chain on the Claude path, 13 files: **15,327 words** before any work
begins. Three files are 55% of it:

| File | Words |
|---|---|
| `ROOT_OPERATING_MANUAL.md` | 3,107 |
| `00-BRAIN\AGENT.md` | 2,675 |
| `00-BRAIN\WHERE_IT_GOES.md` | 2,637 |
| `00-BRAIN\SYSTEM_FLAGS.md` | 1,933 |
| `START_HERE.md` | 1,338 |
| `NOW.md` | 1,068 |
| *(remaining 7)* | 2,569 |

Note this is a **broader denominator** than the 6,773-word figure recorded on
Aug 10 — that measured a narrower set. The two numbers are not directly comparable
and the load should not be described as having doubled.

`.md` mass by section: `03-WIKIS` 1,345 files / 1.73M words · `99-ARCHIVE` 445 /
520K · **`00-BRAIN` 282 / 467K** · `02-LIBRARY` 109 / 128K · `05-BUSINESS` 32 /
25.5K · `04-SCHOOL` 23 / 45.8K · `01-NORTH_STAR` 14 / 17.1K.

The governance layer is the third-largest body of prose in the vault, ahead of
every working section. Council finding C2 — *the control plane consumes the study
window* — has a number now.
