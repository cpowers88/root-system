---
type: map
timeline: reference
tags: [governance]
---

# WHERE_IT_GOES.md — File Placement + Naming Authority
### THE single source for where files go and what they are called. No other file carries these rules.
### Last updated: August 16, 2026 (corrected the stale `02-LIBRARY` line left by the `04-SCHOOL` promotion; added the `04-SCHOOL`/`03-WIKIS` provenance tiebreaker. Prior substantive version: July 25, 2026, wiki machine-interface reconciliation; earlier: 99-ARCHIVE\ARCHIVED_2026-07-11_WHERE_IT_GOES.md)
### Rule: One file, one home. If it fits two places, pick the more permanent one.

---

## Realm Check First

This file governs placement **inside .ROOT**. If the content belongs to another
realm entirely, route it there first — the live workspace entry is `C:\Users\chris\.ROOT\CLAUDE.md`:

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
Digital revenue-stream research, lane evidence/scoring?  → 03-WIKIS\REVENUE_LAB\
Verified external change with a material consequence?    → owning wiki evidence first, then 01-NORTH_STAR\radar.md
Everything else (life, school files, projects, artifacts, reviews) → .ROOT, tree below
```

There is no single knowledge-refinery hub — each wiki runs its own intake.
Active client-specific or private work lives in a separate client workspace or
repository outside `.ROOT`. Only sanitized lessons, reusable methods/assets,
approved case studies, and non-sensitive metadata return to `.ROOT`.

---

## Decision Tree — Where Does This File Go?

```
AI instruction, session log, system flag, or map? → 00-BRAIN\
Durable direction, current strategy, skill gaps, semester goal, or strategic review? → 01-NORTH_STAR\
Material external signal already supported in its evidence home? → 01-NORTH_STAR\radar.md
Tied to a specific KSU course? → 04-SCHOOL\[course]\
Has a deliverable, build, or launch goal? → 02-LIBRARY\.PROJECTS\[NAME]\
Reusable reference (book, concept, cheat sheet)? → 02-LIBRARY\[domain]\
Reusable client-facing capability asset or blank master? → 05-BUSINESS\06-Capability Library\ (or matching 05-BUSINESS folder)
Sanitized field lesson, approved case study, pricing model, or reusable proposal/SOW pattern? → 05-BUSINESS\
Active client-specific/private artifact or engagement workspace? → separate client workspace/repository outside `.ROOT`
Manual file dropped from outside `.ROOT`, or an automatic Obsidian web clipping? → 77-INBOX\ (clear weekly)
Personal reflection or private processing? → 88-JOURNAL\ (AIs do not read)
Old, inactive, deprecated but worth keeping? → 99-ARCHIVE\ (nothing gets deleted)
```

### `04-SCHOOL` vs `03-WIKIS` — the one tiebreaker (added 2026-08-16)

**Two rules above fire on the same physics note.** The Realm Check routes staged
learning content to `03-WIKIS\PHYSICS\`; the Decision Tree routes anything tied to
a KSU course to `04-SCHOOL\`. Both are correct, and the collision fires several
times a day once classes start. **The tiebreaker is provenance, not subject:**

| Ask this one question | Home |
|---|---|
| **KSU gave it to me** — lecture, textbook, D2L, syllabus, assignment prompt, transcript | `04-SCHOOL\[course]\` |
| **We made it** — stages, drills, retrieval checks, calculus-links, miss logs, current-position | `03-WIKIS\[hub]\` |
| **It will be graded** — drafts, problem sets, lab reports, the TCOM report | `04-SCHOOL\[course]\work\` |

*Did KSU give it to me, or did we make it?* — one question, no re-litigating.

This is an operationalization of the structural ruling Chris made 2026-08-12
(`02-LIBRARY` = consult and build with · `03-WIKIS` = what the system learned,
Chris never files into it · `04-SCHOOL` = what he is graded on), not a new rule.
It describes the tree as already built; nothing moves. **Confirm at the Aug 22
dress rehearsal by routing one real file through a `work\` bay.**

`77-INBOX\` is the single universal intake door — manual file drops and
automatic Obsidian clipper output both land here (`Clippings\` retired
2026-07-24; the Obsidian clipper setting now points here instead). Review
weekly and move keepers to one permanent home; it is not a storage
destination. **Routing out of the inbox includes the capture-verification
check — `00-BRAIN\WIKI_SHARED_LAYER.md` rule 9 (added 2026-08-30): the filed
copy is opened and verified on content, not existence, before the capture is
treated as held.**

---

## Naming Conventions — Canonical

| File type | Convention | Example |
|---|---|---|
| Session handoffs | `HANDOFF_MMDD_WHO.md` | `HANDOFF_0615_CLAUDE.md` |
| Daily task reports | `DAILY_YYYY-MM-DD.md` (one per day, append-only; template: `Session_Logs\DAILY_TEMPLATE.md`) | `DAILY_2026-07-09.md` |
| Session reports | `SESSION_REPORT_DATES_WHO.md` | `SESSION_REPORT_JUNE8-9_CLAUDE.md` |
| System-update packets | `Session_Logs\System Update Log\YYYY-MM-DD_TOPIC\` with required `SESSION_INDEX.md` | `2026-07-15_ROOT_REMEDIATION\` |
| Weekly reviews | `WEEKLY_STARTDAY-ENDDAY.md` | `WEEKLY_JUNE2-8.md` |
| Weekly plans (forward, day-by-day, Chris-marked-up; lives in `00-BRAIN\CASTLE\wiki\weekly-plans\`, distinct from the retrospective Weekly Review) | `weekly-plan-YYYY-MM-DD-to-YYYY-MM-DD.md` | `weekly-plan-2026-07-23-to-2026-07-26.md` |
| Monthly reviews | `MONTHLY_MONTH_YEAR.md` | `MONTHLY_JUNE_2026.md` |
| Quarterly audits | `QUARTERLY_Q#_YEAR.md` | `QUARTERLY_Q3_2026.md` |
| Field notes | `FIELDNOTES_DATE_TOPIC.md` | `FIELDNOTES_JUNE5_CONSTRUCTION.md` |
| Morning/Nightly logs | `MORNINGLYDATE.md` | `MORNINGLYJUNE13.md` |
| Project folders | Plain `NAME` (underscores inside name; no `Project-` prefix) | `TCG_POS` |
| Library folders | `##-DOMAIN` numbered, caps | `06-AUTOCAD` |
| Course notes | `##-TopicName.md` | `02-Kinematics.md` |
| Archived versions | `ARCHIVED_YYYY-MM-DD_filename.md` | `ARCHIVED_2026-07-11_ATLAS.md` |
| Shared canonical skills | `00-BRAIN\SKILLS\skill-name\SKILL.md` | `00-BRAIN\SKILLS\session-close\SKILL.md` |

