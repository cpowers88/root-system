---
type: report
timeline: log
status: active
register: system-review
tags: [governance, codex, claude, wsl2, linux, configuration, audit]
created: 2026-08-10
---

# Hybrid WSL2 and Remainder Edits Review — August 10, 2026

## Scope

Read-only Codex review of the committed post-recovery sequence from tag
`pre-rename-2026-08-10` (`e897892`) through current `HEAD` (`0f0b632`), with
special attention to the Windows/WSL2 hybrid implementation and the remaining
governance edits.

No files were edited during the review. Codex did not access `88-JOURNAL` or
the contents of any `raw` folder.

## Verdict

**Request changes before calling the hybrid migration complete.** The
architectural choice is sound, and the remainder edits mostly resolve the
earlier contradictions correctly, but four issues remain.

## Findings

### 1. High — the security control is installed but not proven

`00-BRAIN\SYSTEM_FLAGS.md` correctly leaves flag #92 open because no
WSL-launched Claude session has demonstrated that shell writes to `raw\` and
`88-JOURNAL\` are blocked.

Until that controlled test passes, WSL2 should not be described as the control
that *would have blocked* the prior corruption. It is the intended control,
with effectiveness still awaiting acceptance evidence.

### 2. Medium — flag #92 contains contradictory current state

The same flag row says that no Linux distribution is installed and provides
installation steps, then later says Ubuntu and Claude Code are installed.
Historical detail and current action were appended into one oversized row.

Rewrite the row around the present state and move the installation history into
the session evidence record.

### 3. Medium — an ordinary WSL shell cannot currently find `claude`

Claude Code 2.1.227 exists at the recorded exact path, and its doctor command
runs successfully. Both a non-interactive and an interactive Bash check,
however, returned `claude: command not found`.

The setup currently requires the full executable path:

`~/.nvm/versions/node/v24.19.0/bin/claude`

Add nvm initialization to the appropriate WSL shell startup file or document
an exact launcher command. Claude's doctor also warns that automatic updates
cannot write to the installation folder despite nvm being used.

### 4. Medium — the committed review report breaks the health gate

`00-BRAIN\Session_Logs\codex_report_by_chris_2026-0806_structure_review.md`
lacks required frontmatter. The canonical health gate therefore returns
**BLOCKER**, not clean or pass-with-debt.

The same commit added an empty
`codex_report_by_chris_2026-0806_structure_review.md.txt`, which appears
accidental. Line 2 of the Markdown report also contains trailing whitespace.

## Additional Durability Concern

The `settings.local.json` protection lives only in `.git/info/exclude`. It
works in this current shared checkout, but disappears on clone or repository
reconstruction. A tracked ignore rule would make that safeguard recoverable.

## What Passed

- Boot and governance validation passed.
- Shared-skill mirrors passed.
- Live Markdown text integrity passed.
- Windows and WSL Git state remain aligned, and the worktree was clean.
- The BUSINESS Return Packet repair is structurally correct.
- The retired hub-loader references were repaired correctly.
- `.gitattributes` is sensible for the current tracked files. If shell scripts
  are added later, pin `*.sh`, `*.bash`, and `*.zsh` to LF.
- Four pre-existing CASTLE weekly-plan navigation review items remain. They are
  review debt, not blockers introduced by this change.

## Acceptance Sequence

1. Repair the report frontmatter, empty companion artifact, and whitespace so
   the canonical health gate no longer reports a metadata regression.
2. Make the WSL Claude launch path reliable and rerun `claude doctor`.
3. Rewrite flag #92 around its present state.
4. From a WSL-launched Claude session, run controlled deny tests against
   disposable probe paths governed by the `raw\` and `88-JOURNAL\` rules,
   without reading or altering protected contents.
5. Rerun the canonical root-health gate and record the final flag #92 verdict.

## Validation Evidence

- `python 00-BRAIN\scripts\root_health.py --verbose`: **BLOCKER** because the
  imported Codex report has missing frontmatter; boot/governance, shared-skill
  mirrors, and text integrity passed.
- `git diff --check pre-rename-2026-08-10..HEAD`: one trailing-whitespace
  finding in the imported Codex report.
- WSL exact-path Claude check: version 2.1.227 present and executable.
- WSL ordinary shell lookup: `claude: command not found` in both tested shell
  modes.
- Repository status after review: clean.

