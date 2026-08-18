---
type: flags
timeline: reference
status: active
tags: [governance]
---

# SYSTEM_FLAGS_DETAIL.md — Open Flag Forensics

### Location: 00-BRAIN\ | **NOT loaded at session start.** Open this when *working* a flag.

**`00-BRAIN\SYSTEM_FLAGS.md` is the always-loaded operational register** — it carries what a
session must not do, and one row per open flag. This file carries the measurement history,
what was tried, which probe was wrong, and the provenance disputes. Split 2026-08-13 (T2 /
Phase D), because the register was 29% of every session's boot load and the only component
growing without bound.

**The rule that governs this split, learned from flag #94:**

> **Situational procedures may move. Methods and prohibitions used every time may not.**

Flag #94 was created by the July 11, 2026 slim pass, which moved the seven teaching methods
behind a conditional load; they then stopped being applied. Nothing in this file is a
prohibition or a method. **Every operative constraint stays in the slim register in full
imperative form.** If you find yourself needing this file in order to know what you may not
do, that is a defect — report it.

Closed flags are not here. They live in
`00-BRAIN\Session_Logs\Closed Flags\CLOSED_FLAGS_YYYY-MM.md`.

---

## Flag #102 — Google Drive writes conflict copies into the gitdir

**Raised:** August 16, 2026 · **Priority:** 🔴 HIGH · **Owner:** Chris (the move), Claude Code
(the prep) · **Check:** on completion of the relocation procedure

### The mechanism

Google Drive mirrors `C:\Users\chris\.ROOT`. Git rewrites `.git\refs\heads\main` on every
commit, fetch and pull. When Drive is mid-upload of that file at the moment git rewrites it,
Drive resolves the collision the only way it knows — it writes a **conflict copy** beside the
original, named `main (1)`. That copy carries a **null SHA** and a refname git considers
invalid. Git walks the refs directory, finds it, and refuses to proceed:

```
fatal: bad object refs/heads/main (1)
```

Eight such files appeared on 2026-08-16, stamped at the exact second of three separate git
writes — 11:35:37, 12:16:53, 12:29:59.

### What was never true

**No object corruption ever occurred.** `git fsck` reported bad ref *names* only. Local and
GitHub stayed in sync throughout (`08adc9a`, later `52296bf`). Nothing was lost at any point.
The flag was a availability failure, not an integrity failure — worth stating because a
"corrupted git" framing invites a re-clone, which would have been destructive overkill.

### Resolution measured 2026-08-16

| Check | Result |
|---|---|
| `(1)` files under the gitdir | none |
| `git fetch origin` | exit 0 |
| `git fsck` | clean (one harmless dangling blob) |
| Local vs GitHub | both `52296bf` |
| Working tree | clean |

### Why it stayed HIGH after the breakage cleared

**The cause was untouched.** Drive was *paused*, not unlinked, and
**Drive for desktop has no mechanism to exclude a subfolder from a mirrored folder** — there
is no setting to keep the mirror and skip the gitdir. The failure returns on the first git
write after Drive resumes. A cleared symptom over a live cause is not a closed flag.

### The three options, and why the third was chosen

