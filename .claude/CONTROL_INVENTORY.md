---
type: reference
timeline: reference
register: ai-directive
tags: [governance, security, configuration, flag-95]
created: 2026-08-11
status: live
---

# Control Inventory — what in `.claude\` actually enforces something

### Read this before citing any rule in `settings.json` as protection.

This file exists because a config set can be syntactically valid, pass its
validation gate, and protect nothing. That is flag #95's failure mode, and it
produced five measured instances in two days. The dangerous version is not a
broken rule — it is a rule that **reads as protection in an audit** while
enforcing nothing, because nobody ever measured it.

Two scripts answer two different questions. Do not substitute one for the other:

| Script | Question it answers |
|---|---|
| `00-BRAIN\scripts\validate_boot_chain.py` | Are the rules **present** and well-formed? |
| `00-BRAIN\scripts\verify_controls.py` | Do the rules **bite** in the environment reading them? |

Run the second from **both** Windows and WSL. A control can be live in one and
dead in the other; that asymmetry is the whole point.

---

## Status as measured 2026-08-11

| Control | Windows | WSL | Notes |
|---|---|---|---|
| `permissions.deny` — tool-scoped (`Read`/`Edit`/`Write`) | live | live | Governs **tool calls only**. Matches the command *string*, not the path a command resolves at runtime. |
| `permissions.deny` — `Bash(rm *)` etc. | live | live | Same string-matching limit. `/bin/rm`, a relative path after `cd`, or a glob all walk past it. |
| `permissions` mode locks | live | live | `disableBypassPermissionsMode` / `disableAutoMode` set in both environments. |
| Deployed user policy vault denies | live | live | Windows uses `~/.ROOT/...`; WSL must use the resolved `/mnt/c/...` form. |
| **`sandbox` block (whole)** | **INERT** | **INERT** | See below. |
| `00-BRAIN\scripts\safe_shell.sh` | n/a | **enforcing** | The only measured OS-level write deny in this stack. |
| `PreToolUse` bulk-work gate — `Bash` | **enforcing** | **enforcing** | Added 2026-08-11, measured in both environments the same day. |
| `PreToolUse` bulk-work gate — **`PowerShell`** | **ABSENT** | n/a | **The hook matcher is `"Bash"` only. PowerShell tool calls are completely ungated** — and the 2026-08-10 incident that this whole chain exists to prevent *was a PowerShell script*. See below. |

---

## The `sandbox` block is declarative only — it enforces nothing today

`settings.json` declares `sandbox.enabled: true`, a ten-path `filesystem.denyWrite`
list, a `filesystem.denyRead` entry, and a two-host `network.allowedDomains`
allowlist. **None of it is in force on this machine.**

Measured negative on six independent dimensions, by two separate sessions on
2026-08-11, and reproducible at any time via `verify_controls.py`:

1. No `bwrap` ancestor anywhere in the process lineage.
2. `Seccomp: 0`, `Seccomp_filters: 0`, `NoNewPrivs: 0`.
3. No namespace isolation attributable to the sandbox.
4. Egress to non-allowlisted `example.com` returns HTTP 200.
5. All ten `denyWrite` paths report writable to a spawned child process.
6. The `denyRead` journal directory lists successfully from a child process.

**Do not delete this block.** It is kept deliberately so that the protection
activates if native sandbox support lands on this platform. But until
`verify_controls.py` reports it ENFORCED, no audit, report, or flag may cite it
as a live control, and no work may be planned on the assumption that it holds.

**What actually protects bulk work:** `AGENT.md` § File Safety item 12 — copy-first
(discipline) *and* `safe_shell.sh` (mechanism), both required, each covering the
other's gap.

