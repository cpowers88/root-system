[CmdletBinding()]
param(
    [string]$Source = 'C:\Users\chris\.ROOT',
    [string]$Destination = 'D:\BACKUPS\.ROOT',
    [string]$LogPath = 'D:\BACKUPS\ROOT_backup.log'
)

# Daily local backup: mirrors the live C: vault to D:\BACKUPS\.ROOT.
# Independent of Git (which only holds operating documents/source) and of
# Google Drive (whose folder-icon clobbering and sandbox-ACL problems are why
# this exists). Safe to re-run; /MIR makes the destination match the source,
# including deletions, so the backup never drifts from the live vault.

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $Source)) {
    throw "Source vault not found: $Source"
}
[System.IO.Directory]::CreateDirectory((Split-Path -Parent $Destination)) | Out-Null
[System.IO.Directory]::CreateDirectory((Split-Path -Parent $LogPath)) | Out-Null

# Directory names to skip anywhere in the tree: transient sync artifacts,
# regenerable caches, and dependency/build output. Everything else — journal,
# raw/, archive, wikis, business, etc. — is mirrored in full.
$excludeDirs = @(
    '.git', '.tmp.driveupload', '.tmp.drivedownload', 'tmp',
    '__pycache__', 'node_modules', '.folder-icons', '.venv', 'venv'
)
$excludeFiles = @('Thumbs.db', 'desktop.ini')

$robocopyArgs = @($Source, $Destination, '/MIR', '/R:2', '/W:5', '/NP', '/NFL', '/NDL', "/LOG+:$LogPath")
foreach ($dir in $excludeDirs) { $robocopyArgs += @('/XD', $dir) }
foreach ($file in $excludeFiles) { $robocopyArgs += @('/XF', $file) }

Write-Host "Backing up $Source -> $Destination"
& robocopy @robocopyArgs
$exitCode = $LASTEXITCODE

# Robocopy exit codes 0-7 are all success/informational (0 = no changes,
# 1 = files copied, etc.). 8+ means a real failure.
if ($exitCode -ge 8) {
    Write-Error "robocopy reported a failure (exit code $exitCode). See $LogPath"
    exit $exitCode
}

Write-Host "Backup complete. robocopy exit code $exitCode (0-7 = success). Log: $LogPath"
