---
type: handoff
tags: [reference, system, codex]
---

# HANDOFF — July 13, 2026 — Codex

## Current State

`C:\Users\chris\.ROOT` is the canonical live working tree. All active root and
CASTLE boot pointers, maps, seven wiki guide footers, and Codex project configuration
now identify C: as canonical. The boot-chain validator passes with the live vault-root
Claude router. `G:\My Drive\.ROOT` is a cloud-backup recovery copy
only and must not be used as an AI boot target or working tree. Flag 70 is closed:
the helper was restored and local unelevated operation is working. The approval gate
and network denial remain intentional.

## Open Question or Blocker

None blocking. Chris verified that Drive for desktop syncs the C: vault under
**Computers → this PC → .ROOT** and the live folder/files display green sync marks.
`G:\My Drive\.ROOT` remains a legacy recovery snapshot, not the active cloud-sync path.

## Next Exact Action

Chris continues the Python Stage 2 teaching session with Claude Chat. Future system
work keeps `C:\Users\chris\.ROOT` as the sole working/boot path; Google Drive
Computers is backup only.

## Details Likely to Be Forgotten

- `88-JOURNAL` exists inside the C: vault copy. Codex did not read it. Claude's
  `settings.local.json` denies read/write access using relative paths, so the safeguard
  survives the move; retain it.
- Historical session logs retain G: paths as factual records. Active-reference scans
  must exclude `Session_Logs`, `99-ARCHIVE`, and raw material; do not rewrite history.
- `approval_policy = "on-request"` and disabled network access in `.codex\config.toml`
  are safeguards, not evidence that the current local sandbox is broken.
