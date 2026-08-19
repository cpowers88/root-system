---
type: flags
timeline: now
status: active
tags: [governance]
---

# SYSTEM_FLAGS.md — Open Improvement Flags
### Location: 00-BRAIN\ | Check at every session start.

> **▶ `.ROOT` IS RUNNING. Chris gave `OK TO START` on 2026-08-17.** The pause
> (2026-08-12) and the finding freeze (2026-08-13) are both **over**. New findings are
> worked on their normal priority again — 🔴 in session, 🟠 at the weekly, 🟢 at the
> monthly — not filed to `UPDATE_PLAN.md`. That file is now the update's historical
> record, not a live queue.

### Last updated: August 18, 2026 (evening) — **register header corrected:** it claimed one HIGH flag was open while #102's row read 🟢; no priority changed, the summary line now matches the table. Earlier the same day — **#100 closed:** on-demand stale-overwrite guard shipped with deterministic tests; intentionally not wired into `root_health.py` before Aug 24. **#57 half closed:** the exact PHYS 2211 §54 syllabus arrived, PHYS moved 🔴 → 🟢 across the school files and the semester pathway was rebuilt on it; #16 now carries a real date (Oct 23 torque). Aug 17: pause and finding freeze lifted on `OK TO START`; findings N5 and N6 closed. Aug 16: #102 relocation verified and downgraded 🟢; #102, #100, #101 opened; prohibition 1 extended.

---

## 🚫 Live prohibitions — what a session may NOT do

**These are the operative constraints. They are stated here in full, never as a pointer.**