| | Option | Cost |
|---|---|---|
| A | Unlink `.ROOT` from Drive | Loses the off-machine copy of `88-JOURNAL`, every `raw\`, and 351 PDFs — precisely the material GitHub excludes and the reason the link exists |
| B | Accept recurring cleanup | Breaks git after most sessions, and **only Chris can clear it** — `Remove-Item` is denied to every AI surface here |
| C ✅ | Move the gitdir outside the mirrored tree | Keeps the mirror, removes the only part of the tree that breaks under sync. Nothing is lost: GitHub already holds the full history |

**Chris chose C on 2026-08-16.**

### Why it could not be finished in the session that raised it

`git init --separate-git-dir` renames the `.git` directory, and Windows refuses to rename a
directory any process holds a handle on. GitHub Desktop, Obsidian and Google Drive were all
closed and the rename was **still** denied. The remaining holder was VS Code — and the
Claude Code session doing the work was running inside VS Code's own integrated terminal:

```
pwsh.exe <- claude.exe <- pwsh.exe <- Code.exe <- Code.exe <- explorer.exe
```

Closing the blocker would have ended the session doing the closing. **This is the reusable
lesson: a session cannot remove a lock held by its own parent process.** Any future work that
must move, rename or delete something under `.ROOT` should check the process ancestry first
(`Get-CimInstance Win32_Process`) rather than discovering it after a failed attempt.

### The second-order defect this nearly caused

`backup_to_d_drive.ps1` mirrors with `/MIR` and **deliberately includes** `.git` — its header
records that excluding it once produced *"a restore from D: that produced an unversioned
vault"* (defect 3). Relocating the gitdir would have re-created that defect by a new route,
and would additionally have broken the backup outright: the gitdir is **747 files, 14.4% of
the measured 5,200**, so removing it trips guard C's 10% shrink tripwire on *every* run —
training the operator to reach for `-Force`, which is how a tripwire becomes noise.

Both were fixed before the move, not after: a sentinel-guarded third pass mirrors the external
gitdir to `D:\BACKUPS\.ROOT-git`, and the gitdir is measured back **into** the totals guard C
compares. The path is read from the `.git` pointer file at run time, so no stale second copy
of it exists. Five tests passed, three of them negative. Full account and the step-by-step
procedure: **`Session_Logs\System Update Log\2026-08-12_ROOT_UPDATE\FLAG_102_GITDIR_RELOCATION.md`**.

### The prohibition this generated

`(1)`-suffixed files exist in `raw\`, `99-ARCHIVE` and `77-INBOX` dating to June–August and
are **not** Drive debris. Only ones inside the gitdir, stamped at a git-write moment, are.
A bulk `*(1)*` sweep would destroy `raw\` evidence — **flag #97's exact failure in a new
costume.** Stated operatively in `SYSTEM_FLAGS.md` prohibition 1; never act on it from here.

---

## Flag #101 — forensics not yet written

**Opened 2026-08-16.** The register promises detail for every row and this one does not
have it yet. The source below stands as its record until the forensics are written.

- **#101** (🟢, the bulk-work gate denies read-only work): five blocked calls listed in the
  `SYSTEM_FLAGS.md` row; `.claude\CONTROL_INVENTORY.md` for what the gate actually covers.

---

## Flag #97 — `raw\` capture loss

**Raised:** August 12, 2026 (from the Aug 11 council review) · **Priority:** 🟠 MEDIUM ·
**Owner:** Chris · **Check:** monthly review

### The measurement

Measured 2026-08-11 across all 2,277 non-journal `.md` files: seven files in
`03-WIKIS\SYSTEMS\raw\` hold **two articles between them** (4 identical + 3 identical). This
is capture loss, not duplication.

### The mechanism

The Obsidian clipper pre-fills the note name from whichever tab was active when the popup
opened, then re-extracts the body at save time — so the **filename** is from the intended
source and the **body** is from a different page. This is why a hash-based cleanup is
destructive: the filename is the only surviving record of what was lost.

**Five sources were never captured at all** and survive only as a filename:

1. "Eight Principles of Good Data Management"
2. "Data Management for Researchers"
3. "13 Project management"
4. "Why Trust Science"
5. the O'Dea talk

A second, distinct clipper defect truncates JavaScript-injected content (the Percipio skills
list) and writes malformed frontmatter (`created: 2226-28-12`). Behind KSU auth, manual copy
is the only path.

### Reconciliation — DONE 2026-08-12

`00-BRAIN\Session_Logs\raw_recovery_list_2026-08-12.md`. All 264 raw `.md` hashed and
name-checked; nothing moved, renamed or deleted. The five missing sources are confirmed and
listed, both surviving articles identified with their URLs, and 37 files carrying no
frontmatter `title:` recorded as outside what this method can see.

### The lesson for any future pass — run BOTH checks

Hashing and name-comparison **each missed part of the loss on their own.** `Data Management
for Researchers` and `Eight Principles of Good Data Management` scored *above* the
name-mismatch threshold because they share words with the NIH article that overwrote them —
only the hash caught those. Running one check and calling the queue clean would have been
wrong.

### What remains

Chris re-clipping the five sources in section A, plus **fixing or retiring the clipper before
pointing it at anything else.** The standing warning is inline at `WIKI_SHARED_LAYER.md`
rule 1, where a cleanup pass would actually read it.

**Candidate replacement noted 2026-08-13:** `lucasastorian/llmwiki` ships a Chrome clipper
that captures highlights and margin notes alongside the source. Related to plan item K-3
(an Obsidian capture template routing to `77-INBOX`). Not evaluated, not installed.

---

## Flag #96 — a spawned child process can write `88-JOURNAL` and every `raw\`

**Raised:** August 11, 2026 · **Priority:** 🟠 MEDIUM · **Owner:** re-measure with
`verify_controls.py` from **both** environments at any `.claude\` change and at the monthly
review

### The measurement

Measured 2026-08-11 from WSL via `verify_controls.py`: `sandbox.filesystem.denyWrite`
reports **10 of 10 paths writable to a spawned child**, and `denyRead` on `88-JOURNAL`
reports the directory **listable** by one. From Windows the same check honestly returns NOT
MEASURABLE — so the exposure is *visible only from the Linux side*, which is why it reads as
a back door you cannot see from this side of the gate.

**Do not treat a Windows `NOT MEASURABLE` as evidence of safety.**

### Why this is not a re-raise of #95

Closed flag #95 was the *pattern* — config declaring controls that do not apply — and is
genuinely closed, with `verify_controls.py` as its test. **This flag is the residual live
exposure that closure left behind.** It is recorded as a flag because Chris went looking for
it in `SYSTEM_FLAGS.md` and found nothing; a risk documented only in
`.claude\CONTROL_INVENTORY.md` is not where anyone looks for open risk.

### Provenance note

A WSL-launched session reported this to Chris and stated it had filed a flag. **No flag was
filed** — `SYSTEM_FLAGS.md` was unchanged since commit `4c6ce56` and the working tree was
clean. The finding was correct; the claim of having recorded it was not.

### Live mitigations

1. `AGENT.md` § File Safety 12 requires **both** copy-first and
   `00-BRAIN\scripts\safe_shell.sh` for any bulk or scripted pass. `safe_shell.sh`
   read-only-binds all 10 paths and is measured ENFORCED.
2. Tool-level `Read`/`Edit`/`Write` denies still govern tool calls — though they match
   command *strings*, not runtime-resolved paths, so a glob or a relative path walks past.
3. **Added 2026-08-11 (Chris-approved):** a `PreToolUse` gate,
   `.claude\hooks\require_safe_shell.sh`, denies bulk or scripted `Bash` not launched
   through the wrapper. Measured **ENFORCED in both environments** 2026-08-11.

   *The first Windows measurement said INERT and was wrong:* the probe shelled through
   `cmd.exe`, where `bash` is the WSL launcher, while Claude Code runs hooks through Git
   Bash. `verify_controls.py` no longer reports a probe launch failure as INERT — **a
   measurement that cannot run is not evidence about its subject.**

### Why it stays open — and the operative limit

The gate governs `Bash` **tool calls**, not arbitrary child processes. Its matcher is
`"Bash"` only, so **`PowerShell` tool calls are entirely ungated** — a bulk-shaped PowerShell
pipeline ran unblocked from a Windows session minutes after the Bash side was certified. The
**August 10 incident that caused this entire flag lineage was a PowerShell script**, so the
gate does not cover the shape of the event it exists to prevent, on the platform where that
shape is native.

Accepted-with-controls: the inert sandbox is Claude Code platform behavior, not a `.ROOT`
misconfiguration. If `verify_controls.py` ever reports ENFORCED, close this and relax File
Safety 12.

**Related, filed under the freeze 2026-08-13:** the gate has now produced **five read-only
false positives** (a word-count loop, two `find -exec` inventories, and two `for` loops
merely *reading* files). It classifies on command *shape*, not write *intent*, and the
wrapper it redirects to cannot run on Windows. Proposed fix — allow read-only verbs through
regardless of shape — needs Chris's approval, since `.claude\` is tool configuration.

---

## Flag #57 — EDUCATION syllabus data-quality gaps

**Raised:** July 9, 2026; updated July 29 · **Priority:** 🟠 MEDIUM · **Owner:** Chris,
`04-SCHOOL\SYLLABUS_STATUS.md` · **Check:** weekly from mid-August; **escalate Aug 17**

D2L is accessible, but **PHYS 2211 Section 54** and **ENGR 1000 Fall BWD** remain
unpopulated. Exact-section CSE 1321, CSE 1321L, ECON 1000 and TCOM 2010 captures are all
filed and current.

**Neighbouring PHYS sections are reference-only and cannot establish §54's grading, dates or
policy.** Sections 55 (captured 2026-07-21) and 51 (captured 2026-08-12, filed 2026-08-13)
are both on file — two of three neighbours — and neither closes this flag.

**2026-07-29:** `04-SCHOOL\fall_KSU_schedule.md` (Chris's actual Outlook registration
confirmation) independently confirms **Farhan Islam** and §54's exact meeting times / CRN
83722 — stronger than the prior provisional online-listing match, but still not the syllabus
content (grading, exams, policy, calendar).

Dated punch list with the Aug 17 escalation trigger: `SYLLABUS_STATUS.md` § Pre-Semester
Punch List. **If nothing posts by Aug 17, email the instructors directly.**

---

## Flag #93 — HIGH-flag-before-close rule is prose, not enforced

**Raised:** July 12, 2026; approved Aug 7 · **Priority:** 🟠 MEDIUM · **Owner:** Codex to
design hook mechanics, then Claude Code or Codex implements

`.claude\skills\session-close\SKILL.md` (lines 38–39) states a HIGH flag must be fixed or
explicitly handed to Chris before session close — but **nothing checks this**; a session can
skip it.

Full analysis and proposed target (`.claude\hooks\` or equivalent, firing on
session-close/stop):
`03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\system-evolution\proposals\2026-07-12_session-close-high-flag-hook.md`.

**Status:** approved by Chris 2026-08-07; blocked on Codex's hook-mechanics design (trigger
event, block vs. warn) per the proposal's Risk/Blast Radius note. The 30-day blocker that
originally held this dissolved 2026-08-11 when hooks were proven live.

---

## Flag #16 — spin rule / right-hand rule needs a physical anchor

**Raised:** June 9, 2026 · **Priority:** 🟢 LOW · **Owner:** Atlas / PHYSICS sessions ·
**Check:** the next physics session touching vector products

Covers cross product, torque, angular velocity, and later magnetic-field direction. Curl
fingers in the direction of rotation, thumb points to the vector. Must be anchored before
these topics appear in PHYS 2211.

**Approaching:** Chris is working Vectors (Serway Ch 3) per CASTLE current-position (July 8);
cross product is next door.

---

## Flag #69 — duplicate raw capture, execution blocked

**Raised:** July 12, 2026; decided Aug 2 · **Priority:** 🟢 LOW · **Owner:** Chris (AI cannot
execute this)

`Agents SDK  OpenAI API 1.md` in
`03-WIKIS\AI_AUTOMATION_SYSTEMS\raw\OPEN_AI-CHATGPT_CODEX_FILES\` is byte-identical
(SHA-256 `0ddb73d5...92db1`) to `Agents SDK  OpenAI API.md` — same defect class as closed
flag #63. Content was read once, not double-summarized.

**2026-08-02:** Chris reviewed the full 85-line content (OpenAI Agents SDK docs clipping) and
decided to archive the duplicate. **Blocked on execution** — `raw\` is under a write guard no
available tool can pass, even with Chris's explicit in-session approval. This is a structural
boundary, not a missing permission click.

**Action:** Chris moves it to
`99-ARCHIVE\ARCHIVED_2026-08-02_AI_AUTOMATION_SYSTEMS_raw_Agents-SDK-OpenAI-API-duplicate.md`
himself.

---

*Maintained by: Claude + Chris. Detail is appended here when a flag is opened or worked; the
one-line row in `SYSTEM_FLAGS.md` is updated in the same pass. A flag's forensics move to
`CLOSED_FLAGS_YYYY-MM.md` when it closes.*