**Handoff date format is MMDD numeric — not month name.**
Use `HANDOFF_0615_CLAUDE.md` not `HANDOFF_JUNE15_CLAUDE.md`.
Numeric format sorts correctly in Drive and Session_Logs.

### Case convention (decided 2026-07-25; kebab-case allowed same day)

**The case of a filename tells you whether it is a machine instruction
interface.** This is the same boundary `register:` draws in the Metadata
Standard below — one rule, two expressions.

- **ALL-CAPS `.md` → machine instruction interface.** Boot-chain and
  hub-archetype files keep caps: `AGENT.md`, `CLAUDE.md`, `CODEX.md`,
  `OPERATIONS.md`, `README.md`, `HOW_TO_USE.md`, `CHRIS_CORE.md`,
  `WHERE_IT_GOES.md`, `SYSTEM_FLAGS.md`, `NORTH_STAR.md`, `START_HERE.md`,
  `NOW.md`. These are the files that carry `register:`. Caps makes an
  instruction surface identifiable at a glance in any listing, and these
  filenames are referenced by name across dozens of files and by
  `validate_boot_chain.py`, `root_health.py`, and the skill-sync script —
  renaming them is precisely the stale-reference failure this system exists to
  prevent.
- **lowercase → everything else, going forward.** Notes, reports, wiki pages,
  plans, evidence, summaries. **`snake_case` and `kebab-case` are both
  acceptable** — the rule is lowercase, not one separator. **Match whatever the
  containing folder already uses**; a folder that is consistently one style
  keeps that style, because mixing separators inside one folder is the
  inconsistency this rule exists to prevent. `03-WIKIS` hubs are kebab-case
  (`source-map.md`, `current-position.md`) and stay kebab-case. When a folder
  has no established convention, either is fine — pick one and be consistent.
