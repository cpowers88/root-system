---
type: map
timeline: reference
tags: [governance]
---

# vault_map.md — Powers System Map (.ROOT)
### Navigation file. Two levels deep ON PURPOSE — see Map Rule below.
### Last updated: July 14, 2026 (North Star/link audit + Revenue Lab graph-map reconciliation)
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
├── AGENTS.md / CLAUDE.md  ← Codex/Claude root boot pointers; rules remain in 00-BRAIN
├── START_HERE.md          ← human map + canonical color language
├── ROOT_OPERATING_MANUAL.md ← human operating and proof guide
├── NOW.md                 ← Chris's morning page — maintained by the CASTLE
│
├── ...projectSuccess\     ← WATCHTOWER — material external-change router; eyes, not hands
│   ├── WATCHTOWER.md      ← promotion threshold + evidence-to-test contract
│   └── radar.md           ← lean signal board; never a research library or project queue
│
├── 00-BRAIN\  ← governance + command — load AGENT.md first, then the relevant capability profile
│   ├── AGENT.md           ← universal OS — load FIRST, every session, any engine
│   ├── CLAUDE.md / CODEX.md / ATLAS.md  ← surface capability profiles
│   ├── CHRIS_CORE.md      ← the person file (default load, second)
│   ├── CHRIS.md           ← full profile (monthly review / calibration only)
│   ├── vault_map.md       ← this file
│   ├── WHERE_IT_GOES.md   ← file placement + naming authority (+ Metadata Standard)
│   ├── SYSTEM_FLAGS.md    ← open improvement flags — check at session start
│   ├── COLOR_MAP.yaml     ← machine-canon graph colors (edit it, run scripts\build_graph_colors.py)
│   ├── LOCAL_MACHINE_MAP.md ← C:/D: inventory (reference snapshot)
│   ├── HATS\              ← optional behavior modes (OPERATOR, EDUCATOR, subject hats + playbooks)
│   ├── SKILLS\            ← canonical shared skills; product discovery mirrors are generated
│   ├── CASTLE\            ← command center: OPERATIONS.md + wiki\ (phases, skills,
│   │                         proof-projects, decision-rules, maps); owns .ROOT\NOW.md
│   ├── scripts\           ← maintenance scripts — canonical inventory lives in
│   │                         WHERE_IT_GOES.md (7 as of July 15, 2026, incl.
│   │                         root_health.py and metadata_migration_plan.py)
│   └── Session_Logs\      ← README + DAILYs/templates + active reports;
│                             Report Archive\ = completed standalone reports;
│                             System Update Log\ = monthly ledger + dated evidence packets;
│                             Closed Flags\ = monthly closed-flag ledgers
│
├── 01-NORTH_STAR\  ← the star
│   ├── NORTH_STAR.md      ← THE controlling document — nothing overrides it
│   ├── README.md / SKILL_GAP_ANALYSIS.md
│   ├── System Contracts\  ← ROOT_CAPABILITY_CONTRACT.md; loaded for OS design/evolution audits
│   ├── Weekly Reviews\    ← weeklies + monthlies + template
│   └── Goals & Milestones\ ← CURRENT_STRATEGY.md + time-bounded prep/milestone evidence
│
├── 02-LIBRARY\  ← reusable knowledge, projects, and school file home
│   ├── 00-SCHOOL\         ← course files: 01-CSE-Python, 02-Physics I, 03-TCOM,
│   │                         04-ECON, 05-ENGR, 99-EDG, OneNote, FallKSU.xlsx
│   ├── .PROJECTS\         ← build/project docs (plain NAME; code lives on GitHub)
│   ├── .raw ARCHIVE\      ← general raw source material
│   └── REF-MATH … REF-MISC  ← reference domains (renamed July 15, 2026:
│                              REF- marks "reference pile, not a wiki or the
│                              money system"; empty domains archived; see
│                              02-LIBRARY\README.md)
│
├── 03-WIKIS\  ← eight knowledge hubs — folders inside the single .ROOT vault
│   ├── SYSTEMS\           ← system dynamics + ISYE spine (Sterman, Factory Physics, queuing)
│   ├── PYTHON\            ← Python/CS engine: stages 0–10
│   ├── EDUCATION\         ← general KSU support: TCOM, ECON, ENGR
│   ├── PHYSICS\           ← physics engine: stages 1–18
│   ├── BUSINESS\          ← business research, offers, pricing, audit method, delivery templates
│   ├── TECHNOLOGY\        ← tech landscape + applied technical reference;
│   │                         spine: 02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md
│   ├── AI_AUTOMATION_SYSTEMS\ ← AI/agent research + .ROOT self-evolution proposals
│   └── REVENUE_LAB\       ← digital revenue-lane evidence, scoring, and bounded tests
│
├── 05-BUSINESS\  ← reusable and sanitized money-system assets; no active client-private workspace
│   ├── 01-Audit Templates\ · 02-Field Notes\ · 03-Case Studies\
│   ├── 04-Pricing Models\ · 05-Proposals & SOWs\
│   └── 06-Capability Library\ ← APQC-indexed reusable client-facing assets
│
├── 77-INBOX\    ← manual external-file intake — clear every weekly review
├── Clippings\   ← automatic Obsidian web-clipping intake — clear every weekly review
└── 99-ARCHIVE\  ← nothing gets deleted, it gets archived
```

**Tooling dotfolders at `.ROOT` root (not content, not in the map):** `.obsidian` — vault
config + generated graph.json; `.claude` / `.agents` — AI tool settings; `.codex` — project
Codex settings; `.git` — the live repository metadata. Do not flag these tooling
folders as content strays or route ordinary notes into them. `.tmp.drivedownload`,
`.tmp.driveupload`, and `.trash` are Drive/Obsidian transient tooling paths and are
excluded from the graph; they are not content realms.

**Boundaries:** the castle references, never absorbs. Each wiki refines its own
domain, never governs the system; wikis are folders inside the one `.ROOT` vault,
each with its own section operating context. Watchtower signals retain evidence in
their owning wiki and act only through CASTLE gating, a bounded test, and measured
outcome. Placement authority: `WHERE_IT_GOES.md`.
Local machine (C:/D:) inventory: `LOCAL_MACHINE_MAP.md`.

Active client-specific/private work lives in a separate client workspace or
repository outside `.ROOT`; only sanitized lessons, reusable methods/assets,
approved case studies, and non-sensitive metadata return here.

---

## Folder Verification — by NAME, not ID

Standing mechanism: before any write, confirm the parent chain traces to `.ROOT`
by NAME against the live tree. Folder IDs are retired — do not use them.

---
*Last updated: July 14, 2026 (live-link and graph-map reconciliation) | Next review: weekly*
