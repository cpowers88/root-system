---
type: report
timeline: now
status: active
tags: [laptop, configuration, security, school, fall-2026, d2l, syllabus]
created: 2026-08-18
session_date: 2026-08-18
---

# Campus laptop — config transfer, the second `.ROOT` copy, and the D2L timing correction

### Written 2026-08-18 to be **read on the laptop**, which has no AI assistant by design (`CAMPUS_LAPTOP_BUILD.md` §5). Every command below is meant to be run by Chris directly. Nothing here requires a session to interpret it.

**Delivery:** this file is tracked, so `git pull` in the clone brings it down. It is not in
`88-JOURNAL`, a `raw\`, `77-INBOX`, or `99-ARCHIVE`, so nothing about it is excluded.

**Companion:** `00-BRAIN\CAMPUS_LAPTOP_BUILD.md` §10 was corrected in the same session and
carries the same conclusions in the build record.

---

## Read this first — the one item with a real downside

**Do not delete the second `.ROOT` you can see on the laptop until it is identified.**

The Drive picture changed on **2026-08-16**: the mirror went **live**, mirroring
`C:\Users\chris\.ROOT` up to drive.google.com under **Computers → [device] → `.ROOT`**
(`LOCAL_MACHINE_MAP.md` §*Google Drive — RELINKED 2026-08-16*). Mirrored computer folders
never appear under `My Drive` — that is correct behaviour, and it is why this looks like a
stray copy from the laptop.

If what you are seeing is that mirror surfaced through Drive on the same account, **deleting it
deletes the desktop's only off-machine copy of `88-JOURNAL`, every `raw\`, and 351 PDFs** —
precisely the set GitHub excludes. There is no second copy of those off the desktop.

### Identify it before touching it

```powershell
Get-ChildItem -Path C:\,D:\,G:\ -Filter '.ROOT' -Directory -Recurse -Force -ErrorAction SilentlyContinue |
  Select-Object FullName, CreationTime, LastWriteTime
