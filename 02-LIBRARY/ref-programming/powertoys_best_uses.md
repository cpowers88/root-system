---
type: reference
timeline: reference
status: ready
reference_priority: core
tags: [programming, technology]
created: 2026-07-30
---

# PowerToys — Best Uses on This Windows System

## Direct recommendation

**PowerToys has modest but real leverage now.** Command Palette and FancyZones can reduce daily navigation and window-arrangement friction. File Locksmith, Peek, Text Extractor, and PowerRename are exception tools. Nothing here justifies a separate optimization project.

Chris’s inspected installation on 2026-07-30 is **PowerToys v0.100.2**, up to date, with no reported shortcut conflicts.

The best present configuration is:

1. Keep **Command Palette**, **FancyZones**, **File Locksmith**, and **Find My Mouse** enabled.
2. Enable or retain **Peek**, **Text Extractor**, and **Workspaces** only when their first real use appears.
3. Turn **Awake** on only for a specific long-running process, then turn it back off.
4. Leave advanced utilities alone until a repeated need proves them.

## What it is

Microsoft PowerToys is a free, open-source collection of Windows utilities. Think of it as a carpenter’s finish-tool bag: Windows supplies the main machinery; PowerToys adds small tools that remove repeated friction.

## Recommended first setup

Open **PowerToys Settings → Home** and enable only the utilities below. Learn them in this order instead of turning on everything at once.

