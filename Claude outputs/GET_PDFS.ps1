# GET_PDFS.ps1 — pull Git-excluded reference files from the Drive mirror to the laptop clone
# Run ON THE LAPTOP. CAMPUS_LAPTOP_BUILD.md §6b.
#
#   DRY RUN (default):  powershell -ExecutionPolicy Bypass -File .\GET_PDFS.ps1
#   TIER 1 ONLY:        powershell -ExecutionPolicy Bypass -File .\GET_PDFS.ps1 -Tier 1 -Execute
#   EVERYTHING:         powershell -ExecutionPolicy Bypass -File .\GET_PDFS.ps1 -Tier 4 -Execute
#
# Named files only. Never a folder sweep — that is what would drag 88-JOURNAL onto a machine
# carried around campus (§6a). Every path below is verified to exist on the desktop tree the
# Drive mirror copies.

param(
    [ValidateRange(1,4)][int]$Tier = 4,
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'
$SRC = 'G:\Other computers\DESKTOP\.ROOT'
$DST = 'C:\Users\thein\Documents\root-system'

# tier 1 = ECON quiz closes Sun Sep 13 · tier 2 = PHYS Unit Exam 1 Sep 21 · tier 3 = CSE · tier 4 = TCOM
$Files = @(
  @{T=1; P='04-SCHOOL\04-ECON\modules\week-02-ch2-3\Chapter 2 Lecture Notes.pdf'}
  @{T=1; P='04-SCHOOL\04-ECON\modules\week-02-ch2-3\Chapter 3 Lecture Notes.pdf'}
  @{T=1; P='04-SCHOOL\04-ECON\modules\week-02-ch2-3\Chapter 2 Definition and Terms .pdf'}
  @{T=1; P='04-SCHOOL\04-ECON\modules\week-02-ch2-3\Chapter 3 - Economic Systems.pdf'}
  @{T=1; P='04-SCHOOL\04-ECON\modules\week-02-ch2-3\Chapter 2 Study Guide Multiple Choice .docx'}
  @{T=1; P='04-SCHOOL\04-ECON\modules\week-02-ch2-3\Chapter 3 Study Guide.docx'}
  @{T=1; P='04-SCHOOL\04-ECON\modules\week-02-ch2-3\EconQsSpecialization.pdf'}
  @{T=1; P='04-SCHOOL\04-ECON\modules\week-02-ch2-3\Two person- two goods model.pdf'}

  @{T=2; P='04-SCHOOL\02-Physics I\Syllabus.pdf'}
  @{T=2; P='04-SCHOOL\02-Physics I\PHYS 2211 Math Assessment Test.pdf'}
  @{T=2; P='03-WIKIS\PHYSICS\raw\textbook\Physics book-0001-0100.pdf'}
  @{T=2; P='03-WIKIS\PHYSICS\raw\textbook\Physics book-0101-0200.pdf'}
  @{T=2; P='03-WIKIS\PHYSICS\raw\textbook\Physics book-0201-0300.pdf'}

  @{T=3; P='04-SCHOOL\01-CSE-Python\thinkpython.pdf'}
  @{T=3; P='77-INBOX\Fall-Semester-2026-CSE-1321-BF-(81262)-Programming-Problem-Solving-I.pdf'}
  @{T=3; P='77-INBOX\Fall-Semester-2026-CSE-1321L-04-(86703)-Program-Problem-Solving-I-Lab.pdf'}

  @{T=4; P='04-SCHOOL\03-TCOM\Textbook Doc Files\Open-TC-PDF.pdf'}
  @{T=4; P='04-SCHOOL\03-TCOM\rubrics'}          # folder — small, TCOM-only, no journal risk
)

# ---------------------------------------------------------------------- guards
if (-not (Test-Path $DST)) {
    Write-Host "`nWRONG MACHINE — '$DST' not found. Run this on the laptop.`n" -ForegroundColor Red; exit 1
}
if (-not (Test-Path $SRC)) {
    Write-Host "`nDrive mirror not found at '$SRC'." -ForegroundColor Red
    Write-Host "Open Google Drive and confirm the DESKTOP backup is mounted, then re-run.`n" -ForegroundColor Red; exit 1
}
foreach ($f in $Files) {
    if ($f.P -match '88-JOURNAL') { Write-Host "REFUSED: 88-JOURNAL never leaves the desktop." -ForegroundColor Red; exit 1 }
}

$mode = if ($Execute) { "EXECUTE  (tiers 1-$Tier)" } else { "DRY RUN  (tiers 1-$Tier) — nothing will copy" }
Write-Host "`nGit-excluded reference pull  [$mode]" -ForegroundColor Cyan
Write-Host "  from $SRC`n    to $DST`n"

$copied = 0; $skipped = 0; $absent = 0; [int64]$bytes = 0

foreach ($f in ($Files | Where-Object { $_.T -le $Tier })) {
    $s = Join-Path $SRC $f.P
    $d = Join-Path $DST $f.P
    $name = Split-Path $f.P -Leaf

    if (-not (Test-Path $s)) {
        Write-Host ("  [{0}] absent in mirror  {1}" -f $f.T, $f.P) -ForegroundColor DarkGray; $absent++; continue
    }
    if (Test-Path $d) {
        Write-Host ("  [{0}] already here      {1}" -f $f.T, $name) -ForegroundColor DarkYellow; $skipped++; continue
    }

    $item = Get-Item -LiteralPath $s
    if ($item.PSIsContainer) {
        $sz = (Get-ChildItem -LiteralPath $s -Recurse -File -EA SilentlyContinue | Measure-Object Length -Sum).Sum
        if ($Execute) {
            New-Item -ItemType Directory -Path (Split-Path $d -Parent) -Force | Out-Null
            Copy-Item -LiteralPath $s -Destination $d -Recurse
        }
        Write-Host ("  [{0}] folder {1,8:N1} MB  {2}\" -f $f.T, ($sz/1MB), $name) -ForegroundColor Green
    } else {
        $sz = $item.Length
        if ($Execute) {
            New-Item -ItemType Directory -Path (Split-Path $d -Parent) -Force | Out-Null
            Copy-Item -LiteralPath $s -Destination $d
        }
        Write-Host ("  [{0}] copy   {1,8:N1} MB  {2}" -f $f.T, ($sz/1MB), $name) -ForegroundColor Green
    }
    $bytes += $sz; $copied++
}

Write-Host ("`n{0} to copy, {1} already present, {2} absent — {3:N1} MB total." -f $copied, $skipped, $absent, ($bytes/1MB)) -ForegroundColor Cyan

if (-not $Execute) {
    Write-Host "Dry run only. Add -Execute to copy.`n" -ForegroundColor Green
} else {
    Write-Host "Done. These are all Git-excluded (*.pdf, *.docx, raw\, 77-INBOX)," -ForegroundColor Green
    Write-Host "so they stay untracked and will never be pushed. Verify with: git status`n" -ForegroundColor Green
}

# Deliberately NOT pulled:
#   88-JOURNAL\                          private, never leaves the desktop
#   physic(full_book).pdf   ~80 MB       the three slices above cover Serway 1-7; grab the full
#                                        book later on home wifi if you want the whole text
#   FallKSU.xlsx                         grade workbook stays desktop-only — no merge path
#   ENGR Course Schedule FA26.pdf        unreadable scan; ENGR_SPINE.md already carries the dates
