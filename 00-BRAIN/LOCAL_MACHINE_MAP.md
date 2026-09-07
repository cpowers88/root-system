---
type: reference
timeline: reference
tags: []
---

# LOCAL_MACHINE_MAP.md — Local Machine Inventory (reference snapshot)
### Moved out of vault_map.md July 11, 2026 (slim pass). Environment inventory, not vault governance — load only when local-machine placement matters.
### Local-root cutover: July 13, 2026. Recheck against the live tree before relying on file-level detail.

```
C:\ (NVMe 954GB — Windows, apps, and the live .ROOT workspace)
├── Program Files\   ← installed apps including AutoCAD 2027
├── Users\chris\
│   └── .ROOT\        ← canonical working tree; all AI sessions and Obsidian use this copy
└── Windows\

D:\ (SATA SSD 1.8TB — storage only)
├── GAMES\
├── SCHOOL\          ← Chatt Tech archive + active KSU local files
├── DEV\             ← active\ (code on GitHub — cpowers88) + archive\
├── LIBRARY RESOURCES\ ← reference PDFs
├── House\           ← personal — NOT system content
└── ARCHIVE\         ← cold storage
```

## Google Drive — RELINKED 2026-08-16, and where to actually find it

> ### ❓ "Why don't I see `.ROOT` on Google Drive?"
>
> **Because mirrored computer folders never appear under My Drive.** They live at
> drive.google.com under **Computers → [device name] → `.ROOT`**. `G:\My Drive\` will
> never show it, and that is correct behaviour, not a missing backup.
>
> **This question has now been asked twice** (2026-08-16 and 2026-08-17). It is written here,
> in the machine/backup inventory, because that is where someone looks for it — a note about
> where the mirror appears does not belong in a daily cockpit that gets trimmed.

**Live state, measured 2026-08-17 from Drive's own config**
(`%LOCALAPPDATA%\Google\DriveFS\root_preference_sqlite.db`, `roots` table):

```
title .ROOT | root_path Users\chris\.ROOT | last_seen_absolute_path C:\Users\chris\.ROOT
sync_type 1 (mirror) | destination 1 (to Drive) | state 2 (active)
```

Read that table rather than trusting the UI or this paragraph — it is the authority on whether
the link exists.

**The July 17 retirement is history, not current state.** Drive was disconnected then because
it periodically rewrote every top-level `desktop.ini` in one batch, clobbering the folder-icon
`IconResource` pointers (diagnosed July 16), and its mount could not support the ACL setup
Codex's native sandbox needed (July 13). **Chris relinked it on 2026-08-16** with three
consequences stated and accepted: `88-JOURNAL` goes to Google, a live `.git` gets synced, and
a mirror propagates a mistake rather than protecting from one.

**The `.git` consequence fired within hours and is now permanently fixed** — Drive wrote
conflict copies into `.git\` (flag #102), so the gitdir was relocated to
`C:\Users\chris\.root-git`, a sibling directory Drive never sees. `.git` in the vault is now a
33-byte pointer file. Verified with Drive live and synced: zero conflict copies, `fetch` exit 0,
`fsck` clean.

**`C:\Users\chris\.ROOT\.tmp.driveupload` is Drive's own staging folder** — pending uploads
live there transiently. Items sitting in it means a sync is in flight, not that something is
broken. Do not delete it or add it to a cleanup pass.

### Backup — live and verified 2026-08-12

**Between July 17 and August 12, 2026 this section described a backup that had
never run.** The 2026-08-11 council review caught it; it was built, run, and
verified on 2026-08-12. Keep this paragraph — it is the worked example of the
failure class named in `.claude\CONTROL_INVENTORY.md`: a document asserting a
control, mistaken for the control existing.

| Copy | Path | Status |
|---|---|---|
| Local mirror | `D:\BACKUPS\.ROOT` | **Live.** 3,951 files / 3.38 GB, verified 2026-08-12 |
| Retention | `D:\BACKUPS\snapshots\YYYY-MM-DD_HHmm\` | Dated copy of the *previous* mirror, last 8 kept |
| Off-machine | GitHub | Tracked files only — excludes `88-JOURNAL`, every `raw\`, `77-INBOX`, `99-ARCHIVE`, all PDFs |
| Drive mirror | **Computers → [device] → `.ROOT`** on drive.google.com | **Live since 2026-08-16.** Not under My Drive — see the section above. Carries what GitHub excludes: `88-JOURNAL`, every `raw\`, 351 PDFs |
| ~~Stale~~ | ~~`G:\My Drive\desktop_folder_maybe\.ROOT`~~ | **Deleted by Chris 2026-08-16** (16,091 files, Aug 9 pre-restructure) before bringing the mirror live — the order that mattered. Drive now holds exactly one `.ROOT` tree |
| Unowned | `D:\ARCHIVE\.ROOT` | July 19 copy with a nested `.ROOT\.ROOT`. Nobody maintains it; do not treat it as a backup |

Driven by `00-BRAIN\scripts\backup_to_d_drive.ps1` on Windows Task Scheduler
job **"ROOT Daily Backup to D", daily 12:30**, `-StartWhenAvailable`. The task
runs `%LOCALAPPDATA%\Microsoft\WindowsApps\pwsh.exe` — the version-stable alias.
The absolute `Program Files\WindowsApps\Microsoft.PowerShell_7.6.4.0_...` path
also works but breaks on the next PowerShell update; do not "fix" the task by
substituting it.

Three guards, each tested 2026-08-12:

1. **Source guard** — refuses unless `00-BRAIN\AGENT.md` is present, so it
   cannot mirror an unknown tree.
2. **Destination sentinel** (`.ROOT_BACKUP_ROOT`) — refuses to `/MIR` into any
   folder it did not itself mark, because `/PURGE` deletes whatever is there.
   The sentinel is `/XF`-excluded; without that, `/MIR` deletes its own marker
   and the backup silently stops after exactly one successful run.
3. **Shrink tripwire** — refuses when the source lost >10% of files or bytes
   since the last run, and says so. `-Force` overrides. This is the guard that
   matters: a mirror protects against disk loss, **not** against a bulk script
   damaging many files (2026-08-10: 2,713 files), which `/MIR` would otherwise
   faithfully copy over the good backup. The dated snapshots are the recovery path.

`.pytest_cache` and `.pytest_tmp` under `02-LIBRARY\.PROJECTS\MCP_Bootcamp` are
ACL-locked and raise access-denied on enumeration; they are excluded as
regenerable pytest artifacts. Before that exclusion the job returned exit 9 —
a failure — on every run.

**⚠ Identify before deleting any second `.ROOT` you find. Corrected 2026-08-21** — this
paragraph previously read *"neither it nor Drive sync is a working tree or AI boot target
going forward,"* which was true in the July 17 retirement era and contradicts lines 39–54 of
this same file, where the **Aug 16 relink is recorded as live and measured**. Read as written,
it could authorise deleting the live off-machine backup — the only copy of `88-JOURNAL`, every
`raw\`, and 351 PDFs.

**Two standing rules, stated by Chris 2026-08-21. They are not in tension — read both.**

1. **Google Drive is the live backup. Do not delete it.** The mirror under **Computers →
   [device name] → `.ROOT`** at drive.google.com is `sync_type 1 (mirror)`, `state 2 (active)`
   per lines 39–45. It never appears under `My Drive`, which is precisely why it can read as a
   stray copy from another machine. It is the only off-machine copy of `88-JOURNAL`, every
   `raw\`, and 351 PDFs.
2. **WE DO NOT WORK IN THE GOOGLE DRIVE `.ROOT` FOLDER, EVER.** Not an edit, not a script
   target, not a boot target, not a "quick fix from the other machine." The sole working tree
   is `C:\Users\chris\.ROOT`; the campus laptop works through its git clone
   (`CAMPUS_LAPTOP_BUILD.md` §6). Backup and workspace are different jobs and Drive only has
   the first one.

**On the older snapshots** — `G:\My Drive\New folder\.ROOT`, and the `desktop_folder_maybe\.ROOT`
(16,091 files, Aug 9) that flag #102 records as still present: these are retirement-era
snapshots, not sync targets, and rule 2 covers them too. **Identify before deleting, and the
deletion is Chris's call, not an AI's** — an AI cannot distinguish a stale snapshot from the
live mirror by looking at a folder name, which is the entire reason this paragraph was wrong
before.

Standing rules that involve the local machine:
- Real code (anything with a repo, venv, or node_modules) lives at `D:\DEV` + GitHub, never in the vault or its cloud backup (WHERE_IT_GOES.md § Format Rules).
- `C:\Users\chris\.ROOT\` is the sole exception to the normal no-work-in-profile rule; it is the live vault, not a mirror.
