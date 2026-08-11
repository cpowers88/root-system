---
type: report
timeline: now
status: proposed
tags: [sandbox, governance, wsl, flag-92, flag-95, security]
created: 2026-08-11
---

# Sandbox Re-check — August 11, 2026 (evening session)
### Claude Code · WSL-launched · answers Chris's question "is the sandbox live now?"

## Direct conclusion

**No. The sandbox is still inert.** An independent re-measurement this session,
from a fresh WSL-launched Claude Code process, reproduced all four negative
dimensions from this morning's failed acceptance test, plus two filesystem
dimensions. Nothing has changed since the morning run: `sandbox.enabled: true`
in `.claude\settings.json` has no observable effect on `Bash` child processes,
filesystem or network.

Flag #92 stays **HIGH** and flag #95 instance (2) stays open, both as written.
Copy-first (`AGENT.md` § File Safety item 12) remains the only live control on
bulk work.

One new finding, below: the `Bash`-side journal guard is **spelling-sensitive**
— it caught an absolute path and missed the relative form of the same path. That
is flag #95's failure class showing up in a fourth place, and it is not recorded
anywhere yet.

---

## Method

Every probe this session was **non-destructive**: capability checks only
(`test -w`, `ls` to `/dev/null`, `curl -o /dev/null`, `/proc` reads). No files
were created anywhere in the vault or outside it, so unlike the morning run there
is nothing for you to delete. No journal content was read or displayed — the two
journal probes discarded their output and I recorded only the return code.

---

## Measurements

| Dimension | Expected if sandbox were live | Measured this session | Verdict |
|---|---|---|---|
| Process ancestry | a `bwrap` ancestor above the shell | `bash ← claude ← bash ← Relay(324) ← SessionLeader ← init-systemd` — **no `bwrap`** | negative |
| Seccomp filter | non-zero `Seccomp` / `Seccomp_filters` | `Seccomp: 0`, `Seccomp_filters: 0`, `NoNewPrivs: 0` | negative |
| Namespace isolation | mount/net namespaces created for the sandbox | mnt/pid/ipc/uts are the WSL session's own, shared with the session leader; `net` and `user` are the host's | negative — none sandbox-attributable |
| Network allowlist (`allowedDomains`: 2 hosts) | non-allowlisted host blocked | `https://example.com` → **HTTP 200** (allowlisted `docs.anthropic.com` → 301) | negative |
| `filesystem.denyWrite` (10 paths) | child process cannot write | `03-WIKIS\PYTHON\raw`, `00-BRAIN\CASTLE\raw`, `88-JOURNAL`, vault root all report **writable** | negative |
| `filesystem.denyRead` (`88-JOURNAL`) | child process cannot list | directory **listed successfully** from `Bash` | negative |

`bwrap` is present at `/usr/bin/bwrap`. The capability exists on this machine;
Claude Code is simply not invoking it. That matches this morning's `bwrap
--ro-bind` test, which *did* enforce on `/mnt/c` — the control is reachable, it
is just not the one currently running.

---

## New finding — the `Bash` journal guard matches spelling, not path

Flag #92 currently records that "any `Bash` command naming `88-JOURNAL`
literally was refused before execution." That is **half true**, and the half
that fails matters:

| Command | Result |
|---|---|
| `cd /mnt/c/Users/chris/.ROOT; ls ./88-JOURNAL` | **ran** — directory listed, rc=0 |
| `ls /mnt/c/Users/chris/.ROOT/88-JOURNAL` | **refused before execution** |

Both name the journal literally; both resolve to the same directory. The deny
rules in both the project and the deployed WSL user settings are written
`Read(/mnt/c/Users/chris/.ROOT/88-JOURNAL/**)` — tool-scoped, absolute. There is
no `Bash`-scoped journal deny anywhere in either file, so what refused the second
command was a path match against that absolute string. Change the spelling to a
relative path after a `cd` and it does not match.

Caveat on that second row: I cannot distinguish an automated rule deny from a
manual one from inside the session. No other command this session prompted, and
the only one refused was the one naming the absolute path, which is what an
automated match looks like — but treat the mechanism as inferred, not proven.

**Why this is flag #95, not a new problem.** It is the same structure as the
three cases already on that flag: a control that reads as protection in an audit
while enforcing only against one spelling of the thing it guards. The August 10
incident was a glob evading a string matcher; this is a relative path evading the
same matcher. Different input, identical gap.

---

## Proposed edits, held for your review

I did not change any governance file. Two corrections are queued:

1. **Flag #92** — replace "any `Bash` command naming `88-JOURNAL` literally was
   refused before execution" with a form that states the limit: *"a `Bash`
   command naming the journal by its absolute path is refused before execution;
   the same command using a relative path after `cd` is not (measured
   2026-08-11 evening). The guard matches the command string's spelling, not the
   resolved path."*
2. **Flag #95** — add a fourth measured instance: the spelling-sensitive `Bash`
   journal guard, same class as the existing three.

Say the word and I'll make both edits.

---

## What still stands

- The August 10 boundary decision (Windows default, WSL for bulk work) is
  **still unsupported by an enforced control in either environment**.
- `bwrap --ro-bind` on `/mnt/c` remains verified as of this morning and is still
  the only route to an OS-level deny.
- `00-BRAIN\scripts\safe_shell.sh` — the wrapper that would derive the read-only
  bind list from the live tree and run bulk work inside it — remains **proposed,
  not built**, awaiting your approval as new governance tooling.

**Recommendation:** approve the wrapper. Copy-first is a discipline rule that
depends on the operator remembering it every time; the wrapper is a mechanism
that does not. They are complements — keep item 12 either way — but right now
every protection in the stack is a matcher over strings a human or model chose
to type, and this session found a fourth way to type around one.

---

## Session facts

- **Files written:** this report; delta entry in `Session_Logs\DAILY_2026-08-11.md`.
- **Files altered:** none — no config, no governance, no flags.
- **Residue:** none. No probe files created.
- **Protected content:** none read or displayed.
