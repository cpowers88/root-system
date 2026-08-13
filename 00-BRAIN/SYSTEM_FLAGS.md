---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.

> **⏸ `.ROOT` is PAUSED (declared 2026-08-12, resumes on Chris's `OK TO START`).**
> This is state, not a flag — it lives here because this file is the one thing read
> at every session start. The queue does not run; dated commitments are exempt.
> Authority and full scope: the PAUSED block at the top of `.ROOT\NOW.md`.

### Last updated: August 13, 2026 — **flags #99 and #94 CLOSED.** #99: `sync_shared_skills.py` now mirrors whole directories and fails on a reference absent from a mirror; negative-tested on a deliberate break, and the health gate's "PASS: shared skill mirrors" is earned rather than false. #94 (the seven teaching methods are inlined into `HAT_EDUCATOR.md`, the encoding/retrieval model came with them, and all five subject hats now carry the pointer; ~0 always-load cost). ❄ **Finding freeze operative today** — new findings are filed to the update plan, not worked, unless 🔴 HIGH. Prior — August 12, 2026: flag #97 opened (`raw\` capture loss; do not dedupe on hash). Flag #98 opened and closed the same session (backup asserted but never run), then **re-opened and re-closed after independent Codex review found the first scheduled run had failed while the record said "live and verified"** — snapshot failure now fail-closed, partial snapshots now detectable, scheduled run re-verified `LastTaskResult 0` at 14:27. **Residual: the task's `LogonType` is `Interactive` and still dies with Chris's session; `S4U` needs an elevated run.** August 11: flags #92 and #95 closed, #96 opened. No HIGH flags open.

---

## The Rule

Every system improvement flag lands here the moment it is raised — in a session, a handoff, a weekly, anywhere.

**Timing by priority** — severity is colour-coded in the table so it reads at a glance:

| | Priority | Fix by |
|---|---|---|
| 🔴 | **HIGH** | **In the session that raised it.** Do not close a session with an open HIGH flag |
| 🟠 | **MEDIUM** | The next weekly review |
| 🟢 | **LOW** | The next monthly review |

A flag leaves this file only when the fix is verified in the target file. "I'll remember" is not a status.

If the same flag is re-raised after being closed, it comes back as HIGH.

**History rule (updated July 15, 2026):** this file holds OPEN flags only. When
a flag closes, its row moves in the same session to the monthly ledger at
`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` — no weekly
migration step to forget. Pre-ledger history (June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`. This file is
read at every session start — history in it is a per-session context tax.

---

## OPEN FLAGS

| # | Flag | Raised | Priority | Target | Status |
|---|---|---|---|---|---|
| 97 | **`raw\` capture loss — DO NOT DEDUPE ON HASH.** Measured 2026-08-11 across all 2,277 non-journal `.md` files: seven files in `03-WIKIS\SYSTEMS\raw\` hold two articles between them (4 identical + 3 identical). This is capture loss, not duplication. The Obsidian clipper pre-fills the note name from whichever tab was active when the popup opened, then re-extracts the body at save time — so the **filename** is from the intended source and the **body** is from a different page. **Five sources were never captured at all** and survive only as a filename: "Eight Principles of Good Data Management", "Data Management for Researchers", "13 Project management", "Why Trust Science", and the O'Dea talk. A hash-based cleanup deletes the only remaining record of what is missing. A second, distinct clipper defect truncates JavaScript-injected content (the Percipio skills list) and writes malformed frontmatter (`created: 2226-28-12`); behind KSU auth, manual copy is the only path. Warning is now inline at `WIKI_SHARED_LAYER.md` rule 1, where a cleanup pass would actually read it. | August 12 (from the Aug 11 council review) | 🟠 **MEDIUM** | ~~Reconcile filename against frontmatter `title`/`source` across all 9 `raw\` queues and produce a recovery list — **deleting nothing**.~~ **DONE 2026-08-12: `00-BRAIN\Session_Logs\raw_recovery_list_2026-08-12.md`.** All 264 raw `.md` hashed and name-checked; nothing moved, renamed or deleted. The five missing sources are confirmed and listed, both surviving articles are identified with their URLs, and 37 files carrying no frontmatter `title:` are recorded as outside what this method can see. **Note for any future pass: run BOTH checks.** Hashing and name-comparison each missed part of the loss on their own — `Data Management for Researchers` and `Eight Principles of Good Data Management` scored *above* the name-mismatch threshold because they share words with the NIH article that overwrote them, and only the hash caught them. Remaining action is Chris re-clipping the 5 sources in section A, plus fixing or retiring the clipper before pointing it at anything else. Owner: Chris; check at the monthly review. | OPEN — **reconciliation complete, evidence preserved, nothing deleted**; the 5 sources still need re-capture and the clipper defect is unfixed |
| 96 | **A spawned child process can write to `88-JOURNAL` and every `raw\` folder, in both environments.** Measured again 2026-08-11 from WSL via `verify_controls.py`: `sandbox.filesystem.denyWrite` reports **10 of 10 paths writable to a spawned child**, and `denyRead` on `88-JOURNAL` reports the directory **listable** by one. From Windows the same check honestly returns NOT MEASURABLE, so the exposure is *visible only from the Linux side* — which is why it reads as "a back door you cannot see from this side of the gate." The underlying cause is closed flag #95 instance (2): Claude Code's `sandbox` block is declarative and inert here. **This flag is not a re-raise of #95** — #95 was the *pattern* (config declaring controls that do not apply) and is genuinely closed, with `verify_controls.py` as its test. This flag is the *residual live exposure* that closure left behind, recorded here because Chris went looking for it in `SYSTEM_FLAGS.md` and found nothing. A risk documented only in `.claude\CONTROL_INVENTORY.md` is not where anyone looks for open risk. **Note on provenance:** a WSL-launched session reported this to Chris and stated it had filed a flag. No flag was filed — `SYSTEM_FLAGS.md` was unchanged since commit `4c6ce56` and the working tree was clean. The finding was correct; the claim of having recorded it was not. | August 11 | 🟠 **MEDIUM** | **Accepted-with-controls, not fixable here** — the inert sandbox is Claude Code platform behavior, not a `.ROOT` misconfiguration. Live mitigations: (1) `AGENT.md` § File Safety 12 requires **both** copy-first and `00-BRAIN\scripts\safe_shell.sh` for any bulk or scripted pass; `safe_shell.sh` read-only-binds all 10 paths and is measured ENFORCED. (2) Tool-level `Read`/`Edit`/`Write` denies still govern tool calls, though they match command *strings*, not runtime-resolved paths. (3) **Added 2026-08-11 (Chris-approved):** a `PreToolUse` gate, `.claude\hooks\require_safe_shell.sh`, now denies bulk or scripted `Bash` that is not launched through the wrapper, so item 12 is mechanism rather than prose — the 2026-08-10 glob and the 2026-08-11 `fetch_fred.py` execution are both shapes it blocks. Measured **ENFORCED in both environments** 2026-08-11 — Windows settled the same day by a real bulk `Bash` call being denied plus a corrected probe. (The first Windows measurement said INERT and was wrong: the probe shelled through `cmd.exe`, where `bash` is the WSL launcher, while Claude Code runs hooks through Git Bash. `verify_controls.py` no longer reports a probe launch failure as INERT — a measurement that cannot run is not evidence about its subject.) This narrows *how easily the exposure is reached*; it does not close the exposure, since the gate governs `Bash` tool calls and not arbitrary child processes. **Measured 2026-08-11, and it is the largest remaining hole: the hook's matcher is `"Bash"` only, so `PowerShell` tool calls are entirely ungated — a bulk-shaped PowerShell pipeline ran unblocked from a Windows session minutes after the `Bash` side was certified. The August 10 incident that caused this whole flag lineage was a PowerShell script, so the gate does not cover the shape of the event it exists to prevent, on the platform where that shape is native. Windows bulk work is governed by discipline alone until a `PowerShell` matcher with a PowerShell-aware classifier exists. Do not describe this gate as covering "bulk work" — it covers bulk `Bash`.** **Owner and check moment:** re-measure with `verify_controls.py` from **both** environments at any `.claude\` change and at the monthly review; if it ever reports ENFORCED, close this and relax item 12. Do **not** treat a Windows `NOT MEASURABLE` as evidence of safety. | OPEN — measured, mitigated by the wrapper, not eliminated; accepted limitation pending platform support |
| 57 | **EDUCATION syllabus data-quality gaps.** D2L is accessible but PHYS 2211 Section 54 and ENGR 1000 Fall BWD remain unpopulated. Exact-section CSE 1321, CSE 1321L, ECON 1000, and TCOM 2010 captures are all filed and current (see `04-SCHOOL\SYLLABUS_STATUS.md`). Neighboring PHYS Sections 51 and 55 remain reference-only and cannot establish Section 54 grading, dates, or policy. **2026-07-29:** `04-SCHOOL\fall_KSU_schedule.md` (Chris's actual Outlook registration confirmation) independently confirms **Farhan Islam** and PHYS 2211 §54's exact meeting times/CRN 83722 — stronger than the prior provisional online-listing match, but still not the syllabus content (grading, exams, policy, calendar). A dated punch list with an Aug 17 escalation trigger for both remaining gaps now lives in `SYLLABUS_STATUS.md`'s Pre-Semester Punch List. | July 9; updated July 29 | 🟠 **MEDIUM** | Recheck D2L/Simple Syllabus weekly from mid-August; if nothing posts by **Aug 17**, email the instructor directly. Full detail and owner in `SYLLABUS_STATUS.md`. | OPEN — four of six courses fully filed and current; PHYS §54 instructor confirmed via two independent sources, syllabus content still missing; ENGR BWD source still missing |
| 16 | Spin rule / right-hand rule needs physical anchor from Atlas. Covers: cross product, torque, angular velocity, and future magnetic field direction. Curl fingers in direction of rotation, thumb points to vector. Must be anchored before these topics appear in PHYS 2211. | June 9 | 🟢 **LOW** | Atlas / Physics sessions | OPEN — **approaching**: Chris is now working Vectors (Serway Ch 3) per castle current-position (July 8); cross product is next door. Atlas should anchor it in the next physics session that touches vector products. |
| 69 | `Agents SDK  OpenAI API 1.md` in `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\OPEN_AI-CHATGPT_CODEX_FILES\` is byte-identical (SHA-256 `0ddb73d5...92db1`) to `Agents SDK  OpenAI API.md` — same defect class as closed flag #63 (mis-saved duplicate). Content read once, not double-summarized. **2026-08-02:** Chris reviewed the full 85-line content (OpenAI Agents SDK docs clipping) and decided: archive the duplicate. Blocked on execution — `03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\` is under a sandbox-level write guard that no available tool can pass, even with Chris's explicit approval in-session; this is a structural boundary, not a missing permission click. | July 12; decided Aug 2 | 🟢 **LOW** | Chris to move `Agents SDK  OpenAI API 1.md` to `99-ARCHIVE\ARCHIVED_2026-08-02_AI_AUTOMATION_SYSTEMS_raw_Agents-SDK-OpenAI-API-duplicate.md` himself, outside the sandbox guard | OPEN — decision made, execution blocked by raw-folder sandbox guard, needs Chris to run the move directly |
| 93 | **HIGH-flag-before-close rule is prose, not enforced.** `.claude\skills\session-close\SKILL.md` (lines 38-39) states a HIGH flag must be fixed or explicitly handed to Chris before session close — but nothing currently checks this; a session can skip it. Full analysis and proposed target (`.claude\hooks\` or equivalent, firing on session-close/stop) in `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\system-evolution\proposals\2026-07-12_session-close-high-flag-hook.md`. Chris approved moving forward 2026-08-07. | July 12; approved Aug 7 | 🟠 **MEDIUM** | Codex to design the actual hook mechanics (trigger event, block vs. warn) per the proposal's Risk/Blast Radius note, then Claude Code or Codex implements. | OPEN — approved, needs Codex hook-mechanics design before implementation |
---

## CLOSED FLAGS

Closed flags live in the monthly ledger:
`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` (current month:
`CLOSED_FLAGS_2026-08.md`). Pre-ledger history
(June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`.

---
*Maintained by: Claude + Chris | Reviewed: every session start (HIGH), weekly (MEDIUM), monthly (LOW)*
*Current date stamp lives once, in the header above — do not add a second here.*
