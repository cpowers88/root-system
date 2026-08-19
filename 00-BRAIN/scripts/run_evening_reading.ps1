param()

$ErrorActionPreference = "Stop"
$rootPath = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$instructionPath = Join-Path $rootPath "00-BRAIN\EVENING_READING_INSTRUCTIONS.md"
$outputPath = Join-Path $rootPath "EVENING_READING.md"
$claudePath = (Get-Command claude.exe -ErrorAction Stop).Source

$prompt = @"
Follow the live instruction file at $instructionPath using read-only inspection of $rootPath.
Return only the complete Markdown for $outputPath, including valid frontmatter and whichever blocks that file requires tonight.
Semester mode is live: the School block is mandatory and the Technology block runs ONLY when the instruction file's three-part tie test passes. When it fails, omit the Technology heading entirely rather than printing a stub or a paused note.
Each READ, FOCUS, and STOP line (one set per block) must be one sentence of no more than 35 words. Do not edit files, run commands, use network tools, or add commentary.
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
        throw "Claude did not return a usable evening reading brief."
    }

    $content = ($result -join "`n").Trim() + "`n"
    $frontmatterStart = [regex]::Match($content, '(?m)^---\r?$')
    if ($frontmatterStart.Success) {
        $content = $content.Substring($frontmatterStart.Index).Trim()
    }
    # The contract's output never contains a code fence. Anything from the first bare
    # ``` line onward is wrapper or trailing commentary, so cut there rather than only
    # stripping a fence that happens to sit at the very end. Observed 2026-08-19: the
    # run emitted a correct brief, then a closing fence, then a paragraph explaining
    # why the Technology block was omitted — which § Semester mode forbids.
    $fence = [regex]::Match($content, '(?m)^\s*```')
    if ($fence.Success) {
        $content = $content.Substring(0, $fence.Index)
    }
    $content = $content.Trim() + "`n"
    if (-not $content.StartsWith("---") -or $content -notmatch "\*\*READ" -or $content -notmatch "\*\*FOCUS" -or $content -notmatch "\*\*STOP") {
        $preview = $content.Substring(0, [Math]::Min(500, $content.Length))
        throw "Generated output did not match the required EVENING_READING.md contract. Preview: $preview"
    }

    [System.IO.File]::WriteAllText($outputPath, $content, [System.Text.UTF8Encoding]::new($false))
}
finally {
    [Console]::OutputEncoding = $priorOutputEncoding
    Pop-Location
}