| Priority | Utility | Best use in `.ROOT`, school, and development |
|---|---|---|
| 1 | **Command Palette** | Launch apps, files, folders, Windows settings, terminal profiles, calculations, and commands from one keyboard interface. Default shortcut: `Win` + `Alt` + `Space`. |
| 2 | **FancyZones** | Save a repeatable study layout: source or textbook on one side, Obsidian/editor in the center, terminal or browser on the other. Hold `Shift` while dragging a window into a zone. |
| 3 | **Workspaces** | Reopen a full work setup—Obsidian, browser, editor, and terminal—already placed on screen. Create separate workspaces for Python, physics, and system maintenance. |
| 4 | **PowerRename** | Preview and perform controlled bulk renames in File Explorer. Useful for dated notes or exported course files. Review the preview before applying; never use it in `.ROOT\raw\` or `88-JOURNAL\`. |
| 5 | **Peek** | Preview Markdown, images, PDFs, and code without opening another application. Select a file and use the configured Peek shortcut. |
| 6 | **Text Extractor** | Copy text from an image, screenshot, or inaccessible interface using OCR. Default shortcut: `Win` + `Shift` + `T`. Always compare important extracted text with the source. |
| 7 | **File Locksmith** | Identify which process is holding a file open when Windows refuses a rename, move, or archive operation. Use the File Explorer context menu. |
| 8 | **Always On Top** | Keep a small reference, timer, calculator, or instructions window visible. Default shortcut: `Win` + `Ctrl` + `T`. |
| 9 | **Awake** | Keep the computer awake during a long download, presentation, or supervised process without permanently changing Windows power settings. Turn it off afterward. |
| 10 | **Image Resizer** | Make smaller copies of screenshots or diagrams directly from File Explorer. Keep the original when image quality or evidence matters. |

## High-value supporting tools

- **Advanced Paste:** paste clipboard content as plain text or another useful format. Treat any AI-powered transformation as a draft and do not send private, client, credential, or restricted school data through it.
- **Color Picker:** capture exact colors from the screen for diagrams, presentations, or UI work.
- **Keyboard Manager:** remap awkward keys or create a shortcut only after a repeated need is proven; avoid remapping common system shortcuts casually.
- **Mouse utilities:** use Find My Mouse and Mouse Highlighter during multi-monitor work, demonstrations, or recorded explanations.
- **New+:** create files or folders from reusable templates in File Explorer once a real repeated template exists.
- **PowerToys Run:** still useful as a lightweight launcher (`Alt` + `Space`), but Command Palette is Microsoft’s newer, broader interface. Start with Command Palette rather than learning both at once.
- **ZoomIt:** zoom, annotate, or record during technical teaching and demonstrations.

## Three practical workflows

### Start a Python session

1. Open a saved **Workspaces** layout.
2. Use **FancyZones** to keep instructions, code, and terminal visible together.
3. Use **Command Palette** to open the project folder or terminal.
4. Use **Peek** to inspect reference files without breaking the layout.

### Navigate `.ROOT` with Command Palette

Use `Win` + `Alt` + `Space`, then:

- type an application name such as `Obsidian` or `Visual Studio Code`;
- type `file ` followed by a known filename to search files;
- type `=` followed by a calculation;
- type `$` followed by a Windows setting;
- use a bookmark for a frequently opened folder only after repeated use proves it belongs on the Home page.

Recommended bookmarks, after confirming they work reliably:

- `.ROOT`
- `NOW.md`
- `MORNING_BRIEF.md`
- the active Python project folder

Do not build a large Command Palette dashboard. Its value is quick retrieval, not becoming another cockpit beside `NOW.md`.

### Arrange the production surface with FancyZones

Create one three-column layout:

- **left:** source, textbook, or task instructions;
- **center:** Obsidian or code editor—the main work surface;
- **right:** browser, terminal output, or verification.

This mirrors a construction layout table: reference drawing on one side, workpiece in the center, measuring/checking tool on the other. One stable layout is more valuable than many clever layouts.

### Reopen a proven setup with Workspaces

Create a workspace only after the three-column layout has been used successfully several times. A useful “Python Study” workspace may reopen:

- Obsidian at the learner-position or stage page;
- Visual Studio Code at the active project;
- a browser at the permitted reference source.

Workspaces saves launching and placement; it does not know which files are authoritative or whether yesterday’s page remains current.

### Process screenshots or exported material

1. Use **Text Extractor** to capture otherwise inaccessible text.
2. Verify names, numbers, formulas, and dates against the image.
3. Use **Image Resizer** only on a copy when a smaller working image is needed.
4. File the verified result according to `.ROOT` placement rules.

### Diagnose a blocked file operation

1. Open **File Locksmith** from the file’s context menu.
2. Identify the process holding the file.
3. Save work in that application before closing it.
4. Retry the normal operation; do not force-close an unknown system process.

## Safety and scope

- Do not run PowerToys permanently as administrator unless a specific elevated application requires it. Microsoft warns that always-elevated operation increases security exposure.
- Preview every **PowerRename** batch. In `.ROOT`, archive instead of delete, and never alter files under any `raw\` folder.
- OCR, regex renames, and automated paste transformations can be wrong. Validate consequential output.
- Disable utilities that do not earn regular use; fewer active background tools means less shortcut conflict and less noise.

## Not worth pursuing now

- Developing Command Palette extensions.
- Creating multiple docks, themes, or elaborate bookmark systems.
- Using PowerRename for broad `.ROOT` cleanup.
- Remapping the keyboard without a documented repeated problem.
- Turning on Hosts File Editor, Registry Preview, Environment Variables, or administrator mode merely to explore them.
- Treating PowerToys configuration as productive work after the core friction is removed.

## Honest value verdict

| Utility | Value now | Decision |
|---|---|---|
| Command Palette | High-frequency, small time savings | Keep and build the launch/search habit |
| FancyZones | Useful for study and code/reference visibility | Configure one layout |
| File Locksmith | Valuable when a file is unexpectedly locked | Keep enabled; use only on demand |
| Find My Mouse | Helpful on a large or multi-monitor display | Keep if it solves real cursor loss |
| Peek | Useful but not essential | Enable when quick previews replace app switching |
| Text Extractor | Valuable for inaccessible screenshots or interfaces | Use on demand and verify OCR |
| Workspaces | Potentially useful after the layout stabilizes | Defer until repeated setup friction is observed |
| Everything else | Situational | Ignore until a real task calls for it |

## Official references

- [PowerToys utilities overview](https://learn.microsoft.com/windows/powertoys/)
- [Install and update PowerToys](https://learn.microsoft.com/windows/powertoys/install)
- [Command Palette](https://learn.microsoft.com/windows/powertoys/command-palette/overview)
- [Administrator-mode guidance](https://learn.microsoft.com/windows/powertoys/administrator)

## Next action

Configure one **FancyZones** three-column study layout when convenient. Otherwise, PowerToys is sufficiently understood—move to the next task.