**Owner and check moment** (required by `AGENT.md` Execution Discipline 7 — a
dated trigger nobody evaluates does not exist): re-measured by whoever changes
anything under `.claude\`, and at the monthly review as part of `CASTLE\OPERATIONS.md`'s
cadence. If `verify_controls.py` ever reports the sandbox block ENFORCED, update
this file in the same session and reconsider whether item 12's wrapper
requirement can relax.

---

## The `PreToolUse` bulk-work gate — item 12 stops being prose

`AGENT.md` File Safety 12 requires bulk or scripted work to run through
`safe_shell.sh`. Until 2026-08-11 nothing checked that. The requirement was a
sentence in a file a session might not have read, and the two known incidents —
the 2026-08-10 glob that rewrote 2,713 files, and the 2026-08-11 `fetch_fred.py`
execution that wrote three ECON rows during a probe — were both cases where the
sentence existed and did not fire.

`.claude\hooks\require_safe_shell.sh` (launcher) plus `require_safe_shell.py`
(gate) now deny any `Bash` command that could touch many files in one pass unless
it is launched through the wrapper. **It is a redirect, not a refusal:** the deny
message contains the exact wrapped command to run instead.

**No string override exists, deliberately.** An escape hatch spelled in the
command — an env prefix, a magic comment — is one an AI can type for itself, and
a wall with an AI-accessible door is not a wall. The only ways past are the
wrapper, or Chris editing `ALLOWED_SCRIPTS` / removing the hook. Both are human
acts.

**`ALLOWED_SCRIPTS` is a trust assertion, not a measurement.** Adding a name to
it asserts someone read that script and confirmed it does not write `88-JOURNAL`
or any `raw\`. Anything not named is gated — new-and-unreviewed is precisely the
`fetch_fred.py` shape.

**Fail-closed everywhere.** Missing gate file, no Python interpreter, empty or
unparseable stdin, non-string command, internal crash — all exit 2 (deny). This
is deliberate and is the opposite of the usual hook convention: Claude Code
treats any exit code other than 0 or 2 as a *non-blocking error*, so a hook that
merely breaks lets the tool call through. A gate that fails open is flag #95's
failure mode with extra steps.

**Why a launcher script and not a direct `python` command.** Measured
2026-08-11: WSL has `python3` and no `python`; Windows has `python`
(`C:\Python314`) and no `python3`. Either spelling hardcoded into the hook
`command` is dead in one environment, and a dead hook fails open. The launcher
resolves `python3`/`python`/`py` at run time and denies if none is found.

**Quoted text is data; quoted text fed to `-c` is code.** `git commit -m "while
testing, do not skip"` must pass and `bash -c 'for f in *; do rm $f; done'` must
not, though both contain the same loop-shaped words. The gate blanks quoted spans
before reading a command, except where an interpreter's `-c`/`-e` flag or `eval`
makes the quoted span the program. This is not a refinement — a gate that blocks
ordinary commit messages is one its user turns off within a day, and a turned-off
gate protects nothing.

**Command substitution is evaluated too.** `echo $(bash migrate.sh)` runs the
script while looking like an `echo`, and the substitution survives quoting. Their
bodies are classified recursively (depth-limited).

**Evidence:** `.claude\hooks\test_require_safe_shell.py` — 59 classification
cases and 11 end-to-end cases covering typical, edge, and failure/recovery
shapes, per `AGENT.md`'s Agent Evaluation Gate. Re-run it after any change to
the gate; a regression returns the hook to supervised use.

**What this gate does NOT do.** It reads `Bash` tool calls. It does not constrain
a process once started, does not inspect what an allowlisted script does, and is
pattern-based — a sufficiently novel shape can be built that it does not
recognise. It raises the cost of reaching the exposure in flag #96; it does not
remove it, and `safe_shell.sh` remains the thing that actually enforces.

**Windows measured 2026-08-11: ENFORCED.** Settled from a Windows session two
ways — an actual bulk `Bash` tool call was denied with the correct redirect
message, and `verify_controls.py` now reports `bulk denied (rc=2), ordinary
allowed (rc=0)`. Both environments are live.

