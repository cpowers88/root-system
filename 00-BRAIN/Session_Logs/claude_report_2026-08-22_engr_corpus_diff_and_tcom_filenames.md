---
type: report
timeline: now
status: active
tags: [school, fall-2026, engr-1000, tcom-2010, syllabus, proof]
---

# ENGR Corpus Diff + TCOM Filename Corrections (Claude, 2026-08-22)

### Scope: the three ENGR 1000 web-section syllabi in `04-SCHOOL\05-ENGR`, and the TCOM file-naming literals
### Origin: a `/learn` session that opened on miss-log row 1 (TCOM filenames) and row 5b (PHYS circular motion)
### Status: **findings + a ready-to-apply edit set. Nothing was written outside this file.**

---

## Headline

Two findings, and the second one is the expensive one.

1. **The three ENGR syllabi agree, and none of them contains a calendar.** Flag #57 has
   been hunting a document that structurally cannot hold the answer it was opened for.
2. **`SEMESTER_MAP.md` taught Chris a naming rule that does not exist**, and a cold rep this
   session reproduced that rule four times out of four. This is the **fourth** instance of
   the vault's recurring defect: *a source verified on one property and then trusted on
   another.*

---

## Finding 1 — ENGR corpus verified by byte diff, not by reading

**Method matters here.** The three files were copied out and diffed, because "these are
basically the same" is the exact claim the vault has gotten wrong three times.

**`BWB` vs `BWF`** differ in **four things only**: title, source URL, section number, and
the instructor block. Every other byte is identical.

**`BWB` vs `BWC`** is **pure omission**. `BWC` is missing seven Simple Syllabus blocks —
header/logo, Course Information, Course Materials, Teaching Methods, the no-textbook line,
Department Policies, Recent Scholarship. **It contradicts the others nowhere.**

### The inference that upgrades confidence

**`BWB` is Matt Marshall. `BWF` is Laura Ruhala.** Two different instructors publishing
byte-identical bodies means the body is a **departmental template**, not instructor-authored.
Observed instructor variance across this corpus is **zero**. BWD's *policy* body can be
planned against with reasonable confidence.

### The inference that changes the plan

All three print, verbatim, under Course Calendar: `See D2L for assignment and quiz due dates.`

**ENGR 1000 syllabi contain no calendar — none of them, including BWD's.** The correct BWD
syllabus would have supplied zero dates. This reframes flag #57 from a *failed* search to a
**mis-aimed** one. D2L is the only source of ENGR dates and always was.

### Correction owed to `SEMESTER_MAP.md`

Its current claim — *"the same course-specific core except one redundant no-textbook
sentence"* — is directionally right and **wrong in detail**. Seven omitted blocks, not one
sentence. Same defect shape as Finding 2.

### Bankable now, no D2L required

- 1 credit hour · no textbook · seven assignments at 100 pts each, **lowest dropped**
- Departmental quizzes 50% / homework + other quizzes 50%, **lowest departmental quiz dropped**
- **Late work not accepted, no exceptions. No extra credit.** Hardest deadline policy of the five
- **AI prohibited** — confirmed, matches what the vault already held
- Grades round up at `>= .5`
- ⚠ **Confirm Aug 24:** attendance is graded via *attendance quizzes* in a section with no
  meeting time. Odd enough to ask directly.

---

## Finding 2 — the vault taught a naming rule where the syllabus prints literals

### The rep

Cold, unprompted, four strings requested. Result: **0 of 4 exact.** Section number `04`
correct in all four; the three-surname form on the Instructions project correct.

**But all four answers were the same string**, `LastName_04_AssignmentName`, applied four
times. That is not four near-misses — it is one rule, faithfully retrieved. `.docx` was
absent from all four.

### Where the rule came from

`SEMESTER_MAP.md` states: *"The pattern in the syllabus is `Lastname_Section#_Draft.docx`."*

**Pattern** is the defect. There is no pattern. The syllabus prints four literals that
disagree with each other on capitalization, spacing, and abbreviation. The miss log's own
error class for row 1 is *invented a rule where the source gives literals* — and the vault
is the thing doing the inventing.

`SEMESTER_MAP.md` also prints `Lastname` three times where the syllabus prints `LastName`.

### Fourth instance of the recurring shape

Prior three, already in the miss log's aid-defect section: the `tcom-2010` pages asserting a
fallback filename as required (2026-08-19); six vault files calling a 353-page print-out a
duplicate of the 634-page textbook (2026-08-21); and now this. **Before treating a repeated
miss as a learner gap, check the aid.**

