[CmdletBinding()]
param(
    [ValidateSet('Build', 'Apply', 'Audit', 'All')]
    [string]$Mode = 'Audit',
    [switch]$DryRun,
    [switch]$RefreshExplorer
)

$ErrorActionPreference = 'Stop'

$VaultRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..'))
$AssetRoot = Join-Path $VaultRoot '.folder-icons\v1'
$SourceRoot = Join-Path $AssetRoot 'sources'
$PngRoot = Join-Path $AssetRoot 'png'
$IcoRoot = Join-Path $AssetRoot 'ico'
$PackageVersion = '3.44.0'
$PackageBaseUrl = "https://unpkg.com/@tabler/icons-png@$PackageVersion"

function Get-IconDefinitions {
    @(
        [pscustomobject]@{ Key = 'brain';       Label = 'Brain / operating system'; Glyph = 'brain';            Color = '#0E7490' }
        [pscustomobject]@{ Key = 'north';       Label = 'North Star';               Glyph = 'compass';          Color = '#B45309' }
        [pscustomobject]@{ Key = 'library';     Label = 'Library';                  Glyph = 'library';          Color = '#0F766E' }
        [pscustomobject]@{ Key = 'wikis';       Label = 'Wiki collection';          Glyph = 'books';            Color = '#1D4ED8' }
        [pscustomobject]@{ Key = 'business';    Label = 'Business';                 Glyph = 'briefcase';        Color = '#C2410C' }
        [pscustomobject]@{ Key = 'inbox';       Label = 'Inbox';                    Glyph = 'inbox';            Color = '#A16207' }
        [pscustomobject]@{ Key = 'journal';     Label = 'Journal';                  Glyph = 'notebook';         Color = '#BE185D' }
        [pscustomobject]@{ Key = 'archive';     Label = 'Archive';                  Glyph = 'archive';          Color = '#475569' }
        [pscustomobject]@{ Key = 'watchtower';  Label = 'Watchtower';               Glyph = 'radar';            Color = '#6D28D9' }
        [pscustomobject]@{ Key = 'clippings';   Label = 'Clippings';                Glyph = 'clipboard-text';   Color = '#0F766E' }
        [pscustomobject]@{ Key = 'ai';          Label = 'AI / automation';          Glyph = 'robot';            Color = '#6D28D9' }
        [pscustomobject]@{ Key = 'education';   Label = 'Education';                Glyph = 'school';           Color = '#0369A1' }
        [pscustomobject]@{ Key = 'physics';     Label = 'Physics';                  Glyph = 'atom';             Color = '#0F766E' }
        [pscustomobject]@{ Key = 'python';      Label = 'Python';                   Glyph = 'brand-python';     Color = '#1D4ED8' }
        [pscustomobject]@{ Key = 'revenue';     Label = 'Revenue';                  Glyph = 'coin';             Color = '#15803D' }
        [pscustomobject]@{ Key = 'systems';     Label = 'Systems';                  Glyph = 'hierarchy-3';      Color = '#334155' }
        [pscustomobject]@{ Key = 'technology';  Label = 'Technology';               Glyph = 'cpu';              Color = '#0E7490' }
        [pscustomobject]@{ Key = 'school';      Label = 'School';                   Glyph = 'school';           Color = '#1D4ED8' }
        [pscustomobject]@{ Key = 'raw';         Label = 'Raw sources';              Glyph = 'database';         Color = '#64748B' }
        [pscustomobject]@{ Key = 'template';    Label = 'Templates';                Glyph = 'template';         Color = '#B45309' }
        [pscustomobject]@{ Key = 'notes';       Label = 'Notes';                    Glyph = 'notes';            Color = '#0369A1' }
        [pscustomobject]@{ Key = 'code';        Label = 'Code / scripts';           Glyph = 'code';             Color = '#0F172A' }
        [pscustomobject]@{ Key = 'projects';    Label = 'Projects';                 Glyph = 'rocket';           Color = '#B91C1C' }
        [pscustomobject]@{ Key = 'review';      Label = 'Reviews';                  Glyph = 'calendar-check';   Color = '#6D28D9' }
        [pscustomobject]@{ Key = 'goals';       Label = 'Goals / milestones';       Glyph = 'target';           Color = '#BE123C' }
        [pscustomobject]@{ Key = 'contracts';   Label = 'Contracts';                Glyph = 'file-certificate'; Color = '#4338CA' }
        [pscustomobject]@{ Key = 'logs';        Label = 'Logs / history';           Glyph = 'history';          Color = '#475569' }
        [pscustomobject]@{ Key = 'skills';      Label = 'Skills / capability';      Glyph = 'sparkles';         Color = '#7E22CE' }
        [pscustomobject]@{ Key = 'hats';        Label = 'Hats / modes';             Glyph = 'mask';             Color = '#BE123C' }
        [pscustomobject]@{ Key = 'docs';        Label = 'Documents';                Glyph = 'file-text';        Color = '#2563EB' }
        [pscustomobject]@{ Key = 'outputs';     Label = 'Outputs';                  Glyph = 'package-export';   Color = '#047857' }
        [pscustomobject]@{ Key = 'concepts';    Label = 'Concepts';                 Glyph = 'bulb';             Color = '#B45309' }
        [pscustomobject]@{ Key = 'glossary';    Label = 'Glossary';                 Glyph = 'language';         Color = '#0E7490' }
        [pscustomobject]@{ Key = 'drills';      Label = 'Drills';                   Glyph = 'dumbbell';         Color = '#C2410C' }
        [pscustomobject]@{ Key = 'flashcards';  Label = 'Flash cards';              Glyph = 'cards';            Color = '#6D28D9' }
        [pscustomobject]@{ Key = 'stages';      Label = 'Stages / phases';          Glyph = 'stairs-up';        Color = '#15803D' }
        [pscustomobject]@{ Key = 'problems';    Label = 'Problems / math';          Glyph = 'math';             Color = '#B91C1C' }
        [pscustomobject]@{ Key = 'examples';    Label = 'Examples';                 Glyph = 'list-check';       Color = '#0F766E' }
        [pscustomobject]@{ Key = 'tools';       Label = 'Tools';                    Glyph = 'tool';             Color = '#4338CA' }
        [pscustomobject]@{ Key = 'sources';     Label = 'Source summaries';         Glyph = 'report';           Color = '#64748B' }
        [pscustomobject]@{ Key = 'database';    Label = 'Data / databases';         Glyph = 'database';         Color = '#0F766E' }
        [pscustomobject]@{ Key = 'assets';      Label = 'Media / assets';           Glyph = 'photo';            Color = '#BE185D' }
        [pscustomobject]@{ Key = 'settings';    Label = 'Settings';                 Glyph = 'settings';         Color = '#475569' }
        [pscustomobject]@{ Key = 'health';      Label = 'Health';                   Glyph = 'heart';            Color = '#BE123C' }
        [pscustomobject]@{ Key = 'math';        Label = 'Mathematics';              Glyph = 'math';             Color = '#0F766E' }
        [pscustomobject]@{ Key = 'field';       Label = 'Field operations';         Glyph = 'tool';             Color = '#92400E' }
        [pscustomobject]@{ Key = 'castle';      Label = 'CASTLE command center';     Glyph = 'building-castle';  Color = '#7C2D12' }
        [pscustomobject]@{ Key = 'economics';   Label = 'Economics';                Glyph = 'chart-bar';        Color = '#15803D' }
        [pscustomobject]@{ Key = 'engineering'; Label = 'Engineering';              Glyph = 'ruler-measure';    Color = '#C2410C' }
        [pscustomobject]@{ Key = 'generic';     Label = 'General folder';           Glyph = 'folder';           Color = '#334155' }
    )
}

