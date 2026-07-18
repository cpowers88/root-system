---
type: report
tags: [reference, codex, sandbox, recovery]
---

# Codex Windows Sandbox Recovery — July 13, 2026

## Verified Current State

The July 13 reinstall restored the missing sandbox helper. It now exists at:

`C:\Users\chris\.codex\packages\standalone\current\codex-resources\codex-windows-sandbox-setup.exe`

Installed CLI version: `codex-cli 0.144.1`.

However, a normal sandboxed read in `G:\My Drive\.ROOT` still fails with:

`windows sandbox: helper_unknown_error: setup refresh had errors`

This separates two issues:

1. **Missing helper:** fixed by the reinstall.
2. **Google Drive mount sandbox compatibility / ACL setup:** still unverified and likely the remaining cause.

## Do Not Delete `.codex` Wholesale

Do **not** remove `C:\Users\chris\.codex` as a normal reinstall step. It may hold
authentication, configuration, skills, plugins, session state, and the installed
runtime. Deleting it would add recovery work without addressing the Google Drive
filesystem limitation.

In particular, preserve these paths:

- `C:\Users\chris\.codex\auth.json` — login state; never share its contents.
- `C:\Users\chris\.codex\config.toml` — personal settings.
- `G:\My Drive\.ROOT\.codex\config.toml` — project settings; the current
  `approval_policy = "on-request"` is the intentional human-review backstop.

## Recovery / Verification Procedure

1. Fully quit the Codex desktop app and close every Codex CLI terminal.
2. Reopen the desktop app and open a new PowerShell window.
3. Confirm the installed CLI and helper:

```powershell
codex --version
Test-Path -LiteralPath 'C:\Users\chris\.codex\packages\standalone\current\codex-resources\codex-windows-sandbox-setup.exe'
```

Expected: a current `codex-cli` version and `True`.

4. Test native Windows sandboxing on local NTFS first. This deliberately avoids
   Google Drive, so it isolates whether Codex itself is healthy:

```powershell
$test = "$env:USERPROFILE\CodexSandboxTest"
New-Item -ItemType Directory -Force -Path $test
Set-Content -LiteralPath (Join-Path $test 'sandbox-test.txt') -Value 'sandbox test'
codex exec -C $test --skip-git-repo-check -s workspace-write 'Read sandbox-test.txt and report its exact contents. Do not change any files.'
```

5. Only if the local test succeeds, compare it with `.ROOT`:

```powershell
codex exec -C 'G:\My Drive\.ROOT' --skip-git-repo-check -s workspace-write 'Read NOW.md and report its first heading. Do not change any files.'
```

6. Interpret the outcome:

| Result | Meaning | Action |
|---|---|---|
| Both tests pass | Helper and Drive sandbox setup work. | Keep normal sandboxed use. |
| Local NTFS passes; `.ROOT` fails | Codex is repaired; Google Drive mount cannot complete the needed sandbox setup. | Keep `.ROOT` approval-gated; use a local NTFS checkout/workspace for native sandboxing. |
| Both fail | The Codex runtime/install still has a problem. | Reinstall/update Codex again; send the exact error and the two command outputs to OpenAI support. |

## If the Helper Is Missing Again After a Future Update

1. Do not delete `C:\Users\chris\.codex` first.
2. Quit Codex completely.
3. Use the official Codex installer/updater to repair or reinstall.
4. Repeat the `Test-Path` verification above.
5. If it is still `False`, report the Codex version and this exact expected path to support. Do not attempt to download or copy an `.exe` from an unofficial source.

## Safety Notes

- Do not use `--dangerously-bypass-approvals-and-sandbox` to work around this.
- Do not edit or remove `auth.json` unless you intentionally want to sign out.
- Do not change the `.ROOT` approval backstop until the local and Drive tests establish that the sandbox is working.
- The stale comment in `.ROOT\.codex\config.toml` can be corrected later; its active settings remain appropriate today.

