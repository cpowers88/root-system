# RETIRE_SUPERSEDED.ps1 — .ROOT semester planning-layer retirement
# Approved by Chris 2026-09-09. Nothing is deleted. Everything moves.
#
#   DRY RUN (default):   powershell -ExecutionPolicy Bypass -File .\RETIRE_SUPERSEDED.ps1
#   FOR REAL:            powershell -ExecutionPolicy Bypass -File .\RETIRE_SUPERSEDED.ps1 -Execute
#
# Run the dry run first and read the output. Commit to git before -Execute.

param([switch]$Execute)

$ErrorActionPreference = 'Stop'
$ROOT    = 'C:\Users\chris\.ROOT'

# DESKTOP ONLY. The desktop tree is canonical (CAMPUS_LAPTOP_BUILD.md §6); the laptop clone at
# C:\Users\thein\Documents\root-system receives this retirement as a `git pull`, never by
# running the script there. Refuse rather than half-run on the wrong machine.
if (-not (Test-Path $ROOT)) {
    Write-Host "`nWRONG MACHINE. '$ROOT' not found." -ForegroundColor Red
    Write-Host "Run this on the desktop. On the laptop, pull the result instead:" -ForegroundColor Red
    Write-Host "  git -C C:\Users\thein\Documents\root-system pull`n" -ForegroundColor Red
    exit 1
}
$STAMP   = '2026-09-09'
$ARCHIVE = Join-Path $ROOT "99-ARCHIVE\ARCHIVED_${STAMP}_semester-planning-layer"

# --- superseded by the five COURSE SPINE files -------------------------------
$Retire = @(
  '04-SCHOOL\semester-workload-plan.md',
  '04-SCHOOL\semester-reading-plan.md',
  '04-SCHOOL\week-zero-plan.md',
  '04-SCHOOL\weekly-study-schedule.md',
  '04-SCHOOL\weekly-study-schedule.html',
  '03-WIKIS\PHYSICS\wiki\phys-2211-17-week-math-first-plan.md',
  '03-WIKIS\PHYSICS\wiki\semester-pathway.md',
  '03-WIKIS\PHYSICS\wiki\pacing-trigger-map.md',
  '03-WIKIS\PHYSICS\wiki\syllabus-coverage-ledger.md',
  '03-WIKIS\PYTHON\wiki\cse-1321-17-week-mastery-plan.md',
  '03-WIKIS\PYTHON\wiki\syllabus-alignment.md',
  '03-WIKIS\EDUCATION\wiki\pre-semester-coverage-plan.md'
)

# --- evidence: the D2L captures the spines were built from --------------------
$Route = @(
  @{ From='77-INBOX\PHYS_due_dates.md';        To='04-SCHOOL\02-Physics I\PHYS_due_dates_D2L_2026-09-02.md' },
  @{ From='77-INBOX\CSE_lecture_due_dates.md'; To='04-SCHOOL\01-CSE-Python\CSE_lecture_due_dates_D2L_2026-09-02.md' },
  @{ From='77-INBOX\TCOM_due_dates.md';        To='04-SCHOOL\03-TCOM\TCOM_due_dates_D2L_2026-09-02.md' },
  @{ From='77-INBOX\TCOMassignments.md';       To='04-SCHOOL\03-TCOM\TCOM_calendar_D2L_2026-09-09.md' },
  @{ From='77-INBOX\ECON_due_dates.md';        To='04-SCHOOL\04-ECON\ECON_due_dates_D2L_2026-09-02.md' },
  @{ From='77-INBOX\ENGR_1000_due_dates.md';   To='04-SCHOOL\05-ENGR\ENGR_due_dates_D2L_2026-09-02.md' },
  @{ From='77-INBOX\Fall-Semester-2026-CSE-1321-BF-(81262)-Programming-Problem-Solving-I.pdf';
     To='04-SCHOOL\01-CSE-Python\CSE 1321 BF (81262) Fall 2026 Syllabus.pdf' },
  @{ From='77-INBOX\Fall-Semester-2026-CSE-1321L-04-(86703)-Program-Problem-Solving-I-Lab.pdf';
     To='04-SCHOOL\01-CSE-Python\CSE 1321L 04 (86703) Fall 2026 Syllabus.pdf' },
  @{ From='77-INBOX\Powers_04_Business Email Draft.docx'; To='04-SCHOOL\03-TCOM\work\Powers_04_Business Email Draft.docx' },
  @{ From='77-INBOX\Powers_04_Ethics Analysis.docx';      To='04-SCHOOL\03-TCOM\work\Powers_04_Ethics Analysis.docx' },
  @{ From='77-INBOX\Extra Credit Lab Email - Technical Writing Section 04 Fall Semester 2026 CO - Kennesaw State University.pdf';
     To='04-SCHOOL\03-TCOM\Extra Credit Lab Email.pdf' },
  @{ From='77-INBOX\Chapter 2 Definition and Terms - Contemporary Economic Issues Section BAC Fall Semester 2026 CO.pdf';
     To='04-SCHOOL\04-ECON\modules\Chapter 2 Definitions and Terms.pdf' }
)

