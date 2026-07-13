---
type: reference
tags: [reference]
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

Google Drive backup: `C:\Users\chris\.ROOT` is synced by Drive for desktop under
**Computers → this PC → .ROOT**. `G:\My Drive\.ROOT` is a retained legacy recovery
snapshot only; neither cloud location is a working tree or AI boot target.

Standing rules that involve the local machine:
- Real code (anything with a repo, venv, or node_modules) lives at `D:\DEV` + GitHub, never in the vault or its cloud backup (WHERE_IT_GOES.md § Format Rules).
- `C:\Users\chris\.ROOT\` is the sole exception to the normal no-work-in-profile rule; it is the live vault, not a mirror.
