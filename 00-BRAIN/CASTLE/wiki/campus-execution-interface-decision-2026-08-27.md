---
type: decision-report
timeline: now
status: proposed
tags: [school, fall-2026]
created: 2026-08-27
check_at: 2026-08-30
---

# Fall 2026 Campus Execution Interface — Decision Report

**Status:** Proposed  
**Date:** August 27, 2026  
**Decider:** Chris  
**Decision gate:** choose an operating model; no architecture or placement rule changes in this report are active until Chris approves them.

## Executive verdict

`.ROOT` does not need to become a second coursework system on campus. It needs a small,
reliable interface between two environments that have different jobs:

```text
HOME CONTROL PLANE                         CAMPUS EXECUTION PLANE
.ROOT + AI + durable owner truth           D2L + course files + independent work
weekly brief --------------------------->  one visible work packet
owner updates <---------------------------  short return packet
```

**Recommendation:** keep the desktop `.ROOT` canonical, keep the campus laptop structurally
AI-clean for graded work, and add a **Campus Bridge** with only three parts:

1. a generated, tracked `CAMPUS_BRIEF.md` containing today's allowed work, exact source/file,
   deadline, and proof;
2. a dedicated KSU OneDrive course workspace for active Office/PDF/course binaries, with the
   current week marked **Always keep on this device**; and
3. one append-only `CAMPUS_RETURN.md` containing only outcome, evidence location, miss/status,
   and next action—never assignment content.

This is an incremental evolution of the current two-machine design, not a new operating
system. Run it for one real campus block, reconcile it at home, and keep/modify/revert on
evidence at the August 30 return.

## What the live system proves

1. **Campus is load-bearing.** `CAMPUS_LAPTOP_BUILD.md` measures 16.33 campus work hours per
   week—roughly 58% of the semester's outside-class study time. A home-only execution model
   cannot carry the semester.
2. **The laptop itself is not the failure.** Its August 18 build verified Python, VS Code
   without AI extensions, Git pull/push, Obsidian, Microsoft 365, D2L access, and Respondus
   installation. The remaining exam gate is a real authenticated Respondus practice quiz.
