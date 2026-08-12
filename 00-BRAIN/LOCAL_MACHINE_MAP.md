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

Backup (updated July 17, 2026): Google Drive's **Computers → this PC → .ROOT**
sync is retired. Root cause: Drive periodically rewrote every top-level
`desktop.ini` in one batch, clobbering the folder-icon `IconResource` pointers
(diagnosed July 16), and Drive's mount also couldn't support the ACL setup
Codex's native sandbox needed (July 13). Rather than work around it with a
daily icon re-apply task, Chris is disconnecting the sync (Drive Preferences →
My computer → `.ROOT` → Stop backup) and replacing it with a local mirror.

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
| Stale | `G:\My Drive\New folder\.ROOT` | One-time manual copy, 2026-08-09. **Not** `G:\My Drive\.ROOT` — that path does not exist |
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

`G:\My Drive\New folder\.ROOT` is a stale snapshot only; neither it nor Drive
sync is a working tree or AI boot target going forward.

Standing rules that involve the local machine:
- Real code (anything with a repo, venv, or node_modules) lives at `D:\DEV` + GitHub, never in the vault or its cloud backup (WHERE_IT_GOES.md § Format Rules).
- `C:\Users\chris\.ROOT\` is the sole exception to the normal no-work-in-profile rule; it is the live vault, not a mirror.