### Unresolved contradiction — ask Diamond Aug 25

The syllabus says the Business Email draft goes to the **D2L Assignments folder as a file**
(Week 1 Thu) *and* is **emailed with a subject line** (Week 2 Tue), while Course Policies
says *"I do NOT accept email attachments for any assignment!"* All three cannot be true.

### Also confirmed: the Business Email has no instructions on disk

`Course Resources\`, `Worked Examples\` and `work\` were searched. **There is no Business
Email assignment sheet anywhere in the vault**, and that is correct — assignment files with
their own SUBMISSION sections are D2L-only, and D2L opens Aug 24. Chris flagged this as a gap
in himself; it is not one. Draft is worked in class **Thu Aug 27**, due **Tue Sep 1**.

---

## Finding 3 — Chris's date ruling, promoted to a standing rule

> *"They are horrible with fixing dates on recycled syllabi; the weeks of classes are correct
> on all of them."* — Chris, 2026-08-22

Observed across four syllabi. This converts `SEMESTER_MAP.md`'s week→date conversion from a
**derivation** into a **documented property of the source**. It belongs in Standing Rules, not
in the TCOM section, so future sessions stop re-deriving it.

---

## EDIT SET — for Codex, held for approval

> ⚠ **Sequencing gate.** Edits 1–5 all land in `04-SCHOOL\SEMESTER_MAP.md`. If Codex's
> in-flight large edit has that file loaded, **queue this behind it and re-read before
> applying.** `NOW.md`: *after any pull, re-read before writing; a loaded copy can go stale
> mid-session, and that happened for real on Aug 18.*

> ⚠ **Every backticked string below is a literal.** Copy, do not retype. No smart quotes, no
> collapsed double spaces, no "fixing" the inconsistent capitalization — **the inconsistency
> is the content.** `.docx` stays on all four.

### 1. `SEMESTER_MAP.md` → ENGR 1000 section

FIND:
```
Three neighboring Fall 2026 web sections (BWB, BWC,
BWF) have the same course-specific core except one redundant no-textbook sentence:
```
REPLACE:
```
Three neighboring Fall 2026 web sections (BWB, BWC, BWF) were byte-diffed
2026-08-22, not eyeballed. BWB and BWF are identical except for title, source
URL, section number and instructor block. BWC is a pure subset — it omits seven
Simple Syllabus blocks (header, Course Information, Course Materials, Teaching
Methods, the no-textbook line, Department Policies, Recent Scholarship) and
contradicts the others nowhere. The earlier "one redundant no-textbook sentence"
claim was wrong in detail and is corrected here:
```

FIND:
```
This is **strong provisional structure, not BWD authority**. BWD's dates, weekly
order, quiz mechanics, synchronous/asynchronous execution, and Raoufi-specific
rules remain 🔴 until D2L or the exact syllabus supplies them.
```
REPLACE:
```
**Confidence upgraded 2026-08-22, and the target changed.** BWB is Matt Marshall;
BWF is Laura Ruhala. Two different instructors publishing byte-identical bodies
means the body is a **departmental template**, not instructor-authored — observed
instructor variance is zero. BWD's *policy* body can be planned against with
reasonable confidence.

**But all three print `See D2L for assignment and quiz due dates` under Course
Calendar.** ENGR 1000 syllabi contain no calendar — none of them, including BWD's.
Flag #57 has been hunting a document that structurally cannot hold the answer it
was opened for. This is a mis-aimed search, not a failed one. **D2L is the only
source of ENGR dates and always was.**

Still 🔴: every date, weekly order, quiz mechanics, and synchronous/asynchronous
execution. Confirm on day one: attendance is graded via attendance quizzes in a
section with no meeting time.
```

### 2. `SEMESTER_MAP.md` → ingestion list, row 2

FIND: `| 2 | ENGR | **BWD syllabus + meeting format.** *Email if not posted* |`

REPLACE: `| 2 | ENGR | **All dates, from D2L — the syllabus was never going to have them (2026-08-22).** Also confirm meeting format and the attendance-quiz mechanic |`

### 3. `SEMESTER_MAP.md` → Standing rules, new bullet

ADD:
```
- **KSU recycles syllabi and does not fix the printed dates, but the week
  structure is always correct.** Chris's ruling 2026-08-22, observed across four
  syllabi. This is why the week→date conversion in this file is a documented
  property of the source, not a derivation. Do not re-derive it each session;
  do confirm the resulting dates in D2L.
