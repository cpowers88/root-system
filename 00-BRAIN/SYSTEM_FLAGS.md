---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.

> **⏸ `.ROOT` is PAUSED (declared 2026-08-12, resumes on Chris's `OK TO START`).**
> The queue does not run; dated commitments are exempt. Full scope: the PAUSED block
> at the top of `.ROOT\NOW.md`.
>
> **❄ FINDING FREEZE operative (2026-08-13).** New findings are **filed** to
> `Session_Logs\System Update Log\2026-08-12_ROOT_UPDATE\UPDATE_PLAN.md`, **not worked** —
> unless 🔴 HIGH. Binds every surface including Codex.

### Last updated: August 13, 2026 — flags #99 and #94 closed; this file split into operational register + forensic detail (T2).

---

## 🚫 Live prohibitions — what a session may NOT do

**These are the operative constraints. They are stated here in full, never as a pointer.**

1. **DO NOT DEDUPE `raw\` ON HASH — and AI may not write under any `raw\` at all.**
   Seven files in `03-WIKIS\SYSTEMS\raw\` hold only two articles between them, and **five
   sources survive as a filename with no content.** The filename is the *only* record of
   what is missing, so a hash-based cleanup destroys the evidence rather than tidying it.
   Two checks are required for any future pass — hashing and name-comparison each missed
   part of the loss alone. *(flag #97)*

2. **The bulk-work gate covers `Bash`, NOT `PowerShell`.** Its matcher is `"Bash"` only, so
   PowerShell tool calls are entirely ungated — and the August 10 incident that created this
   control was a PowerShell script. **Never describe the gate as covering "bulk work"; it
   covers bulk `Bash`.** On Windows, bulk work is governed by discipline alone: copy-first
   **and** `00-BRAIN\scripts\safe_shell.sh`, per `AGENT.md` File Safety 12. A spawned child
   process can still write `88-JOURNAL` and every `raw\`. *(flag #96)*

3. **Situational procedures may move behind a conditional load. Methods and prohibitions
   used every time may not.** The July 11, 2026 slim pass moved the seven teaching methods
   behind a trigger; they stopped being applied, which became flag #94 (closed 2026-08-13).
   This is the guardrail on every future load-reduction pass, including this file's own.

---

## The Rule

Every system improvement flag lands here the moment it is raised — in a session, a handoff,
a weekly, anywhere.

| | Priority | Fix by |
|---|---|---|
| 🔴 | **HIGH** | **In the session that raised it.** Do not close a session with an open HIGH flag |
| 🟠 | **MEDIUM** | The next weekly review |
| 🟢 | **LOW** | The next monthly review |

A flag leaves this file only when the fix is verified in the target file. "I'll remember" is
not a status. If the same flag is re-raised after being closed, it comes back as HIGH.

**History rule:** this file holds OPEN flags only. When a flag closes, its row moves in the
same session to `00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md`.

---

## OPEN FLAGS — index

**No HIGH flags open.** Full forensics for every row: **`00-BRAIN\SYSTEM_FLAGS_DETAIL.md`**
(not loaded at session start — open it when *working* a flag).

| # | Subject | Pri | Owner | Next action / check moment |
|---|---|---|---|---|
| **97** | `raw\` capture loss — **prohibition 1 above**. Reconciliation done, nothing deleted; recovery list on file | 🟠 | Chris | Re-clip 5 lost sources; **fix or retire the clipper before pointing it at anything else**. Monthly review |
| **96** | Spawned child can write `88-JOURNAL` + every `raw\` — **prohibition 2 above**. Accepted-with-controls; not fixable here | 🟠 | re-measure `verify_controls.py` | At any `.claude\` change **and** monthly. Do not read Windows `NOT MEASURABLE` as safety |
| **57** | PHYS 2211 **§54** and ENGR 1000 BWD syllabi still unpopulated. Neighbour sections 51 + 55 on file are reference-only and do **not** substitute | 🟠 | Chris, `04-SCHOOL\SYLLABUS_STATUS.md` | **Aug 17 — escalate: email the instructors directly** |
| **93** | HIGH-flag-before-close rule is prose, not enforced — a session can skip it | 🟠 | Codex → Claude Code | Codex designs hook mechanics (block vs. warn), then implement. Approved Aug 7 |
| **16** | Right-hand rule needs a physical anchor before cross product / torque appear | 🟢 | Atlas / PHYSICS | Next physics session touching vector products — **approaching** |
| **69** | Byte-identical duplicate in AIAS `raw\`; archive decided, AI cannot execute it | 🟢 | Chris | Chris moves the file himself, outside the `raw\` guard |

---

## CLOSED FLAGS

`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` (current:
`CLOSED_FLAGS_2026-08.md`). Pre-ledger history (June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`.

---
*Maintained by: Claude + Chris | Reviewed: every session start (HIGH), weekly (MEDIUM), monthly (LOW)*
*Split into register + detail 2026-08-13 (T2). **Check moment:** re-test at the Friday gate and again at the next monthly review — keep/modify/revert on fresh-session behaviour and flag discoverability.*
