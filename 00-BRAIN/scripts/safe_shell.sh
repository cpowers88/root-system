#!/usr/bin/env bash
#
# safe_shell.sh — run bulk or scripted `.ROOT` work behind a real OS-level write deny.
#
# WHY THIS EXISTS (flag #92, measured 2026-08-11)
#   Claude Code's own `sandbox` block is inert on this machine. Two independent
#   sessions measured it negative on six dimensions: no `bwrap` ancestor in the
#   process lineage, `Seccomp: 0`/`NoNewPrivs: 0`, no sandbox-attributable
#   namespaces, network egress to a non-allowlisted host returning HTTP 200, all
#   `denyWrite` samples writable by a child process, and the `denyRead` journal
#   directory listable. The project permission layer that remains matches command
#   *strings*, not the paths a command resolves at runtime — which is exactly how
#   the 2026-08-10 glob rewrote 2,713 files, protected folders included.
#
#   `bwrap --ro-bind` DOES enforce on `/mnt/c` (it is v9fs/9p, not DrvFs): a write
#   to a read-only bind returns `Read-only file system`, rc=1. This wrapper is
#   therefore the only currently-verified OS-level control in the stack.
#
# USAGE — from WSL, with the vault as the working directory:
#   00-BRAIN/scripts/safe_shell.sh <command> [args...]   run a command confined
#   00-BRAIN/scripts/safe_shell.sh --list                print the derived deny list
#   00-BRAIN/scripts/safe_shell.sh --selftest            prove enforcement, then exit
#
# From Windows PowerShell:
#   wsl -e bash -lc "cd /mnt/c/Users/chris/.ROOT && 00-BRAIN/scripts/safe_shell.sh ..."
#
# DERIVATION
#   The protected list is derived from the LIVE TREE, never hardcoded, so a new
#   hub's `raw/` folder is protected the day it appears. It mirrors
#   `validate_boot_chain.py`'s `required_raw` set (88-JOURNAL, CASTLE/raw, and
#   every `03-WIKIS/*/raw`). If you change the derivation in one file, change it
#   in the other — a silent divergence between them is flag #95's failure mode.
#
# FAIL-CLOSED
#   If `bwrap` is absent, the vault cannot be located, or the derivation yields an
#   implausibly short list, this script REFUSES TO RUN rather than running the
#   command unprotected. A wrapper that silently degrades to no protection is
#   worse than no wrapper, because it reads as a control in an audit.

set -euo pipefail

die() { printf 'safe_shell: %s\n' "$*" >&2; exit 2; }

# --- locate the vault ---------------------------------------------------------
script_path="$(readlink -f "${BASH_SOURCE[0]}")"
VAULT="$(cd "$(dirname "$script_path")/../.." && pwd -P)"
[[ -f "$VAULT/00-BRAIN/AGENT.md" ]] || \
  die "resolved vault root '$VAULT' has no 00-BRAIN/AGENT.md — refusing to run."

# --- derive the protected list from the live tree -----------------------------
protected=()
[[ -d "$VAULT/88-JOURNAL" ]]            && protected+=("$VAULT/88-JOURNAL")
[[ -d "$VAULT/00-BRAIN/CASTLE/raw" ]]   && protected+=("$VAULT/00-BRAIN/CASTLE/raw")

hub_raw_count=0
shopt -s nullglob
for d in "$VAULT"/03-WIKIS/*/raw; do
  [[ -d "$d" ]] || continue
  protected+=("$d")
  hub_raw_count=$((hub_raw_count + 1))
done
shopt -u nullglob

# Fail closed on an implausible derivation. These three conditions are what a
# broken glob, a wrong vault root, or a half-mounted filesystem look like.
[[ -d "$VAULT/88-JOURNAL" ]] || \
  die "88-JOURNAL not found under '$VAULT' — derivation is wrong, refusing to run."
[[ -d "$VAULT/00-BRAIN/CASTLE/raw" ]] || \
  die "00-BRAIN/CASTLE/raw not found — derivation is wrong, refusing to run."
(( hub_raw_count >= 1 )) || \
  die "no 03-WIKIS/*/raw directories found — derivation is wrong, refusing to run."

# --- --list -------------------------------------------------------------------
if [[ "${1:-}" == "--list" ]]; then
  printf 'vault: %s\n' "$VAULT"
  printf 'read-only binds (%d):\n' "${#protected[@]}"
  printf '  %s\n' "${protected[@]}"
  exit 0
fi

command -v bwrap >/dev/null 2>&1 || \
  die "bwrap not installed — the OS-level deny is unavailable, refusing to run."

# --- build the bwrap argument vector ------------------------------------------
bwrap_args=(--bind / / --dev-bind /dev /dev --proc /proc --chdir "$PWD")
for p in "${protected[@]}"; do
  bwrap_args+=(--ro-bind "$p" "$p")
done

# --- --selftest ---------------------------------------------------------------
# Proves ENFORCEMENT, not presence. Three probes, none of which creates a file
# when the control holds; if a probe unexpectedly succeeds it says so loudly and
# names the residue, because a silent pass is the thing this flag is about.
if [[ "${1:-}" == "--selftest" ]]; then
  probe_dir="${protected[$(( ${#protected[@]} - 1 ))]}"   # last hub raw/ dir
  printf 'safe_shell selftest\n  vault:  %s\n  binds:  %d\n  probe:  %s\n\n' \
    "$VAULT" "${#protected[@]}" "$probe_dir"

  bwrap "${bwrap_args[@]}" -- bash -c '
    set -u
    vault="$1"; probe_dir="$2"; fails=0

    # 1. the vault itself must remain writable, or the wrapper is useless
    if [ -w "$vault" ]; then
      echo "  PASS  vault writable inside sandbox"
    else
      echo "  FAIL  vault NOT writable inside sandbox — bulk work cannot run here"
      fails=$((fails + 1))
    fi

    # 2. a direct, literal write into a protected dir must be refused
    if ( : > "$probe_dir/.safe_shell_selftest_direct" ) 2>/dev/null; then
      echo "  FAIL  direct write into protected dir SUCCEEDED"
      echo "        residue: $probe_dir/.safe_shell_selftest_direct"
      fails=$((fails + 1))
    else
      echo "  PASS  direct write into protected dir refused"
    fi

    # 3. the August 10 shape: target resolved by a glob at runtime, so the
    #    protected path never appears literally in any command string
    hit=""
    for d in "$vault"/03-WIKIS/*/raw; do hit="$d"; done
    if [ -z "$hit" ]; then
      echo "  FAIL  glob probe resolved nothing — test is not exercising anything"
      fails=$((fails + 1))
    elif ( : > "$hit/.safe_shell_selftest_glob" ) 2>/dev/null; then
      echo "  FAIL  glob-expanded write SUCCEEDED — the Aug 10 shape is NOT blocked"
      echo "        residue: $hit/.safe_shell_selftest_glob"
      fails=$((fails + 1))
    else
      echo "  PASS  glob-expanded write refused (the Aug 10 shape)"
    fi

    echo
    if [ "$fails" -eq 0 ]; then
      echo "SELFTEST PASS — OS-level write deny is enforcing."
      exit 0
    fi
    echo "SELFTEST FAIL — $fails probe(s) failed. Do NOT run bulk work behind this."
    exit 1
  ' _ "$VAULT" "$probe_dir"
  exit $?
fi

# --- run the requested command ------------------------------------------------
(( $# > 0 )) || die "no command given. Try --selftest, --list, or a command to run."

exec bwrap "${bwrap_args[@]}" -- "$@"