function New-RoundedPath {
    param([System.Drawing.RectangleF]$Rectangle, [single]$Radius)

    $path = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $diameter = $Radius * 2
    $arc = [System.Drawing.RectangleF]::new($Rectangle.X, $Rectangle.Y, $diameter, $diameter)
    $path.AddArc($arc, 180, 90)
    $arc.X = $Rectangle.Right - $diameter
    $path.AddArc($arc, 270, 90)
    $arc.Y = $Rectangle.Bottom - $diameter
    $path.AddArc($arc, 0, 90)
    $arc.X = $Rectangle.Left
    $path.AddArc($arc, 90, 90)
    $path.CloseFigure()
    return $path
}

function New-RecolorAttributes {
    param([System.Drawing.Color]$Color)

    $matrix = [System.Drawing.Imaging.ColorMatrix]::new()
    $matrix.Matrix00 = 0
    $matrix.Matrix11 = 0
    $matrix.Matrix22 = 0
    $matrix.Matrix33 = 1
    $matrix.Matrix40 = $Color.R / 255.0
    $matrix.Matrix41 = $Color.G / 255.0
    $matrix.Matrix42 = $Color.B / 255.0
    $matrix.Matrix44 = 1
    $attributes = [System.Drawing.Imaging.ImageAttributes]::new()
    $attributes.SetColorMatrix($matrix)
    return $attributes
}

