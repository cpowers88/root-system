---
name: root-health
description: Run and interpret the canonical read-only `.ROOT` health gate. Use when Chris asks to check system health or integrity, after governance/wiki/metadata/shared-skill changes, or before a system checkpoint.
---

# Check `.ROOT` Health

1. Run `python 00-BRAIN\scripts\root_health.py` from `.ROOT`.
2. Treat a nonzero exit or `BLOCKER` as a stop. Report the failing named scope
   and its evidence; do not continue to a checkpoint.
3. Report `PASS WITH DEBT` honestly. Name the wiki review count and reviewed
   frontmatter debt; never translate that state to “clean.”
4. Use `--strict` only when the acceptance condition is zero debt. Use `--json`
   for machine-readable output and `--verbose` when child output is needed.
5. State the gate's listed “not evaluated” scopes when they matter to the task,
   and route those questions to their owning review instead of inferring a pass.
6. Before a commit, confirm both the staged and unstaged whitespace checks pass;
   one cannot substitute for the other.

The command and this skill are read-only. They do not authorize repairs, baseline
refreshes, raw writes, or journal access.
