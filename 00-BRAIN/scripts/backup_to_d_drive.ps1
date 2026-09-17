[CmdletBinding()]
param(
    [string]$Source          = 'C:\Users\chris\.ROOT',
    [string]$Destination     = 'D:\BACKUPS\.ROOT',
    [string]$SnapshotRoot    = 'D:\BACKUPS\snapshots',
    [string]$LogPath         = 'D:\BACKUPS\ROOT_backup.log',
    [string]$StatePath       = 'D:\BACKUPS\ROOT_backup_state.json',
    [int]   $KeepSnapshots   = 8,
    # Written into a snapshot only after its robocopy succeeds. A snapshot
    # directory without this file is a partial copy, not a restore point.
    [string]$SnapshotDoneMarker = '.snapshot_complete',
    [int]   $ShrinkTolerancePercent = 10,
    # The gitdir moved out of the vault on 2026-08-16 (flag #102). Google Drive
    # mirrors .ROOT and conflict-copied .git\refs on every git write, producing
    # null-SHA refs with invalid names that made `git fetch` fail outright.
    # Drive offers no way to exclude a subfolder from a mirrored folder, so the
    # repo metadata moved out instead of the mirror being abandoned.
    # The live gitdir path is READ FROM the .git pointer file at run time and is
    # deliberately NOT a parameter here — a hardcoded second copy of that path
    # would be a claim that could go stale, and this script would not notice.
    [string]$GitDestination  = 'D:\BACKUPS\.ROOT-git',
    [switch]$DryRun,
    [switch]$Force
)

# ---------------------------------------------------------------------------
# Local backup of the live .ROOT vault to D:.
#
# Why this exists: GitHub is the only working off-machine backup and .gitignore
# excludes 88-JOURNAL, every raw/, 77-INBOX, 99-ARCHIVE and all PDFs — roughly
# 1.71 GB of irreplaceable source. Google Drive's folder-icon clobbering and
# sandbox-ACL problems are why the local mirror is the primary, not the fallback.
#
# Rewritten 2026-08-12 (Chris-directed) after the 2026-08-11 council review
# verified that the original script had never run and that three live documents
# described it as an active daily mirror. Three defects are addressed here:
#
#   1. /MIR purges the destination. A mirror is protection against disk loss,
#      NOT against the failure mode this vault actually experiences — a bulk
#      script damaging many files at once (2026-08-10: 2,713 files). Without
#      retention, the next run faithfully mirrors the damage. Fixed by taking a
#      dated snapshot of the PREVIOUS mirror before each run.
#   2. /MIR pointed at a wrong -Destination would purge whatever is there.
#      Fixed by a sentinel file: this script refuses to mirror into any folder
#      it did not itself mark as a backup root.
#   3. .git was excluded, so a restore from D: produced an unversioned vault.
#      Now included.
#
# Amended 2026-08-16 (flag #102). The gitdir may now live OUTSIDE the vault,
# because Google Drive mirrors .ROOT and conflict-copied .git\refs on every git
# write - producing null-SHA refs with invalid names that made `git fetch` fail
# outright. Drive has no mechanism to exclude a subfolder from a mirrored
# folder, so the repo metadata moved rather than the mirror being abandoned.
# Two consequences are handled below, and both had to be, or the relocation
# would have quietly re-created defect 3:
#
#   a. /MIR would have purged .git from the destination and left a working tree
#      with no history. A third pass mirrors the external gitdir separately.
#   b. The gitdir is 747 files, 14.4% of the measured source. Removing it from
#      the vault would trip guard C's 10% shrink tripwire on every run, so the
#      gitdir is measured back INTO the totals guard C compares.
#
# The script reads the live gitdir path from the .git pointer file at run time
# and works unchanged in either layout - self-contained or relocated.
#
# 88-JOURNAL: robocopy mirrors it, and it is measured only through robocopy's
# own /L /NFL /NDL summary, which reports totals and never emits a path. No
# process here reads journal content or enumerates journal filenames
# (AGENT.md File Safety 8).
#
# Exit codes: 0 success, 1 guard tripped (nothing was written), 2 robocopy
# failure. Safe to re-run.
# ---------------------------------------------------------------------------

