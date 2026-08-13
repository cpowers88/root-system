---
type: plan
timeline: now
register: system-review
status: active
tags: [update, structure, instruction-layer, governance, plan]
created: 2026-08-12
session_date: 2026-08-12
---

# `.ROOT` Update — Live Plan

> **This is the controlling plan for the current update. It is LIVE and evolves.**
> If you are a fresh session picking this up: read this file before proposing any
> update work. Do not re-derive the plan from conversation — extend this file.
> **Every completed item gets marked here in the same session it is completed**,
> because council finding C1 is that this vault detects correctly and then fails to
> propagate. A plan that lags reality is the defect, not the record.

> **Companion — read after this file:** `claude_report_2026-08-12_friday_readiness.md`
> (this folder). It carries the root cause of the repeated stalls, four corrections to
> this plan measured live on 2026-08-12 evening, the one-day execution sequence for
> Thursday Aug 13, and the proposed pass/fail definition of the Friday Aug 14 morning test.

## Where this stands

Chris paused `.ROOT` on 2026-08-12 and directed the runway (now → Aug 24) at four
things in his own order: `.ROOT` into good operating and upgrading order, his own
comfort with the folder structure and how work moves through it, calculus review,
and TCOM structure. **This plan covers the first two.** Sequencing authority is
Chris's; AI proposes optimal pathways and does not re-order silently.

The update's optimization target was named on 2026-08-10 and has not changed:
**pathways, not names.** How much an agent must read and how work moves — not what
folders are called.

## Constraints that govern every item below

1. **`.ROOT` is PAUSED** until Chris types `OK TO START`. Scope: the PAUSED block in
   `NOW.md`. Chris-directed system work continues; that is the point of the pause.
2. **Fixed dates are exempt from the pause:** Aug 17 flag #57 syllabus escalation,
   Aug 22 rehearsal, **Aug 24 classes**, HP Victus wipe (unscheduled, needs a full session).
3. **File Safety 12** — bulk or scripted work requires **both** copy-first and
   `00-BRAIN\scripts\safe_shell.sh`. Run it via
   `wsl -e bash -lc "cd /mnt/c/Users/chris/.ROOT && 00-BRAIN/scripts/safe_shell.sh ..."`.
   Run `--selftest` first; it must PASS all three probes before bulk work.
