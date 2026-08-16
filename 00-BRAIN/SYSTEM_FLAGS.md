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

### Last updated: August 16, 2026 (evening) — #102's gitdir relocation executed and verified; it stays 🔴 pending step 4 only. Earlier that day: #102, #100 and #101 opened; prohibition 1 extended.

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

**🔴 ONE HIGH FLAG OPEN — #102.** Full forensics for every row:
**`00-BRAIN\SYSTEM_FLAGS_DETAIL.md`** (not loaded at session start — open it when
*working* a flag).

| # | Subject | Pri | Owner | Next action / check moment |
|---|---|---|---|---|
| **102** | **Google Drive writes conflict copies into `.git\`.** ✅ **Breakage cleared Aug 16**, and ✅ **the durable fix is now installed** — the gitdir was relocated to `C:\Users\chris\.root-git` at 18:14, outside every Drive-mirrored folder. `.git` is a 33-byte pointer file; `fetch` exit 0; `fsck` clean; backup re-run with the new layout (`D:\BACKUPS\.ROOT-git`, 752 files, sentinel present) and guard C did **not** trip. The VS Code lock that blocked the earlier session was environmental — a Windows Terminal session with `Code`/`Drive`/`Obsidian`/`GitHub Desktop` all closed renamed it first try. **Still HIGH for one reason only: step 4 has not run.** Drive was not loaded, so "no conflict copy returns after a git write with Drive live" is designed-for, not yet measured — and this flag has already been widened once by measurement | 🔴 | Claude Code (steps 1–3 done) → step 4 needs Drive up | **Step 4 only:** resume Drive, `git fetch origin`, then `Get-ChildItem C:\Users\chris\.root-git -Recurse -Force -Filter '*(1)*'` — **expect no output**. Downgrade to 🟢 on that. Procedure + full execution record: `System Update Log\2026-08-12_ROOT_UPDATE\FLAG_102_GITDIR_RELOCATION.md` |
| **100** | **A stale copy silently overwrote two authoritative files** and was committed (`1c7bebc`): `UPDATE_PLAN.md` 1,081→252 lines, `fall_2026_capacity_decision.md` reverted past its own first commit. **Two candidate vectors, neither excluded:** an editor buffer held open across days, or Drive pushing down an older version — Drive is proven to write into the live vault (#102), and `(1)` copies dated **Aug 13** appeared in the tree only after the Aug 16 link. **Nothing detects this**: `root_health.py` reads disk and cannot know a file predates its own history; the frontmatter audit passed over the `register:` violation the same save introduced. Recovered from `1c7bebc~1` | 🟠 | Chris (procedural) → Claude Code (control) | **Now:** `git diff` before committing a file you did not edit this session. **After Aug 24:** design a pre-commit check for a file shrinking sharply or reverting past its last commit. Monthly review |
| **101** | **The bulk-work gate denies read-only work.** Five blocks in one session (2026-08-16): `git show \| grep`, `find -exec ls`, a `for` loop running `wc`, `xargs printf`, and **a `git commit` whose only offence was the word "robocopy" inside the commit message prose.** It matches shell *shape and text*, not write intent; on Windows the offered remedy is a WSL re-launch of a command that only reads. **Risk is erosion, not breakage** — it trains sessions toward the `ALLOWED_SCRIPTS` hatch, which `AGENT.md` File Safety 12 names as not-a-control. Related to #96 (same gate) | 🟢 | **Chris** (`.claude\` is tool config, needs his approval) | Exempt an explicit read-only verb set in `.claude\hooks\require_safe_shell.py`; do **not** widen `ALLOWED_SCRIPTS` instead. At any `.claude\` change |
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