$ErrorActionPreference = 'Stop'

$SentinelName = '.ROOT_BACKUP_ROOT'
$VaultMarker  = '00-BRAIN\AGENT.md'   # proves -Source is really the vault

function Write-Step { param([string]$Message) Write-Host "==> $Message" }
function Fail-Guard {
    param([string]$Message)
    Write-Host ''
    Write-Host "GUARD TRIPPED — nothing was written." -ForegroundColor Red
    Write-Host $Message -ForegroundColor Red
    exit 1
}

# --- Shared robocopy shape: measurement and mirror must agree exactly --------
# .git is deliberately NOT excluded. These are transient sync artifacts,
# regenerable caches, and dependency/build output only.
#
# .pytest_cache / .pytest_tmp: measured 2026-08-12, both are ACL-locked under
# 02-LIBRARY\.PROJECTS\MCP_Bootcamp and raise UnauthorizedAccessException on
# enumeration, which made robocopy return exit 9 (8 = failure) on every run.
# They are regenerable pytest artifacts, so they are excluded rather than
# forced — but they are named here, not silently swallowed, because a backup
# that reports failure for a reason nobody wrote down gets ignored.
# .folder-icons is deliberately NOT excluded (Chris, 2026-08-12). The original
# script skipped it as a cache; it is not one — it is 478 files of Chris's own
# folder-icon setup, the same customization Google Drive kept clobbering, which
# is part of why Drive sync was retired. Regenerating it by hand is real work.
$excludeDirs  = @(
    '.tmp.driveupload', '.tmp.drivedownload', 'tmp',
    '__pycache__', 'node_modules', '.venv', 'venv',
    '.pytest_cache', '.pytest_tmp', '.mypy_cache', '.ruff_cache'
)
$excludeFiles = @('Thumbs.db', 'desktop.ini')

# The sentinel lives in the destination and has no counterpart in the source,
# so /MIR's /PURGE deletes it — measured on the first real run, 2026-08-12.
# That would have tripped guard B on every subsequent run and silently ended
# the backup after exactly one success. Excluded so it survives the mirror.
$excludeFiles += $SentinelName

$excludeArgs = @()
foreach ($dir  in $excludeDirs)  { $excludeArgs += @('/XD', $dir) }
foreach ($file in $excludeFiles) { $excludeArgs += @('/XF', $file) }

# --- Guard A: the source really is the vault --------------------------------
if (-not (Test-Path -LiteralPath $Source)) {
    Fail-Guard "Source vault not found: $Source"
}
if (-not (Test-Path -LiteralPath (Join-Path $Source $VaultMarker))) {
    Fail-Guard @"
Source does not look like the .ROOT vault: $Source
Expected to find $VaultMarker inside it. Refusing to mirror an unknown tree.
"@
}

# --- Guard A2: resolve the gitdir, wherever it lives ------------------------
# .git is a DIRECTORY when the repo is self-contained, and a FILE containing
# "gitdir: <path>" once it has been relocated out of the vault (flag #102).
# Both layouts must yield a restorable repo, so this resolves whichever is
# actually live instead of assuming either one. Defect #3 in the header above
# (a restore that produced an unversioned vault) is what happens when the repo
# metadata is silently absent from the backup, and moving the gitdir out of the
# mirrored tree is a new way to reach that same outcome.
$dotGit         = Join-Path $Source '.git'
$externalGitDir = $null