```

Then read the result:

| What the path looks like | Verdict |
|---|---|
| Under `G:\`, or any `GoogleDrive` / DriveFS mount | **Live mirror — leave it alone.** This is the desktop's backup seen from another machine, not a stray copy |
| A plain local folder, timestamped **Aug 9 2026 or earlier** | Pre-restructure snapshot. Safe to remove **after** confirming it is not a Drive mount point |
| A local folder containing a nested `.ROOT\.ROOT` | Same shape as the unowned `D:\ARCHIVE\.ROOT`. Safe to remove |
| `C:\Users\thein\Documents\root-system` | **This is your working clone.** Not a duplicate |

A folder can be a Drive mount and still look local. If the timestamps are recent and the tree
is large, treat it as the mirror until proven otherwise.

**Related documentation defect, desktop-side:** `LOCAL_MACHINE_MAP.md:110` still reads
"`G:\My Drive\New folder\.ROOT` is a stale snapshot only; neither it nor Drive sync is a
working tree or AI boot target going forward." That sentence is left over from the July 17
retirement and contradicts lines 39–45 of its own file, where the relink is recorded as live.
**It is the single sentence most likely to authorise deleting the wrong tree.** Fix on the
desktop.

---

## Part A — the sandbox rules are already on the laptop

`.claude\` is tracked in git. The clone already contains, at
`C:\Users\thein\Documents\root-system\.claude\`:

```
.claude/settings.json                     ← deny list, mode locks, PreToolUse hook, sandbox block
.claude/hooks/require_safe_shell.sh        ← launcher (resolves python3/python/py at run time)
.claude/hooks/require_safe_shell.py        ← the File Safety 12 bulk-work gate
.claude/hooks/test_require_safe_shell.py   ← 59 classification + 11 end-to-end cases
.claude/CONTROL_INVENTORY.md               ← what actually enforces vs. what only reads as protection
.claude/user-settings-policy.template.json ← the deploy artifact for user scope
```

**There is nothing to copy over the virtual network for project scope.** `git pull` is the
transfer mechanism and it has already run. The `PreToolUse` hook is declared as
`bash "${CLAUDE_PROJECT_DIR}/.claude/hooks/require_safe_shell.sh"` — a variable, not an
absolute path — so it resolves correctly under a different username without editing.

### What is genuinely missing

| File | Why absent | Action |
|---|---|---|
| `~\.claude\settings.json` (user scope) | Outside the repo | Deploy from the template — Part B |
| `~\.claude\settings.local.json` | `.gitignore:69` excludes it deliberately | Recreate only if needed |
| `~\.codex\AGENTS.md`, `~\.codex\config.toml` | User scope, outside the repo | **Skip** unless Codex is being installed — see Part C |

---

## Part B — deploying user scope, and the path trap that would make it useless

`.claude\user-settings-policy.template.json` exists for exactly this purpose. **Do not copy the
desktop's live `~\.claude\settings.json`** — it is desktop-shaped.

### The trap

The template spells its vault rules `~/.ROOT/88-JOURNAL/**`. On the laptop the vault is at
`C:\Users\thein\Documents\root-system` — different username (`thein`, not `chris`) and
different folder name. Deployed unchanged, **all five vault deny rules would guard
`C:\Users\thein\.ROOT`, which does not exist**: five rules protecting an empty directory while
the real tree sits open.

This is the failure mode `CONTROL_INVENTORY.md` was written to prevent — config that reads as
protection in an audit and enforces nothing — and it is the same shape as the documented WSL
case in that file's §*Vault paths in user-scope policy*.

### Write this to `C:\Users\thein\.claude\settings.json`

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "autoUpdatesChannel": "latest",
  "theme": "dark",
  "permissions": {
    "deny": [
      "Read(~/Documents/root-system/88-JOURNAL/**)",
      "Edit(~/Documents/root-system/88-JOURNAL/**)",
      "Write(~/Documents/root-system/88-JOURNAL/**)",
      "Edit(~/Documents/root-system/**/raw/**)",
      "Write(~/Documents/root-system/**/raw/**)",
      "Bash(rm *)",
      "Bash(rmdir *)",
      "Bash(git reset --hard*)",
      "Bash(git clean *)",
      "PowerShell(Remove-Item *)",
      "PowerShell(Clear-Content *)"
    ],
    "defaultMode": "default",
    "disableBypassPermissionsMode": "disable",
    "disableAutoMode": "disable"
  }
}
```

The `model` line from the template is deliberately omitted — set that per machine.

### Do not "standardize" the two spellings

Project scope (`.claude\settings.json` in the repo) uses leading-slash project-relative
spellings — `Read(/88-JOURNAL/**)`. User scope uses `~/...`. **These are required to differ.**
`00-BRAIN\scripts\validate_boot_chain.py` encodes the split as `project_required_deny` vs.
`user_required_deny`. Forcing them to match on 2026-07-17 broke the validator and produced a
root-health BLOCKER (SYSTEM_FLAGS #76). Read the validator before editing either file's path
syntax.

### Honest note on what these rules buy on this machine

`88-JOURNAL` and every `raw\` are gitignored and **are not on the laptop at all**. The five
vault rules above are forward-looking guards — they bite only if journal or raw content ever
reaches this machine by hand, which rule 3 of `CAMPUS_LAPTOP_BUILD.md` §6 says must not happen.
The rules doing real work here are the destructive-command denies and the two mode locks.

State that plainly rather than counting eleven rules as eleven protections. That distinction is
the entire subject of `CONTROL_INVENTORY.md`.

### Verify rather than assume

```powershell
cd C:\Users\thein\Documents\root-system
python 00-BRAIN\scripts\validate_boot_chain.py    # rules present and well-formed
python 00-BRAIN\scripts\verify_controls.py        # rules actually bite in this environment
```

Presence is not function. `LOCAL_MACHINE_MAP.md` records a backup documented as live for 26
days that had never run; the same standard applies here.

---

## Part C — the decision this transfer depends on

`CAMPUS_LAPTOP_BUILD.md` §5 made the AI boundary **structural**: CSE 1321 and ENGR 1000
prohibit generative AI, PHYS 2211 is treated as prohibited until §54 says otherwise — three of
five courses. §10 records that Claude Code, Codex, and Microsoft's chat extension were all
removed from VS Code on this machine, with no Copilot detected and Settings Sync disabled.

**Permission rules only bite when an agent is reading them.** Deployed today they gate nothing,
because there is nothing on this machine to gate.

That is not an argument against staging the file — having it in place *before* an assistant
ever lands is the right order. But **installing an AI assistant on the laptop reverses §5's
integrity decision**, and that should be a deliberate choice, not a side effect of copying
config across. If the answer is "no assistant," deploy Part B as a dormant guard and skip the
Codex files entirely.

---

## Part D — the D2L timing correction

**The LockDown Browser practice quiz could not have been done before Aug 24.** D2L does not
open until the first day of classes, verified 2026-08-13 against KSU's own documentation
(`SEMESTER_MAP.md` §*What must come from D2L*), which already ruled that the practice run
happens in week 1 rather than before it. An empty D2L before Aug 24 is normal and is **not** an
account problem.

**The real deadline is Test 1, Monday Oct 5** — six weeks after D2L opens.

| Date | Event |
|---|---|
| **Mon Aug 24** | D2L opens. Week 1 begins |
| Sun Sep 6 | Quiz 1 |
| **Mon Oct 5** | **TEST 1** — first confirmed LockDown Browser requirement |
| Mon Nov 9 | Test 2 |

### Scope correction — LockDown is exam-scoped, not quiz-wide

`CAMPUS_LAPTOP_BUILD.md` §2.1 reads the requirement as covering all 10 quizzes and 3 exams. The
syllabus is narrower:

- Line 84: "**Exams** will require the use of the Respondus LockDown Browser…"
- Line 82: quizzes and exams are *delivered online through D2L* — a different claim

Treat LockDown as exam-scoped and **confirm against the live D2L quiz settings in week 1**,
because the syllabus is demonstrably carrying stale text (Part E).

### Do these now — none depend on D2L

1. **Webcam and microphone** in Windows Camera and Sound settings. This is the hardware half of
   the LockDown requirement and the place a BIOS camera toggle or physical shutter would
   surface. Two minutes, and August is when you want to find a problem, not Oct 5.
2. **Campus Wi-Fi** (`KSU Wireless` / eduroam) — on campus, not at home.
3. **Charger endurance** and KSU service logins.

---

## Part E — syllabus date errors, to verify in week 1

The CSE 1321 calendar runs **Monday–Sunday**, quizzes due **Sunday 11:59 PM**, tests Monday
(MWF/MW) or Tuesday (TR). **Week 1 = Aug 24 is correct as printed.** Measured against that
pattern, in `03-WIKIS\PYTHON\raw\syllabi\CSE 1321 BF (81262) Fall 2026 Syllabus.md`:

| Line | Problem | Status |
|---|---|---|
| 236 | Week 15 topic reads "*May 4th, 2026, Last Day of Classes*" in a **Fall** syllabus | **Confirmed error.** Spring 2026 template carryover — May 4 and Dec 7 are both Mondays; the date column was updated and the parenthetical was not |
| 221 | Week 1 "Syllabus & Policy Quizzes" due **Dec. 07** | **Ambiguous — do not assume a typo.** It breaks the Sunday-due pattern (week 1's Sunday is Aug 30), but Dec 7 *is* the last day of classes, exactly where an open-all-semester policy quiz would legitimately sit. Resolve in D2L |
| 237 | Final Exams Week "**Dec 8 – 24**" | Questionable — 17 days, ending Christmas Eve. Verify against the KSU academic calendar |
| 235–236 | **Module 7 never appears** (0, 1, 2, 3, 4, 5.1, 5.2, 6, TBD, 8) | Week 14's "TBD" is probably Module 7 |

Either reading of the Dec 07 item leaves the laptop conclusion unchanged: a syllabus/policy
quiz is not an exam, so LockDown is not implicated either way.

**Why this matters beyond four dates.** One confirmed carryover means the document cannot be
trusted for exact dates without a second check. From Aug 24, the live D2L course and Chris's
own calendar are the authorities; this syllabus is a draft until then.

`SEMESTER_MAP.md:261` currently queues this as "confirm the week-1 quiz date anomaly" —
singular. It is four items, and the carryover is the reason to distrust the rest.

---

## Checklist

| # | Item | Depends on | Done |
|---|---|---|---|
| 1 | Run the `Get-ChildItem` sweep; **identify the second `.ROOT` before deleting anything** | Nothing | ☐ |
| 2 | Webcam + microphone in Windows Camera | Nothing | ☐ |
| 3 | Campus Wi-Fi on campus | Being on campus | ☐ |
| 4 | Charger endurance + KSU logins | Nothing | ☐ |
| 5 | Decide the §5 question — assistant on this machine, yes or no | Chris | ☐ |
| 6 | Deploy user-scope `settings.json` with rewritten paths (Part B) | #5 | ☐ |
| 7 | `validate_boot_chain.py` + `verify_controls.py` on the laptop | #6 | ☐ |
| 8 | Confirm whether Quiz 1 requires LockDown | D2L, Aug 24 | ☐ |
| 9 | LockDown practice quiz | D2L, **well before Oct 5** | ☐ |
| 10 | Verify the four Part E date items | D2L, Aug 24 | ☐ |

**Desktop-side, separate:** fix `LOCAL_MACHINE_MAP.md:110`; expand `SEMESTER_MAP.md:261` from
one anomaly to four.

---

*Sources: `00-BRAIN\CAMPUS_LAPTOP_BUILD.md` §5, §6, §10 · `00-BRAIN\LOCAL_MACHINE_MAP.md`
§Google Drive, §Backup · `.claude\CONTROL_INVENTORY.md` §Environment-dependent values ·
`04-SCHOOL\SEMESTER_MAP.md` §What must come from D2L · `03-WIKIS\PYTHON\raw\syllabi\CSE 1321 BF
(81262) Fall 2026 Syllabus.md` lines 82, 84, 219–237.*
