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
My computer → `.ROOT` → Stop backup) and replacing it with a local mirror:
`D:\BACKUPS\.ROOT`, kept current by `00-BRAIN\scripts\backup_to_d_drive.ps1`
(robocopy `/MIR`) on a daily Windows Task Scheduler job ("ROOT Daily Backup to
D", 21:00). This covers everything Git doesn't track — journal, raw/, archive,
binaries. `G:\My Drive\.ROOT` remains a retained legacy recovery snapshot only;
neither it nor Drive sync is a working tree or AI boot target going forward.

Standing rules that involve the local machine:
- Real code (anything with a repo, venv, or node_modules) lives at `D:\DEV` + GitHub, never in the vault or its cloud backup (WHERE_IT_GOES.md § Format Rules).
- `C:\Users\chris\.ROOT\` is the sole exception to the normal no-work-in-profile rule; it is the live vault, not a mirror.
