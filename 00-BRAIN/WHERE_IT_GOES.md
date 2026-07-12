---
type: map
tags: [reference, governance]
---

# WHERE_IT_GOES.md — File Placement + Naming Authority
### THE single source for where files go and what they are called. No other file carries these rules.
### Last updated: July 11, 2026 (slim pass: folder narrative collapsed to one-liners — deep structure is vault_map.md's job; prior version: 99-ARCHIVE\ARCHIVED_2026-07-11_WHERE_IT_GOES.md)
### Rule: One file, one home. If it fits two places, pick the more permanent one.

---

## Realm Check First

This file governs placement **inside .ROOT**. If the content belongs to another
realm entirely, route it there first — realm-level routing authority is `G:\My Drive\CLAUDE.md`:

```
Roadmap, phase, skill sequencing, proof-project status? → CASTLE\
Business research, market direction, blank templates?   → 03-WIKIS\BUSINESS\
Staged learning content (Python/CS · physics)?          → 03-WIKIS\PYTHON\ · 03-WIKIS\PHYSICS\
General KSU support (TCOM/ECON/ENGR)?                    → 03-WIKIS\EDUCATION\
Tech-adoption landscape / skill-roadmap research /       → 03-WIKIS\TECHNOLOGY\
  applied technical reference (web frameworks, distributed
  systems, DevOps, data science)?
System dynamics / ISYE-prep content?                      → 03-WIKIS\SYSTEMS\
AI/agent research, .ROOT self-evolution proposals?       → 03-WIKIS\AI_AUTOMATION_SYSTEMS\
Everything else (life, school files, projects, artifacts, reviews) → .ROOT, tree below
```

There is no single knowledge-refinery hub — each wiki runs its own intake.
Filled/used client artifacts always land in .ROOT (05-BUSINESS), not in the wikis.

---

## Decision Tree — Where Does This File Go?

```
AI instruction, session log, system flag, or map? → 00-BRAIN\
Five-year plan, skill gaps, weekly/monthly review? → 01-NORTH_STAR\
Tied to a specific KSU course? → 02-LIBRARY\00-SCHOOL\[course]\
Has a deliverable, build, or launch goal? → 02-LIBRARY\.PROJECTS\[NAME]\
Reusable reference (book, concept, cheat sheet)? → 02-LIBRARY\[domain]\
Reusable client-facing capability asset? → 05-BUSINESS\06-Capability Library\
Clients, offers, pricing, proposals, field observations? → 05-BUSINESS\
Web clipping or unsorted quick capture? → 77-INBOX\ (root level — clear weekly)
Personal reflection or private processing? → 88-JOURNAL\ (AIs do not read)
Old, inactive, deprecated but worth keeping? → 99-ARCHIVE\ (nothing gets deleted)
```

`77-INBOX\Clippings\` receives Obsidian clipper output automatically — review weekly,
move keepers to their permanent home.

---

## Naming Conventions — Canonical

| File type | Convention | Example |
|---|---|---|
| Session handoffs | `HANDOFF_MMDD_WHO.md` | `HANDOFF_0615_CLAUDE.md` |
| Daily task reports | `DAILY_YYYY-MM-DD.md` (one per day, append-only; template: `Session_Logs\DAILY_TEMPLATE.md`) | `DAILY_2026-07-09.md` |
| Session reports | `SESSION_REPORT_DATES_WHO.md` | `SESSION_REPORT_JUNE8-9_CLAUDE.md` |
| Weekly reviews | `WEEKLY_STARTDAY-ENDDAY.md` | `WEEKLY_JUNE2-8.md` |
| Monthly reviews | `MONTHLY_MONTH_YEAR.md` | `MONTHLY_JUNE_2026.md` |
| Quarterly audits | `QUARTERLY_Q#_YEAR.md` | `QUARTERLY_Q3_2026.md` |
| Field notes | `FIELDNOTES_DATE_TOPIC.md` | `FIELDNOTES_JUNE5_CONSTRUCTION.md` |
| Morning/Nightly logs | `MORNINGLYDATE.md` | `MORNINGLYJUNE13.md` |
| Project folders | Plain `NAME` (underscores inside name; no `Project-` prefix) | `TCG_POS` |
| Library folders | `##-DOMAIN` numbered, caps | `06-AUTOCAD` |
| Course notes | `##-TopicName.md` | `02-Kinematics.md` |
| Archived versions | `ARCHIVED_YYYY-MM-DD_filename.md` | `ARCHIVED_2026-07-11_ATLAS.md` |

**Handoff date format is MMDD numeric — not month name.**
Use `HANDOFF_0615_CLAUDE.md` not `HANDOFF_JUNE15_CLAUDE.md`.
Numeric format sorts correctly in Drive and Session_Logs.

**Do not copy these tables into other files.** vault_map and AGENT.md point here.
One copy, zero drift.

---

## The Folders — one line each (structure detail: vault_map.md)

