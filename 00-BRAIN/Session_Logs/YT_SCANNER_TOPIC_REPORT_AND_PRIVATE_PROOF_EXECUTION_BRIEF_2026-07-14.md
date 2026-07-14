---
type: execution-brief
status: approved
tags: [now, revenue, youtube, scanner, claude-code]
created: 2026-07-14
execution-owner: Claude Code
---

# YT Scanner Topic Report + Private Proof — Execution Brief

## Objective

Advance the Chris-approved practical AI/software tutorial path through two
bounded internal proofs:

1. Upgrade the existing scanner so a topic can be ranked without manual SQL by
   total views, views/subscriber, and measured view velocity after repeat
   snapshots.
2. Prepare one private 8–12 minute tutorial proof from work already completed:
   **How I used Claude Code, Python, SQLite, and the free YouTube API to find
   breakout videos.**

This brief does not authorize a channel, account creation, publishing,
monetization, affiliate links, outreach, paid tools, or child-directed content.

## Phase, Service, Proof, and Displacement

- **Phase:** Foundation / active Revenue Lab Lane A validation, July–August 2026.
- **Service unlocked:** evidence-based technical education that can later support
  owned distribution and the advisor-builder service path.
- **Proof project:** generate an exact top-ten topic report, then make one private
  scanner walkthrough and record total added production minutes.
- **Displacement:** the weekly scan replaces the existing 30-minute technology-
  landscape rep; the private proof replaces one Python/SQL/communication rep and
  is capped at 90 added minutes.

## Scope

### In scope

- `02-LIBRARY\.PROJECTS\YT_Outlier_Scanner\scanner.py`
- `02-LIBRARY\.PROJECTS\YT_Outlier_Scanner\README.md`
- One new private-proof outline in the scanner project folder.
- SQLite schema migration using `CREATE TABLE IF NOT EXISTS`; preserve all data.
- Offline tests and one bounded live verification using the existing free API key.

### Out of scope

- Publishing or creating a YouTube/social account.
- Filming or editing the private proof on Chris's behalf.
- Copying another creator's script, title, thumbnail, or footage.
- AI-generated mass-content workflows.
- Paid software, quota extensions, billing changes, or new credentials.
- Any read of `88-JOURNAL` or write to a `raw\` folder.

## Preconditions

1. Read live `scanner.py` and `README.md` before editing.
2. Preserve `.env` and never print, log, copy, or commit the API key.
3. Preserve `scanner.db`; schema changes must be additive and non-destructive.
4. Confirm the report at
   `03-WIKIS\REVENUE_LAB\wiki\yt-outlier-scanner-first-findings-2026-07-14.md`
   remains the decision source.

## Required Changes

### 1. Add an offline `topic-report` command

Target interface:

```text
python scanner.py topic-report "Claude Code tutorial" --top 10 --rank views
python scanner.py topic-report "Claude Code tutorial" --top 10 --rank breakout
python scanner.py topic-report "Claude Code tutorial" --top 10 --rank velocity
```

Options:

- `keyword` — exact stored discovery keyword.
- `--top N` — default 10.
- `--rank views|breakout|velocity` — default `views`.
- `--format all|long|short` — default `all`.

Output fields: rank, exact video title, channel, publish date, format, current
views, subscriber count when public, views/subscriber, and measured views/day
when available. If the exact keyword is absent, print available stored keywords
and exit cleanly. This command must not load an API key or use the network.

### 2. Preserve discovery snapshots

Current state: `discoveries` uses `(video_id, keyword)` as its primary key and
`INSERT OR REPLACE`, so each refresh overwrites the prior observed view count.

Add an append-only `discovery_snapshots` table with at least:

```text
video_id, keyword, observed_at, views, subscriber_count
```

Use a primary key that permits repeat observations while preventing duplicate
rows from the same run. Every successful `discover` run must update the latest
row in `discoveries` and append one snapshot.

Velocity definition:

```text
(latest_views - earliest_views) / elapsed_days
```

Require two snapshots separated by at least 24 hours. Until then, display
`n/a`; do not substitute lifetime average views/day and call it velocity.

### 3. Correct quota accounting for the June 2026 granular model

Current text/code incorrectly treats `search.list` as 100 units per call in the
general 10,000-unit bucket. Google now documents a separate default bucket of
100 `search.list` calls/day, with each call costing 1 unit in that bucket; other
read endpoints remain in the general 10,000-unit/day bucket.

Replace the single `QUOTA_USED` presentation with separate counters, for example:

```text
Search calls this run: 8 / 100 daily default
Other read units this run: 16 / 10,000 daily default
```

Source of truth:
`https://developers.google.com/youtube/v3/determine_quota_cost`