**A false negative was found and fixed in the same check — read this before
trusting any measurement here.** The first Windows run reported the gate
**INERT (rc=127)**. The gate was fine; the *probe* was wrong. `check_bulk_gate()`
ran the hook command through `subprocess(shell=True)`, which on Windows goes via
`cmd.exe`, where `bash` resolves to the **WSL launcher**
(`...\WindowsApps\bash.exe`) and cannot open a Windows-style path. Claude Code
runs shell-form hooks through **Git Bash** (`C:\Program Files\Git\bin\bash.exe`),
so the real hook fired the whole time. The probe now rewrites `bash` to Git Bash
on Windows, and — more importantly — **rc=127 is no longer reported as INERT at
all.** A probe that could not launch says nothing about its subject, so it now
records NOT MEASURABLE with an instruction to confirm via a real bulk call.

**This is flag #95's failure mode inverted, and it is just as dangerous.** There,
config read as protection and enforced nothing. Here, a working control read as
dead. A false "dead" reading gets a functioning guard ripped out, or gets an
environment declared unprotected and worked in accordingly. **The rule that
generalises: never let a measurement's own failure to run count as evidence about
the thing it measures.**

### The gate covers `Bash` and NOT `PowerShell` — measured 2026-08-11

`settings.json` declares the hook with `"matcher": "Bash"`. Nothing else. A
bulk-shaped `PowerShell` call — a pipeline into `ForEach-Object` over every
markdown file in the vault — **ran with no gate**, verified from a Windows
session immediately after the `Bash` side was certified ENFORCED.

**This matters more than any other line in this file.** The 2026-08-10 incident
that produced flag #92, flag #96, `safe_shell.sh`, item 12, and this gate was a
**PowerShell script** that rewrote 2,713 files. The gate built in response does
not cover the shape of the incident that caused it, on Windows, where PowerShell
is the native shell and the tool this vault reaches for first.

Do not describe the bulk-work gate as covering "bulk work." It covers **bulk
`Bash`**. Until a `PowerShell` matcher exists with a PowerShell-aware classifier
(`ForEach-Object`, pipelines, `-Recurse`, `Remove-Item`, `Set-Content` over a
glob — none of which the current bash-shaped patterns recognise), Windows bulk
work is governed by discipline alone.

`verify_controls.py` measures the `Bash` path only, so it reports ENFORCED while
this hole is open — which is exactly the "reads as protection in an audit"
failure this file exists to prevent, occurring inside the file's own subject.
Extending the gate is queued as the next control-plane task.

---

## Environment-dependent values — the portability rules

Everything below is a place where one config is read from two environments.

**Interpreter names.** WSL has `python3` and no `python`; Windows has `python`.
An allow rule naming the wrong one never matches, and every scripted run prompts.
Carry **both spellings** for each script. `verify_controls.py` checks that each
script is reachable by at least one spelling in the current environment — not
that every rule resolves, since one of each pair is always dead by design.

**Vault paths in user-scope policy.** `~/.ROOT` is correct on Windows and wrong
in WSL, where `~` is `/home/<user>` and `~/.ROOT` does not exist. A policy
deployed there unchanged installs five rules guarding an empty directory while
the real vault stays open. `user-settings-policy.template.json` ships the
Windows spelling; **substitute the resolved absolute path when deploying outside
Windows.** `validate_boot_chain.py` accepts both spellings for the *template*
(a source artifact adapted at deploy time) but requires a spelling that actually
resolves for a *deployed* policy.

**Path separators.** Backslash rules match only Windows-typed commands. Prefer
forward slashes, which work in both.

**`PowerShell(...)` deny rules.** Inert in WSL — there is no PowerShell tool
there. Harmless, but they are not the WSL-side control they appear to be.

---

## When you change anything in `.claude\`

1. Run `validate_boot_chain.py` — rules present and well-formed.
2. Run `verify_controls.py` from **Windows and WSL** — rules actually bite.
3. If you touched `.claude\hooks\`, run
   `python3 .claude/hooks/test_require_safe_shell.py` — the gate still classifies
   correctly and still fails closed.
4. If a control measures INERT, either record it here or remove it. Leaving it
   silent is the one outcome this file exists to prevent.
