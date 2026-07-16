---
type: reference
timeline: now
status: ready-for-local-rep
tags: [technology, business-intelligence, looker-studio, youtube]
---

# Looker Studio Market Export - Field Dictionary

**Dataset**: `LOOKER_STUDIO_MARKET_DATA.csv` (100 deduplicated rows)

**Boundary**: Mechanical scanner evidence only. Search categories and
matched topics record query provenance; they are not human relevance,
niche, revenue, demand, or publishing judgments.

## Generation Record

- Database: `scanner.db`
- Ranking: `views`
- Format: `all`
- Category filter: `all`
- Relevance gate: `strict`
- Topic coverage: `36/36`
- Deduplicated candidates before top-N: `2113`
- Latest stored observation: `2026-07-14 19:23:53Z`

## Fields

| Field | Looker Type | Meaning / caution |
|---|---|---|
| `rank` | Number | Position under the selected export ranking. |
| `video_id` | Text | Stable YouTube identifier; use as the row key. |
| `video_url` | URL | Direct source link. |
| `title` | Text | Exact stored title; spreadsheet-formula prefixes are neutralized. |
| `channel` | Text | Exact stored channel title. |
| `published_date` | Date | ISO `YYYY-MM-DD`; confirm Looker recognizes it as Date. |
| `format` | Text | `long` or heuristic `short` (duration at most 180 seconds). |
| `views` | Number | Latest stored view count, not revenue or demand. |
| `subscribers` | Number | Latest public channel count; blank when hidden/unavailable. |
| `views_per_subscriber` | Decimal | Views divided by subscribers; blank when unavailable. |
| `measured_views_per_day` | Decimal | Snapshot velocity; blank until observations span 24 hours. |
| `search_categories` | Text | Pipe-separated search provenance, not classification. |
| `matched_search_topics` | Text | Pipe-separated exact queries returning the video. |
| `category_count` | Number | Number of market categories returning the video. |
| `topic_count` | Number | Number of exact queries returning the video. |
| `ranking_metric` | Text | Export control: `views`, `breakout`, or `velocity`. |
| `relevance_gate` | Text | `strict` title screen or unfiltered `raw`. |
| `latest_observation_utc` | Date & Time | Freshness marker for stored evidence. |

## First Bounded Dashboard Rep

1. Import the CSV into a private Google Sheet; do not publish it.
2. Connect that Sheet to a private Looker Studio report.
3. Confirm the field types above before building charts.
4. Add one scorecard for row count, one bar chart for views by search
   category, and one table with title, format, views, views/subscriber,
   topic count, and source URL.
5. Add a format filter and a published-date control.
6. Record what the dashboard makes easier to notice than the worksheet.

Do not infer income, market demand, or a channel decision from this rep.
Its proof target is basic data connection, field typing, filtering, and
clear presentation of already-collected evidence.