$mode = if ($Execute) { 'EXECUTE' } else { 'DRY RUN — nothing will move' }
Write-Host "`n.ROOT semester planning-layer retirement  [$mode]`n" -ForegroundColor Cyan

# ---------------------------------------------------------------- archive ----
Write-Host "ARCHIVE -> $ARCHIVE" -ForegroundColor Yellow
if ($Execute -and -not (Test-Path $ARCHIVE)) { New-Item -ItemType Directory -Path $ARCHIVE -Force | Out-Null }

$archived = 0; $missing = 0
foreach ($rel in $Retire) {
    $src = Join-Path $ROOT $rel
    if (-not (Test-Path $src)) { Write-Host "  skip (not found) $rel" -ForegroundColor DarkGray; $missing++; continue }
    $dst = Join-Path $ARCHIVE ("ARCHIVED_${STAMP}_" + (Split-Path $rel -Leaf))
    if ($Execute) {
        if (Test-Path $dst) { Write-Host "  skip (target exists) $rel" -ForegroundColor DarkYellow; continue }
        Move-Item -LiteralPath $src -Destination $dst
    }
    Write-Host "  archive  $rel"
    $archived++
}

# ------------------------------------------------------------------ route ----
Write-Host "`nROUTE INBOX -> course folders" -ForegroundColor Yellow
$routed = 0
foreach ($m in $Route) {
    $src = Join-Path $ROOT $m.From
    $dst = Join-Path $ROOT $m.To
    if (-not (Test-Path $src)) { Write-Host "  skip (not found) $($m.From)" -ForegroundColor DarkGray; continue }
    if (Test-Path $dst)        { Write-Host "  skip (target exists) $($m.To)" -ForegroundColor DarkYellow; continue }
    if ($Execute) {
        $parent = Split-Path $dst -Parent
        if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
        Move-Item -LiteralPath $src -Destination $dst
    }
    Write-Host "  route    $($m.From)`n             -> $($m.To)"
    $routed++
}

# --------------------------------------------------------------- manifest ----
if ($Execute) {
    $manifest = @"
---
type: log
status: live
updated: $STAMP
tags: [governance, school]
---

# Archived $STAMP — semester planning layer

Retired because the five COURSE SPINE files became the single owner of school dates:

  04-SCHOOL\01-CSE-Python\CSE_SPINE.md
  04-SCHOOL\02-Physics I\PHYS_SPINE.md
  04-SCHOOL\03-TCOM\TCOM_SPINE.md
  04-SCHOOL\04-ECON\ECON_SPINE.md
  04-SCHOOL\05-ENGR\ENGR_SPINE.md

Every file here was authored before 2026-08-24 — before a single class met — and three were
built on syllabi later proven to describe the previous Spring term. They are kept as history.
Nothing here is a valid source for a date.

Rationale: 04-SCHOOL\SEMESTER_TUTOR_PLAN.md
Files: $archived archived, $routed routed from 77-INBOX.
"@
    Set-Content -LiteralPath (Join-Path $ARCHIVE 'README.md') -Value $manifest -Encoding UTF8
}

Write-Host "`n$archived to archive, $routed routed, $missing not found." -ForegroundColor Cyan
if (-not $Execute) { Write-Host "Dry run only. Re-run with -Execute to move files.`n" -ForegroundColor Green }
else { Write-Host "Done. Now run: python 00-BRAIN\scripts\root_health.py`n" -ForegroundColor Green }

# NOT touched, deliberately:
#   SEMESTER_MAP.md          — keep as the syllabus-fact record; strip its dated scheduling by hand
#   FallKSU.xlsx             — keeps grades and submission status; stop using it for schedule
#   SYLLABUS_STATUS.md       — still the provenance index; add the term-check gate
#   */wiki/learning-path.md  — teaching sequence, not a schedule. Keep.