if (Test-Path -LiteralPath $dotGit -PathType Leaf) {
    $pointer = (Get-Content -LiteralPath $dotGit -Raw).Trim()
    if ($pointer -notmatch '(?m)^gitdir:\s*(.+?)\s*$') {
        Fail-Guard @"
$dotGit is a file but has no 'gitdir:' line.

That is neither a working repo nor a recognisable pointer, and mirroring past it
would back up a vault whose history cannot be restored. Refusing.
"@
    }
    $candidate = $Matches[1]
    if (-not [System.IO.Path]::IsPathRooted($candidate)) {
        $candidate = Join-Path $Source $candidate
    }
    $candidate = [System.IO.Path]::GetFullPath($candidate)

    if (-not (Test-Path -LiteralPath $candidate -PathType Container)) {
        Fail-Guard @"
.git points to a gitdir that does not exist: $candidate

The vault is using an external gitdir but the target is missing, so a restore
from this backup would produce an unversioned vault - defect #3 in this
script's header, reached by a different route. Refusing.
"@
    }
    $externalGitDir = $candidate
    Write-Step "External gitdir in use: $externalGitDir"
}
elseif (Test-Path -LiteralPath $dotGit -PathType Container) {
    # Self-contained repo: the main mirror below already carries .git.
    Write-Step 'Gitdir is inside the vault; the main mirror carries it'
}
else {
    Write-Warning "No .git at $dotGit - backing up an unversioned tree."
}

# --- Load prior state (needed by guards B and C) ----------------------------
$prior = $null
if (Test-Path -LiteralPath $StatePath) {
    try { $prior = Get-Content -LiteralPath $StatePath -Raw | ConvertFrom-Json }
    catch { Write-Warning "State file unreadable, treating this as a first run: $StatePath" }
}

# --- Guard B: the destination is a backup root this script owns -------------
$sentinelPath = Join-Path $Destination $SentinelName

function New-Sentinel {
    param([string]$Path = $sentinelPath)
    Set-Content -LiteralPath $Path -Encoding utf8 -Value @"
This folder is the .ROOT local backup root.
Marked $(Get-Date -Format 'yyyy-MM-dd HH:mm') by 00-BRAIN\scripts\backup_to_d_drive.ps1.
Do not delete this file: the script refuses to mirror into a folder without it.
"@
}

if (Test-Path -LiteralPath $Destination) {
    if (-not (Test-Path -LiteralPath $sentinelPath)) {
        # Recoverable case: a prior successful run recorded this exact
        # destination as ours, so the sentinel is missing rather than absent.
        if ($prior -and $prior.destination -eq $Destination) {
            Write-Step "Sentinel missing but prior run owns $Destination — re-marking"
            if (-not $DryRun) { New-Sentinel }
        } else {
            Fail-Guard @"
Destination exists but is not marked as a .ROOT backup root: $Destination

/MIR would DELETE everything in it that is not in the source. Refusing.

If this folder really is meant to be the backup root and you accept that its
current contents will be purged, mark it yourself and re-run:

    New-Item -ItemType File '$sentinelPath'
"@
        }
    }
} elseif (-not $DryRun) {
    Write-Step "Creating backup root $Destination"
    [System.IO.Directory]::CreateDirectory($Destination) | Out-Null
    New-Sentinel
}
if (-not $DryRun) {
    [System.IO.Directory]::CreateDirectory((Split-Path -Parent $LogPath)) | Out-Null
}

# --- Measure the source (totals only; no paths are emitted) -----------------
Write-Step 'Measuring source'
$measureArgs = @($Source, (Join-Path $env:TEMP 'root_backup_measure_noop'),
                 '/L', '/S', '/E', '/NJH', '/NFL', '/NDL', '/BYTES',
                 '/R:0', '/W:0', '/XJ') + $excludeArgs
$measureOut = & robocopy @measureArgs 2>&1

$srcFiles = $null; $srcBytes = $null
foreach ($line in $measureOut) {
    if ($line -match '^\s*Files\s*:\s*(\d+)') { $srcFiles = [int64]$Matches[1] }
    if ($line -match '^\s*Bytes\s*:\s*(\d+)') { $srcBytes = [int64]$Matches[1] }
}
if ($null -eq $srcFiles -or $null -eq $srcBytes) {
    Fail-Guard @"
Could not read a file/byte total from robocopy's summary.
A measurement that cannot run is not evidence that the source is intact,
so this run stops rather than mirroring blind.
"@
}
Write-Host ("    source: {0:N0} files, {1:N2} GB" -f $srcFiles, ($srcBytes / 1GB))