1. **DO NOT DEDUPE `raw\` ON HASH — and AI may not write under any `raw\` at all.**
   Seven files in `03-WIKIS\SYSTEMS\raw\` hold only two articles between them, and **five
   sources survive as a filename with no content.** The filename is the *only* record of
   what is missing, so a hash-based cleanup destroys the evidence rather than tidying it.
   Two checks are required for any future pass — hashing and name-comparison each missed
   part of the loss alone. *(flag #97)*

   **Extended 2026-08-16 (flag #102):** `(1)`-suffixed files exist in `raw\`, `99-ARCHIVE\`
   and `77-INBOX\` dating to June–August. **They are not Drive conflict debris and must not
   be swept.** Only the eight inside `.git\`, stamped Aug 16, are. A bulk `*(1)*` cleanup
   would destroy `raw\` evidence — this is flag #97's exact failure in a new costume.

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

**🟢 NO HIGH FLAGS OPEN.** *(Corrected 2026-08-18 — this line still read "🔴 ONE HIGH FLAG
OPEN — #102" while #102's own row, three lines below, had been marked 🟢 on the Aug 16
measurement. Codex's morning health review spotted the contradiction and correctly made no
repair — it was a read-only pass. Reconciling an index line to the table beneath it is
maintenance, not a downgrade: **no flag's priority was changed by this edit.** It matters
because `AGENT.md` forbids closing a session with an open HIGH flag, so a stale header makes
that rule unenforceable in both directions.)*

Full forensics for every row: **`00-BRAIN\SYSTEM_FLAGS_DETAIL.md`** (not loaded at session
start — open it when *working* a flag).

| # | Subject | Pri | Owner | Next action / check moment |
|---|---|---|---|---|
| **102** | **Google Drive writes conflict copies into `.git\`.** ✅ **FIXED AND MEASURED 2026-08-16.** The gitdir was relocated to `C:\Users\chris\.root-git`, outside every Drive-mirrored folder, and **step 4 passed with Drive live and synced**: git writes produced **zero conflict copies** in the gitdir and none new in the vault; `fetch` exit 0; `fsck` clean. Drive can no longer reach the repo metadata at all. Downgraded 🔴 → 🟢 on that measurement, per the procedure's own downgrade rule. **Not yet closed** — the passing sample is one evening, and this flag has already been widened once by measurement. It closes at the Aug 23 backup review if a week of Drive runtime stays clean | 🟢 | Claude Code (done) → Chris confirms at the Aug 23 review | **Re-check at the Aug 23 backup review:** `Get-ChildItem C:\Users\chris\.root-git -Recurse -Force -Filter '*(1)*'` — no output closes it. **Separate and still open:** the stale `G:\My Drive\desktop_folder_maybe\.ROOT` (16,091 files, Aug 9) is still on Drive, so Drive holds two `.ROOT` trees. Full record: `System Update Log\2026-08-12_ROOT_UPDATE\FLAG_102_GITDIR_RELOCATION.md` |
| **101** | **The bulk-work gate denies read-only work.** Five blocks in one session (2026-08-16): `git show \| grep`, `find -exec ls`, a `for` loop running `wc`, `xargs printf`, and **a `git commit` whose only offence was the word "robocopy" inside the commit message prose.** It matches shell *shape and text*, not write intent; on Windows the offered remedy is a WSL re-launch of a command that only reads. **Risk is erosion, not breakage** — it trains sessions toward the `ALLOWED_SCRIPTS` hatch, which `AGENT.md` File Safety 12 names as not-a-control. Related to #96 (same gate) | 🟢 | **Chris** (`.claude\` is tool config, needs his approval) | Exempt an explicit read-only verb set in `.claude\hooks\require_safe_shell.py`; do **not** widen `ALLOWED_SCRIPTS` instead. At any `.claude\` change |
| **97** | `raw\` capture loss — **prohibition 1 above**. Reconciliation done, nothing deleted; recovery list on file | 🟠 | Chris | Re-clip 5 lost sources; **fix or retire the clipper before pointing it at anything else**. Monthly review |
| **96** | Spawned child can write `88-JOURNAL` + every `raw\` — **prohibition 2 above**. Accepted-with-controls; not fixable here | 🟠 | re-measure `verify_controls.py` | At any `.claude\` change **and** monthly. Do not read Windows `NOT MEASURABLE` as safety |
| **57** | **HALF CLOSED 2026-08-18.** ✅ **PHYS 2211 §54 syllabus RECEIVED** direct from Farhan Islam — the Aug 17 escalation email worked overnight. Exact section confirmed (it lists recitations 51–54 under one lecture, including §54 Fri 11:30 Atrium 1116). Grading, all four unit-exam dates + the final, the AI policy, scope, and a clean 15-week calendar are all now known; `04-SCHOOL\SEMESTER_MAP.md` moved PHYS 🔴 → 🟢 and the pathway was rebuilt the same session. **Remaining: ENGR 1000 BWD only.** Instructor is **Kamyar Raoufi**, not Lori Lowder (corrected 2026-08-17; ENGR rotates instructors across a standardized syllabus) | 🟠 | Chris, `04-SCHOOL\SYLLABUS_STATUS.md` | **ENGR half only.** Raoufi (`kraoufi@`) was asked how the 50% attendance-quiz component works in a web section — a question no reference syllabus can answer. **Sent is not received.** Check moment: **Fri Aug 21.** No reply by then → plan ENGR as if attendance is graded and verify in week 1; re-check D2L on Aug 24 when it opens. **PHYS needs no further action** beyond confirming §54's unit-exam room/time on day one (the syllabus prints another section's recitation slot) |
| **93** | HIGH-flag-before-close rule is prose, not enforced — a session can skip it | 🟠 | Codex → Claude Code | Codex designs hook mechanics (block vs. warn), then implement. Approved Aug 7 |
| **16** | Right-hand rule needs a physical anchor before cross product / torque appear | 🟢 | Atlas / PHYSICS | ⏰ **Now dated (2026-08-18, from the exact §54 syllabus): torque and moment of inertia are lectured Fri Oct 23.** On the one-week-ahead rule the anchor is **due in the Oct 12–18 study window.** Use his hands and a real wrench or breaker bar, never a symbol rule (`HAT_PHYSICS` § Method 4) |
| **69** | Byte-identical duplicate in AIAS `raw\`; archive decided, AI cannot execute it | 🟢 | Chris | Chris moves the file himself, outside the `raw\` guard |

---

## CLOSED FLAGS

`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md` (current:
`CLOSED_FLAGS_2026-08.md`). Pre-ledger history (June 8 – July 11, 83 rows):
`99-ARCHIVE\ARCHIVED_2026-07-11_SYSTEM_FLAGS_CLOSED_TABLE.md`.

---
*Maintained by: Claude + Chris | Reviewed: every session start (HIGH), weekly (MEDIUM), monthly (LOW)*
*Split into register + detail 2026-08-13 (T2). **Check moment:** re-test at the Friday gate and again at the next monthly review — keep/modify/revert on fresh-session behaviour and flag discoverability.*
