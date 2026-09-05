---
type: reference
title: "FRED datasets — ECON 1000 dataset prep"
created: 2026-07-21
description: "Four real FRED (Federal Reserve Economic Data) series pulled via the FRED API, matched to ECON 1000's core macro topics."
tags: [economics, dataset, econ-1000]
timeline: reference
---

# FRED Datasets — ECON 1000

Pulled directly from the FRED API (Federal Reserve Bank of St. Louis),
2026-07-21, via `FRED_API_KEY` stored outside the vault at
`C:\Users\chris\.root-secrets\FRED.env` (never committed, never placed in
`.ROOT`). Public-domain data; attribute as "Source: FRED, Federal Reserve
Bank of St. Louis" when used.

| File | Series | Covers | Observations |
|---|---|---|---|
| `GDP.csv` | Gross Domestic Product (nominal, quarterly, billions $) | 1947-01-01 to 2026-01-01 | 317 |
| `GDPC1.csv` | Real GDP (chained 2017 dollars, quarterly) | 1947-01-01 to 2026-01-01 | 317 |
| `CPIAUCSL.csv` | Consumer Price Index, All Urban Consumers (monthly) | 1947-01-01 to 2026-06-01 | 953 |
| `UNRATE.csv` | Unemployment Rate, seasonally adjusted (monthly) | 1948-01-01 to 2026-06-01 | 941 |

Each file is two columns: `date`, `value`. Missing/withheld observations
(FRED's `.` placeholder) are already filtered out.

## Why these four

Matched directly to ECON 1000's confirmed syllabus topics: GDP & economic
growth (`GDP`, `GDPC1`), inflation (`CPIAUCSL`), unemployment (`UNRATE`) —
see `03-WIKIS\EDUCATION\wiki\fall-2026-course-briefs.md`. Also usable as
real-data reps for the SQL and data-visualization capability lines tracked
in `00-BRAIN\CASTLE\wiki\current-position.md` (July weak links #1 and #4),
independent of the ECON coursework itself.

## Refreshing

`00-BRAIN\scripts\fetch_fred.py` reads the key from the external `.env` and
re-fetches all four series; re-run it any time to get current data instead
of manually re-downloading.
