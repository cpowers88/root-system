---
type: report
tags: [log, audit, governance]
status: report-only
created: 2026-07-15
---

# `.ROOT` System Integrity Audit — July 15, 2026

## Executive verdict

`.ROOT` has a sound top-level architecture, a clean universal boot chain, eight
fully formed wiki hubs, current North Star/strategy contracts, and synchronized
shared skills. It is not structurally broken.

The real problem is **false assurance at the interfaces**. Current validators can
say PASS while launch-directory-dependent Claude settings, stale live project
language, unresolved planned links, and 621 metadata violations remain. The system
has good parts, but some of the checks prove only narrow conditions and are being
described as proof of the whole.

The most likely cause of Claude behaving differently while looking at different
parts of `.ROOT` is the set of nested `.claude/settings.local.json` files under
`03-WIKIS`. Official Claude Code documentation says hooks and most settings load
from the **current working directory's** `.claude` folder with no parent-directory
fallback. Launching Claude at `.ROOT`, `03-WIKIS`, or a particular hub can therefore
produce different permission behavior.

This was a report-only audit. No governance, project, wiki, skill, raw, archive, or
private file was changed. The report was written while another Claude session had
uncommitted work in progress, so the NOW/flag inconsistency below is explicitly a
snapshot and must be checked again at that session's close.

## Audit scope and evidence

- Loaded the required governance chain: `AGENT.md`, `CODEX.md`, `CHRIS_CORE.md`,
  `SYSTEM_FLAGS.md`, `NORTH_STAR.md`, `ROOT_CAPABILITY_CONTRACT.md`, placement/maps,
  CASTLE, current strategy, prep plan, Watchtower, and the four canonical skills.
- Inventoried 1,110 live Markdown files outside journal, archive, raw, tooling
  mirrors, and session-log history.
- Ran the current deterministic checks:
  - boot validation: PASS, 30 boot files / 1,094 live pages;
  - strict wiki lint: 0 blockers, 0 review debt, 716 expected findings;
  - shared skills: PASS, four canonical skills and two mirrors;
  - frontmatter audit: 621 findings across 1,136 files.
- Scanned live project status, nested tool configuration, direct path claims,
  retired terminology, duplicate hashes, tiny/empty files, skill commands, review
  cadence, raw-archive duplication, and links outside the wiki linter's scope.
- Did not read `88-JOURNAL` and did not display or read secret contents.

The differing page totals above are not themselves corruption; each script has a
different exclusion model. They do show that `.ROOT` lacks one shared definition of
"live auditable file," which makes cross-script PASS claims hard to compare.

## Confirmed findings

### P0 — fix before trusting another Claude launch from a subfolder

#### 1. Claude safety and permissions depend on launch directory

The hardened root file is:

- `.claude\settings.local.json` — Manual/default mode, journal denies, raw write
  denies, destructive-command denies, and sandbox restrictions.

Eight additional local settings files exist below it:

- `03-WIKIS\.claude\settings.local.json`
- `03-WIKIS\AI_AUTOMATION_SYSTEMS\.claude\settings.local.json`
- `03-WIKIS\BUSINESS\.claude\settings.local.json`
- `03-WIKIS\EDUCATION\.claude\settings.local.json`
- `03-WIKIS\PHYSICS\.claude\settings.local.json`
- `03-WIKIS\PYTHON\.claude\settings.local.json`
- `03-WIKIS\SYSTEMS\.claude\settings.local.json`
- `03-WIKIS\TECHNOLOGY\.claude\settings.local.json`

None carries the root journal/raw sandbox boundary. The parent `03-WIKIS` file is a
stale migration allowlist that includes `rm -rf wiki .claude`, `rm -f CLAUDE.md
HOW_TO_USE.md desktop.ini`, broad moves, and broad shell patterns. Hub files contain
old one-session allowances such as `Bash(python *)`, `Bash(cd *)`, `PowerShell(New-Item
*)`, and obsolete scratch paths. They are globally gitignored, so repository review
does not expose their drift.

