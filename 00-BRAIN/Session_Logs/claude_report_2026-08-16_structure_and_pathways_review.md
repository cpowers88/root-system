---
type: report
timeline: now
status: active
tags: [structure, instruction-layer, governance, school, fall-2026]
created: 2026-08-16
session_date: 2026-08-16
---

# Structure + Instruction-Pathway Review — 8 days to Aug 24

### Requested by Chris 2026-08-16 (Sunday). Read-only audit; no structural changes made. New findings filed to `UPDATE_PLAN.md` per the finding freeze.

**Question asked:** is the folder system and the AI instruction/pathway layer ready to
operate a real semester, and what formatting changes are worth making before the Aug 17–21
test week?

**Answer:** the *structure* is ready. The *routing into it* is not. One missing table is
worth more than every other item in this report combined.

---

## 1. Measured state — today, live

| Gate | Result |
|---|---|
| `validate_boot_chain.py` | **PASS** — 32 boot files, 1,369 live pages, no stale governance reference |
| `root_health.py` | **PASS, exit 0** — blockers 0, **review debt 0**, frontmatter 0, 1,546 files, 0 findings |
| `sync_shared_skills.py --check` | **PASS** (via health gate), earned since T4 |
| Always-load chain | **5,803 words** across 6 files — confirms the Aug 13 figure exactly |
| Git | working tree clean; **1 commit ahead of `origin/main`** (push is Chris's call) |

**The health gate is cleaner than it has been all month.** It read `PASS WITH DEBT` on Aug 13;
the CASTLE index fix yesterday cleared all four review items. This is the first full PASS on
record.

### The estate, measured

| Realm | `.md` | All files | Reading |
|---|---|---|---|
| `03-WIKIS` | 1,362 | 2,407 | 8 hubs, AI-grown — correct that it is the largest |
| `99-ARCHIVE` | 445 | 605 | history; excluded from the graph |
| `00-BRAIN` | 304 | 373 | **77% is `Session_Logs` history**; the instruction layer is ~17K words |
| `02-LIBRARY` | 109 | 4,893 | file count is `.PROJECTS` vendored deps, not content |
| `04-SCHOOL` | 32 | 166 | course files + `OneNote` + `work\` bays |
| `05-BUSINESS` | 32 | 41 | reusable/sanitized only, as specified |
| `01-NORTH_STAR` | 17 | 20 | correctly small |
| root | 9 | — | 4 pointers, 3 dashboards, 2 human docs |

---

## 2. What is genuinely ready

These were checked against the live tree, not against a map.

- **All eight `03-WIKIS` hubs conform to the archetype** — `OPERATIONS.md`, `README.md`,
  `HOW_TO_USE.md`, `raw\`, `wiki\`. Zero hubs carry the retired `CLAUDE.md`/`AGENTS.md`
  loaders. The 2026-08-10 removal held.
- **`04-SCHOOL` is the shape it was promoted to be** — five Fall course folders, each with a
  `work\` bay and a `README.md` carrying its own academic-integrity boundary. `99-EDG`
  correctly excluded.
- **`04-SCHOOL\SEMESTER_MAP.md` is the strongest operational document in the vault.** Real
  Fall dates, per-item confidence marks, the D2L-opens-Aug-24 finding, and an honest
  statement of what the rehearsal week can run on without D2L. This is the instrument the
  test week should actually run on.
- **The provenance tiebreaker works.** *"Did KSU give it to me, or did we make it?"* resolves
  the `04-SCHOOL` vs `03-WIKIS` collision in one question, and it will fire several times a
  day from Aug 24.
- **The teaching layer is integrated.** Seven hats to one standard, methods carrying their
  own triggers inline, `HAT_PHYSICS_MATH.md` routed at row 2. Each subject hat states its own
  load chain in its header.
- **The always-load chain is near minimal at 5,803 words** and the human documents
  (`START_HERE`, `ROOT_OPERATING_MANUAL`) are correctly outside it.

---

## 3. The one finding that matters — no course→hat routing exists

**Every subject hat states its own load chain. Nothing states which hat to load.**

`HAT_PHYSICS.md:10` says: *AGENT.md → surface profile → CHRIS_CORE.md → HAT_EDUCATOR.md →
this file → `PHYSICS\wiki\current-position.md` → latest handoff.* That is a correct,
complete pathway — **and it is only readable by a session that has already opened
`HAT_PHYSICS.md`.**

What the always-load chain actually says about hats, in full:

| File | Text |
|---|---|
| root `CLAUDE.md` / `AGENTS.md` | "optional `00-BRAIN\HATS\` mode" |
| `AGENT.md` § Profile precedence | "an optional `HATS\` mode" |
| `AGENT.md` § Wikis and CASTLE | "Hats are cross-model modes, not roles" |
| `CHRIS_CORE.md` footer | "optional modes in `HATS\`" |

**Four mentions, zero triggers.** `AGENT.md` § Session Start Protocol steps 1–6 never
reaches a hat at all — step 6 is "name the critical path and work."

**This is flag #94's defect class exactly**, and the vault has already written the rule for
it: *a rule's trigger is part of the rule* (`UPDATE_PLAN.md` lesson 5). The seven teaching
methods existed and did not fire because nothing named when. The hats have the same shape
today.

**Consequence from Aug 24:** Chris opens a session and says "physics." The session must
guess whether to load `HAT_PHYSICS`, `HAT_PHYSICS_MATH`, `HAT_EDUCATOR`, the hub
`OPERATIONS.md`, `current-position.md`, or `SEMESTER_MAP.md` — and in what order. It will
sometimes guess right. That is not an operating system; it is a rehearsal that passed because
the person running it already knew the answer.

**Fix — one table, ~90 words, in `AGENT.md`.** Not a new document, not a second dashboard:

| Chris opens with | Load |
|---|---|
| physics / PHYS / WebAssign | `HAT_PHYSICS` → `PHYSICS\OPERATIONS.md` → `wiki\current-position.md` |
| calculus mechanics inside physics | add `HAT_PHYSICS_MATH` |
| python / CSE / code | `HAT_PYTHON` → `PYTHON\OPERATIONS.md` → `wiki\current-position.md` |
| TCOM / a document for a reader | `HAT_TCOM` → `EDUCATION\wiki\courses\tcom-2010\` |
| ECON | `HAT_ECON` → `EDUCATION\wiki\courses\econ-1000\` |
| ENGR | `HAT_ENGR1000` |
| any teaching block | `HAT_EDUCATOR` under the subject hat |
| what is due / a date | `04-SCHOOL\SEMESTER_MAP.md` first — it outranks every hat on facts |

**Cost:** ~90 always-load words (5,803 → ~5,893, +1.5%). **Buys:** the correct chain fires
on the first line of every school session instead of on the session's judgment.

This is the highest-value formatting change available before the test week, and it is the
only one I would call blocking. Everything below is real but smaller.

---

## 4. Navigation documents that are stale — and it is the school move they missed

`04-SCHOOL` was promoted out of `02-LIBRARY` on 2026-08-12 (`3f78fa4`, 105 references
rewritten across 46 files). **Two of the files it did not fully reach are the two navigation
documents Chris himself opens.**

### 4a. `00-BRAIN\vault_map.md` — the map still nests school inside the library

Line 82–84 of the verified-map tree:

```
├── 02-LIBRARY\  ← reusable knowledge, projects, and school file home
│   ├── 04-SCHOOL\   ← course files: 01-CSE-Python, 02-Physics I, ...
```

`04-SCHOOL` **does not appear at root level in the map at all.** Its header still reads
*"Last updated: July 29, 2026."*

This file *was* edited on Aug 13 during T7 — the Watchtower entries are correctly repointed
to `01-NORTH_STAR`. The school correction and the date stamp were not carried in the same
pass. **Council finding C1 again: detection worked, propagation was partial.**

Two smaller staleness items in the same file: `scripts\` is described as *"7 as of July 15"*
(there are 21 scripts plus two subfolders), and `HATS\`/`SKILLS\` are written in caps while
the live folders are `hats`/`skills` (known C-2, case-insensitive, cosmetic).

### 4b. `START_HERE.md` — contradicts itself on where school files live

| Line | Says |
|---|---|
| 33 | `02-LIBRARY` — "Also `.PROJECTS` (build docs), **`04-SCHOOL` (course files)**" |
| 76 | Color table: `🟠 Orange — 02-LIBRARY — reference + projects + **school file home**` |
| 133 | "course files live at **`04-SCHOOL`**" ✅ correct |

Chris's own human entrance document gives him two different answers on the same page. It also
lists reference folders as `REF-…` when the live tree is lowercase `ref-<name>`.

**Why these two matter more than their size suggests.** Chris's stated runway goal #2 is
*"comfort with the folder structure and how work moves through it."* These are the exact two
files that goal is served by, and both currently describe the tree as it was before the
single largest structural change of the month.

---

## 5. Remaining findings — real, smaller, all filed

| # | Finding | Pri |
|---|---|---|
| **N4** | **`CASTLE\wiki\current-position.md` is 28 days stale and 15 days past its own stated reconciliation date** ("Next monthly reconciliation: August 1, 2026"). It records Python at **Stage 3**; learner truth and `NOW.md` both say **Stage 4b**. `NOW.md` names this file as the owner of "sequence and proof status" — so the cockpit points at a file that disagrees with the cockpit. Codex filed the staleness (W3); the contradiction is new | 🟠 |
| **N5** | **An unrouted ENGR 1000 §BD syllabus sits in `77-INBOX`** (captured Aug 14), one day before the flag #57 escalation email. `SEMESTER_MAP.md` already found that `SYLLABUS_STATUS.md` omits the §05 file — so **two** ENGR reference syllabi are on disk that the source index does not name, going into tomorrow's email. Seven more inbox items from Aug 13 are past their weekly clear | 🟠 |
| **N6** | **`NOW.md` is 3,377 words** — larger than `AGENT.md`, and it carries the whole update history. Execution Discipline 3 ("one visible lane") is not met by a cockpit that takes four screens. It is correct *for the pause*; it is wrong for a semester. Proposal: at `OK TO START`, cut the update narrative to one link and hold the cockpit at ≤600 words | 🟠 |
| **N8** | **Hub shared-layer conformance is 4 of 8.** `AI_AUTOMATION_SYSTEMS`, `BUSINESS`, `PHYSICS`, `REVENUE_LAB` do not name `WIKI_SHARED_LAYER.md` in their `OPERATIONS.md`. **PHYSICS is the one that matters** — hardest course, four meetings a week. (Codex measured 3/8 on Aug 13; EDUCATION has since been fixed) | 🟢 |
| **N7** | **CASTLE still carries `CLAUDE.md`, `AGENTS.md`, `CODEX.md` loaders.** Not a rule violation — the removal rule names `03-WIKIS` hubs, and CASTLE is in `00-BRAIN`. But it is the last place two entry conventions coexist, and CASTLE is described everywhere as a hub | 🟢 |
| **N9** | `00-BRAIN\skills\_staged\handoff\` is still tracked and still awaiting Chris's disposition (C-3). The sync validator now WARNs about it on every run, which is correct and non-fatal | 🟢 |

---

## 6. What this means for the test week

The Aug 17–21 week is *week 1 done early* (Chris's Friday ruling), running on material
already on disk because D2L does not open until Aug 24. The structure supports that. The
routing does not, yet.

**Order that respects the day:** today's committed work is the three fresh-session
rehearsals. §3's routing table should land **before** them, because it is the thing the
rehearsal is meant to test — and File Safety 10 means it cannot be tested in the session that
writes it. §4's two navigation fixes are cheap and can land in the same pass. Everything in
§5 waits.

**What would make the test week's result trustworthy:** grade whether the *session* found the
right chain, not whether Chris steered it there. That is the difference between "structurally
ready for rehearsal" and "ready for unsupervised trust" — Codex's verdict, still standing.

---

*Method: live filesystem scan and both gates run this session; no map or prior report trusted
for a path claim. No files modified by this review except the findings filed to
`UPDATE_PLAN.md`. Owner of the update: `Session_Logs\System Update Log\2026-08-12_ROOT_UPDATE\UPDATE_PLAN.md`.*