- **00-BRAIN\** — AI instructions and coordination: AGENT.md (OS), lane files
  (CLAUDE/CODEX/ATLAS), CHRIS_CORE/CHRIS, vault_map, this file, SYSTEM_FLAGS,
  COLOR_MAP.yaml (edit it, then run `scripts\build_graph_colors.py` — never
  hand-edit graph.json). Subfolders: `HATS\` (optional modes — short, active
  prompts), `CASTLE\` (command-center wiki; owns `.ROOT\NOW.md`),
  `Session_Logs\` (current handoffs + DAILYs + reports; `Report Archive\`
  inside), `scripts\` (build_graph_colors.py, wiki_lint.py,
  frontmatter_audit.py, validate_boot_chain.py). `.md` only. NOT here: course
  notes, project files, personal writing.
- **01-NORTH_STAR\** — NORTH_STAR.md, README.md, SKILL_GAP_ANALYSIS.md,
  `Weekly Reviews\`, `Goals & Milestones\`. NOT here: session logs, course
  notes, project files.
- **02-LIBRARY\00-SCHOOL\** — course-file home, one folder per course
  (01-CSE-Python, 02-Physics I, 03-TCOM, 04-ECON, 05-ENGR, 99-EDG deferred);
  no extra KSU shell. `FallKSU.xlsx` + `OneNote\` live directly here.
  **AI restriction: CSE 1321 and ENGR 1000 prohibit AI on submitted
  coursework** — concepts fine, submitted work is Chris's alone (EDG same
  rule if reactivated).
- **02-LIBRARY\.PROJECTS\** — one folder per build, plain `NAME\`; `Docs\`,
  `Code\` (reference only — real code lives local + GitHub; small single-file
  scripts allowed per Format Rules). Live project list and status:
  `.ROOT\NOW.md` + `00-BRAIN\CASTLE\wiki\`. NOT here: reference material,
  business templates.
- **02-LIBRARY\** — reusable knowledge by numbered domain (00-SCHOOL,
  01-PHYSICS … 10-HEALTH, 99-MISC). PDFs for books, `.md` for notes. NOT
  here: project files.
- **05-BUSINESS\** — the money system: 01-Audit Templates, 02-Field Notes,
  03-Case Studies, 04-Pricing Models, 05-Proposals & SOWs, 06-Capability
  Library (reusable client-facing assets indexed by APQC process). NOT here:
  business reference books (→ 02-LIBRARY\05-BUSINESS).
- **77-INBOX\** — landing zone; nothing lives here past one weekly review.
- **88-JOURNAL\** — private; no AI reads this folder.
- **99-ARCHIVE\** — the safety net; nothing gets deleted, it gets archived
  as `ARCHIVED_DATE_filename.md`. Verify parent chains by NAME against the
  live tree (vault_map.md).

---

## Wiki Intake Boundary

Each of the seven `03-WIKIS` hubs handles its own source intake per its own
`CLAUDE.md` (raw/ folder, ingest protocol, page format) — route new source
material by subject using the Realm Check table above. Shared wiki rules
(raw immutability, chunking, session minimums, lint, ingest discipline) live
once in `00-BRAIN\AGENT.md § Wiki Shared Layer`.

**Lane rules:** new AI/LLM/agent research routes to `AI_AUTOMATION_SYSTEMS` —
TECHNOLOGY's `ai-and-llm/` subfolder is closed inherited reference.
`02-LIBRARY\08-AI-AUTOMATION` is an artifact/reference home, not a wiki
intake lane.

When wiki knowledge becomes a client-facing or system artifact, the artifact
lives in the normal Second Brain location:
- audit method or business artifact → `05-BUSINESS`
- active build artifact → `02-LIBRARY\.PROJECTS`
- stable reference material → `02-LIBRARY`
- system decision or handoff → `00-BRAIN\Session_Logs`

---

## Tag Standard — One Copy, Defined Here

Every `.md` in `.ROOT` carries frontmatter:

```yaml
---
type: <what it is>      # os · hat · map · star · ops · guide · pointer · flags · template ·
                        # log · report · plan · tracker · project · note · reference · raw ·
                        # dashboard · board · strategy · worksheet (+ wiki-specific types)
tags: [<timeline>, <topics...>]
---
```

**Timeline tag — exactly one per file** (the sequential axis):
`now` · `next` · `later` · `parked` · `reference` — wikis may use their
native equivalents (`priority/now`, `stage-NN`, `phase-N`), same ramp.
Files that only record history use `log` instead of a timeline tag.

**Topic tags — zero or more** (the categorical axis): `governance`,
`north-star`, `watchtower`, `school`, `business`, `programming`,
`ai-automation`, `physics`, `math`, `project`, `audit`, `pricing`,
`client`, `meta-learning`, `raw`, `cs50p`, `econ` — extend sparingly;
a topic tag must group 3+ files or it's noise.

**Graph view (one vault):** one `.obsidian/graph.json` at `.ROOT` root.
Categorical (the MAP): one color per section + one per `03-WIKIS` hub;
archives, Report Archive, and 77-INBOX filtered out. Sequential ("what's
next"): filter the graph's search by timeline tag (`#now` → `#next` →
`#later` → `#parked` → `#reference`), optionally with
`path:"03-WIKIS/[hub]"`. Human-facing color table: `START_HERE.md`.
Maintenance: Graph Color Maintenance skill in `AGENT.md`.

Rules: new file → frontmatter required at creation. Timeline tags move
(now→reference etc.) at reviews or stage advances. Never invent a second
tagging scheme — extend this one.

---

## Format Rules

- `.md` for everything written — notes, plans, logs, templates, reference
- **Never create Google Docs.** Option B only: upload with `disableConversionToGoogleType: True`
- `.pdf` — syllabi, textbooks, official documents only
- `.py` / `.js` / `.sql` — small project scripts and single-file tools MAY live in
  `.ROOT` inside their project folder (e.g. tracker.py + academic.db). Larger
  codebases — anything with a repo, venv, or node_modules — live local
  (`D:\DEV`) + GitHub, never Drive; the `.git`/`.venv`/`node_modules`
  spot-check in AGENT.md still applies.
- `.txt` — quick captures in 88-JOURNAL only; convert to `.md` when permanent

---
*Last updated: July 11, 2026 (slim pass) | Location: 00-BRAIN\WHERE_IT_GOES.md*
