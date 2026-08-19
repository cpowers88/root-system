param()

# Generates root MORNING_BRIEF.md from 00-BRAIN\MORNING_LAUNCH_INSTRUCTIONS.md.
#
# Written 2026-08-18. Until then the morning brief had instructions but no
# generator and no scheduled task, so it refreshed only when a session happened
# to remember -- git history shows gaps of 4-5 days. Evening reading has been
# automated since July; this closes the asymmetry. Same contract shape, same
# read-only tool set, same UTF-8 handling (flag #80).

$ErrorActionPreference = "Stop"
$rootPath = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$instructionPath = Join-Path $rootPath "00-BRAIN\MORNING_LAUNCH_INSTRUCTIONS.md"
$outputPath = Join-Path $rootPath "MORNING_BRIEF.md"
$claudePath = (Get-Command claude.exe -ErrorAction Stop).Source

$prompt = @"
Follow the live instruction file at $instructionPath using read-only inspection of $rootPath.
Return only the complete Markdown for $outputPath, including valid frontmatter with a `generated:` date of today, an H1 naming today's date and weekday, and the three required lines.
Write exactly three lines - **ATTENTION**, **START**, and **CHRIS** - each one sentence of no more than 35 words, each naming its exact owner file.
Once the semester has begun (from 2026-08-24), the START line must reflect the current week of 04-SCHOOL\semester-workload-plan.md.
Do not edit files, run commands, use network tools, add commentary, or wrap the output in a code fence.
"@

Push-Location $rootPath
$priorOutputEncoding = [Console]::OutputEncoding
try {
    # Flag #80: PowerShell decodes a native process's stdout using the console output
    # codepage. Under the default OEM codepage every UTF-8 em dash arrived as the
    # mojibake "ΓÇö" BEFORE WriteAllText ever saw it, so the no-BOM UTF8Encoding on
    # the write side could not fix it. Decode the child process as UTF-8 instead.
    [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

    $result = $prompt | & $claudePath -p --safe-mode --no-session-persistence --model sonnet --effort low --permission-mode dontAsk --tools "Read,Glob,Grep"
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace(($result -join "`n"))) {
        throw "Claude did not return a usable morning brief."
    }

    $content = ($result -join "`n").Trim() + "`n"

    # Drop anything before the frontmatter.
    $frontmatterStart = [regex]::Match($content, '(?m)^---\r?$')
    if ($frontmatterStart.Success) {
        $content = $content.Substring($frontmatterStart.Index).Trim()
    }

    # Remove stray code-fence lines ANYWHERE, not only a trailing one.
    # run_evening_reading.ps1 strips only a fence at end-of-file, so on
    # 2026-08-18 a mid-file fence plus a trailing commentary paragraph both
    # survived into the published brief and had to be removed by hand.
    $content = [regex]::Replace($content, '(?m)^\s*```[a-zA-Z]*\s*$\r?\n?', '')

    # The contract's last line is CHRIS. Anything after it is commentary the
    # instructions forbid, so truncate rather than trusting the model to omit it.
    $chrisLine = [regex]::Match($content, '(?m)^\*\*CHRIS.*$')
    if ($chrisLine.Success) {
        $content = $content.Substring(0, $chrisLine.Index + $chrisLine.Length)
    }
    $content = $content.Trim() + "`n"

    if (-not $content.StartsWith("---") -or
        $content -notmatch "\*\*ATTENTION" -or
        $content -notmatch "\*\*START" -or
        $content -notmatch "\*\*CHRIS") {
        $preview = $content.Substring(0, [Math]::Min(500, $content.Length))
        throw "Generated output did not match the required MORNING_BRIEF.md contract. Preview: $preview"
    }

    [System.IO.File]::WriteAllText($outputPath, $content, [System.Text.UTF8Encoding]::new($false))
}
finally {
    [Console]::OutputEncoding = $priorOutputEncoding
    Pop-Location
}