```

### 4. `SEMESTER_MAP.md` → TCOM filename paragraph

FIND the paragraph opening: `**TCOM's file-naming convention is graded.** The pattern in the syllabus is`

REPLACE the whole paragraph with:
```
**TCOM's file-naming convention is graded, and there is no pattern.** The syllabus
prints four literals that disagree with each other; any rule derived from them is
wrong. Copy them character for character. Chris's section is **04**.

| Assignment | Syllabus literal | Chris's version |
|---|---|---|
| Business Email Draft | `Lastname_Section#_Draft.docx` | `Powers_04_Draft.docx` |
| Business Email Final | `StudentLastName_ Section#_Business Email Final.docx` | `Powers_04_Business Email Final.docx` |
| Document Redesign | `Lastname_ Section#_DocRedesign.docx` | `Powers_04_DocRedesign.docx` |
| Instructions Group Project | `LastNameLastNameLastName_ Section#_Instructions draft.docx` | `PowersChaseChavez_04_Instructions draft.docx` |

Not a filename — the Business Email draft **email subject line**:
`Lastname_ Section#_Business Email draft`.

⚠ **Unresolved contradiction, ask Diamond Aug 25.** The syllabus says the draft goes
to the D2L Assignments folder as a file *and* is emailed with a subject line, while
her policies say *I do NOT accept email attachments for any assignment*. All three
cannot be true.
```

### 5. `SEMESTER_MAP.md` → week 14 TCOM row

FIND: `LastnameLastnameLastname_04_Instructions draft.docx`

REPLACE: `LastNameLastNameLastName_04_Instructions draft.docx`

*(Capital `N` in each `Name`. The vault had drifted from the source.)*

### 6. `04-SCHOOL\miss-log.md` → row 1 and the aid-defect section

- Row 1 reads *"Write the five exact assignment filenames from memory"*; its re-aim says
  *"the four printed strings."* Reconcile to: `four exact assignment filenames plus the one
  email subject line`.
- Append to row 1 status: `re-run scheduled — Mon Aug 24 or Tue Aug 25, cold. The 2026-08-22
  pass does not count as the spaced rep; answers were shown.`
- Add the fourth aid-defect instance: `SEMESTER_MAP.md` calling the naming convention a
  *pattern*, and printing `Lastnamex3` where the syllabus prints `LastNamex3`.

### 7. `00-BRAIN\SYSTEM_FLAGS.md` → flag #57

**Not read this session — no find/replace offered.** Substance: **#57 does not close, but its
aim changes.** Mark the BWD-syllabus search **mis-aimed and retired** — ENGR syllabi carry no
calendar. What remains open is D2L ingestion of ENGR dates on Aug 24, already item 2 in the
`SEMESTER_MAP` list. **Re-word, do not re-run.**

---

## Housekeeping flagged, not actioned

Two incorrect in-person ENGR syllabi were **deleted rather than archived** on 2026-08-22
(Chris, self-reported). Rule 2 is *nothing gets deleted, it gets archived*. `.ROOT` is
git-tracked, so if they were ever committed they are recoverable:
`git log --diff-filter=D --name-only`. Then either restore-and-archive, or record them as
unrecoverable in the archive log. Low value in themselves; the habit is the point.

The three web syllabi moved `77-INBOX` → `04-SCHOOL\05-ENGR`. That is correct routing, not a
deletion. `99-ARCHIVE` holds nothing dated 2026-08-22.

---

## Left open when this session ended

- **PHYS miss-log row 5b** — one cold circular-motion problem in an unfamiliar setup (banked
  curve, conical pendulum, or vertical-loop bottom), **with no reminder that direction and the
  real force are wanted.** Not run this session.
- **TCOM row 1** — Chris to build a verbatim reference note by *copying* the four literals
  from the syllabus, then the cold re-rep Aug 24–25.
- **`NOW.md` item 2 conflicts with miss-log row 2.** `NOW.md` says resume TCOM at "Part B
  (~8 uncued policy facts)"; the miss log re-aimed that same set on 2026-08-20 to **do not
  cold-drill — skim before Sep 1 with the syllabus open.** The miss log owns re-aimed reps.
  **Correct `NOW.md` at the Sunday Aug 23 review.**

---

*Owner: `04-SCHOOL` for the corrections; this report lives in `00-BRAIN\Session_Logs` per
`START_HERE.md`. Sources read: `NOW.md`, `START_HERE.md`, `04-SCHOOL\miss-log.md`,
`SEMESTER_MAP.md`, the TCOM §04 syllabus, and the three ENGR web-section syllabi.
Nothing outside this file was written.*