- **True acronyms stay capitalized inside a lowercase name:** `AI`, `MCP`,
  `SOW`. Write `AI_automation_notes.md` or `AI-automation-notes.md`, not
  `ai_automation_notes.md`.
- **Dated/templated names in the table above win** where they conflict — an
  existing convention like `DAILY_2026-07-09.md` is not a case violation.
- **No unilateral renames.** Existing ALL-CAPS content files are grandfathered.
  Rename one only when it is already being edited and the rename is cheap
  (no inbound `[[wikilink]]` or path reference). Anything with live inbound
  references stays put unless Chris asks — a rename that breaks a pointer costs
  more than the inconsistency it fixes.
- **Folders:** the current top-level realm names (`00-BRAIN`, `01-NORTH_STAR`,
  `03-WIKIS`, hub names, `CASTLE`) are settled and stay as they are. New
  subfolders are lowercase — snake_case or kebab-case, matching their parent.

**Do not copy these tables into other files.** vault_map and AGENT.md point here.
One copy, zero drift.

---

## The Folders — one line each (structure detail: vault_map.md)

- **00-BRAIN\** — AI instructions and coordination: AGENT.md (OS), capability
  profiles (CLAUDE/CODEX), CHRIS_CORE/CHRIS, vault_map, this file, SYSTEM_FLAGS,
  COLOR_MAP.yaml (edit it, then run `scripts\build_graph_colors.py` — never
  hand-edit graph.json). Subfolders: `HATS\` (optional modes — short, active
  prompts), `CASTLE\` (command-center wiki; owns `.ROOT\NOW.md`),
  `Session_Logs\` (DAILYs, templates, and active reports; local operating guide:
  `Session_Logs\README.md`; three evidence homes inside: `Report Archive\` for
  completed standalone reports/handoffs, `System Update Log\` for the monthly
  one-row-per-system-commit ledger plus dated multi-commit evidence packets,
  and `Closed Flags\` for the monthly closed-flag ledger — SYSTEM_FLAGS.md
  holds OPEN flags only),
  `scripts\` (build_graph_colors.py, frontmatter_audit.py,
  metadata_migration_plan.py, root_health.py, sync_shared_skills.py,
  validate_boot_chain.py, wiki_lint.py), plus
  `SKILLS\` as the canonical source for shared native skills. `.md` only except
  approved scripts. NOT here: course
  notes, project files, personal writing.
- **01-NORTH_STAR\** — durable direction in NORTH_STAR.md; progressive-loading
  router in README.md; and `Goals & Milestones\` for CURRENT_STRATEGY.md,
  `fall_2026_semester.md`, `capability_development_goal.md`,
  `value_production_goal.md`, and milestone evidence — that folder's own
  `OPERATIONS.md` is its machine rule set, and weekly plans live in CASTLE, not
  here; `System Contracts\` for North-Star-derived OS capability and
  return contracts. NOT here: generic AI governance, domain research, live projects,
  or session logs.
- **00-BRAIN\Session_Logs\** — daily logs, handoffs, retrospective weekly/monthly
  reviews, and their templates. NOT here: durable direction or live strategy.
- **01-NORTH_STAR\ (Watchtower)** — exactly two Watchtower files: operating contract in
  WATCHTOWER.md and material external-signal routing in radar.md. Evidence remains
  in the owning wiki; projects and strategy decisions never live here.
- **04-SCHOOL\** — course-file home, one folder per course
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
- **02-LIBRARY\** — reusable knowledge by reference domain: the `ref-<name>`
  piles plus `.PROJECTS\` (renamed July 15, 2026 to `REF-<NAME>`, then to
  lowercase `ref-<name>` between July 13-27 under the lowercase-everything-else
  naming rule; see `02-LIBRARY\README.md`). PDFs for books, `.md` for notes.
  NOT here: project files outside `.PROJECTS\`, and **not course files** —
  `00-school\` was promoted out to top-level `04-SCHOOL\` on 2026-08-12
  (`3f78fa4`, 105 references rewritten). Corrected here 2026-08-16; this line
  still described the pre-promotion tree.
- **05-BUSINESS\** — the reusable and sanitized money system: 01-Audit
  Templates, 02-Field Notes, 03-Case Studies, 04-Pricing Models, 05-Proposals
  & SOWs, 06-Capability Library (reusable client-facing assets indexed by APQC
  process). NOT here: active client-specific/private work (→ separate client
  workspace/repository outside `.ROOT`) or business reference books
  (→ 02-LIBRARY\ref-business).
- **77-INBOX\** — universal intake: manual external-file drops and automatic
  Obsidian clipping both land here (`Clippings\` retired 2026-07-24); nothing
  lives here past one weekly review.
- **88-JOURNAL\** — private; no AI reads this folder.
- **99-ARCHIVE\** — the safety net; nothing gets deleted, it gets archived
  as `ARCHIVED_DATE_filename.md`. Verify parent chains by NAME against the
  live tree (vault_map.md).

---

## Wiki Intake Boundary

Each of the eight `03-WIKIS` hubs handles its own source intake per its own
`OPERATIONS.md` (raw/ folder, ingest protocol, page format) — route new source
material by subject using the Realm Check table above. Shared wiki rules
(raw immutability, chunking, session minimums, lint, ingest discipline) live
once in `00-BRAIN\WIKI_SHARED_LAYER.md`.

**Hub archetype standard (what files a session may assume exist):** every hub
carries `OPERATIONS.md` (canonical local machine contract — the hub's entry
point; the `CLAUDE.md`/`AGENTS.md` loaders were removed 2026-08-10 and must not
return), `README.md` (short human entrance), `HOW_TO_USE.md` (human
workflow), `wiki\index.md` (catalog), and `wiki\log.md` (operational history).
No other file is universal. **Learning
engines** (PYTHON, PHYSICS, EDUCATION) additionally own `wiki\current-position.md`
as learner truth, and at full build-out a `learning-path`, `parking-lot`,
`templates\`, and stage machinery (EDUCATION grows these on demand).
**Research-retrieval and application-decision hubs** own no current-position
file — their `wiki\index.md` is the retrieval layer, and their Hub Contract
names the current-truth file. Do not retrofit learning scaffolding onto a
research hub or expect index-only navigation from a learning hub.

**Lane rules:** new AI/LLM/agent research routes to `AI_AUTOMATION_SYSTEMS` —
TECHNOLOGY's `ai-and-llm/` subfolder is closed inherited reference.
`02-LIBRARY\REF-AI-AUTOMATION` is an artifact/reference home, not a wiki
intake lane.

**Raw-intake rule:** if source material lands in `00-BRAIN\CASTLE\raw\`
that matches a `03-WIKIS` hub's charter (e.g., AI/LLM/agent docs), relocate
it to that hub's own `raw/` before processing — do not ingest it in place.
CASTLE's `raw\` is a triage/staging point, not a permanent intake lane;
CASTLE orients and sequences, it does not do a wiki's primary research
(`00-BRAIN\CASTLE\OPERATIONS.md`).

`02-LIBRARY\.raw ARCHIVE\` is a closed legacy source holding area, not an
intake lane. Add nothing new there. Because its name carries the raw boundary,
do not move, rename, delete, or edit its contents without Chris's explicit raw
exception. The hash-backed disposition of its 12 retained files is recorded in
`00-BRAIN\Session_Logs\System Update Log\2026-07-15_ROOT_REMEDIATION\ROOT_REMEDIATION_PHASE_6D_SOURCE_ROUTING_DISPOSITION_2026-07-15.md`.

When wiki knowledge becomes a client-facing or system artifact, the artifact
lives in the normal Second Brain location:
- reusable/sanitized audit method or business artifact → `05-BUSINESS`
- active client-specific/private work → separate client workspace/repository outside `.ROOT`
- active build artifact → `02-LIBRARY\.PROJECTS`
- stable reference material → `02-LIBRARY`
- system decision or handoff → `00-BRAIN\Session_Logs`

---

## Metadata Standard — One Copy, Defined Here

Every `.md` in `.ROOT` carries frontmatter:

```yaml
---
type: <what it is>      # os · hat · map · star · ops · guide · pointer · flags · template ·
                        # log · report · plan · tracker · project · note · reference · raw ·
                        # dashboard · board · strategy · worksheet (+ wiki-specific types)