function New-TileBitmap {
    param(
        [System.Drawing.Image]$Glyph,
        [int]$Size,
        [System.Drawing.Color]$Background,
        [System.Drawing.Color]$Foreground
    )

    $bitmap = [System.Drawing.Bitmap]::new($Size, $Size, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $graphics.Clear([System.Drawing.Color]::Transparent)

    $inset = [Math]::Max(1, [int]($Size * 0.035))
    $rect = [System.Drawing.RectangleF]::new($inset, $inset, $Size - (2 * $inset), $Size - (2 * $inset))
    $radius = [single]([Math]::Max(2, $Size * 0.18))
    $path = New-RoundedPath -Rectangle $rect -Radius $radius
    $brush = [System.Drawing.SolidBrush]::new($Background)
    $graphics.FillPath($brush, $path)

    if ($Size -ge 32) {
        $pen = [System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(65, 255, 255, 255), [Math]::Max(1, $Size * 0.015))
        $graphics.DrawPath($pen, $path)
        $pen.Dispose()
    }

    $padding = [int]($Size * 0.20)
    $destination = [System.Drawing.Rectangle]::new($padding, $padding, $Size - (2 * $padding), $Size - (2 * $padding))
    $attributes = New-RecolorAttributes -Color $Foreground
    $graphics.DrawImage($Glyph, $destination, 0, 0, $Glyph.Width, $Glyph.Height, [System.Drawing.GraphicsUnit]::Pixel, $attributes)

    $attributes.Dispose()
    $brush.Dispose()
    $path.Dispose()
    $graphics.Dispose()
    return $bitmap
}

function Convert-BitmapsToIco {
    param(
        [object[]]$Frames,
        [string]$OutputPath
    )

    $payloads = @()
    foreach ($frame in $Frames) {
        $stream = [System.IO.MemoryStream]::new()
        $frame.Bitmap.Save($stream, [System.Drawing.Imaging.ImageFormat]::Png)
        $payloads += ,$stream.ToArray()
        $stream.Dispose()
    }

    $output = [System.IO.FileStream]::new($OutputPath, [System.IO.FileMode]::Create)
    $writer = [System.IO.BinaryWriter]::new($output)
    $writer.Write([uint16]0)
    $writer.Write([uint16]1)
    $writer.Write([uint16]$Frames.Count)
    $offset = 6 + (16 * $Frames.Count)

    for ($index = 0; $index -lt $Frames.Count; $index++) {
        $size = [int]$Frames[$index].Size
        $writer.Write([byte]($(if ($size -eq 256) { 0 } else { $size })))
        $writer.Write([byte]($(if ($size -eq 256) { 0 } else { $size })))
        $writer.Write([byte]0)
        $writer.Write([byte]0)
        $writer.Write([uint16]1)
        $writer.Write([uint16]32)
        $writer.Write([uint32]$payloads[$index].Length)
        $writer.Write([uint32]$offset)
        $offset += $payloads[$index].Length
    }

    foreach ($payload in $payloads) {
        $writer.Write($payload)
    }

    $writer.Dispose()
    $output.Dispose()
}

function Build-IconLibrary {
    Add-Type -AssemblyName System.Drawing
    foreach ($path in @($AssetRoot, $SourceRoot, $PngRoot, $IcoRoot)) {
        [System.IO.Directory]::CreateDirectory($path) | Out-Null
    }

    $definitions = Get-IconDefinitions
    $sizes = @(16, 24, 32, 48, 64, 128, 256)
    foreach ($definition in $definitions) {
        $sourcePath = Join-Path $SourceRoot "$($definition.Glyph).png"
        if (-not (Test-Path -LiteralPath $sourcePath)) {
            $sourceUrl = "$PackageBaseUrl/icons/outline/$($definition.Glyph).png"
            Write-Host "Downloading $($definition.Glyph)..."
            Invoke-WebRequest -Uri $sourceUrl -OutFile $sourcePath -UseBasicParsing
        }

        $source = [System.Drawing.Image]::FromFile($sourcePath)
        $background = [System.Drawing.ColorTranslator]::FromHtml($definition.Color)
        $foreground = [System.Drawing.Color]::White
        $frames = @()
        foreach ($size in $sizes) {
            $tile = New-TileBitmap -Glyph $source -Size $size -Background $background -Foreground $foreground
            $frames += [pscustomobject]@{ Size = $size; Bitmap = $tile }
            if ($size -eq 256) {
                $tile.Save((Join-Path $PngRoot "$($definition.Key).png"), [System.Drawing.Imaging.ImageFormat]::Png)
            }
        }

        Convert-BitmapsToIco -Frames $frames -OutputPath (Join-Path $IcoRoot "$($definition.Key).ico")
        foreach ($frame in $frames) { $frame.Bitmap.Dispose() }
        $source.Dispose()
    }

    Invoke-WebRequest -Uri "$PackageBaseUrl/LICENSE" -OutFile (Join-Path $AssetRoot 'TABLER_LICENSE.txt') -UseBasicParsing
    @(
        "Generated folder icon library"
        "Source: Tabler Icons PNG package $PackageVersion"
        "License: MIT; see TABLER_LICENSE.txt"
        "Generated: $([DateTime]::Now.ToString('yyyy-MM-dd HH:mm:ss'))"
    ) | Set-Content -LiteralPath (Join-Path $AssetRoot 'SOURCE.txt') -Encoding utf8

    New-ContactSheet -Definitions $definitions
    & attrib.exe +h +s (Join-Path $VaultRoot '.folder-icons') | Out-Null
    Write-Host "Built $($definitions.Count) icons in $IcoRoot"
}

function New-ContactSheet {
    param([object[]]$Definitions)

    Add-Type -AssemblyName System.Drawing
    $columns = 5
    $cellWidth = 220
    $cellHeight = 145
    $rows = [Math]::Ceiling($Definitions.Count / $columns)
    $sheet = [System.Drawing.Bitmap]::new($columns * $cellWidth, $rows * $cellHeight)
    $graphics = [System.Drawing.Graphics]::FromImage($sheet)
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.Clear([System.Drawing.ColorTranslator]::FromHtml('#F1F5F9'))
    $labelFont = [System.Drawing.Font]::new('Segoe UI Semibold', 11)
    $keyFont = [System.Drawing.Font]::new('Consolas', 9)
    $labelBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml('#0F172A'))
    $keyBrush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml('#475569'))

    for ($index = 0; $index -lt $Definitions.Count; $index++) {
        $definition = $Definitions[$index]
        $column = $index % $columns
        $row = [Math]::Floor($index / $columns)
        $x = ($column * $cellWidth) + 12
        $y = ($row * $cellHeight) + 12
        $icon = [System.Drawing.Image]::FromFile((Join-Path $PngRoot "$($definition.Key).png"))
        $graphics.DrawImage($icon, $x, $y, 76, 76)
        $graphics.DrawString($definition.Label, $labelFont, $labelBrush, $x, $y + 84)
        $graphics.DrawString($definition.Key, $keyFont, $keyBrush, $x, $y + 108)
        $icon.Dispose()
    }

    $sheet.Save((Join-Path $AssetRoot 'folder-icon-preview.png'), [System.Drawing.Imaging.ImageFormat]::Png)
    $keyBrush.Dispose()
    $labelBrush.Dispose()
    $keyFont.Dispose()
    $labelFont.Dispose()
    $graphics.Dispose()
    $sheet.Dispose()
}