# The gitdir counts toward the protected estate even when it sits outside the
# vault, so it is measured into the same totals guard C compares and the state
# file records. Without this, relocating it drops the measured source by 747
# files - 14.4% of 5,200, measured 2026-08-16 - and guard C reads a deliberate
# relocation as catastrophic loss. It would then refuse every run until somebody
# reached for -Force, which is how a tripwire gets trained into noise.
if ($externalGitDir) {
    $gitMeasureArgs = @($externalGitDir,
                        (Join-Path $env:TEMP 'root_gitdir_measure_noop'),
                        '/L', '/S', '/E', '/NJH', '/NFL', '/NDL', '/BYTES',
                        '/R:0', '/W:0', '/XJ')
    $gitMeasureOut = & robocopy @gitMeasureArgs 2>&1

    $gitFiles = $null; $gitBytes = $null
    foreach ($line in $gitMeasureOut) {
        if ($line -match '^\s*Files\s*:\s*(\d+)') { $gitFiles = [int64]$Matches[1] }
        if ($line -match '^\s*Bytes\s*:\s*(\d+)') { $gitBytes = [int64]$Matches[1] }
    }
    if ($null -eq $gitFiles -or $null -eq $gitBytes) {
        Fail-Guard @"
Could not read a file/byte total for the external gitdir: $externalGitDir
A measurement that cannot run is not evidence the repo is intact.
"@
    }
    Write-Host ("    gitdir: {0:N0} files, {1:N2} GB" -f $gitFiles, ($gitBytes / 1GB))

    $srcFiles += $gitFiles
    $srcBytes += $gitBytes
    Write-Host ("    estate: {0:N0} files, {1:N2} GB (vault + gitdir)" -f $srcFiles, ($srcBytes / 1GB))
}

# --- Guard C: shrink tripwire against the last successful run ---------------
# ($prior was loaded above, before guard B.)
if ($prior -and $prior.files -gt 0) {
    $floor      = (100 - $ShrinkTolerancePercent) / 100
    $filesFloor = [int64][math]::Floor($prior.files * $floor)
    $bytesFloor = [int64][math]::Floor($prior.bytes * $floor)
    if ($srcFiles -lt $filesFloor -or $srcBytes -lt $bytesFloor) {
        $msg = @"
The source shrank by more than $ShrinkTolerancePercent% since the last successful run.

    last run ($($prior.timestamp)):  $('{0:N0}' -f [int64]$prior.files) files, $('{0:N2}' -f ([int64]$prior.bytes / 1GB)) GB
    now:                            $('{0:N0}' -f $srcFiles) files, $('{0:N2}' -f ($srcBytes / 1GB)) GB

/MIR would propagate that loss into the backup. If the shrink is intentional
(a real archive or cleanup), re-run with -Force. If it is not, DO NOT force —
the current backup at $Destination still holds the larger tree.
"@
        if (-not $Force) { Fail-Guard $msg }
        Write-Warning "Shrink tripwire overridden by -Force."
        Write-Host $msg
    }
}

# --- Snapshot the PREVIOUS mirror before overwriting it ---------------------
# This is the retention layer. /MIR alone cannot recover a file that a bulk
# script damaged in the source and the next run then mirrored.
$mirrorHasContent = (Test-Path -LiteralPath $Destination) -and
    ((Get-ChildItem -LiteralPath $Destination -Force |
        Where-Object { $_.Name -ne $SentinelName } | Measure-Object).Count -gt 0)