3. **The current Git boundary is useful but incomplete.** Git carries the operating Markdown,
   but `.gitignore` excludes PDFs, DOCX, XLSX, PPTX, images, databases, every `raw\`, and other
   binaries. The clone can show the plan while omitting the textbook or file the plan names.
4. **The return path did not fire in real use.** On day one, the laptop made no `.ROOT` edits
   and pushed nothing. Captures reached the desktop later through `77-INBOX`. The system has a
   home planning loop and a campus execution loop, but no deliberately small handoff between
   them.
5. **Independent assignment work is not evidence that `.ROOT` failed.** CSE 1321/1321L and
   ENGR 1000 prohibit AI on submitted work; TCOM forbids AI drafting. A system that tries to be
   an always-present campus copilot would be optimizing against the course boundary.
6. **The repository is structurally healthy.** The canonical `root_health.py --verbose` gate
   passed August 27: boot/governance, wiki navigation, frontmatter, CASTLE freshness, skill
   mirrors, whitespace, and Markdown integrity. This is an interface problem, not a reason for
   another vault-wide rebuild. The health gate does not evaluate semantic freshness.
7. **Two semantic drifts matter.** `LOCAL_MACHINE_MAP.md` still omits the measured laptop, and
   contains mutually inconsistent statements about the stale Drive `.ROOT` tree now tracked by
   flag #105. Neither causes the campus-access failure, but both should be corrected if this
   operating model is approved.

## Requirements

Any viable model must:

- preserve the AI prohibition on CSE and ENGR submissions and the no-drafting rule for TCOM;
- work offline for the active block after one preparation pass;
- expose one next action without loading the full vault;
- make current Office files, PDFs, and required course assets reachable;
- return proof/status to `.ROOT` without copying graded content into AI context;
- avoid a second canonical vault, a second dashboard, and another large maintenance cadence;
- fail visibly when sync, source availability, or academic permission is uncertain; and
- cost less coordination time than it saves.

## Options considered

### Option A — Keep the current clone-only model unchanged

| Dimension | Assessment |
|---|---|
| Setup | None |
| Campus access | Markdown only; binaries missing |
| Academic-integrity fit | Strong |
| Offline reliability | Partial |
| Return path | Weak |
| Ongoing friction | High |

**Pros:** no new service, no governance change, preserves the clean coursework machine.  
**Cons:** reproduces the measured day-one behavior; `.ROOT` can name work but cannot reliably
supply its source assets or receive the result.  
**Verdict:** reject as the semester default.

### Option B — Make the laptop a full peer `.ROOT` + AI workstation

| Dimension | Assessment |
|---|---|
| Setup | Medium |
| Campus access | High |
| Academic-integrity fit | Poor for three courses |
| Offline reliability | Medium |
| Conflict/blast radius | High |
| Ongoing friction | Medium–high |

**Pros:** the same agents, files, and workflows are available everywhere.  
**Cons:** removes the machine-level AI boundary, creates two writable system surfaces, still
does not solve Git-ignored binaries by itself, and increases sync/conflict and exam-software
risk. It asks Chris to repeatedly police a boundary the current laptop design made structural.
  
**Verdict:** do not adopt during Fall 2026. Reconsider only if a future course mix permits AI
and campus repeatedly needs genuine system-building rather than coursework execution.

### Option C — Remote into the home desktop from campus

| Dimension | Assessment |
|---|---|
| Setup | Medium–high |
| Campus access | Full while connected |
| Academic-integrity fit | Medium; depends on strict task separation |
| Offline reliability | None |
| Security/availability | Home power, network, authentication, and host edition become dependencies |
| Ongoing friction | Medium |

**Pros:** full canonical `.ROOT` with no second writable vault.  
**Cons:** makes every session network-dependent; remote-access software is a poor neighbor for
Respondus; Windows' built-in Remote Desktop requires the host PC to run a Pro edition; and a
remote desktop provides far more capability than a normal campus block needs.  
**Verdict:** emergency/non-graded fallback only, on a separately tested path. Never the normal
coursework interface and never active during an exam.

### Option D — Cloud-sync the whole vault through Obsidian Sync or another second sync service

| Dimension | Assessment |
|---|---|
| Setup/cost | Medium; potentially paid |
| Campus access | High, selectively configurable |
| Academic-integrity fit | Medium |
| Offline reliability | Strong if configured and tested |
| Conflict/blast radius | High beside the existing Git + Drive design |
| Ongoing friction | Medium |

**Pros:** Obsidian Sync can selectively include PDFs and folders and maintain local copies on
multiple devices.  
**Cons:** `.ROOT` already has Git for tracked work and Drive for full backup. Obsidian's own
documentation warns against mixing sync services on the same vault; introducing it here would
reopen exactly the duplicate-authority and conflict problems the August work just stabilized.
  
**Verdict:** reject for the live `.ROOT` vault. A separate, disposable campus-pack vault is a
future fallback only if the proposed bridge cannot meet measured retrieval needs.

### Option E — Control plane + Campus Bridge + separate course workspace

| Dimension | Assessment |
|---|---|
| Setup | Low–medium |
| Campus access | Exact active packet plus complete course binaries |
| Academic-integrity fit | Strong |
| Offline reliability | Strong after one explicit test |
| Conflict/blast radius | Low |
| Ongoing friction | Low if the two packets stay under one minute each |

**Pros:** fits how the courses are actually taught, preserves independent work, uses the
existing laptop and Git clone, solves the binary gap through KSU's existing Microsoft 365
surface, and gives `.ROOT` the one thing it currently lacks: a controlled return.  
**Cons:** requires one bounded placement decision for active course files outside the canonical
vault and discipline to keep the brief/return interfaces small.  
**Verdict:** **recommended.**

## Recommended operating model

### Home — `.ROOT` owns orientation, preparation, and reconciliation

- Sunday/at-home planning reconciles D2L, grades, misses, and course-owner truth.
- Before the next campus run, `.ROOT` emits one brief, not another roadmap.
- AI may teach permitted concepts with fresh examples, build study aids, audit rules, and
  reconcile returned evidence. It does not open, draft, solve, rewrite, or debug prohibited
  submitted work.
- Full system work, governance, durable wiki maintenance, and technology/business work remain
  home-desktop work unless a separate non-course block explicitly activates them.

### Campus — execute the brief without booting the operating system

- D2L/instructor remains the official source; the brief never overrides it.
- Open the active course workspace and `CAMPUS_BRIEF.md`; no full CASTLE load is required.
- Do the assignment, lab, reading, or practice independently in the appropriate course tool.
- If a rule or source conflicts, stop the item, capture the exact conflict, and continue with
  another permitted block. Do not use AI to reason around the course rule.
- End with the five-field return below. Target time: 60 seconds.

```text
Outcome:
Evidence location or score:
Status/movement:
Reusable asset candidate: yes/no
Next exact action or miss:
```

### File and sync boundary

- **`.ROOT`:** desktop canonical; Git clone on laptop remains a scoped operating reference.
- **KSU OneDrive course workspace:** active PDFs, DOCX, XLSX, PPTX, and submitted-work files;
  current-week folders marked **Always keep on this device**. This is an execution workspace,
  not a second knowledge vault.
- **Google Drive `.ROOT`:** backup only, unchanged; never a campus workspace.
- **Brief/return:** tracked Markdown containing metadata and pointers only. No assignment prompt,
  draft, solution, quiz question, WebAssign content, or private course material enters the
  packet.

This boundary needs Chris's approval because `WHERE_IT_GOES.md` currently says course-tied
files live under `04-SCHOOL`. If approved, the smallest governance change is a precise
execution-workspace exception—not a rewrite of the placement map.

## Four-home-day pilot

### Day 1 — approve the boundary and test the course workspace

1. Chris chooses Option E or redirects it.
2. On the laptop, sign into KSU OneDrive and create one Fall 2026 course workspace outside the
   `.ROOT` clone.
3. Put only one week's active course binaries there and mark the folder **Always keep on this
   device**.
4. Disconnect Wi-Fi and prove the named files open and save.

**Proof:** one PDF and one DOCX open, edit, save, and reopen offline; sync completes after
reconnection.

### Day 2 — build the smallest bridge

1. Create the brief and return templates only after the Option E decision.
2. Populate them from the current weekly plan for one fresh, non-graded practice block.
3. Confirm the brief contains no prohibited content and fits on one screen.

**Proof:** Chris can identify the source, action, stop condition, and proof in under two
minutes without opening `NOW.md` or the full weekly plan.

### Day 3 — simulated campus run

1. Pull the Git clone.
2. Turn Wi-Fi off.
3. Run a 60–90 minute independent practice/reading block from the brief.
4. Write the return packet and reconnect/push.

**Proof:** the block finishes with no missing asset, no AI surface, no duplicate file, and a
return packet written in under one minute.

### Day 4 — home reconciliation and verdict

1. Pull on the desktop and re-read before writing.
2. Reconcile the return to the owning course/wiki/CASTLE file.
3. Measure preparation time, start time, missing-context events, return time, and conflicts.
4. At the August 30 CASTLE return, record **keep / modify / revert**.

**Proof:** owner truth and the next action can be updated from the packet in under five minutes,
without exposing graded work to AI.

## Acceptance and stop rules

Keep the model only if all are true after the real pilot:

- campus start takes less than two minutes;
- every active file opens offline;
- the brief has one action and no copied dashboard;
- the return takes one minute or less;
- home reconciliation takes five minutes or less;
- no prohibited assignment content enters AI context;
- no Git conflict, duplicate vault, or Drive workspace appears; and
- Chris reports the interface helps execution rather than adding ceremony.

Modify or revert if any condition fails twice. Escalate to a separate Obsidian campus-pack
vault only if missing-reference friction repeats after the course workspace is proven. Test
remote access only if a real non-graded need requires the full home environment from campus.

## Consequences and affected owners if approved

| Change | Owner / likely file | Authority |
|---|---|---|
| Approve Option E and the external execution-workspace exception | Chris | Required before implementation |
| Define the brief and return packet | CASTLE, likely `CAMPUS_LAPTOP_BUILD.md` plus two small interfaces | Structural interface; Chris approval |
| Record the laptop in the machine inventory | `00-BRAIN\LOCAL_MACHINE_MAP.md` | Ordinary reconciliation after approval |
| Correct the #105 stale-tree contradiction | `LOCAL_MACHINE_MAP.md` + flag owner evidence | Reconcile only after exact Drive tree is verified; no deletion |
| Test offline course files and the round trip | Laptop + desktop | Chris operates credentials; AI records results |
| Review pilot | August 30 CASTLE return | Keep / modify / revert |

## External capability checks — August 27, 2026

- KSU's current student technology guide includes Microsoft 365 and OneDrive:
  [KSU Technology Guide for Students](https://campus.kennesaw.edu/offices-services/uits/docs/technology-guide/ksu-technology-guide-students.pdf).
- Microsoft documents that OneDrive folders can be marked **Always keep on this device** for
  offline access: [OneDrive Files On-Demand](https://support.microsoft.com/en-us/onedrive/save-disk-space-with-onedrive-files-on-demand-for-windows).
- GitHub Codespaces can provide browser-based repository access, but it clones the repository
  and therefore does not solve `.gitignore`'s missing binaries:
  [What are GitHub Codespaces?](https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces).
- Obsidian Sync supports selective file/folder sync, while Obsidian cautions against mixing sync
  services on the same vault: [Selective syncing](https://obsidian.md/help/sync/settings) and
  [sync methods and cautions](https://obsidian.md/help/sync-notes).
- Microsoft's built-in Remote Desktop requires the host PC to run Windows Pro:
  [How to use Remote Desktop](https://support.microsoft.com/en-US/Windows/Experience/Connectivity-Networking/how-to-use-remote-desktop).

## Decision

**Recommended decision:** approve **Option E** for a four-day pilot, with no full-vault sync,
no campus AI install, no remote-access default, and no governance change beyond the smallest
course-execution workspace exception that the successful pilot proves necessary.

**What would change the recommendation:** a course explicitly permits AI on submitted work;
campus repeatedly requires full system-building; the course workspace fails offline; or the
brief/return bridge fails its time and conflict gates twice.

**Next exact action:** Chris rules Option E; if approved, begin Day 1 with one course, one PDF,
one DOCX, and one offline round-trip—not the whole semester tree.