4. **The `PreToolUse` gate covers `Bash` and NOT `PowerShell`** (flag #96). The
   2026-08-10 incident that caused 2,713 corrupted files was a PowerShell script.
   **Do not run bulk rewrites through PowerShell.** Chris denied two such commands
   on Aug 12 and was right both times.
5. **Never run an untested bulk-rewrite construct against the working tree.** Dry-run
   against copies, verify, then apply. This is the rule Aug 10 broke.
6. **Do not dedupe `raw\` on hash** (flag #97). Filenames are the only record of what
   is missing. AI may not write under `raw\` at all (`NORTH_STAR.md` §3).
7. **Historical records are not rewritten.** A log saying `00-school` was true when
   written. Rewriting `Session_Logs\` or `99-ARCHIVE\` to match today falsifies the record.
8. **Do not self-approve governance doctrine.** Frame, audit, implement and validate an
   *approved* change; do not originate a high-impact doctrine Chris has not authorized.

## The structural ruling already made (2026-08-12)

Three nouns, and the one sentence Chris can hold:

| | |
|---|---|
| `02-LIBRARY` | reference shelves and projects — what he consults and builds with |
| `03-WIKIS` | **what the system learned** — AI-grown, messy by permission, he never files into it |
| `04-SCHOOL` | **what he is graded on** |

This is what makes background AI ingestion safe to run: it lands in `03-WIKIS`, which
Chris does not navigate.

---

## DONE — 2026-08-12

| # | Item | Commit |
|---|---|---|
| 1 | `.ROOT` PAUSED; scope in `NOW.md`, mirrored to `MORNING_BRIEF.md`, banner in `SYSTEM_FLAGS.md` | `8cab756` |
| 2 | Backup built, guarded (3 negative-tested guards), scheduled, verified | `8cab756` |
| 3 | Three stale documents corrected in the same session (`START_HERE`, `vault_map`, `LOCAL_MACHINE_MAP`) | `8cab756` |
| 4 | Flag #97 opened; destructive repair blocked in writing at `WIKI_SHARED_LAYER.md` rule 1 | `8cab756` |
| 5 | `.folder-icons` un-excluded + second pass for its 165 `desktop.ini` | `8cab756` |
| 6 | **Level 0 structure:** `02-LIBRARY\00-school` → `04-SCHOOL`, 105 refs across 46 live files | `3f78fa4` |
| 7 | `.tmp.driveupload` (1,403) + `.trash` quarantined to `D:\BACKUPS\quarantine\2026-08-12\` | `3f78fa4` |
| 8 | Backup defects found by Codex review fixed; records reconciled to live state | `2a9caf5` |
| 9 | **Council step 1:** `raw\` recovery list, nothing deleted | `d5b06ff` |

**Verified state after 9:** boot chain PASS (31 files, 1,351 live pages); `root_health.py`
PASS WITH DEBT exit 0 (4 pre-existing CASTLE items, 0 findings); scheduled backup
`LastTaskResult 0`, snapshots 8/8 marked complete.

---

## REMAINING

### Phase A — Level 0 leftovers (small, no dependencies)

| Item | Ruling | Status |
|---|---|---|
| `tmp\` — 259 files / 29 MB PDF-extraction scratch | No overlap with the 5 lost sources (checked). Excluded from **both** GitHub and the D: backup | ✅ **RULED 2026-08-12: DELETE** |
| `outputs\` — `real_world_dataset_opportunity_map_2026-07-16` (xlsx + 4 charts) | Closest thing in the vault to an executed analysis with a delivered artifact — the evidence class the company objective needs. **Keep its build input `tmp\spreadsheets\` with it**, exempt from the `tmp\` delete | ✅ **RULED 2026-08-12: KEEP, move into `02-LIBRARY`** |
| `...projectSuccess\` — holds `radar.md`, `WATCHTOWER.md` | WATCHTOWER is a real `.ROOT` concept; `radar.md` belongs with it | ✅ **RULED 2026-08-12: keep both files → `01-NORTH_STAR\`, kill the folder** |
| `EVENING_READING.md` | **STAYS at root** — generated dashboard, peer of `MORNING_BRIEF.md` | settled |
| `needs_for_physics.md` | **STAYS** — live calculus–physics bridge scratch, Jul 30–Aug 23 sprint, destination already documented in `PHYSICS\wiki\calculus-links\` | settled |
| ~~`claude_and_chris_direction.md` moves to `01-NORTH_STAR\`~~ | **⚠ STALE ENTRY — corrected 2026-08-12 evening.** Chris had already moved it. It is live at **`01-NORTH_STAR\claude_and_chris_direction.md`**; a second copy is a historical record in `System Update Log\2026-07-24_ROOT_ARCHITECTURE_UPDATE\` and stays there. **Phase F's "root, 31 KB" is stale for the same reason** | ✅ **ALREADY DONE by Chris** |
| Graph drift: `.vs` and `outputs` uncolored/unexcluded | `outputs\` is now ruled — add both to `COLOR_MAP.yaml` after the move | **unblocked, to do Thursday** |

### Phase B — The archive rotation (NO LONGER A BLOCKER — corrected 2026-08-12 evening)

**⚠ CORRECTED. This section previously read "The Aug 3–9 weekly review does not exist"
and named itself the blocker gating Phase C. That was already false when written.**
`WEEKLY_AUGUST3-9.md` was filed 2026-08-12 at 15:31 (committed in `7b95c12`,
`status: complete`, 978 words), and the Aug 6–9 DAILY files were rotated to
`Report Archive\` the same day. The plan was last edited at 18:54 — over three hours
after the blocker cleared — and still carried it. **This is council finding C1 occurring
inside the plan that warns about C1.** Evidence and method:
`claude_report_2026-08-12_friday_readiness.md` §2.2 and §3, in this folder.

**Phase C is unblocked.** The loose-file count was also wrong: **34 loose files, 31 of
them `.md`**, not 37.

`AGENT.md:240` is correct and does not change. Three items remain, only one of which is work:

| Item | State | Action |
|---|---|---|
| `DAILY_2026-08-02.md` | Its weekly (`WEEKLY_JULY27-AUGUST2.md`) is on file | **Archivable immediately** |
| `DAILY_2026-07-20` … `DAILY_2026-07-26` (7 files) | **No `WEEKLY_JULY20-26` exists and none will** — that period closed at monthly level in `MONTHLY_JULY_2026.md`. The archive rule keys on a weekly that will never be written | **Needs Chris's ruling:** accept the monthly as the authorizing close, then rotate. Do not backfill a weekly for a closed month — that is writing history |
| `DAILY_2026-07-16.md` | Loose file **and** `ARCHIVED_2026-07-16_DAILY_2026-07-16.md` both exist, with **different bodies** (940 vs 6,561 words) | Disposition before rotating — do not move blind |

**Gap to record:** `AGENT.md:240` has no branch for a week closed at monthly level. One
clause, not a rewrite.

### Phase C — `00-BRAIN` structure (UNBLOCKED — B was never the blocker it claimed)

Measured 2026-08-12:

| | Files | KWords | |
|---|---|---|---|
| `Session_Logs\` | 202 | 361.3 | 77% of `00-BRAIN` — history, not governance |
| `CASTLE\` | 71 | 79.4 | sequencing layer |
| `hats\` | 13 | 7.7 | the ONLY conditional-load layer |
| `skills\` | 17 | 3.6 | |
| 19 loose `.md` | 19 | ~17.0 | **the actual instruction layer** |

`Session_Logs` breakdown: `System Update Log` 87 · `Report Archive` 44 · loose reports
32 · handoffs 19 · DAILY 17 · closed flags 3.

**C-open ran 2026-08-12. Three findings:**

- **C-1 → flag #99 (real, and worse than the council said).** `sync_shared_skills.py`
  mirrors `SKILL.md` only, not skill directories. `writing-for-agents\SKILL.md` links
  twice to `SKILL-MECHANICS.md`, which is **absent from both mirrors**. `--check` returns
  PASS exit 0 over it, **and `--sync` — the documented remedy — does not fix it.**
  `root_health.py:178` calls `--check`, so the health gate inherited the false PASS all
  day. Fix: mirror whole directories, and fail when a `SKILL.md` references an absent file.
- **C-2 (downgraded — do not inflate this).** Instruction files spell `00-BRAIN\SKILLS\`
  and `HATS\` (7 refs each); the real folders are `skills` and `hats`. **Tested from WSL:
  `/mnt/c` is case-INsensitive, both paths resolve.** So this is a documentation-vs-actual
  inconsistency, **not** a live breakage. Worth tidying, not worth a flag.
- **C-3 (residue).** `00-BRAIN\skills\_staged\handoff\` is **tracked** (2 files, dated
  2026-08-10) and its `SKILL.md` **differs** from the live `handoff` skill. The sync
  validator counts 6 canonical skills and never sees it — present in git, invisible to
  validation. Needs disposition: promote, delete, or move out of the canonical tree.

`hats\` inventory (12 files, 7.7K): the `HAT_*_PLAYBOOKS.md` trio is 2,540 words of the
total, and `HAT_EDUCATOR_PLAYBOOKS.md` (618w) is the file at the centre of open flag #94.

**Correction on record:** an earlier claim that "`00-BRAIN` is 467K words of governance
outweighing coursework 10:1" was misleading. 77% is history and 17% is CASTLE. The
instruction layer is ~17K words. **The problem is load, not mass.**

### Phase D — The load pattern / instruction-layer cut (NEEDS CHRIS'S AUTHORIZATION)

**⚠ CORRECTED 2026-08-12. An earlier figure in this file said ~15,327 words always-load.
That was wrong** — it measured an assumed file list rather than the chain the system
actually specifies. `BOOT_FILES` in `validate_boot_chain.py` is a **stale-reference
checklist, not a load manifest** (it even annotates one entry "Conditionally loaded, not
always-boot"). The Aug 10 figure of 6,773 was correct. Do not re-derive the larger number.

**The real always-load is 6,803 words** (measured Aug 12 afternoon), per root `CLAUDE.md`
and `AGENT.md` § Session Start Protocol. **Re-measured the same evening: 6,859** —
`SYSTEM_FLAGS.md` gained **+106 words from flag #99 alone**, while the other five files
measure −50 in aggregate as word-count tool variance. **The growth term is real and it is
`SYSTEM_FLAGS.md`: 1,933 → 2,091 → 2,197 words in a single day, +13.7%.**

| File | Words | Share |
|---|---|---|
| `00-BRAIN\AGENT.md` | 2,675 | 39% |
| **`00-BRAIN\SYSTEM_FLAGS.md`** | **2,091** | **31%** |
| `00-BRAIN\CHRIS_CORE.md` | 893 | 13% |
| `01-NORTH_STAR\NORTH_STAR.md` | 582 | 9% |
| `00-BRAIN\CLAUDE.md` (profile) | 459 | 7% |
| root `CLAUDE.md` (pointer) | 103 | 1% |

**NOT always-loaded, and correctly so:** `START_HERE.md` (1,338) and
`ROOT_OPERATING_MANUAL.md` (3,107) both carry `register: human-context` and are Chris's
documents; the manual's own subtitle says it "does not repeat the map or copy AI
governance — it points to both." `WHERE_IT_GOES.md` (2,637), `NOW.md` (1,269) and
`MORNING_BRIEF.md` (189) load situationally. **That separation already exists. There is no
easy win there — it was already taken.**

**So the instruction layer is near minimal, and the target changes.** `SYSTEM_FLAGS.md` is
31% of every session's load **and is the only component that grows without bound.** It was
1,933 words on the morning of Aug 12 and 2,091 by that afternoon — ~158 words added by
that day's own flag #97 and #98 work. Every flag opened, updated or root-caused adds
permanently to what every future session must read, and the growth is forensic narrative:
flag #96's entry alone runs several hundred words of measurement history.

**The Phase D question is therefore:** does the full flag register need to load every
session, or does a session need the open-flag summary — what is open, how severe, what it
forbids — plus a pointer to the forensics? Better ratio than cutting `AGENT.md`, and it
does not touch the flag #94 hazard, because flag archaeology is not a method: nothing an
agent needs in order to *act* would stop loading.

**⚠ HAZARD — this was attempted once and caused an open flag.** The **July 11 slim
pass** moved substance behind a conditional load and produced **flag #94** (teaching-hat
methods that stopped loading when needed), still open. The governing rule, from the
Aug 10 handoff:

> **Situational procedures may move. Methods used every time may not.**

So the cut is a per-section judgment against *"does an agent need this in EVERY session,
or only in a specific situation?"* — **not** a word-count target. Seat 2's proposed
"2,548 → ~1,000 words" is the wrong shape; it optimizes the number, not the load.

**Proposed method (awaiting Chris's yes):** go section-by-section through the four
files, tag each section keep / move-to-conditional / cut, and **bring Chris the table
before anything moves.** Proposal, not fait accompli.

### Phase E — The output bay (deadline Aug 24)

`04-SCHOOL` fixed *buried*. It does **not** answer where a TCOM draft in progress lives
versus the course material it came from. From Aug 24 Chris produces ~27 h/week of
coursework — drafts, problem sets, lab reports, a technical report worth 35% of TCOM.

Claude's recommendation on record: **output goes inside each course folder**, not a
separate top-level folder — at 27 h/week he should not navigate between "my TCOM
materials" and "my TCOM drafts." **Not yet ruled on by Chris.**

Related calendar fact (Aug 9, from the Cowork session): **BUILD/PROJECTS time on the
semester calendar is zero**, and 16 study blocks are unlabeled.

### Phase F — The July 26 interview

`claude_and_chris_direction.md` (root, 31 KB, `status: in-progress`) is an interview
**already run on 2026-07-26 with Chris's Round One answers in it.** It sat unmined for
17 days — C1 in its purest form.

Decided 2026-08-12: **do not run a fresh interview.** Mine this one, then ask only what
is genuinely unanswered. Chris's own words are better data than anything he would say
today after being primed.

His Round One Q1 answer, which already governs Phase E:

> *"Right now I feel like there is a lot of just jumping into things and no structure, I
> need to know all the requirements to do the school work. Do not just assume I will do
> things on my own... you tell me the evening before what to read to be prepared... I
> don't study without being told what to study, I will go tangent and read something
> else completely."*

`EVENING_READING.md` is the system already answering part of that.

### Phase G — Carried, not scheduled

- **Restore test.** The backup is built and verified but has **never been restored from**.
  Codex: a backup is not proven until recovery is exercised. Restore a sample from both
  mirror and one snapshot into a temp dir, compare hashes.
- **PowerShell control gap** (flag #96) — needs a PowerShell-aware classifier before the
  gate can be called platform-complete.
- **Backup task residual** — `LogonType` is `Interactive` and dies with Chris's session.
  `S4U` returned `Access is denied`; needs an elevated run:
  `Set-ScheduledTask -TaskName "ROOT Daily Backup to D" -Principal (New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType S4U -RunLevel Limited)`
- **Flag #97 remainder** — 5 sources still need re-clipping; the clipper defect that
  caused the loss is unfixed. Fix or retire the clipper before pointing it at anything.
- **Council steps 3–8** — proof instrument, one ML rep on real data, goal rewording,
  session-close hook (flag #93), `sync_shared_skills.py` fix, instruction-layer cut
  (= Phase D). Step 1 ✅ and step 2 ✅ are done.

### Phase H — The Friday Aug 14 morning gate (Chris's definition, ruled 2026-08-12)

**Chris's words:** *"I was going to pass all the gates and take the TCOM, CSE, and PHYS
wiki structures for a test run."*

So the gate has two halves. The technical half is already understood. The second half is
the real test, and **it has a gap that must be closed Thursday or the test cannot run as
described.**

**⚠ Measured 2026-08-12 evening: there is no TCOM wiki.** Two of the three named structures
exist; the third does not.

| Course | Wiki hub | State |
|---|---|---|
| **PHYS** | `03-WIKIS\PHYSICS\` | ✅ Full hub — `concepts`, `drills`, `equations`, `flashcards`, `glossary`, `common-errors`, `problem-types`, `calculus-links`, `diagrams`, `appendix`, `parked-advanced`, plus `raw\` and `templates\` |
| **CSE** | `03-WIKIS\PYTHON\` | ✅ Full hub — `concepts`, `drills`, `code-patterns`, `errors`, `flashcards`, `glossary`, `mini-projects`, `source-summaries`, `parked-advanced`. Serves CSE 1321; the name is the only mismatch |
| **TCOM** | **none** | ❌ **No hub exists.** Only `04-SCHOOL\03-TCOM\` (`Notes\`, `Textbook Doc Files\`) and `hats\HAT_TCOM.md` |

TCOM 2010 carries a technical report worth **35% of the grade**. It is the course with the
least structure and the highest single-assignment weight.

**Thursday action:** build the TCOM hub on the proven PHYSICS/PYTHON pattern — do not
invent a third shape. Then the Friday test runs all three as Chris described.

**Gate checks (technical half):** `validate_boot_chain.py` PASS · `root_health.py` exit 0 ·
`sync_shared_skills.py --check` **must FAIL** on a deliberately broken reference after the
flag #99 fix. *A validator that still returns PASS there was moved, not fixed.*

**Gate checks (structure half):** for each of PHYS, CSE, TCOM — can a session route a new
source into the hub, retrieve a concept, and produce a drill, without Chris directing the
filing? Full proposed check table: `claude_report_2026-08-12_friday_readiness.md` §6.

### Phase I — The safe word (Chris-directed 2026-08-12)

**Chris's words:** *"I need to be able to steer the ship when I need to, almost like we need
a special safe word so you know it is time to just do whatever the task I am asking for is."*

**The problem it solves:** this system's defaults — challenge once, propose before acting,
bring the table first, name the material risk — are correct for governance work and are
**exactly wrong when Chris has already decided and wants execution.** He currently has no
way to say "the deliberation is finished" that the system recognizes as an instruction
rather than as more conversation to weigh.

**Proposed mechanism** — one clause in `AGENT.md`, Chris picks the word:

> **Direct Execution.** When Chris opens an instruction with `<WORD>`, the agent executes
> the task as stated. No proposal step, no alternatives, no challenge-once, no
> restating the risk. Ask only if the instruction is genuinely ambiguous about *what to
> do* — never about whether to do it.
>
> **Unchanged by the safe word, always:** File Safety (copy-first + wrapper for bulk),
> `raw\` immutability, `88-JOURNAL` privacy, academic integrity, and destructive-action
> confirmation. These are the hull, not the steering.

✅ **DONE 2026-08-12. Chris chose `Richard F`.** Implemented in `AGENT.md` § Task Completion
and Constructive Challenge as *"Direct Execution — the safe word."* Boot chain PASS after.

**Note for the Phase D pass:** this added ~120 words to an always-loaded file. That is a
deliberate, Chris-directed exception to the load-reduction target — **it buys back far more
than it costs**, because every avoided round-trip of proposals and confirmations is a session
Chris does not have to steer twice. Do not "optimize" it away.

**File Safety 10 applies:** the safe word does not work in a session that was already running
when the clause was written. It is live from the next fresh session onward.

### Phase J — Three rulings from Chris's 2026-08-12 evening review

#### J-1. The `SYSTEM_FLAGS.md` load-rule contradiction — Chris delegated the call

Chris: *"first real call from me and I say do what you think is right to align them."*

**Ruling made:** the ambiguity exists because the file currently does two jobs. Once Phase D
splits it, the two jobs get two answers and all three lines agree:

| Line | Today | After the split |
|---|---|---|
| `AGENT.md` L134 (Session Start step 3) | "Check `SYSTEM_FLAGS.md`" → always | **Stays "always"** — pointing at the slim file, which is prohibitions only |
| `AGENT.md` L153 (File Safety 7) | "required context for system, file-write, and review sessions" → situational | **Re-points to `SYSTEM_FLAGS_DETAIL.md`** — the forensics, genuinely situational |
| The file's own header | "Check at every session start" | **Stays** — true of the slim file |

**Principle: always-load the prohibitions, situationally-load the forensics.** That is the
same shape as the Phase D split itself, so the load rule and the file structure finally agree.

**Sequencing note — this is a dependency, not a delay.** The alignment must land in the *same
pass* as the split. Editing L153 to point at `SYSTEM_FLAGS_DETAIL.md` before that file exists
creates a dangling reference in an always-loaded governance file, and
`validate_boot_chain.py` would correctly fail it.

#### J-2. Do TCOM and the other courses get their own wiki hubs? — **No, with one build**

Chris's instinct — *"maybe the wikis are not even needed as the other courses should be
easier to manage"* — **is right for ECON and ENGR, and wrong for TCOM.** Measured state:

| Location | Contents |
|---|---|
| `EDUCATION\wiki\courses\econ-1000\` | **Real content** — drills, flashcards, glossary, reading-guides, semester-map (5 files) |
| `EDUCATION\wiki\courses\tcom-2010\` | **One file** — `semester-map.md` |
| `EDUCATION\wiki\methods\`, `references\`, `course-briefs\` | Meta-learning content — learning-how-to-learn, AI programs, Fall course briefs |
| `EDUCATION\raw\` | 240 files — syllabi, Open-TC course resources, textbook docs |

**The real finding: `EDUCATION` is doing two unrelated jobs** — it is a *meta-learning hub*
(how Chris learns) **and** a *catch-all container* for courses that never got their own hub.
That is why the structure feels arbitrary: PHYSICS and PYTHON got hubs, ECON and TCOM got
subfolders inside a hub nominally about learning theory.

**The decision rule, derived from `NORTH_STAR.md` §2 — not invented here:**

> **A subject earns its own top-level hub when its knowledge outlives the course.**

| Subject | Outlives the course? | Ruling |
|---|---|---|
| **PHYSICS**, **PYTHON** (CSE) | Yes — both are named in NORTH_STAR §2's permanent capability base and feed everything after | ✅ Own hubs, correct as-is |
| **ECON 1000**, **ENGR 1000** | No — one-semester requirements; the knowledge is used for a grade and rarely again | ❌ **Stay in `EDUCATION\wiki\courses\`.** Chris is right |
| **TCOM 2010** | **The course doesn't; the content does.** "Communication" is explicitly in NORTH_STAR §2's permanent capability base, and writing technical reports and proposals is a direct revenue skill for the company | ⚠️ **Build it out — but inside `EDUCATION`, not as a new hub** |

**Why not three new hubs:** each top-level hub permanently adds an `OPERATIONS.md`, a
`current-position.md`, `index`/`log`/`source-map`, session start/close minimums, `wiki_lint`
scope, and health-gate scope. **Three new hubs for courses that end in December is permanent
overhead bought for temporary work** — and the health gate already carries 4 review-debt
items against 710 expected navigation links.

**T8 is therefore re-scoped:** build `EDUCATION\wiki\courses\tcom-2010\` out on the proven
PHYSICS/PYTHON pattern (concepts, drills, glossary, flashcards, common-errors, plus the
existing semester-map). Same work, no new hub. **Friday's structure test then runs all three
as Chris described** — PHYS, CSE, and TCOM.

**Named promotion trigger (so this is a decision, not a deferral):** promote TCOM to its own
top-level hub when the 35% technical report is delivered **and** it has produced reusable
writing assets — report templates, document patterns — that a client project would reuse.
**Structure follows evidence; do not build the hub speculatively.**

#### J-0. Part 3 of the review packet — **ALL APPROVED by Chris 2026-08-12 evening**

| # | Item | Ruling |
|---|---|---|
| 1 | `AGENT.md` moves (−742; routing tables, forensic history, single-circumstance procedures) | ✅ **APPROVED — do this move** |
| 2 | `SYSTEM_FLAGS.md` split (−1,390) | ✅ **APPROVED** |
| 3 | `CHRIS_CORE.md` Aptitude Interaction Map (−110) | ✅ **KEEP IT** — Chris: *"May as well keep it."* `CHRIS_CORE.md` is untouched at 892 words |
| 4 | Defer Execution Discipline (517w) to its own dedicated pass | ✅ **YES** — Chris: *"we need to do this correctly."* **Do not touch it Thursday** |
| 5 | Inline the seven teaching methods into `HAT_EDUCATOR.md` (flag #94) | ✅ **APPROVED — do it** |
| 6 | The safe word | ✅ **`Richard F`** — implemented, see Phase I |

**Revised always-load target: 6,883 → ~4,700 words (−32%)**, reflecting Chris's decision to
keep the Aptitude Map and the ~120 words the safe word adds. **The target moved because Chris
ruled, not because the measurement changed.** Both changes are correct: the Aptitude Map is
person-contract, and the safe word buys back more time than it costs.

#### J-3. Should some hats become skills? — **Yes: the three playbook files**

Chris: *"should some become skills instead of hats, if that is more efficient."*

Applying `AGENT.md`'s own Extension table — *"the same multi-step procedure repeats → skill"*
— and its own definition, *"hats are cross-model modes, not roles"*:

> **A hat is a stance — how to behave. A skill is a procedure — what steps to run.**

By that line, **three files are procedures wearing hat filenames:**

| File | Words | Why it is a skill |
|---|---|---|
| `HAT_ENGINEERING_PLAYBOOKS.md` | 981 | Its own header: *"Load only the procedure whose trigger fires"* |
| `HAT_OPERATOR_PLAYBOOKS.md` | 908 | Per-procedure triggers, named explicitly |
| `HAT_EDUCATOR_PLAYBOOKS.md` | 608 | Contains four procedures **literally labelled SKILL** |
| **Total** | **2,497** | **33% of the entire hats layer** |

**The payoff is not tidiness — it is flag #94's defect class, fixed structurally.** A skill's
`description` field is a machine-read firing trigger the harness evaluates. A playbook's
*"Load when running a teaching session"* is prose hoping an agent notices. **That is exactly
the difference between the engineering/operator playbooks, which name a firing condition, and
the educator playbook, which names a vibe.** Converting them replaces a judgment call with a
mechanism — the same move that turned File Safety 12 from prose into the `PreToolUse` gate.

**Stay hats** (all stance, not procedure): `HAT_EDUCATOR`, `HAT_OPERATOR`,
`HAT_TECHNOLOGY_ENGINEER`, `HAT_SOFTWARE_ENGINEER`, and the five subject hats.

**This does not replace the flag #94 fix — both, not either.** The seven teaching *methods*
still inline back into `HAT_EDUCATOR.md` (T3), because methods used every teaching session may
not move. The four *procedures* become skills.

**Sequencing: decide now, execute after Friday.** Thursday is already ~7.5 hours, and
**flag #99 means the skill mirror pipeline is currently broken** — `sync_shared_skills.py`
copies `SKILL.md` only, not directories, and certifies the result PASS. Pushing 2,497 words of
new skills through a pipe that silently drops files is how this vault creates its next flag.
**Order: fix #99 (T4) → Friday gate → convert the playbooks.**

#### J-4. The learning-styles question — **we already have it, and it is better than that**

Chris asked (2026-08-12) whether the learning research he found could be implemented, and
offered to re-find it. **He does not need to.** It is already captured and processed:

- **`03-WIKIS\EDUCATION\wiki\methods\learning-how-to-learn-principles.md`** — created
  2026-07-12, extracted from the Justin Sung *"Learn To Learn in 109 minutes"* transcript
  (`EDUCATION\raw\`, 21,329 words, captured 2026-06-06, reviewed in five chunks).
- It is a careful, source-critical extraction: it separates the usable framework from the
  transcript's uncited neuroscience and program marketing, and says so explicitly.

**On "learning styles" specifically — `.ROOT` already ruled, correctly, on 2026-07-12.**
§1 of that file states: *"Do not lock Chris into a fixed visual/auditory/read-write/
kinaesthetic identity."* **That matches the research** — modality-matching is one of the most
thoroughly failed ideas in education science. **If what Chris found the other day is a
VARK-style "you are a visual learner" framework, the honest answer is that it does not work,
and his own vault got this right a month ago.**

**What is real, and is not the same thing:** Chris's aptitude profile in `CHRIS_CORE.md` —
3D Visualizer, Numerical Detective, Cue User, Visual Scanner — comes from an actual ability
assessment. **Aptitudes are measured strengths; learning styles are self-reported identities.
Using the first is evidence-based; using the second is not.**

**The actual finding — and it is the answer to Chris's whole objective.** Three pieces of one
learning system exist in this vault, and **none of them reference each other:**

| Piece | Where | Job | Status |
|---|---|---|---|
| The **personal constraint** | `CHRIS_CORE.md` §3, *Make Arbitrary Knowledge Retrievable* | Cue-dependent associative memory: one precise meaning, apply immediately, anchor, retrieve later | ✅ Always loads |
| The **tactics** | `HAT_EDUCATOR.md` — 7 methods | Skeleton First, One Concept at a Time, Term Anchoring, Explain-It-Back, Cold Checks, Physical Anchors, Short Corrections | ⚠️ **Half-loads — flag #94** |
| The **model** | `learning-how-to-learn-principles.md` | Encoding vs retrieval; retrieval matched to intended use; higher-order integration; opportunistic retrieval; the beginner study loop | ❌ **No hat references it. It has never loaded in a teaching session** |

**The hat has tactics with no model. The model has no route into a session. The person
contract has the constraint but not the method.** This is council finding C1 — detection
works, propagation fails — applied directly to Chris's own learning, which is the one place
it costs the most.

**Recommendation — fold this into the flag #94 fix (T3), not as separate work:**

1. When the seven methods inline back into `HAT_EDUCATOR.md`, **carry the encoding/retrieval
   distinction in with them.** It is the model that explains *when* each of the seven fires.
2. **Bring in the retrieval-matched-to-use table** (§2 of the methods file) — *"recall a term →
   flashcard; explain a concept → explain-back; solve a problem → fresh problem; communicate
   professionally → draft for a real audience."* This is the single most directly usable thing
   in the file and it maps cleanly onto TCOM, ECON, PHYS and CSE.
3. **Add the pointer to all five subject hats**, which is the other half of flag #94's fix.
4. **The Beginner Study Loop (§10) is a procedure, not a stance → it becomes a skill** in the
   J-3 conversion. It is the clearest example in the vault of a hat-file paragraph that should
   be an invocable skill.

**Cost: ~0 always-load words** — all of it lives in the conditional hat layer.

**Why this matters more than the rest of the update:** Chris's stated objective is speed of
obtain → recall → learn → convert to skill. **The system already contains a validated answer
to that and has never once loaded it during teaching.** Everything else in this update makes
sessions faster. This one makes the learning stick.

---

### Phase K — Opened 2026-08-12 evening, for tomorrow. **Not decided tonight.**

Three items Chris raised at session end. Recorded so they survive the window; **each needs a
real conversation, not a same-night ruling.**

#### K-1. Learning pace — breadth-first, depth on return

Chris: *"it is better sometimes to push through the material and discuss while it is unknown
then go back and work it, not stick to the same problem until a single problem is drilled and
move on."*

This is a **teaching-design directive, not a preference to note and forget.** It says: make a
first pass for coverage and discussion while the material is still unfamiliar, then return for
depth — rather than drilling each item to mastery before advancing.

**⚠ It is in live tension with `HAT_EDUCATOR.md`'s "One Concept at a Time," and possibly with
"Proof moves the stage immediately" (`AGENT.md` Execution Discipline 5).** Do not silently
resolve that tension. **Resolve it explicitly during the T3 flag #94 fix**, because both the
seven methods and this pace rule land in the same file in the same pass.

Note the fit with J-4: the methods file already distinguishes *encoding* from *retrieval*.
Chris is describing a **first-pass encoding sweep before retrieval practice**, which the model
supports — the two are not actually in conflict once named that way. Confirm with Chris.

#### K-2. A mutual calibration record — "if we are not grading each other, how are we improving"

Chris wants a kept record of **what actually works between him and the AI, graded in both
directions.** This does not exist. The nearest things are `SYSTEM_LEARNINGS.md` (system
lessons, not interaction) and `CHRIS.md`'s monthly/quarterly calibration (one direction only).

**Open question for tomorrow:** new file, or a section in an existing owner? Constraints that
must hold — it has to be **cheap to append during a session**, must not become a third
dashboard (Execution Discipline 3), and must not grow unbounded into the boot load, which is
the exact defect Phase D is fixing. **A calibration record that repeats `SYSTEM_FLAGS.md`'s
growth pattern would be a self-inflicted wound.**

#### K-3. Templates — including an Obsidian capture template into `77-INBOX`

Chris: *"I need to use them more to my advantage... we can build our own template for obsidian
capture to go to INBOX."*

**Direct connection to flag #97, which makes this more valuable than it looks.** The Obsidian
clipper is *the defect that lost five sources* — it pre-fills the note name from whichever tab
was active, then re-extracts the body at save time, so filename and content come from
different pages. Flag #97's remaining action is *"fix or retire the clipper before pointing it
at anything else."*

**A purpose-built capture template routing to `77-INBOX` is a candidate replacement for the
broken clipper, not merely a convenience.** Scope it that way tomorrow.

Existing template infrastructure to reuse rather than reinvent: `03-WIKIS\PHYSICS\templates\`,
`03-WIKIS\PYTHON\templates\`, `Session_Logs\DAILY_TEMPLATE.md`,
`HANDOFF_TEMPLATE.md`, `WEEKLY_REVIEW_TEMPLATE.md`.

---

## Decisions — RULED BY CHRIS 2026-08-12 evening

| # | Decision | Ruling |
|---|---|---|
| 1 | **Phase D instruction-layer cut** | ✅ **AUTHORIZED, proposal-first.** Bring the section-by-section keep / move-to-conditional / cut table to Chris **before anything moves**. The three live prohibitions stay in full imperative form. This is the guardrail that prevents a repeat of the July 11 pass that created flag #94 |
| 2 | **July 20–26 DAILY archive** | ✅ **RULED: accept `MONTHLY_JULY_2026.md` as the authorizing close**, rotate the 7 files, and add one clause to `AGENT.md:240` covering weeks closed at monthly level. **Do not backfill a weekly for a closed month** — that is writing history (constraint 7) |
| 3 | `tmp\`, `outputs\`, `...projectSuccess\`, `claude_and_chris_direction.md` | ✅ **ALL RULED** — see the Phase A table above |
| 4 | **Friday gate definition** | ✅ **RULED by Chris:** pass all gates, **then take the TCOM, CSE and PHYS wiki structures for a test run.** See Phase H |
| 5 | **Output bay shape** — inside each course folder, or separate? | **still open** — Phase E; hard deadline Aug 24, ruled by Aug 17 |
| 6 | `.PROJECTS` — keep the dot, or renumber to `00-PROJECTS` | **still open** — Phase C |
| 7 | Council decisions 1, 2, 4 in `COUNCIL_RECONCILED_VERDICT.md` | **still open** — council steps 3–8 |

## New asks from Chris, 2026-08-12 evening

| # | Ask | Where it lands |
|---|---|---|
| 1 | **"I would like to review the load `.md` files and wiki `.md` file hats"** | Review packet for Chris — the 6 always-load files and the 12 `hats\` files, summarized so he can rule rather than wade. **Feeds Phase D's proposal-first table** |
| 2 | **A "safe word"** — a control phrase meaning *stop proposing, stop challenging, just execute the task as asked* | Governance addition; proposed wording in Phase I |
| 3 | **Structured studying, research and teaching support** — while keeping his ability to "steer the ship" | The `hats\` review (ask 1) and flag #94 are the live edge of this. Phase E and CASTLE own the rest |

## Lessons that must not be relearned

1. **Presence is not function.** Hit five times this week: the inert sandbox, the dead
   backup, a validator passing over a broken reference, a scheduled task registering
   "Ready" then failing, and a task reporting `LastTaskResult 0` over work that never ran.
   **Verify by running, never by reading.**
2. **Detection works; propagation fails** (council C1). Correct the live documents in the
   *same session* as the finding.
3. **Two checks, not one.** On `raw\`, hashing and filename-comparison each missed part of
   the loss. Running one and calling the queue clean would have been wrong.
4. **`git grep` only searches tracked files.** The `04-SCHOOL` residual check inherited that
   blindness and missed two untracked files. Filesystem scan as well, always.
5. **A rule's trigger is part of the rule.** The DAILY archive step is real and correct; it
   never fired because the weekly report that authorizes it was never filed.

## How to maintain this file

- Mark items done **here**, in the session they are done, with the commit SHA.
- New findings go in the relevant Phase, not into conversation.
- If Chris re-orders the phases, record that he did and do not silently re-order back.
- When the update completes, set `status: complete` and write the closing `SESSION_INDEX.md`
  verdict in this same folder.