if ($mirrorHasContent) {
    $stamp    = Get-Date -Format 'yyyy-MM-dd_HHmm'
    $snapPath = Join-Path $SnapshotRoot $stamp
    if ($DryRun) {
        Write-Step "[dry run] Would snapshot the current mirror to $snapPath"
    } else {
        Write-Step "Snapshotting the current mirror to $snapPath"
        [System.IO.Directory]::CreateDirectory($snapPath) | Out-Null
        & robocopy $Destination $snapPath '/E' '/R:1' '/W:2' '/NP' '/NFL' '/NDL' '/XJ' "/LOG+:$LogPath" | Out-Null

        # FAIL CLOSED. Previously this only warned and let /MIR proceed, which
        # removed the protection against source-side corruption in exactly the
        # run where it had already proven unreliable. Reported by Codex review,
        # 2026-08-12.
        if ($LASTEXITCODE -ge 8) {
            Write-Error @"
Snapshot FAILED (robocopy exit $LASTEXITCODE) - refusing to mirror.
Mirroring now would overwrite the only good copy with no retained fallback.
Log: $LogPath
"@
            exit 2
        }

        # Mark the snapshot complete. Measured 2026-08-12: the 12:30 scheduled
        # run was terminated 11 seconds in (0xC000013A) and left a 1,527-file
        # directory beside 4,267-file complete ones, indistinguishable by name,
        # date, or presence. An unmarked directory is not a restore point, and
        # the rotation below must never retain one as though it were.
        Set-Content -LiteralPath (Join-Path $snapPath $SnapshotDoneMarker) `
            -Encoding utf8 -Value @"
complete: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
source mirror: $Destination
robocopy exit: $LASTEXITCODE
"@

        # Prune: incomplete snapshots are deleted on sight regardless of age -
        # they are not restore points and must not occupy a retention slot.
        # Only complete ones count toward $KeepSnapshots.
        $all = Get-ChildItem -LiteralPath $SnapshotRoot -Directory | Sort-Object Name -Descending
        $complete = @()
        foreach ($s in $all) {
            if (Test-Path -LiteralPath (Join-Path $s.FullName $SnapshotDoneMarker)) {
                $complete += $s
            } else {
                Write-Host "    discarding INCOMPLETE snapshot $($s.Name)"
                Remove-Item -LiteralPath $s.FullName -Recurse -Force
            }
        }
        if ($complete.Count -gt $KeepSnapshots) {
            foreach ($old in $complete | Select-Object -Skip $KeepSnapshots) {
                Write-Host "    pruning old snapshot $($old.Name)"
                Remove-Item -LiteralPath $old.FullName -Recurse -Force
            }
        }
    }
} else {
    Write-Step 'No existing mirror to snapshot (first run)'
}

# --- Mirror -----------------------------------------------------------------
$robocopyArgs = @($Source, $Destination, '/MIR', '/R:2', '/W:5',
                  '/NP', '/NFL', '/NDL', '/XJ') + $excludeArgs
# A dry run must not need the log directory to exist, and must not append a
# "run" to the log that never happened.
if ($DryRun) { $robocopyArgs += '/L' } else { $robocopyArgs += "/LOG+:$LogPath" }

Write-Step ($DryRun ? "[dry run] Mirroring $Source -> $Destination" : "Mirroring $Source -> $Destination")
& robocopy @robocopyArgs
$exitCode = $LASTEXITCODE

# robocopy 0-7 are success/informational (0 = no changes, 1 = files copied).
# 8+ is a real failure.
if ($exitCode -ge 8) {
    Write-Error "robocopy reported a failure (exit code $exitCode). See $LogPath"
    exit 2
}

# --- Second pass: the desktop.ini backup ------------------------------------
# Measured 2026-08-12: the mirror carried 313 of 478 .folder-icons files. The
# missing 165 were every desktop.ini under .folder-icons\v1\desktop-ini-backup\,
# removed by the global /XF desktop.ini above. That exclusion is right for the
# vault at large (those files are Windows/Drive-generated), and exactly wrong
# here — a desktop.ini *is* the icon assignment, so without them a restore
# yields 313 icon images and nothing that tells Windows where they go.
#
# /E, not /MIR: robocopy never purges what it excludes, which is how the
# sentinel survives, so the parent mirror will not delete what this pass adds.
# The trade is that a desktop.ini deleted from the source lingers in the mirror
# until a full re-seed. For an intentional backup of 165 tiny files, keeping a
# stale one is the cheaper failure than dropping a live one.
$iconBackupRel = '.folder-icons'
$iconSrc = Join-Path $Source $iconBackupRel
if (-not $DryRun -and (Test-Path -LiteralPath $iconSrc)) {
    Write-Step 'Second pass: .folder-icons desktop.ini (excluded from the mirror by design)'
    & robocopy $iconSrc (Join-Path $Destination $iconBackupRel) '/E' '/R:2' '/W:5' `
        '/NP' '/NFL' '/NDL' '/XJ' "/LOG+:$LogPath" | Out-Null
    if ($LASTEXITCODE -ge 8) {
        Write-Error "The .folder-icons second pass failed (robocopy exit $LASTEXITCODE). See $LogPath"
        exit 2
    }
}

# --- Third pass: the external gitdir ----------------------------------------
# /MIR, not /E: git deletes refs and packs as well as adding them, and a stale
# ref resurrected from a backup is worse than no backup at all.
#
# No $excludeArgs here, deliberately. A repo must be copied whole - and the
# vault's exclude list carries '/XD tmp', which would silently skip any git
# directory that happened to be named tmp. The one exclusion kept is the
# sentinel, for the reason recorded at the vault mirror above: it has no
# counterpart in the source, so /MIR's purge deletes it and trips the guard on
# every subsequent run.
if ($externalGitDir) {
    $gitSentinel = Join-Path $GitDestination $SentinelName

    if (Test-Path -LiteralPath $GitDestination) {
        if (-not (Test-Path -LiteralPath $gitSentinel)) {
            if ($prior -and $prior.gitDestination -eq $GitDestination) {
                Write-Step "Gitdir sentinel missing but prior run owns $GitDestination - re-marking"
                if (-not $DryRun) { New-Sentinel $gitSentinel }
            } else {
                Fail-Guard @"
Gitdir backup destination exists but is not marked as a .ROOT backup root:
$GitDestination

/MIR would DELETE everything in it that is not in the gitdir. Refusing.

If this really is the intended destination and you accept that its current
contents will be purged, mark it yourself and re-run:

    New-Item -ItemType File '$gitSentinel'
"@
            }
        }
    } elseif (-not $DryRun) {
        Write-Step "Creating gitdir backup root $GitDestination"
        [System.IO.Directory]::CreateDirectory($GitDestination) | Out-Null
        New-Sentinel $gitSentinel
    }

    $gitArgs = @($externalGitDir, $GitDestination, '/MIR', '/R:2', '/W:5',
                 '/NP', '/NFL', '/NDL', '/XJ', '/XF', $SentinelName)
    if ($DryRun) { $gitArgs += '/L' } else { $gitArgs += "/LOG+:$LogPath" }

    if ($DryRun) {
        Write-Step "[dry run] Mirroring gitdir $externalGitDir -> $GitDestination"
    } else {
        Write-Step "Third pass: gitdir $externalGitDir -> $GitDestination"
    }
    & robocopy @gitArgs | Out-Null

    if ($LASTEXITCODE -ge 8) {
        Write-Error @"
The gitdir pass failed (robocopy exit $LASTEXITCODE). See $LogPath

The vault mirror succeeded, so this backup holds the working tree but NOT the
history. That is defect #3 in this script's header - do not treat it as a
complete restore point until this pass succeeds.
"@
        exit 2
    }
}

# --- Record state for the next run's tripwire -------------------------------
if (-not $DryRun) {
    [pscustomobject]@{
        timestamp      = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
        source         = $Source
        destination    = $Destination
        gitDir         = $externalGitDir
        gitDestination = $(if ($externalGitDir) { $GitDestination } else { $null })
        files          = $srcFiles
        bytes          = $srcBytes
        exitCode       = $exitCode
    } | ConvertTo-Json | Set-Content -LiteralPath $StatePath -Encoding utf8
}

Write-Host ''
if ($DryRun) {
    Write-Host "Dry run complete. Nothing was written. robocopy exit $exitCode (0-7 = success)."
} else {
    Write-Host "Backup complete. robocopy exit $exitCode (0-7 = success)."
    Write-Host "  mirror:    $Destination"
    if ($externalGitDir) {
        Write-Host "  gitdir:    $externalGitDir -> $GitDestination"
    } else {
        Write-Host "  gitdir:    inside the vault mirror"
    }
    Write-Host "  snapshots: $SnapshotRoot (keeping $KeepSnapshots)"
    Write-Host "  log:       $LogPath"
}

# Explicit, or robocopy's own exit code leaks out — and robocopy's "1" (files
# copied, i.e. success) would be indistinguishable from this script's "1"
# (guard tripped, nothing written) to a scheduled task or a caller.
exit 0
