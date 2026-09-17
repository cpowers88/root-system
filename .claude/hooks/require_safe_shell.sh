#!/usr/bin/env bash
#
# require_safe_shell.sh — interpreter-resolving launcher for the PreToolUse gate.
#
# WHY A LAUNCHER EXISTS AT ALL
#   A hook is one command string read from two environments. Measured 2026-08-11:
#   WSL has `python3` and no `python`; Windows has `python` (C:\Python314) and no
#   `python3`. Either spelling hardcoded into settings.json is dead in one of the
#   two environments — and a dead hook is a NON-BLOCKING error, so the tool call
#   proceeds. That is flag #95's failure mode reappearing inside its own fix: a
#   control that reads as protection in an audit and stops nothing.
#
#   This script resolves the interpreter at run time and FAILS CLOSED if none is
#   found, so the gate can be absent-and-loud but never absent-and-silent.
#
# EXIT CODES (PreToolUse contract)
#   0  no opinion — command is not bulk work, or is already wrapped
#   2  blocked
#   Any other code is treated by Claude Code as a non-blocking error, so this
#   script must never exit with one. Every failure path below exits 2.

set -uo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
gate="$here/require_safe_shell.py"

emit_deny() {
  # stdout: the structured decision Claude Code acts on.
  # stderr: the same text, for the transcript.
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":%s}}' \
    "$(printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g; s/$/\\n/' | tr -d '\n' | sed 's/^/"/; s/$/"/')"
  printf '%s\n' "$1" >&2
  exit 2
}

if [[ ! -f "$gate" ]]; then
  emit_deny "require_safe_shell: gate script missing at $gate — failing closed. Bulk-work protection is unavailable; restore the file or remove the hook from settings.json deliberately."
fi

PY=""
for candidate in python3 python py; do
  if command -v "$candidate" >/dev/null 2>&1; then
    PY="$candidate"
    break
  fi
done

if [[ -z "$PY" ]]; then
  emit_deny "require_safe_shell: no Python interpreter found (tried python3, python, py) — failing closed. The bulk-work gate cannot evaluate this command, so it will not be allowed through unmeasured."
fi

exec "$PY" "$gate"
