---
type: reference
tags: [reference]
---

# LOCAL_MACHINE_MAP.md — Local Machine Inventory (reference snapshot)
### Moved out of vault_map.md July 11, 2026 (slim pass). Environment inventory, not vault governance — load only when local-machine placement matters.
### Snapshot verified June 14, 2026 (WizTree scan) — recheck against the live tree before relying on file-level detail.

```
C:\ (NVMe 954GB — Windows + apps only)
├── Program Files\   ← installed apps including AutoCAD 2027
├── Users\chris\     ← Windows user profile only — do not store work here
└── Windows\

D:\ (SATA SSD 1.8TB — storage only)
├── GAMES\
├── SCHOOL\          ← Chatt Tech archive + active KSU local files
├── DEV\             ← active\ (code on GitHub — cpowers88) + archive\
├── LIBRARY RESOURCES\ ← reference PDFs
├── House\           ← personal — NOT system content
└── ARCHIVE\         ← cold storage
```

G: = Google Drive stream (no local mirror of the system).

Standing rules that involve the local machine:
- Real code (anything with a repo, venv, or node_modules) lives at `D:\DEV` + GitHub, never Drive (WHERE_IT_GOES.md § Format Rules).
- `C:\Users\chris\` holds no system content — past local mirrors there were duplicates and were deleted.