timeline: <current action>      # now · next · later · parked · reference · log
stage: <static position>        # optional: 2 · phase-1 · foundation
status: <artifact condition>    # optional: active · ready · draft · paused · complete
reference_priority: <utility>   # optional: core · supporting · lookup
tags: [<topics...>]
---
```

**Timeline — exactly one property per file** (the action axis): `now` means
touch it now; `next` means on deck; `later` means intentionally deferred;
`parked` means inactive pending a decision or trigger; `reference` means use
when needed; `log` means historical record. Timeline answers only **when to
act**. A curriculum stage, roadmap phase, artifact status, or reference
priority cannot substitute for it.

**Independent optional properties:** `stage` records a stable curriculum or
roadmap position; `status` records the artifact's condition or workflow state;
`reference_priority` records usefulness as `core`, `supporting`, or `lookup`.
Values for `stage` and `status` may follow a realm's documented vocabulary, but
must be explicit non-empty scalars. Do not infer them from a filename.

**Topic tags — zero or more** (the categorical axis): the approved list and
its rationale live in `00-BRAIN\TAG_REGISTRY.md`, not duplicated here —
extend sparingly; a topic tag must group 3+ files or it's noise.

**`register:` — instruction-interface files only** (defined here 2026-07-25,
closing flag #84). It declares *who a file is written for and how it is meant to
be consumed*, so a loading AI knows whether it is reading an instruction to
execute or context to understand. **Exactly five approved values:**

| Value | Applies to | Register |
|---|---|---|
| `ai-directive` | canonical machine contracts — `AGENT.md`, `OPERATIONS.md`, hub `CLAUDE.md` | terse, absolute, executable |
| `ai-loader` | thin pointer files whose only job is routing a session into a chain | pointer only, no rules |
| `ai-profile` | surface capability profiles — `00-BRAIN\CLAUDE.md`, `CODEX.md` | strengths and access notes |
| `human-context` | human entrances — `README.md`, `HOW_TO_USE.md`, `START_HERE.md`, `CHRIS_CORE.md` | chunked, explanatory, written for Chris |
| `compatibility-pointer` | a retained file that exists only to redirect an older reference | supersession notice |

**A file that is not an instruction interface does not carry `register:` at
all.** Wiki content pages, reports, reviews, weekly plans, logs, and evidence
are described by `type:` — adding a register value to them invents a second
classification scheme for something `type:` already answers. Do not mint a new
value to describe a document's genre; if a file seems to need a sixth value,
that is the signal it should not carry the property.

Origin and scope decision: `vault-skeleton-design.md` §7.1 proposed the
property as a binary and §8.5 required validation rules before adoption;
neither gate was met and it spread by sibling precedent to 61 files and 8
values, two of them minted by the July 24–25 update's own output. The live
audit found the five values above applied correctly and consistently across 56
instruction-interface files, and three genre-describing values leaked onto five
non-instruction files. Chris scoped it to instruction interfaces on 2026-07-25;
the five leaks were stripped in the same pass.

**Transition rule:** legacy control tags (`now`, `priority/now`, `stage-NN`,
`phase-N`, and similar) remain audit-compatible until Phase 5 migrates their
realm. New or edited frontmatter uses properties. Once `timeline:` is present,
no legacy control tag may remain in `tags`; dual encoding is an error.

**Graph view (one vault):** one `.obsidian/graph.json` at `.ROOT` root.
Categorical (the MAP): one color per section + one per `03-WIKIS` hub;
archives, Report Archive, and 77-INBOX filtered out. Sequential ("what's
next"): search by property (`[timeline:now]` → `[timeline:next]` →
`[timeline:later]` → `[timeline:parked]` → `[timeline:reference]`), optionally
with `path:"03-WIKIS/[hub]"`. Query static position with `[stage:2]`, artifact
condition with `[status:active]`, reference usefulness with
`[reference_priority:core]`, and topics with `tag:#business`. Human-facing
color table: `START_HERE.md`.
Maintenance: Graph Color Maintenance skill in `AGENT.md`.

Rules: new file → frontmatter required at creation. Timeline changes only when
the action horizon changes; stage/status/reference priority change on their own
evidence. Never invent a second metadata scheme — extend this one.

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
*Last updated: August 16, 2026 (`02-LIBRARY` line corrected; `04-SCHOOL`/`03-WIKIS` provenance tiebreaker added) | Location: 00-BRAIN\WHERE_IT_GOES.md*