### 4. Update usage documentation

Current README status says `awaiting API key` and omits `discover` even though
the key exists and live discovery scans succeeded. Update status and usage to
document `discover`, `topic-report`, offline/network boundaries, snapshot
velocity, separate quota buckets, and the review-only charter.

### 5. Prepare the private-proof outline

Create:
`02-LIBRARY\.PROJECTS\YT_Outlier_Scanner\PRIVATE_PROOF_OUTLINE.md`

It must contain:

- Audience: a beginner who wants to research a YouTube topic without paid tools.
- Promise: build/use a free local scanner to find exact top videos and reachable
  small-channel breakouts.
- 8–12 minute structure: problem, free stack, one command, exact result, what the
  metrics mean, limitations, close.
- Screen list: terminal command, topic report, SQLite location, report artifact.
- Privacy checklist: `.env` never visible; no API key; no private vault content;
  no school submission material; use a clean terminal working directory.
- Production timer fields: preparation, recording, editing, total added minutes.
- Accuracy rule: demonstrate only behavior verified in the live tool.

Do not draft a copied title or thumbnail. Provide three original working-title
options based on the actual proof and mark them `internal only`.

## Exact Implementation Order

1. Record `git status --short` and preserve unrelated work.
2. Run `python scanner.py selftest` before edits.
3. Add snapshot schema and storage path.
4. Add pure query/ranking helpers and `topic-report` CLI.
5. Correct quota counters and messages.
6. Extend selftest with synthetic discovery + two-snapshot cases.
7. Update README.
8. Create the private-proof outline.
9. Run all acceptance checks.
10. Return a concise validation report; do not publish anything.

## Acceptance Checks

1. `python scanner.py selftest` passes and now covers:
   - existing channel-format median behavior;
   - exact topic lookup;
   - views ranking;
   - breakout ranking;
   - velocity unavailable with one snapshot;
   - velocity correct with two snapshots at least 24 hours apart.
2. Existing commands still work: `discover`, `add-channel`, `harvest`, `report`.
3. `topic-report "Claude Code tutorial" --top 10 --rank views` reproduces the
   stored top-ten ordering led by `What is Claude Code?` without network access.
4. `topic-report ... --rank velocity` prints `n/a` until a qualifying second
   snapshot exists.
5. A bounded live discovery run prints separate Search and other-read counters.
6. `scanner.db` retains existing `channels`, `videos`, and `discoveries` rows.
7. `.env` remains ignored and its value never appears in output, diffs, logs,
   reports, or the private-proof outline.
8. `git diff --check` passes for touched tracked files.

## Stop Conditions

Stop and report rather than improvising if:

- migration would delete or rebuild existing scanner data;
- the API key appears in any output or diff;
- Google returns a quota/billing error;
- accurate velocity would require invented or backfilled historical values;
- implementation expands beyond the files and behavior named here;
- the private proof would expose private vault, family, credential, or protected
  academic material.

## Archive Actions

None. Update the live project files in place; do not create duplicate copies.

## Return Report Format

- Files changed.
- Commands run and pass/fail results.
- Schema migration result and row-count preservation.
- Exact example `topic-report` output summary.
- Quota counter verification.
- Private-proof outline path.
- Remaining blocker or `none`.
- Explicit statement: no account, publishing, monetization, outreach, or paid
  action occurred.

## Skill and Tool Candidates

- **Candidate:** technical tutorial production
  - `execution-owner: Claude Code`
  - Location: this private proof and future validated content workflow.
  - Recommended output type: CASTLE skill page only if the private proof stays
    within the 90-minute cap and Chris approves recurring use after review.
  - Proposed destination:
    `00-BRAIN\CASTLE\wiki\skills\technical-tutorial-production.md`
  - Current action: proposal only; do not create the skill page yet.
