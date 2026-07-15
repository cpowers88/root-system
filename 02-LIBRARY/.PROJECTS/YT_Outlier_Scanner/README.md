---
type: project
timeline: now
status: active
tags: [business, revenue, programming]
---

# YT Outlier Scanner — Lane A Research Tool
### Created July 14, 2026 | Owner: Chris | Status: live discovery verified; selftest PASS
### Charter: `03-WIKIS\REVENUE_LAB\` Lane A research phase ONLY — produces a niche
### shortlist; no channel, posting, or monetization decision comes from this tool.

## What It Does

Finds **breakout videos**: each video's views divided by its own channel's
median views, computed **separately for Shorts and long-form** (Shorts view
counts include starts/replays since March 2025 — mixing formats would poison
the median). A high ratio means *that specific video* broke out, not just
"big channel." Repeated breakout patterns across a niche = the replicable
signal worth studying.

The wide-net `discover` command also stores recent topic results. The offline
`topic-report` command ranks one exact stored keyword by total views,
views/subscriber (`breakout`), or measured snapshot velocity.

The broader `market-report` command combines the defined desk-based research
universe, deduplicates videos returned by multiple searches, preserves their
matched topics/categories, and ranks the overall pool. Its default `strict`
mode applies transparent title checks to obvious search noise; use
`--relevance raw` to audit every stored API candidate.

## One-Time Setup (Chris, ~5 minutes)

1. Go to https://console.cloud.google.com/ (sign in with your normal Google
   account) → project picker (top bar) → **New Project** → name it
   `yt-outlier-scanner` → Create.
2. With that project selected: **APIs & Services → Library** → search
   **"YouTube Data API v3"** → Enable.
3. **APIs & Services → Credentials → + Create Credentials → API key.**
   Copy the key. (Optional hardening: click the key → "Restrict key" →
   API restrictions → YouTube Data API v3 only.)
4. Outside the `.ROOT` vault, create
   `C:\Users\chris\.root-secrets\YT_Outlier_Scanner.env` containing exactly one line:
   ```
   YOUTUBE_API_KEY=paste-your-key-here
   ```
   The scanner loads this external file automatically. Never place the key inside
   `.ROOT`, even in a gitignored file.

**Cost: $0 under the default YouTube Data API quota.** No paid tool or billing
change is part of this project. Under Google's June 2026 granular model,
`search.list` has a separate default allowance of 100 calls/day, with each call
costing one unit in that bucket. Other read requests use the general default
10,000-unit/day bucket. Google Cloud Console remains the usage source of truth.

The API key is already configured locally for the verified scanner. Keep the
external secret file private and never show it in recordings, screenshots, output,
the vault, or commits.

## Usage

```
python scanner.py discover --keywords "Claude Code tutorial" --days 180
python scanner.py discover --market --days 180
python scanner.py market-report --top 100 --rank views
python scanner.py market-report --top 100 --rank breakout --format long
python scanner.py market-report --category software_tutorials
python scanner.py market-report --relevance raw --top 20
python scanner.py topic-report "Claude Code tutorial" --rank views
python scanner.py topic-report "Claude Code tutorial" --rank breakout
python scanner.py topic-report "Claude Code tutorial" --rank velocity
python scanner.py topic-report "Claude Code tutorial" --format long
python scanner.py add-channel @SomeHandle --niche trades
python scanner.py harvest                 # pulls uploads + stats for all channels
python scanner.py report                  # niche breakout rates + top outliers
python scanner.py report --niche trades --top 30
python scanner.py selftest                # offline logic check (no key needed)
```

Seed channel candidates live in [channels_seed.md](channels_seed.md) — confirm them
WITH Chris, by niche, before the next harvest.

### Offline and network boundaries

- `market-report`, `topic-report`, `report`, and `selftest` are local-only. They
  do not load the API key and do not make network requests.
- The market universe currently has 36 documented topics across practical AI,
  software tutorials, software/app reviews, small-business AI, and adult-facing
  family technology. `discover --market` uses two Search calls per topic, or 72
  of the separate 100-call daily default.
- `market-report` returns up to 100 deduplicated rows by default. The same video
  can preserve multiple matched topics without appearing multiple times.
- `topic-report` returns up to 100 rows by default. Use `--top N` for a smaller
  review slice. If fewer than 100 rows are stored, it returns everything
  available without padding or invented data.
- `discover`, `add-channel`, and `harvest` call the YouTube Data API and require
  the locally stored key.
- Every successful `discover` refresh updates the latest `discoveries` row and
  appends a real observation to `discovery_snapshots`.
- Measured velocity is `(latest views - earliest views) / elapsed days`. It is
  shown only when two observations are at least 24 hours apart. Until then it is
  `n/a`; lifetime average views/day is never substituted.
- Quota output reports Search calls and other-read units separately.

## Method Notes (honest limits)

- **Outlier metric:** views ÷ channel-format median. Needs ≥8 videos per
  channel per format (`--min-videos`) or that cohort is skipped.
- **Shorts heuristic:** duration ≤ 180s. Imperfect (some long-form is short);
  good enough for research ranking, not for publication claims.
- **Views ≠ revenue.** RPM varies by niche and is Tier 2 data at best (see
  [lane-a-content-channel.md](../../../03-WIKIS/REVENUE_LAB/wiki/lane-a-content-channel.md)).
  This tool ranks attention patterns; the revenue question stays with the
  REVENUE_LAB scorecard.
- **Recency bias:** a 2-week-old video hasn't finished accumulating views;
  compare videos of similar age when reading the report.
- **Search is a sample, not a census.** Relevance results can be noisy and need
  human classification before any content decision.
- **Strict relevance is a first pass, not truth.** It checks stored titles for
  topic-specific terms and removes known ambiguous matches (for example,
  Minecraft obsidian results). It cannot verify the full video's substance.
  `--relevance raw` keeps the unfiltered candidate pool auditable.
- **Review-only charter:** findings support an internal proof and later CASTLE
  review. They do not authorize an account, publishing, monetization, affiliate
  links, outreach, paid tools, or child-directed content.

## Files

- `scanner.py` — single-file stdlib-only tool (no venv, no dependencies)
- `scanner.db` — SQLite data (generated; gitignored)
- `discovery_snapshots` — append-only observations inside `scanner.db`
- `C:\Users\chris\.root-secrets\YT_Outlier_Scanner.env` — external API key file;
  intentionally outside this vault and project
- [channels_seed.md](channels_seed.md) — niche/channel working list
- [PRIVATE_PROOF_OUTLINE.md](PRIVATE_PROOF_OUTLINE.md) — internal 8–12 minute walkthrough plan
