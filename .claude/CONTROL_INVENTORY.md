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
3. If a control measures INERT, either record it here or remove it. Leaving it
   silent is the one outcome this file exists to prevent.