Claude Code's current documentation states that settings arrays merge across scopes,
permission resolution is deny → ask → allow, and most settings load from the current
working directory's `.claude` folder with **no parent-directory fallback**. See
[Claude Code permissions](https://code.claude.com/docs/en/permissions) and
[Claude Code settings](https://code.claude.com/docs/en/settings).

**Impact:** root protections can be absent when Claude is launched inside
`03-WIKIS` or a hub. This also explains why journal protection can appear
deterministic in one session and "convention-only" in another.

**Best correction:** until repaired, launch Claude only from
`C:\Users\chris\.ROOT` and verify the active settings source with `/status` or
`/permissions`. Then, with Chris's approval, archive/remove the eight nested local
settings files and place hard private/raw denies at a scope that cannot disappear
when the launch directory changes (preferably user/managed hard denies, with the
root project file retaining `.ROOT`-specific convenience policy). Add a validator
that fails on any non-root `.claude/settings*.json` shadow.

#### 2. The current boot validator cannot see this failure class

`00-BRAIN\scripts\validate_boot_chain.py` excludes every path containing
`.claude` and validates only the root settings file. It therefore reports PASS while
the eight nested settings files exist. Its stale-language scan is also a curated
regex list, not a general direct-path or semantic-owner check.

**Best correction:** add explicit nested-configuration discovery before applying
the `.claude` exclusion. Treat any nested settings file as a blocker unless listed
in a reviewed exception table.

### P1 — live semantic interfaces disagree

#### 3. The live KSU Academic Tracker brief still describes the retired system

`02-LIBRARY\.PROJECTS\KSU_Academic_Tracker\KSU_Academic_Tracker_Brief.md`
is tagged `now` but still says:

- note paths live under retired `04-SCHOOL\01-KSU\...`;
- the tracker is a "Track 2 project that serves Track 1";
- POL is the product and resumes after the tracker.

Current authority says course files live under `02-LIBRARY\00-SCHOOL`, the
track/lane identity model is retired, and POL is not an active governing build.

**Best correction:** update this brief to the permanent-capability/current-strategy
model, replace sample paths with the live course paths, and make the July 25 real-data
test its only active next step. Add this exact file to the stale-interface regression
set; flag #75's claimed direct-path/stale-language PASS missed it.

#### 4. `NOW.md` and SYSTEM_FLAGS #51 disagree in the in-flight snapshot

At audit time, `SYSTEM_FLAGS.md` moves #51 to CLOSED and `CASTLE\OPERATIONS.md`
records the new Fall calendar, while `NOW.md` still tells Chris to build that calendar
and says tagging stops August 22–23.

**Impact:** the morning cockpit points to already-completed system work rather than
Physics Stage 3.

**Best correction:** the active Claude session must refresh `NOW.md` before close.
If it does, this finding closes as an in-flight edit-order issue. If it does not, the
session-close contract failed and #75 should be reopened under the re-raise rule.

#### 5. Project space contains duplicate and expired authority

- `FMLS_ListingOS_PAUSED\` and `listing-packet\` both describe the same
  `cpowers88/listing-packet-clean1` repository. The first is a parked May snapshot;
  the second is a move pointer to `D:\DEV\active\Project-listing-packet`.
- `FMLS_PROJECT_STATUS.md` still names an old
  `C:\Users\chris\projects\listing-packet-clean1` output path and says Notion owns
  operational status, which conflicts with the current `.ROOT`/CASTLE contract even
  though a new warning labels the body historical.
- `listing-packet\MOVED_TO_LOCAL.md` says a `.gdoc` is still present; it is not. Only
  nested `desktop.ini` files remain under its empty output folders.
- `TCG_POS\TCG_POS_SCOPING.md` is tagged parked but still says PENDING COMMITMENT and
  carries a June 23 decision deadline with no recorded verdict.

**Best correction:** one project, one status pointer. Keep a single parked ListingOS
entry that points to the verified local repo and archive the duplicate wrapper after
inbound-reference checks. Convert TCG POS to an explicit `PAUSED — no qualifying
commitment by 2026-06-23` record or document the real exception.

#### 6. The Watchtower board violates its own promotion threshold

`...projectSuccess\radar.md` contains a legacy product rumor without a real evidence
home and an internal "Watchtower established" seed row even though WATCHTOWER.md
requires a verified external change, evidence home, material consequence, and review
trigger.

**Best correction:** move the seed event to history/DAILY, return the unverified
product rumor to AI_AUTOMATION_SYSTEMS research, and allow the live radar to be empty.
An empty truthful board is better than rows that teach agents to ignore the contract.

#### 7. Weekly outcome review has stopped

No July weekly exists. The latest weekly file is `WEEKLY_JUNE9-18.md`, despite the
North Star/CASTLE weekly review contract and major July changes.

**Impact:** dailies and system edits are accumulating without the intended outcome,
capacity, evidence, and opportunity consolidation layer.

**Best correction:** do one recovery weekly covering the meaningful period since
June 19; do not fabricate several backfilled weeklies. Use it to separate system
maintenance from learning, delivery, and income evidence.

### P1 — validation and metadata give misleading assurance

#### 8. The frontmatter check reports 621 violations but always exits success

Current result:

- 100 files missing `type:`;
- 521 files without exactly one recognized timeline tag.

Concentrations include:

- missing type: BUSINESS 53, `02-LIBRARY` 43, CASTLE 2, Revenue Lab 2;
- timeline: PHYSICS 272, PYTHON 164, `02-LIBRARY` 45,
  AI_AUTOMATION_SYSTEMS 34, TECHNOLOGY 4, CASTLE 1, BUSINESS 1.

The 44-file `02-LIBRARY\08-AI-AUTOMATION\make.com_notes\` corpus alone produces
85 findings (42 missing type, 43 missing timeline) and contains 142 `docId:` pseudo-
links that ordinary Markdown scanners interpret as broken local links.

`frontmatter_audit.py` returns exit code 0 regardless of findings. Calling the run a
"PASS" means only "no new finding relative to memory," not compliance with the
Tag Standard.

**Best correction:** add `--strict`, machine-readable output, and an explicit
reviewed baseline. Reports must say `BASELINE DEBT: 621`, not PASS. Zero new debt and
zero total debt are different acceptance conditions.

#### 9. The timeline-tag design conflates three different meanings

The standard treats `now/next/later`, `priority/now`, and `stage-02` as equivalents.
They are not equivalent:

- `now/next/later` is dynamic execution state;
- `priority/now` in inherited knowledge pages is reading/usefulness ranking;
- `stage-02` is static curriculum position.

There are 73 SYSTEMS pages tagged `priority/now` and 37 TECHNOLOGY pages tagged
`priority/now`. A "what matters now" view therefore returns at least 110 knowledge
pages before current projects and learning actions. Meanwhile current Python and
Physics stage pages often store `priority: current` or `status: ready/draft` as
properties that the audit ignores. `START_HERE.md` instructs `tag:#now` while also
describing `priority/now` and stage tags as if the same query finds them.

**Best correction:** approve one two-axis schema before bulk metadata edits. Recommended:

```yaml
type: stage
timeline: now              # dynamic: now/next/later/parked/reference/log
stage: 2                   # static curriculum position
status: in-progress        # artifact/proof state
tags: [python, programming]
```

Keep reading rank in a separate property such as `reference_priority`. Update the
graph/search instructions to a query verified in Obsidian, then migrate with a
deterministic dry-run script. Do not "fix" individual `now` tags before this decision.

#### 10. Wiki lint intentionally masks real unresolved connections

The strict run reports 0 blockers / 0 review debt, but also:

- 135 unresolved PHYSICS links classified as planned;
- 536 files absent from selective navigation indexes;
- 25 inactive PHYSICS drafts;
- 20 code/example false positives.

In `wiki_lint.py`, `is_physics_planned()` ends with
`or hub.name == "PHYSICS"`, so every unresolved PHYSICS target is automatically
"expected," including a future typo in an active page. Link resolution also checks
only whether a matching basename exists somewhere in the vault; it does not verify
that a path-qualified wikilink resolves to the intended file.

**Best correction:** remove the unconditional PHYSICS exemption, use a reviewed
manifest or explicit frontmatter for planned targets, resolve path-qualified links
as paths, and report selective-index omissions as `navigation coverage`, not as
proof of exhaustive inventory. Planned missing pages can remain planned, but users
should not be given clickable links that fail.

#### 11. No validator owns direct paths and project semantics outside the wikis

The current linter ignores `02-LIBRARY` and ordinary path strings. That is how the
retired `04-SCHOOL` path, duplicate project wrappers, passed decision deadline, and
missing `.gdoc` survived a claimed direct-path check.

Twenty ambiguous bare wikilinks also remain outside `03-WIKIS`, mostly CASTLE names
such as `source-map`, `current-position`, `index`, and `log` that exist in several
hubs. Obsidian may resolve the nearest file, but a fresh AI or text-only reader can
select the wrong owner.

**Best correction:** add an all-live-file direct-path/link validator and qualify
authority-bearing CASTLE links with their vault-relative path. Do not require fully
qualified paths in ordinary same-folder learning pages.

### P2 — skills, commands, intake, and file clarity

#### 12. Skills are synchronized, but session-close has an ambiguous path

All four canonical skills match both generated mirrors:

- `atlas-brief`
- `graph-colors`
- `profit-gate`
- `session-close`

The `session-close` skill says to read `AGENT.md` and `CASTLE\OPERATIONS.md` without
their vault-relative locations. From the canonical skill folder, those are not
literal relative paths.

**Best correction:** change the canonical skill to
`00-BRAIN\AGENT.md` and `00-BRAIN\CASTLE\OPERATIONS.md`, then sync. After the
validator work, add a small `root-health` skill that invokes one canonical health
command; do not copy the audit procedure into every profile.

#### 13. Commands are fragmented and inconsistently described

The system currently requires four separate commands for boot, wiki, metadata, and
skill integrity. `START_HERE.md` and `WHERE_IT_GOES.md` sometimes say to run
`build_graph_colors.py` directly while the skill correctly says
`python 00-BRAIN\scripts\build_graph_colors.py`.

**Best correction:** add one read-only `root_health.py` orchestrator with clearly
named scopes and exit codes. It should call the existing scripts rather than replace
them, then add settings-shadow, direct-path, project-status, review-cadence,
duplicate/empty, and stale-interface checks. Document one Windows-safe invocation.

#### 14. Two source/intake areas have no clear ownership return

1. `02-LIBRARY\.raw ARCHIVE\` holds 12 source files. Seven have byte-identical
   copies in live homes (Co-Intelligence, Entrepreneurship, Foundations of Scalable
   Systems, Python Crash Course, Checklist Manifesto, Phoenix Project, Think Python;
   Think Python has two additional copies). Other files may be processed but have no
   manifest proving their evidence home.
2. The 44-file `make.com_notes` corpus is neither a clean immutable source set nor a
   normalized live reference collection. Only `make-com-landscape-rep.md` is linked
   from the live knowledge system; the rest carry imported pseudo-links and most of
   the `02-LIBRARY` metadata debt.

**Best correction:** create a manifest outside the immutable source folders that
maps every `.raw ARCHIVE` file to `duplicate / processed / unprocessed / evidence
home`. Close `.raw ARCHIVE` to new intake. For Make.com, retain the one synthesis,
then either route true source captures to TECHNOLOGY raw with an ingest record or
normalize the files as a deliberately indexed reference corpus. Do not leave the
folder half-source and half-live.

#### 15. Two VSM clippings are in the CSE/Python course folder

- `02-LIBRARY\00-SCHOOL\01-CSE-Python\Notes\Value Stream Mapping for Adding Value.md`
- `02-LIBRARY\00-SCHOOL\01-CSE-Python\Notes\Value stream Mapping Article.md`

They are business/systems sources tagged coding/programming, and their author fields
create unresolved `[[Will VanDenBerg]]` / `[[GBMP]]` notes.

**Best correction:** confirm whether the source is already represented in SYSTEMS or
BUSINESS. If yes, archive the misplaced copies with a source-home note; if not, route
them through the owning wiki's raw/intake process. Use plain author text unless a
person/organization note genuinely exists.

#### 16. Proposal metadata is inconsistent; the pending hook proposal is stale

Ten files inside `AI_AUTOMATION_SYSTEMS\wiki\proposals\` use `type: report` rather
than `type: proposal`, while the index correctly treats them as proposals. Their
status is carried only in prose/index, not frontmatter.

The pending HIGH-flag hook proposal cites an old mirror skill path/line number and a
retired mandatory Codex→Claude lane. It proposes a hook before documenting repeated
close failures or validating current Claude 2.1.210 hook mechanics.

**Best correction:** normalize proposal type/status in one batch. Put the hook idea
on HOLD pending evidence of repeated missed HIGH-flag closes; first make the
session-close skill and health command deterministic. Re-evaluate a hook only if the
prose/skill mechanism actually fails.

#### 17. Minor wording/tombstone cleanup should not lead the work

- `03-WIKIS\TECHNOLOGY\CLAUDE.md` says "FORGE is retiring" although it retired
  July 7. Change to past tense during the semantic batch.
- `00-BRAIN\AI_OS_CORE.md` is an accurate retired-name pointer with no live inbound
  reference outside history. It is not a boot problem. Keep or archive at a normal
  cleanup review; do not spend the active repair window on it.
- The root `CODEX.md` pointer does not repeat "optional HATS" while `AGENTS.md` does.
  `AGENT.md` already supplies the HATS rule, so this is symmetry/clarity, not a broken
  boot chain.

## Assessment of Claude's current queued edits

| Claude finding | Independent verdict |
|---|---|
| Add optional HATS to root `CODEX.md` | Safe cosmetic symmetry; low priority because `AGENT.md` already governs it. |
| AI_AUTOMATION_SYSTEMS CLAUDE.md lacks index/log/North Star links | Overstated. Its folder structure names index/log, and `HOW_TO_USE.md` explicitly loads index, log, and the capability contract. Add a Start Here line only if useful; it is not a missing system connection. |
| Change AI_AUTOMATION_SYSTEMS `now` tags to `reference` | Do not do in isolation. BUSINESS, REVENUE_LAB, and TECHNOLOGY operating files also use `now`; resolve the timeline schema first. |
| Change ten proposal files from `report` to `proposal` | Valid batch cleanup; also add explicit status from the index. |
| Approve/reject the HIGH-flag hook | HOLD and revalidate; the proposal contains stale paths/lane language and lacks repeated-failure evidence. |
| July weekly is missing | Confirmed functional gap. Run one recovery weekly. |
| `.raw ARCHIVE` needs routing | Confirmed, but seven files are already exact duplicates. Build a manifest before moving anything. |
| Journal privacy is convention-only | Incorrect when the hardened root policy is active; conditionally true when Claude launches from a nested settings root. Fix the settings shadow, not the prose boundary. |

## What is already solid

- Universal boot chain and North Star progressive loading resolve.
- Eight hub skeletons exist: CLAUDE, HOW_TO_USE, index, log, and raw boundaries.
- Wiki live inventory counts checked for SYSTEMS/TECHNOLOGY and current stage truth
  checked for PYTHON/PHYSICS.
- Shared skill hashes match canonical plus both mirrors.
- No byte-identical duplicate live Markdown files were found outside raw/archive.
- No zero-byte live Markdown placeholders remain; PHYSICS `.gitkeep` files are
  harmless legacy scaffolding.
- No secret-like filenames were found inside the live non-journal/non-archive vault;
  the external scanner secret path exists without its contents being read.
- Current top-level North Star, strategy, capability contract, placement authority,
  and client boundary are mutually consistent.

## Recommended edit plan

### Phase 0 — stabilize Claude before more review work

1. Finish or stop the current Claude session cleanly; refresh NOW after #51.
2. Until settings are repaired, launch Claude only from `.ROOT` and verify setting
   sources.
3. Reopen semantic drift as HIGH when implementation begins, because #75 has been
   re-raised by confirmed stale live interfaces.

**Acceptance:** root settings are the active source; NOW does not name completed
calendar work; no concurrent session is editing the same targets.

### Phase 1 — close the small live contradictions

1. Fix the KSU Tracker brief.
2. Consolidate ListingOS/listing-packet status; record TCG as paused.
3. Clean the Watchtower board.
4. Run one recovery weekly.
5. Correct the Technology FORGE tense and other exact stale strings found in this
   report.

**Acceptance:** a fresh session can answer current project, path, next-action, and
strategy questions without oral history.

### Phase 2 — repair the safety and validator layer

1. Resolve/archive nested Claude settings and establish launch-independent hard
   denies with Chris approval.
2. Extend boot validation for nested settings and direct-path/project semantics.
3. Fix `wiki_lint.py` path resolution and PHYSICS exemption.
4. Add strict/baseline/JSON modes to frontmatter audit.
5. Add the read-only `root_health.py` orchestrator and canonical `root-health` skill.
6. Update session-close paths and sync mirrors.

**Acceptance:** one command returns nonzero for a real blocker; deliberate baseline
debt is reported by name/count; a test typo in an active PHYSICS link is caught; a
nested settings file fails the run.

### Phase 3 — approve and migrate the metadata model

1. Approve the two-axis timeline/stage/status schema.
2. Update WHERE_IT_GOES, START_HERE, templates, graph instructions, and audits once.
3. Generate a dry-run mapping for all 621 current findings.
4. Migrate by realm, beginning with active authority/project files and the Make.com
   corpus; verify graph behavior in Obsidian after each batch.

**Acceptance:** zero unexplained metadata findings; the "now" view is small and
actionable; stage and reference priority remain searchable without pretending to be
today's queue.

### Phase 4 — source and navigation cleanup

1. Build the `.raw ARCHIVE` manifest and Make.com disposition.
2. Route/archive the two misplaced VSM sources.
3. Replace planned broken links with explicit planned references or create them only
   when the stage becomes active.
4. Qualify ambiguous authority-bearing CASTLE links.
5. Normalize proposal metadata; leave the hook on HOLD unless evidence changes.

**Acceptance:** every source set has an owner/evidence home; selective indexes say
they are selective; no live clickable link is knowingly broken without an explicit
planned marker.

## Recommended lead and validation

Use one local implementation surface for the coherent patch set, not simultaneous
Claude/Codex edits to the same files. The best sequence is:

1. Chris approves the plan and the configuration/governance scope.
2. One local agent implements phase by phase with preserved before-states.
3. A different surface independently reviews the diffs and acceptance output.
4. Test Claude from `.ROOT` and one formerly problematic subfolder in fresh sessions.

The first exact action is **not another broad rewrite**. It is to finish the current
Claude session, refresh NOW, and then fix the launch-directory settings shadow before
trusting further audit automation.

## Implementation verification note — July 15, 2026

Phase 1 rechecked this report's settings diagnosis against Claude Code 2.1.210 and
the current official documentation. The docs support the reported settings scopes,
deny → ask → allow precedence, and source-relative file-rule paths, but they do not
support the report's stronger wording that project settings use the current working
directory with “no parent-directory fallback.” Treat that causal statement as
unproven rather than as current documentation.

The correction does not change the remediation decision: user-scope `~/.ROOT/...`
denies provide the launch-independent boundary; one tracked root project file owns
`.ROOT` policy; and nested settings copies are prohibited because they create hidden,
ignored configuration drift. A second correction is also material: Claude's
operating-system sandbox is not available on native Windows. File-tool permission
denies remain enforced by Claude Code, but arbitrary subprocess file access is not
OS-sandboxed there. Fresh-session `/status` and `/permissions` checks remain the
required human behavior test.
