---
type: reference
timeline: reference
status: active
register: human-context
tags: [machine, laptop, school, fall-2026, setup]
created: 2026-08-13
---

# CAMPUS_LAPTOP_BUILD.md — HP Victus build specification

### Companion to `LOCAL_MACHINE_MAP.md`, which inventories the desktop and does not currently mention this machine at all. Written 2026-08-13 at Chris's request, after a Windows wipe was already performed and ad-hoc installs begun.

---

## 1. What this machine is for — and what it is not

The calendar answers this precisely. From Aug 24 the laptop carries roughly **20 hours a week
of on-campus working time**: Mon 10:15–12:30, Wed 10:15–12:15, Tue midday, Thu 12:00–14:00 and
15:00–17:00, Fri 15:00–17:00. Its job is those blocks.

| It **is** | It is **not** |
|---|---|
| The coursework machine — Python, writing, reading, D2L | A second full `.ROOT` development environment |
| The **exam machine** (§2 — this is non-negotiable) | A games machine, whatever HP shipped it as |
| A read-mostly `.ROOT` client | The canonical vault. `C:\Users\chris\.ROOT` on the desktop stays canonical |
| Portable, battery-first | A place where irreplaceable data lives only |

**Design rule:** the desktop is where the system gets built; the laptop is where the semester
gets done. Everything below follows from that split.

---

## 2. Hard requirements from the syllabi — the part that was never written down

These come from the exact-section syllabi already on disk, not from assumption. **Both were
absent from every `.ROOT` file before today.**

### 2.1 CSE 1321 exams require Respondus LockDown Browser

> *"Exams will require the use of the Respondus LockDown Browser, which will require a webcam,
> a microphone, and reliable internet access."*
> — `CSE 1321 BF (81262) Fall 2026 Syllabus.md:84`

10 quizzes and 3 exams (Test 1, Test 2, Final) are delivered **online through D2L**, and the
syllabus states he does **not** attend class on exam dates. That means the exam happens
wherever he is — and this machine has to be able to run it.

**Consequences for the build, all of them real:**

- **Webcam and microphone must work.** Many Victus models ship with a BIOS-level camera toggle
  and a physical shutter. Verify both, in Windows Camera, before Aug 24.
- **Install LockDown Browser from the D2L course link only.** It is an institution-specific
  build; a generic download from the vendor will not authenticate against KSU's D2L.
- **It will not run reliably inside a VM**, and it blocks screen capture, remote-access tools,
  and most background applications. This constrains §4's install list.
- **Run one practice quiz with it well before Test 1.** A LockDown failure discovered at exam
  time is a zero, not an inconvenience. This is the single highest-consequence untested item on
  the machine.

### 2.2 ENGR 1000 BWD has no published meeting format

No meeting time on the registrar record and none on the calendar, for a 1-credit course whose
AI policy is known-prohibited. Chris's read is that it is likely online — roughly twelve
~40-minute sessions, or one longer block. **Until the BWD syllabus lands, assume it is online
and that this laptop may need to join live sessions** — which reinforces the webcam/mic
requirement above. This is the second half of flag #57.

---

## 3. The wipe — what "best" actually means, and how to tell what you got

A Windows wipe was already done. **Which kind matters**, because two of the three leave HP's
factory image intact.

| Method | Result |
|---|---|
| Settings → Reset this PC → Remove everything → **Local reinstall** | Restores the **HP factory image**. All OEM bloatware returns |
| Same, but **Cloud download** | Fresh Microsoft build, but the OEM recovery partition and some HP packages typically survive |
| **Clean install from a Microsoft ISO** (Media Creation Tool → USB) | Genuinely clean. Requires installing chipset/GPU/hotkey drivers manually from HP's support page afterward. **This is "best"** |

### Check which one you have — run this on the laptop

```powershell
Get-AppxPackage | Where-Object { $_.Name -match 'HP|myHP|Poly|WildTangent|Booking|ExpressVPN' } |
  Select-Object Name, PackageFullName
Get-CimInstance Win32_Product | Where-Object { $_.Name -match 'McAfee|HP |Norton|WildTangent' } |
  Select-Object Name
Get-ComputerInfo | Select-Object WindowsProductName, WindowsEditionId, OsHardwareAbstractionLayer
```

**If HP/McAfee/WildTangent packages appear, it was a factory reset, not a clean install.**

**Recommendation:** if the machine is not yet holding anything that would be painful to lose,
redo it once as a clean ISO install. It costs about 90 minutes and it is the only version that
does not leave you managing HP's software for four months. If reinstalling is not appealing,
uninstalling the OEM packages found above gets ~85% of the benefit for 15 minutes of work.

