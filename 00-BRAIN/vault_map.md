---
type: map
tags: [reference, governance]
---

# vault_map.md — Powers System Map (.ROOT)
### Navigation file. Two levels deep ON PURPOSE — see Map Rule below.
### Last updated: July 11, 2026 (slim pass: local-machine tree → LOCAL_MACHINE_MAP.md, dated stamps removed; prior version: 99-ARCHIVE\ARCHIVED_2026-07-11_vault_map.md)
### System: local C: workspace (truth) + Obsidian (capture/graph) + GitHub (code). G: is cloud backup only. Everything lives in .ROOT.

---

## The System in One Sentence

Everything lives in `.ROOT`. `00-BRAIN` governs. `01-NORTH_STAR` commands. `02-LIBRARY\00-SCHOOL` holds course files. `03-WIKIS` grow knowledge. `05-BUSINESS` makes it money. Chris decides.

## The Map Rule

This map stays **two levels deep**. File-level maps go stale within days and then lie.
When file-level truth is needed: look at the live tree. Never trust a written
file list older than the current session.

---

## G:\My Drive — Backup Only

```
G:\My Drive\.ROOT\  ← retained legacy recovery snapshot only; never an AI boot target or working tree.

**Live cloud backup:** Google Drive → **Computers → this PC → .ROOT**, synchronized
from `C:\Users\chris\.ROOT` by Drive for desktop.
```

## .ROOT — Verified Map

```
.ROOT\
├── START_HERE.md          ← human map + canonical color language
├── NOW.md                 ← Chris's morning page — maintained by the CASTLE
│
├── ...projectSuccess\     ← WATCHTOWER — trends, signals, opportunity radar
│   ├── WATCHTOWER.md      ← operating rules: what to track, weekly sweep, castle-gate routing
│   └── radar.md           ← the live signal board
│
├── 00-BRAIN\  ← governance + command — load AGENT.md first, then the relevant lane file
│   ├── AGENT.md           ← universal OS — load FIRST, every session, any engine
│   ├── CLAUDE.md / CODEX.md / ATLAS.md  ← engine lane files
│   ├── CHRIS_CORE.md      ← the person file (default load, second)
│   ├── CHRIS.md           ← full profile (monthly review / calibration only)
│   ├── vault_map.md       ← this file
│   ├── WHERE_IT_GOES.md   ← file placement + naming authority (+ Tag Standard)
│   ├── SYSTEM_FLAGS.md    ← open improvement flags — check at session start
│   ├── COLOR_MAP.yaml     ← machine-canon graph colors (edit it, run scripts\build_graph_colors.py)
│   ├── LOCAL_MACHINE_MAP.md ← C:/D: inventory (reference snapshot)
│   ├── HATS\              ← optional behavior modes (OPERATOR, EDUCATOR, subject hats + playbooks)
│   ├── CASTLE\            ← command center: OPERATIONS.md + wiki\ (phases, skills,
│   │                         proof-projects, decision-rules, maps); owns .ROOT\NOW.md
│   ├── scripts\           ← maintenance scripts (build_graph_colors.py, wiki_lint.py,
│   │                         frontmatter_audit.py, validate_boot_chain.py)
│   └── Session_Logs\      ← current handoffs + DAILY_YYYY-MM-DD.md + reports
│                             (Report Archive\ inside)
│
├── 01-NORTH_STAR\  ← the star
│   ├── NORTH_STAR.md      ← THE controlling document — nothing overrides it
│   ├── README.md / SKILL_GAP_ANALYSIS.md
│   ├── Weekly Reviews\    ← weeklies + monthlies + template
│   └── Goals & Milestones\
│
├── 02-LIBRARY\  ← reusable knowledge, projects, and school file home
│   ├── 00-SCHOOL\         ← course files: 01-CSE-Python, 02-Physics I, 03-TCOM,
│   │                         04-ECON, 05-ENGR, 99-EDG, OneNote, FallKSU.xlsx
│   ├── .PROJECTS\         ← build/project docs (plain NAME; code lives on GitHub)
│   ├── .raw ARCHIVE\      ← general raw source material
│   └── 01-PHYSICS … 10-HEALTH, 99-MISC  ← reference domains
│
├── 03-WIKIS\  ← seven knowledge hubs — folders inside the single .ROOT vault
│   ├── SYSTEMS\           ← system dynamics + ISYE spine (Sterman, Factory Physics, queuing)
│   ├── PYTHON\            ← Python/CS engine: stages 0–10
│   ├── EDUCATION\         ← general KSU support: TCOM, ECON, ENGR
│   ├── PHYSICS\           ← physics engine: stages 1–18
│   ├── BUSINESS\          ← business research, offers, pricing, audit method, delivery templates
│   ├── TECHNOLOGY\        ← tech landscape + applied technical reference;
│   │                         spine: 02-LIBRARY\08-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md
│   └── AI_AUTOMATION_SYSTEMS\ ← AI/agent research + .ROOT self-evolution proposals
│
├── 05-BUSINESS\  ← the money system
│   ├── 01-Audit Templates\ · 02-Field Notes\ · 03-Case Studies\
│   ├── 04-Pricing Models\ · 05-Proposals & SOWs\
│   └── 06-Capability Library\ ← APQC-indexed reusable client-facing assets
│
├── 77-INBOX\    ← capture landing zone — clear every weekly review (Clippings\ inside)
└── 99-ARCHIVE\  ← nothing gets deleted, it gets archived
```

**Tooling dotfolders at `.ROOT` root (not content, not in the map):** `.obsidian` — vault
config + generated graph.json; `.claude` / `.agents` — AI tool settings; `.codex` — project
Codex settings. A `.git` directory may be provisioned by local tooling, but this vault is
not itself a Git repository. Do not flag these tooling folders as strays.

**Boundaries:** the castle references, never absorbs. Each wiki refines its own
domain, never governs the system; wikis are folders inside the one `.ROOT` vault,
each with its own `CLAUDE.md` scope. Watchtower signals act only through the
castle's adding-a-profit-skill gate. Placement authority: `WHERE_IT_GOES.md`.
Local machine (C:/D:) inventory: `LOCAL_MACHINE_MAP.md`.

---

## Folder Verification — by NAME, not ID

Standing mechanism: before any write, confirm the parent chain traces to `.ROOT`
by NAME against the live tree. Folder IDs are retired — do not use them.

---
*Last updated: July 11, 2026 (slim pass) | Next review: weekly*
