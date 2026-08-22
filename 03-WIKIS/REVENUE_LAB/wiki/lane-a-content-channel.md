---
type: reference
tags: [business, revenue]
timeline: now
---

# Lane A — Content Channel, Data-Driven (YouTube / TikTok)
### Evidence page | Scan Session 2 — July 14, 2026 | Status: EVIDENCE GATHERED, scored

## The Hypothesis

High-view content can be systematically identified from public platform data
and replicated in a niche where Chris's knowledge and lifestyle fit; the
audience compounds into every other lane (leads, trust, collabs, products).

## Tier 1 Evidence — Monetization Mechanics (platform primary sources)

- **[YouTube Partner Program](https://www.youtube.com/creators/earn/youtube-partner-program/):**
  full ad revenue requires **1,000 subscribers + 4,000 public watch-hours
  (past 12 months) OR 10M Shorts views (90 days)**, then a ~1-month review.
  A lower 500-subscriber tier unlocks fan-funding only.
- **[TikTok Creator Rewards Program](https://support.tiktok.com/en/business-and-creator/creator-rewards-program/creator-rewards-program):**
  requires **10,000 followers + 100,000 views in the last 30 days**; only
  videos **≥60 seconds** qualify; a video needs 1,000+ qualified views before
  it earns anything.
- **[YouTube Data API v3 quota](https://developers.google.com/youtube/v3/determine_quota_cost):**
  **free 10,000 units/day**; `videos.list` (includes full view/like statistics)
  costs **1 unit**, `search.list` costs 100. → The systematic data scan is
  genuinely free at research scale if designed around cheap endpoints.

## Tier 2 Evidence — What the Views Actually Pay

- Long-form YouTube RPM (revenue per 1,000 views): **$2–8 global average**;
  finance $8–20, tech $4–8, education $2.75–5.50
  ([multi-channel RPM data](https://air.io/en/air-data-findings/youtube-shorts-rpm-vs-long-form-how-much-do-shorts-earn-in-2026)).
- **Shorts RPM: $0.03–0.08** — 3–14% of long-form; it takes ~11,000–34,000
  Shorts views to earn what 1,000 long-form views earn.
- TikTok Creator Rewards RPM: **$0.40–1.20**, higher for finance/tech/business
  content ([program guides](https://postlinkapp.com/blog/tiktok-creator-rewards-program)).

## The Honest Math (survival-lane test)

- $500/month from long-form ads at a $4 RPM requires **~125,000 views/month,
  every month** — after first clearing the eligibility bar and review.
- Chris's stated aspiration (1M views weekly) at TikTok's $0.40–1.20 RPM ≈
  $1,600–4,800/month **if achieved** — and view outcomes are not schedulable.
  The median new channel earns ~$0 for months.
- Realistic time-to-first-ad-dollar: **4–8+ months**. Earlier revenue for
  small channels comes from sponsorship/affiliate/leads — which are also
  audience-dependent.
- **Conclusion the numbers force: Lane A cannot be the survival lane.** It is
  a legitimate compounding lane — the only lane whose asset (audience) feeds
  all four North Star asset classes.

## The Data Scan IS Buildable (Chris's core question — answered yes)

The "systematically break down what gets views" analysis is a real, free,
legal data project on public data:

1. **Harvest cheap:** for candidate niches, pull channels' full upload lists
   via `playlistItems.list` (1 unit) and batch statistics via `videos.list`
   (1 unit per 50 videos). ~10k units/day ≈ hundreds of channels, thousands
   of videos daily — no scraping, no ToS gray zone.
2. **The outlier metric:** a video's views ÷ its own channel's median views.
   That separates "big channel" from "this specific video broke out" — the
   replicable signal Chris is after.
3. **Store in SQLite, analyze in Python** — the same stack as the KSU tracker.
   This is permanent-capability work (APIs, SQL, data analysis) even if the channel
   verdict is "not yet." The no-orphan test passes twice.
4. Output: a niche shortlist where outlier-rate is high AND Chris has real
   material (construction knowledge, build-in-public .ROOT/ISYE story,
   large-family life) AND RPM is decent.

*Charter note: enabling the API needs a Google Cloud project key on Chris's
existing Google account — account-adjacent, so it gets Chris's explicit OK
before Session 3 builds anything.*

## Rubric Scores (1–5)

| Criterion | Score | Justification |
|---|---|---|
| Time-to-first-dollar | **1** | 4–8+ months realistic; eligibility bars + unschedulable virality |
| Daily-footprint fit | **4** | Records what already happens (PC, builds, study, family range); hidden cost is editing hours — must be budgeted, not ignored |
| Skill overlap | **5** | The data scan is a real Python/SQL/API project; on-camera reps serve the communication-development goal |
| Compounding | **5** | Audience is the definitive compounding asset; feeds leads, trust, collabs, products — all four asset classes |
| Variance | **1** | Extreme — median outcome near $0 for months; upside real but not plannable |
| **Total** | **16/25** | Wrong survival lane, right compounding lane |

## Open Items Before the Scorecard

- Chris's OK to create the YouTube Data API key (account-adjacent action).
- Niche candidates to seed the scan (working list: contractor/trades education,
  build-in-public AI-systems/student story, large-family life — pick by data).
- Editing-time budget: what's the realistic hours-per-video Chris can sustain
  during the semester? The footprint score holds only if this stays small.

## Independent Evidence Audit — July 14, 2026 (Codex)

The initial Session 2 research is retained above. This pass corrects the
platform facts and separates platform requirements from revenue forecasts.

### Verified / Corrected Platform Facts

- Full ad revenue requires **1,000 subscribers plus 4,000 valid public watch
  hours in 12 months, or 10M valid public Shorts views in 90 days**. The lower
  expanded-YPP tier requires **500 subscribers, three public uploads in 90 days,
  and 3,000 watch hours or 3M Shorts views**; it enables fan funding and selected
  Shopping features, not ad revenue.
- The default Data API allocation remains **10,000 units/day** for most reads;
  `videos.list` and `playlistItems.list` cost 1 unit, and `videos.list` supports
  up to 50 video IDs in a request.
- `search.list` no longer costs 100 units. It has a **separate 100-call daily
  bucket**, at 1 point per call. The practical scan design is to seed known
  channel IDs and spend search calls only to expand the candidate set.
- Since March 31, 2025, a Short's public `viewCount` includes starts and replays
  without a minimum watch-time requirement. Analyze Shorts and long-form content
  separately; a combined outlier metric would mislead.

### Forecast Claims Not Yet Evidenced

Third-party RPM ranges, the 4–8+ month first-ad-dollar estimate, and monthly
view/revenue arithmetic are planning assumptions, not platform facts. TikTok
eligibility establishes a high threshold; its payout range needs a more credible,
platform-transparent source before it can affect the scorecard.

### Revised Provisional Rubric (evidence-only)

| Criterion | Score | Evidence-based reason |
|---|---:|---|
| Time-to-first-dollar | **1** | high thresholds are verified; time to reach them is unknown |
| Daily-footprint fit | **2** | document-existing-work is promising, but editing/consistency cost is untested |
| Skill overlap | **5** | API, Python, SQL, and analysis directly strengthen the permanent capability base |
| Compounding | **5** | an audience can become durable owned distribution if it gains traction |
| Variance | **1** | thresholds and no personal performance data make this highly uncertain |
| **Total** | **14/25** | a capability-compounding experiment, never survival income |

### Sources Checked

- [YouTube — Expanded Partner Program](https://support.google.com/youtube/answer/13429240)
- [YouTube — Partner Program Eligibility](https://support.google.com/youtube/answer/72851)
- [YouTube Data API — Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost)
- [YouTube Data API — videos.list](https://developers.google.com/youtube/v3/docs/videos/list)
- [YouTube Data API — playlistItems.list](https://developers.google.com/youtube/v3/docs/playlistItems/list)

### July 14 Market-Claim Clipping — Input, Not Proof

`raw/19 Most Profitable YouTube Niches 2026 (Real RPM Data).md` is an
OutlierKit vendor article that claims niche RPM/CPM ranges and describes an
outlier-detection method. It does not expose the underlying creator dashboards
or a reproducible dataset, and it sells the named analysis tool. Preserve it as
a Tier 3 market hypothesis/source lead only: it may suggest categories for the
scanner, but it does not change the scorecard, validate RPM, or justify a
channel decision. Any useful claim must be reproduced from public API data or
verified against a traceable primary source.
