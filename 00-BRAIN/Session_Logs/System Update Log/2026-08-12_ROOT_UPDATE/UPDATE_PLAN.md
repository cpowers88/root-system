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
| `tmp\` — 259 files / 29 MB PDF-extraction scratch | Chris to confirm delete; no overlap with the 5 lost sources (checked). Excluded from **both** GitHub and the D: backup | **awaiting Chris, DELETE** |
| `outputs\` — `real_world_dataset_opportunity_map_2026-07-16` (xlsx + 4 charts) | Not construction data. Closest thing in the vault to an executed analysis with an artifact. Paired with `tmp\spreadsheets\` (its build input) — they live or die together | **awaiting Chris, save these two folers if you think it is right** |
| `...projectSuccess\` — holds `radar.md`, `WATCHTOWER.md` | Keep files, kill the folder name. WATCHTOWER is a real `.ROOT` concept | **awaiting Chris on destination, execute: kill folder name and make it real** |
| `EVENING_READING.md` | **STAYS at root** — generated dashboard, peer of `MORNING_BRIEF.md` | settled |
| `needs_for_physics.md` | **STAYS** — live calculus–physics bridge scratch, Jul 30–Aug 23 sprint, destination already documented in `PHYSICS\wiki\calculus-links\` | settled |
| `claude_and_chris_direction.md` | Moves to `01-NORTH_STAR\`. **Do not delete — it is the July 26 interview with Chris's own answers** | **to do, I moved it** |
| Graph drift: `.vs` and `outputs` uncolored/unexcluded | Add to `COLOR_MAP.yaml` once `outputs\` is ruled on | **blocked on `outputs\`** |

### Phase B — The weekly review (BLOCKER — unblocks Phase C)

**The Aug 3–9 weekly review does not exist.** `AGENT.md:240` gates the DAILY archive
step on the WEEKLY report being filed. Until it exists, DAILY files cannot legally
rotate to `Session_Logs\Report Archive\`, which is why **37 files sit loose** in
`Session_Logs`. This is a blocked dependency, not a discipline failure.

**Next exact action:** file the Aug 3–9 weekly review per `CASTLE\OPERATIONS.md`'s
weekly close, then run the archive step the same day.

**CODEX filed this**

### Phase C — `00-BRAIN` structure (blocked on B for the Session_Logs half)

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

**Correction on record:** an earlier claim that "`00-BRAIN` is 467K words of governance
outweighing coursework 10:1" was misleading. 77% is history and 17% is CASTLE. The
instruction layer is ~17K words. **The problem is load, not mass.**

### Phase D — The load pattern / instruction-layer cut (NEEDS CHRIS'S AUTHORIZATION)

**The finding:** ~15,327 of roughly 23,000 instruction words load on **every** session.
Two-thirds of everything ever written to govern this vault is read before Chris types
anything. `hats\` (7.7K) is the only conditional layer that exists.

Always-loaded, measured:

| File | Words |
|---|---|
| `ROOT_OPERATING_MANUAL.md` | 3,107 |
| `00-BRAIN\AGENT.md` | 2,675 |
| `00-BRAIN\WHERE_IT_GOES.md` | 2,637 |
| `00-BRAIN\SYSTEM_FLAGS.md` | 1,933 |
| `START_HERE.md` | 1,338 |
| `NOW.md` | 1,068 |
| remaining 7 | 2,569 |

The first four are 11.7K of the 15.3K.

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

---

## Decisions waiting on Chris

| # | Decision | Blocks |
|---|---|---|
| 1 | **Authorize the Phase D instruction-layer cut** (proposal-first method) | Phase D — the only item that changes every future session |
| 2 | **Output bay shape** — inside each course folder, or separate? | Phase E; hard deadline Aug 24 |
| 3 | `tmp\`, `outputs\`, `...projectSuccess\` disposition | Phase A, graph drift |
| 4 | `.PROJECTS` — keep the dot (sorts to top of Explorer) or renumber to `00-PROJECTS` (sorts identically without reading as machine layer) | Phase C |
| 5 | Council decisions 1, 2, 4 still open in `COUNCIL_RECONCILED_VERDICT.md` | Council steps 3–8 |

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