### Edition — check before you decide anything else

Victus laptops usually ship **Windows 11 Home**, which has no BitLocker (only Device
Encryption, and only if the hardware qualifies), no Group Policy, and no Hyper-V. For a machine
carried to and from campus daily with coursework on it, **encryption is the thing worth
caring about.** Check `WindowsEditionId` above, and check whether KSU's OnTheHub store offers a
free Windows Education upgrade — the same store where JMP was claimed
(`04-SCHOOL\KSU Academic Software Offers 2026.md`). Education edition includes BitLocker.

---

## 4. What to install — three tiers

### Tier 1 — required, install before Aug 24

| Item | Note |
|---|---|
| **Windows updates to current**, then drivers from **HP's support page** | Chipset, GPU, hotkeys. Do not rely on Windows Update alone for the dGPU |
| **Respondus LockDown Browser** | **From the D2L course link only.** §2.1 |
| **Python 3.12+ from python.org** | Not the Microsoft Store build — cleaner `PATH`, fewer surprises in a first programming course. Tick *"Add python.exe to PATH"* |
| **A plain editor for CSE work** | See §5 — this choice is an integrity decision, not a preference |
| **Microsoft 365** (KSU account) | Word is the practical requirement for TCOM 2010's deliverables |
| **A PDF reader** | Textbooks: `thinkpython.pdf`, `physic.pdf` |
| **Browser + KSU sign-in**, D2L, Owl Express, WebAssign (PHYS) | Verify each actually loads and authenticates |
| **Obsidian** | Points at the `.ROOT` clone from §6 |
| **Git** | The sync mechanism, §6 |

### Tier 2 — install when a real need appears

7-Zip · JMP (already licensed, ISYE statistics) · Zoom or Teams if ENGR 1000 turns out to be
synchronous.

### Tier 3 — do not install on this machine

Games and the HP gaming stack · McAfee/Norton trials (Defender is sufficient and does not nag
during an exam) · overlapping statistics platforms — `KSU Academic Software Offers 2026.md`
already ruled this: *"Do not install overlapping statistical or qualitative platforms merely
because they are free"* · anything that runs a background overlay, because **LockDown Browser
will object to it during an exam.**

---

## 5. The integrity boundary — the one decision that actually matters

**CSE 1321 and ENGR 1000 prohibit generative AI on submitted work. PHYS 2211 is treated as
prohibited until §54's syllabus says otherwise.** That is three of five courses.

The desktop has Claude Code, Codex, and a full AI toolchain. **Do not reproduce that on the
laptop.** Not because Chris would cheat — because the boundary should be **structural rather
than a decision he has to re-make every time he opens an editor while tired at 16:00 on a
Tuesday.** `AGENT.md` makes this same move repeatedly: File Safety 12 became a `PreToolUse`
gate precisely because prose asking an agent to remember is not a control.

**Recommended shape:**

| Surface | Machine | Why |
|---|---|---|
| CSE assignments, quizzes, exams | **Laptop, no AI assistant installed** | The prohibition becomes a property of the machine |
| PHYS problem sets | Laptop | Same, until §54 says otherwise |
| TCOM / ECON course-permitted work | Either | Verify per assignment |
| `.ROOT` system work, AI-assisted building, the data/ML reps | **Desktop** | Where the toolchain lives |

**Concretely: install a plain editor on the laptop — VS Code with no Copilot, or Thonny, which
is the conventional first-course Python editor and has a visible variable-state debugger that
suits how Chris learns.** If VS Code is chosen, do not sign into Copilot on this machine at all.
An editor that cannot autocomplete his homework is a feature here.

**This also solves a technical problem:** LockDown Browser blocks background applications, so a
machine without an AI assistant running is a machine that does not fail an exam for a reason
that has nothing to do with cheating.

---

## 6. The `.ROOT` link — and the Drive ruling this closes

`NOW.md` open risk 3 says the Drive link is dead — `G:\My Drive\...` last synced **Aug 9**,
predates the `04-SCHOOL` restructure, still holds quarantined junk, and includes `88-JOURNAL`
and `.git`. The standing recommendation is *"replace it with a scoped link rather than
re-syncing this one,"* ruled by Aug 17.

**The scoped link already exists: `git clone` from GitHub.**