function Get-RelativeVaultPath {
    param([string]$FullPath)
    return [System.IO.Path]::GetRelativePath($VaultRoot, $FullPath).Replace('/', '\')
}

function Get-ExclusionReason {
    param([string]$RelativePath)

    if ($RelativePath -match '^(?i)88-JOURNAL(?:\\|$)') { return 'private-journal' }
    if ($RelativePath -match '^(?i)99-ARCHIVE\\') { return 'archived-history' }
    if ($RelativePath -match '(?i)(^|\\)(raw|\.raw ARCHIVE)(\\|$)') { return 'immutable-raw' }
    if ($RelativePath -match '(?i)(^|\\)(\.agents|\.claude|\.codex|\.folder-icons|\.git|\.obsidian|\.tmp\.drivedownload|\.tmp\.driveupload|\.trash|tmp|__pycache__|node_modules|\.idea|_validation_yaml)(\\|$)') { return 'generated-or-application-state' }
    return $null
}

function Get-FolderIconType {
    param([string]$RelativePath)

    $normalized = $RelativePath.Replace('/', '\')
    $name = [System.IO.Path]::GetFileName($normalized)

    $exact = @{
        '...projectSuccess' = 'watchtower'; '.agents' = 'ai'; '.claude' = 'ai'; '.codex' = 'code'; '.obsidian' = 'settings'
        '00-BRAIN' = 'brain'; '01-NORTH_STAR' = 'north'; '02-LIBRARY' = 'library'; '03-WIKIS' = 'wikis'
        '05-BUSINESS' = 'business'; '77-INBOX' = 'inbox'; '99-ARCHIVE' = 'archive'; 'Clippings' = 'clippings'
        '00-BRAIN\CASTLE' = 'castle'; '00-BRAIN\HATS' = 'hats'; '00-BRAIN\scripts' = 'code'
        '00-BRAIN\Session_Logs' = 'logs'; '00-BRAIN\SKILLS' = 'skills'
        '01-NORTH_STAR\Goals & Milestones' = 'goals'; '01-NORTH_STAR\System Contracts' = 'contracts'
        '01-NORTH_STAR\Weekly Reviews' = 'review'
        '02-LIBRARY\.PROJECTS' = 'projects'; '02-LIBRARY\00-SCHOOL' = 'school'
        '02-LIBRARY\REF-AI-AUTOMATION' = 'ai'; '02-LIBRARY\REF-BUSINESS' = 'business'
        '02-LIBRARY\REF-FIELD-OPERATIONS' = 'field'; '02-LIBRARY\REF-HEALTH' = 'health'
        '02-LIBRARY\REF-MATH' = 'math'; '02-LIBRARY\REF-META-HOW-TO-WORK' = 'settings'
        '02-LIBRARY\REF-MISC' = 'library'; '02-LIBRARY\REF-PROGRAMMING' = 'code'
        '02-LIBRARY\00-SCHOOL\01-CSE-Python' = 'python'; '02-LIBRARY\00-SCHOOL\02-Physics I' = 'physics'
        '02-LIBRARY\00-SCHOOL\03-TCOM' = 'notes'; '02-LIBRARY\00-SCHOOL\04-ECON' = 'economics'
        '02-LIBRARY\00-SCHOOL\05-ENGR' = 'engineering'; '02-LIBRARY\00-SCHOOL\99-EDG' = 'engineering'
        '03-WIKIS\AI_AUTOMATION_SYSTEMS' = 'ai'; '03-WIKIS\BUSINESS' = 'business'
        '03-WIKIS\EDUCATION' = 'education'; '03-WIKIS\PHYSICS' = 'physics'; '03-WIKIS\PYTHON' = 'python'
        '03-WIKIS\REVENUE_LAB' = 'revenue'; '03-WIKIS\SYSTEMS' = 'systems'; '03-WIKIS\TECHNOLOGY' = 'technology'
        '05-BUSINESS\01-Audit Templates' = 'template'; '05-BUSINESS\02-Field Notes' = 'notes'
        '05-BUSINESS\03-Case Studies' = 'examples'; '05-BUSINESS\04-Pricing Models' = 'revenue'
        '05-BUSINESS\05-Proposals & SOWs' = 'contracts'; '05-BUSINESS\06-Capability Library' = 'skills'
    }
    if ($exact.ContainsKey($normalized)) { return $exact[$normalized] }
    if ($normalized -match '^(?i)99-ARCHIVE\\') { return 'archive' }
    if ($normalized -match '(?i)(^|\\)skills\\') { return 'skills' }
    if ($normalized -match '^(?i)02-LIBRARY\\\.PROJECTS\\[^\\]+$') { return 'projects' }
    if ($normalized -match '(?i)(^|\\)OneNote(?:\\|$)') { return 'notes' }
    if ($normalized -match '(?i)(^|\\)\.vscode(?:\\|$)') { return 'settings' }
    if ($normalized -match '(?i)\\Textbook Doc Files\\') { return 'docs' }
    if ($normalized -match '(?i)\\wiki\\ai-and-llm(?:\\|$)') { return 'ai' }
    if ($normalized -match '(?i)\\wiki\\devops(?:\\|$)|\\wiki\\security(?:\\|$)') { return 'technology' }
    if ($normalized -match '(?i)\\wiki\\distributed-systems(?:\\|$)') { return 'systems' }
    if ($normalized -match '(?i)\\wiki\\decision-rules(?:\\|$)') { return 'contracts' }
    if ($normalized -match '(?i)\\wiki\\(common-errors|errors)(?:\\|$)') { return 'problems' }
    if ($normalized -match '(?i)\\wiki\\diagrams(?:\\|$)') { return 'assets' }
    if ($normalized -match '(?i)\\wiki\\appendix(?:\\|$)') { return 'docs' }
    if ($normalized -match '(?i)\\wiki\\ai-integration-company(?:\\|$)') { return 'business' }
    if ($normalized -match '(?i)(^|\\)\.agents(?:\\|$)') { return 'ai' }
    if ($normalized -match '(?i)\\themes\\') { return 'assets' }
    if ($normalized -match '(?i)\\System Update Log\\') { return 'logs' }
    if ($normalized -match '(?i)\\outputs\\') { return 'outputs' }
    if ($normalized -match '(?i)PROMPTS for AIchat') { return 'ai' }
    if ($normalized -match '(?i)Stock Market Books') { return 'library' }
    if ($normalized -match '^(?i)02-LIBRARY\\REF-PROGRAMMING\\') { return 'code' }

    switch -Regex ($name) {
        '^(?i)wiki$' { return 'wikis' }
        '^(?i)templates?$' { return 'template' }
        '(?i)(^|[-_ ])notes?$|lecture-notes|Think Python Notes' { return 'notes' }
        '(?i)^books?$|textbook|Libraries|library' { return 'library' }
        '(?i)^scripts?$|^code$|code-patterns|software-craft|software-engineering|web-frameworks' { return 'code' }
        '(?i)^projects?$|mini-projects|proof-projects' { return 'projects' }
        '(?i)^docs?$|documentation|howto|tutorial|syllabus|reference' { return 'docs' }
        '(?i)session[_ -]?logs|^logs?$|reports?|Report Archive|System Update Log|Closed Flags' { return 'logs' }
        '(?i)^skills?$|service-capabilities|Capability Library' { return 'skills' }
        '(?i)tool-capability-library|^tools?$|tool-docs' { return 'tools' }
        '(?i)source-summaries|internal-sources|external-sources|official-docs|standards|market-research' { return 'sources' }
        '(?i)^concepts?$' { return 'concepts' }
        '(?i)^glossary$' { return 'glossary' }
        '(?i)^drills?$|loose-practice' { return 'drills' }
        '(?i)flash.?cards?' { return 'flashcards' }
        '(?i)^stages?$|^phases$|parked-advanced' { return 'stages' }
        '(?i)problem-types|problem-guides|equations|calculus-links' { return 'problems' }
        '(?i)examples?|worked-examples|case-studies' { return 'examples' }
        '(?i)^outputs?$' { return 'outputs' }
        '(?i)database|data-science|data-mining' { return 'database' }
        '(?i)^assets?$|images|pdfs|themes|user-experience' { return 'assets' }
        '(?i)settings|config|inspectionProfiles|installing|whatsnew' { return 'settings' }
        '(?i)python|Jupcode|CS50P' { return 'python' }
        '(?i)physics' { return 'physics' }
        '(?i)business|pricing|proposals|services' { return 'business' }
        default { return 'generic' }
    }
}

function Read-DesktopIni {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) { return '' }
    $bytes = [System.IO.File]::ReadAllBytes($Path)
    if ($bytes.Length -eq 0) { return '' }
    if (($bytes.Length -ge 2 -and $bytes[0] -eq 0xFF -and $bytes[1] -eq 0xFE) -or ($bytes.Length -ge 2 -and $bytes[1] -eq 0)) {
        return [System.Text.Encoding]::Unicode.GetString($bytes).TrimStart([char]0xFEFF)
    }
    return [System.Text.Encoding]::UTF8.GetString($bytes)
}

function Set-DesktopIniIcon {
    param(
        [string]$FolderPath,
        [string]$IconPath
    )

    $iniPath = Join-Path $FolderPath 'desktop.ini'
    $text = Read-DesktopIni -Path $iniPath
    $lines = if ($text) { @($text -split '\r?\n') } else { @() }
    $output = [System.Collections.Generic.List[string]]::new()
    $inShellSection = $false
    $foundShellSection = $false
    $insertedIcon = $false

    foreach ($line in $lines) {
        if ($line -match '^\[(.+)\]$') {
            if ($inShellSection -and -not $insertedIcon) {
                $output.Add("IconResource=$IconPath,0")
                $insertedIcon = $true
            }
            $inShellSection = $Matches[1] -ieq '.ShellClassInfo'
            if ($inShellSection) { $foundShellSection = $true }
            $output.Add($line)
            continue
        }
        if ($inShellSection -and $line -match '^(?i)(IconResource|IconFile|IconIndex)=') { continue }
        $output.Add($line)
    }

    if ($foundShellSection) {
        if (-not $insertedIcon) { $output.Add("IconResource=$IconPath,0") }
    } else {
        $prefix = [System.Collections.Generic.List[string]]::new()
        $prefix.Add('[.ShellClassInfo]')
        $prefix.Add('ConfirmFileOp=0')
        $prefix.Add("IconResource=$IconPath,0")
        $prefix.Add('')
        foreach ($line in $output) { $prefix.Add($line) }
        $output = $prefix
    }

    $content = (($output -join "`r`n").TrimEnd() + "`r`n")
    $encoding = [System.Text.UnicodeEncoding]::new($false, $false)
    if (Test-Path -LiteralPath $iniPath) {
        & attrib.exe -r -h -s $iniPath | Out-Null
    }
    try {
        [System.IO.File]::WriteAllText($iniPath, $content, $encoding)
    } finally {
        if (Test-Path -LiteralPath $iniPath) { & attrib.exe +h +s $iniPath | Out-Null }
    }
    & attrib.exe +r $FolderPath | Out-Null
}

function Get-FolderInventory {
    $directories = Get-ChildItem -LiteralPath $VaultRoot -Recurse -Directory -Force -ErrorAction SilentlyContinue
    foreach ($directory in $directories) {
        $relative = Get-RelativeVaultPath -FullPath $directory.FullName
        $exclusion = Get-ExclusionReason -RelativePath $relative
        $type = if ($exclusion) { $null } else { Get-FolderIconType -RelativePath $relative }
        [pscustomobject]@{
            FullPath = $directory.FullName
            RelativePath = $relative
            Type = $type
            Exclusion = $exclusion
        }
    }
}

function Apply-FolderIcons {
    if (-not (Test-Path -LiteralPath $IcoRoot)) {
        throw "Icon library not found. Run -Mode Build first."
    }

    $inventory = @(Get-FolderInventory)
    $backupRoot = Join-Path $AssetRoot 'desktop-ini-backup'
    $createdListPath = Join-Path $AssetRoot 'created-desktop-ini.txt'
    if (-not $DryRun) { [System.IO.Directory]::CreateDirectory($backupRoot) | Out-Null }
    $createdPaths = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    if (Test-Path -LiteralPath $createdListPath) {
        foreach ($line in [System.IO.File]::ReadAllLines($createdListPath)) {
            if ($line) { $null = $createdPaths.Add($line) }
        }
    }
    $applied = 0
    foreach ($item in $inventory) {
        if ($item.Exclusion) { continue }
        $iconPath = Join-Path $IcoRoot "$($item.Type).ico"
        if (-not (Test-Path -LiteralPath $iconPath)) { throw "Missing icon: $iconPath" }
        if ($DryRun) {
            Write-Host "DRY RUN $($item.RelativePath) -> $($item.Type)"
        } else {
            $iniPath = Join-Path $item.FullPath 'desktop.ini'
            if (Test-Path -LiteralPath $iniPath) {
                $backupPath = Join-Path $backupRoot (Join-Path $item.RelativePath 'desktop.ini')
                $backupParent = Split-Path -Parent $backupPath
                [System.IO.Directory]::CreateDirectory($backupParent) | Out-Null
                if (-not (Test-Path -LiteralPath $backupPath)) {
                    [System.IO.File]::WriteAllBytes($backupPath, [System.IO.File]::ReadAllBytes($iniPath))
                }
            } else {
                $null = $createdPaths.Add($item.RelativePath)
            }
            Set-DesktopIniIcon -FolderPath $item.FullPath -IconPath $iconPath
        }
        $applied++
    }
    if (-not $DryRun) {
        [System.IO.File]::WriteAllLines($createdListPath, @($createdPaths | Sort-Object), [System.Text.UTF8Encoding]::new($false))
    }
    Write-Host "Assigned $applied folders; skipped $($inventory.Count - $applied) protected/generated folders."
}

function Audit-FolderIcons {
    $inventory = @(Get-FolderInventory)
    $rows = foreach ($item in $inventory) {
        if ($item.Exclusion) {
            [pscustomobject]@{ Path = $item.RelativePath; Type = ''; Status = 'SKIPPED'; Detail = $item.Exclusion }
            continue
        }
        $expected = Join-Path $IcoRoot "$($item.Type).ico"
        $iniPath = Join-Path $item.FullPath 'desktop.ini'
        $content = Read-DesktopIni -Path $iniPath
        $configured = $content -match ('(?im)^IconResource=' + [regex]::Escape($expected) + ',0\s*$')
        $status = if (-not (Test-Path -LiteralPath $expected)) { 'MISSING_ICON' } elseif ($configured) { 'PASS' } else { 'NOT_CONFIGURED' }
        [pscustomobject]@{ Path = $item.RelativePath; Type = $item.Type; Status = $status; Detail = $expected }
    }

    [System.IO.Directory]::CreateDirectory($AssetRoot) | Out-Null
    $rows | Export-Csv -LiteralPath (Join-Path $AssetRoot 'folder-icon-audit.csv') -NoTypeInformation -Encoding utf8
    $summary = $rows | Group-Object Status | Sort-Object Name | Select-Object Name, Count
    $summary | Format-Table -AutoSize
    return $rows
}

function Invoke-ExplorerRefresh {
    Add-Type @'
using System;
using System.Runtime.InteropServices;
public static class FolderIconShellRefresh {
    [DllImport("shell32.dll")]
    public static extern void SHChangeNotify(uint wEventId, uint uFlags, IntPtr dwItem1, IntPtr dwItem2);
}
'@
    [FolderIconShellRefresh]::SHChangeNotify(0x08000000, 0, [IntPtr]::Zero, [IntPtr]::Zero)
    $refreshTool = Join-Path $env:SystemRoot 'System32\ie4uinit.exe'
    if (Test-Path -LiteralPath $refreshTool) { & $refreshTool -show | Out-Null }
}

switch ($Mode) {
    'Build' { Build-IconLibrary }
    'Apply' { Apply-FolderIcons }
    'Audit' { $null = Audit-FolderIcons }
    'All' {
        Build-IconLibrary
        Apply-FolderIcons
        $null = Audit-FolderIcons
    }
}

if ($RefreshExplorer -and -not $DryRun) { Invoke-ExplorerRefresh }