`.gitignore` excludes exactly what should never leave the desktop — `88-JOURNAL`, every `raw\`,
`77-INBOX`, `99-ARCHIVE`, PDFs, and `MCP_Bootcamp`'s vendored environment. What remains tracked
is precisely the campus working set: `NOW.md`, `00-BRAIN`, `04-SCHOOL`, `01-NORTH_STAR`, and the
wiki prose. **The exclusion list that was written for backup safety is already the correct
scoping rule for a portable machine.** Nothing new needs building.

```powershell
# on the laptop
git clone https://github.com/<user>/root-system.git C:\Users\<user>\.ROOT
```

**Rules for the clone, so it does not become the fourth unowned copy** — `D:\ARCHIVE\.ROOT` is
the cautionary example already in `LOCAL_MACHINE_MAP.md`:

1. **The desktop stays canonical.** The laptop clone is a working copy, never the source of truth.
2. **Pull at the start of every campus session; commit and push at the end.** This is the
   `EVENING_READING.md` / session-close rhythm, applied to a second machine.
3. **`88-JOURNAL` never reaches this machine.** Git already guarantees it — do not defeat it by
   copying folders across manually.
4. **Coursework in progress is the one thing that lives here first.** Push it the same day, or
   it exists on a laptop that gets carried around a campus.

**This also answers the Aug 17 Drive ruling: no Drive relink is needed.** Retire the dead
`G:\My Drive` copy rather than repairing it.

---

## 7. Verification checklist — everything gets tested, nothing gets assumed

`LOCAL_MACHINE_MAP.md` already records why: a backup was documented as live for 26 days without
ever running. **Presence is not function. Verify by running.**

| # | Check | Pass condition |
|---|---|---|
| 1 | Windows edition and encryption | Recorded; encryption on, or a decision made not to |
| 2 | OEM bloatware | The §3 query returns nothing meaningful |
| 3 | Webcam **and** microphone | Both produce output in Windows Camera and Sound settings |
| 4 | **LockDown Browser on a real D2L practice quiz** | Launches, authenticates, completes. **Do this first — it has the longest failure tail** |
| 5 | `python --version` in a new terminal | Returns 3.12+ without a full path |
| 6 | Editor runs a script and hits a breakpoint | Works, with **no AI assistant signed in** |
| 7 | D2L, Owl Express, WebAssign, KSU email | All authenticate |
| 8 | `git clone` + `git pull` | Vault present; `88-JOURNAL` **absent** — confirm by looking |
| 9 | Obsidian opens the clone | Graph and links resolve |
| 10 | **Battery under real load** | Survives a 2h15 Monday block at 09:10–12:30 without a charger. If not, plan around outlets or fix power settings |
| 11 | Campus Wi-Fi (`KSU Wireless`/eduroam) | Connects on campus, not just at home |
| 12 | Printing, if TCOM needs hard copy | Deferred until a syllabus requires it |

**Check 10 is the one people skip.** A gaming laptop with a discrete GPU can run 90 minutes on
battery. Set the Windows power mode to *Best power efficiency* on battery and confirm the dGPU
is not driving the internal display when it does not need to.

---

## 8. Sequence for this afternoon

Chris has the laptop beside him and the calendar block runs **12:15–17:00**.

1. Run the §3 queries. Decide clean-install vs. cull — **10 minutes, and it gates everything else.**
2. Uninstall Tier 3. Windows Update + HP drivers.
3. **LockDown Browser and a practice quiz** (check 4) — longest failure tail, do it early.
4. Python + editor, no AI assistant (§5).
5. `git clone` (§6), Obsidian onto it.
6. Walk the §7 table. Record results.
7. Add the machine to `LOCAL_MACHINE_MAP.md` — it is not in the inventory today.

---

## 9. For Codex review

Four points where an independent look is worth having, phrased as questions rather than tasks:

1. **§6 — is `git clone` genuinely the right scoped link**, or does a campus session need
   something in the untracked set (a `raw\` source, a PDF textbook) often enough that
   git-only becomes friction? `thinkpython.pdf` and `physic.pdf` are both untracked, and both
   are course textbooks. *This is the weakest joint in the spec.*
2. **§5 — is a hard AI/no-AI split by machine correct**, or does it push Chris toward working
   on the wrong machine and defeating the split by convenience?
3. **§3 — is a clean ISO reinstall worth 90 minutes** eleven days out, given `OK TO START`
   lands Sunday Aug 16 and the rehearsal week starts Aug 17?
4. **§2.1 — is anything else in the five syllabi a machine requirement** that neither Claude
   nor Chris has extracted? LockDown Browser was found only by grepping the raw syllabi. *One
   grep found one requirement; assume it did not find all of them.*

---

*Companion: `LOCAL_MACHINE_MAP.md` (desktop inventory, backup posture). Course sources:
`04-SCHOOL\SYLLABUS_STATUS.md`. Time shape:
`Session_Logs\System Update Log\2026-08-12_ROOT_UPDATE\COUNCIL_SEMESTER_READINESS_2026-08-13.md` §Seat 3.*
