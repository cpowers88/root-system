---
type: source-summary
status: parked
source_role: reference
difficulty: post-stage-10
source_file: raw/books/PracticalSQL.pdf
tags: [reference, programming, parked, sql-strand]
---

# Practical SQL: Working with Dates and Times

**Summary**: The four datetime data types and their extraction/construction functions (`date_part()`, `make_date()`/`make_timestamptz()`), managing PostgreSQL session time zones and the `AT TIME ZONE` keywords, and performing date/interval arithmetic — demonstrated finding hourly ridership and trip-time patterns in NYC taxi data and calculating multi-segment, multi-timezone Amtrak trip durations with `justify_interval()`.

**Sources**: PracticalSQL.pdf (Anthony DeBarros, 2nd ed., 2022), Chapter 12 ("Working with Dates and Times")

**Last updated**: 2026-06-20

---

## The Four Datetime/Interval Types (Review and Extension)

`timestamp` (with `timestamp with time zone`/`timestamptz` strongly preferred — without it, times from different locations can't be compared), `date` (date only; the ISO 8601 `YYYY-MM-DD` format is the recommended, internationally unambiguous choice), `time` (time only; `time with time zone`/`timetz` is **discouraged** since a time zone is meaningless without an accompanying date), and `interval` (a duration, e.g. `12 days`, with no fixed start/end point). The first three are *datetime types* (their values are *datetimes*); `interval` is the lone *interval type*. All four correctly handle calendar nuances — PostgreSQL rejects June 31 and only allows February 29 in leap years.

## Extracting and Constructing Datetime Values

`date_part('unit', value)` pulls a single component (`year`, `month`, `day`, `hour`, `minute`, `seconds`, `timezone_hour`, `week`, `quarter`, `epoch`) out of a date/time/timestamp — the standard tool whenever an analysis needs to group or filter by just one piece of a timestamp (e.g., by hour of day). `epoch` returns seconds elapsed since 1970-01-01 00:00 UTC — useful for absolute numeric comparison between two timestamps, but **subject to floating-point imprecision and the looming "Year 2038 problem"** where the value grows too large for some systems. ANSI-standard `extract(unit FROM value)` does the same job and is preferred for cross-database portability (notably absent from Microsoft SQL Server), though `date_part()`'s name is more self-documenting.

`make_date(year, month, day)`, `make_time(hour, minute, seconds)`, and `make_timestamptz(year, month, day, hour, minute, second, time_zone)` build a datetime value from separate integer components — useful whenever a source dataset stores year/month/day in separate columns rather than one combined date field. `current_setting('timezone')` can be passed directly into `make_timestamptz()`'s time-zone argument to default to the session's own zone.

## Retrieving the Current Date and Time

`current_timestamp` (PostgreSQL shorthand `now()`) returns the timestamp **with** time zone at query start; avoid `localtimestamp` (no time zone — meaningless across locations) and `localtime`. **All of these are fixed at the start of the query/transaction** — every row in a 100,000-row update gets the identical timestamp. The PostgreSQL-specific `clock_timestamp()` instead records the actual elapsed clock time at each row, useful when you genuinely need a distinct per-row timestamp, at some performance cost on large operations.

## Working with Time Zones

`SHOW timezone;` or `SELECT current_setting('timezone');` reveals the session's active time zone. `SELECT * FROM pg_timezone_names` / `pg_timezone_abbrevs` lists every valid zone name/abbreviation with its current UTC offset and daylight-saving status — a faster lookup than searching the web. `SET TIME ZONE 'zone_name';` changes the *session's* time zone (not the server's permanent `postgresql.conf` setting) — this governs how `timestamptz` values are displayed and how time-zone-less input gets interpreted, **but the underlying stored value is always UTC internally** — only the display changes. The `AT TIME ZONE 'zone_name'` keywords let you view a single value through a different zone's lens without altering the session setting at all — handy for one-off comparisons.

## Date/Time Arithmetic

Standard math operators work on datetimes and intervals: subtracting one `date` from another returns an integer day-count; subtracting one `timestamp` from another returns an `interval`; adding an `interval` to a `date`/`timestamp` returns a new datetime. **Time-zone awareness is essential for correct interval math** — subtracting two `timestamptz` values correctly accounts for any time-zone difference between them, while plain `timestamp` (no zone) would silently produce a wrong duration if the two values came from different zones.

## Applied: NYC Taxi Ridership Patterns

Using `date_part('hour', pickup_timestamp)` grouped and counted, hourly taxi pickup volume on a sample day showed a clear pattern — lowest overnight (2-5 AM), a sharp morning rise (5-8 AM), a relatively flat midday, and a second evening peak (6-10 PM) — exported to CSV and charted in Excel for a clearer visual read than the raw table. A separate query computing **median** trip duration per pickup hour (via `percentile_cont(.5) WITHIN GROUP (ORDER BY dropoff - pickup)`, reusing Chapter 6's median technique) found the longest median trips occurred around 1 PM (15 minutes) and the shortest in the early morning — consistent with traffic-driven trip-time variation. **Both findings illustrate the same underlying lesson: a question this specific ("when are trips longest, not just most frequent") needs a deliberately chosen statistic (median trip duration by hour), not just a raw count.**

## Applied: Multi-Timezone Trip Duration (Amtrak)

A six-segment cross-country train route, with each `departure`/`arrival` timestamp entered in its *local* time zone (`timestamptz`), demonstrates why time-zone-aware storage matters for duration math: subtracting `arrival - departure` per segment correctly returns the true elapsed travel time even when a segment crosses time zones — a plain `timestamp` would silently misstate the duration in that case. `to_char(timestamp, format_string)` (PostgreSQL-specific) formats a timestamp into a custom display string (e.g., `'YYYY-MM-DD HH12:MI a.m. TZ'`).

Summing per-segment intervals with a window function (`sum(arrival - departure) OVER (ORDER BY trip_id)`) for a cumulative running total produces an **awkward, hard-to-read result** — PostgreSQL tracks the day-portion and the hour/minute-portion of summed intervals separately, so a true 5-day-13-hour total displays as the confusing "2 days 85:47:00." **`justify_interval()` wrapped around the sum normalizes this** — rolling every full 24-hour block up into the days value (and every 30-day block into months) — turning "2 days 85:47:00" into the correct, readable "5 days 13:47:00."

## Key Takeaways

- Always store and work with `timestamptz`, never bare `timestamp`, for any event whose date/time will ever be compared across locations or summed across time-zone boundaries — the stored value is always UTC internally regardless of display setting, but only `timestamptz` carries the offset needed for correct math.
- `date_part()`/`extract()` is the standard way to group or filter by a single component (hour, day of week, month) of a timestamp — the go-to technique for "what time of day/week/year does X happen most" questions.
- `SET TIME ZONE` changes only the current session's display/interpretation, not the underlying data or the server's permanent configuration — safe to experiment with.
- When summing `interval` values with a window function, wrap the result in `justify_interval()` to get a readable, properly rolled-up days/hours/minutes total instead of PostgreSQL's separately-tracked day/time components.

## Connects to

- [[sql-data-types]] — extends Chapter 4's introduction of the four datetime/interval types directly into their manipulation functions and time-zone mechanics.
- [[sql-basic-math-and-stats]] — the median-trip-duration-by-hour query reuses percentile_cont() from Chapter 6 verbatim, applied to an interval rather than a numeric column.
- [[sql-statistical-functions]] — the cumulative-duration window-function pattern (sum() OVER (ORDER BY ...)) is the same window-function syntax introduced for rank()/dense_rank() and rolling averages in Chapter 11, applied here to interval arithmetic.

## Pathway Placement

- **Role**: reference for the parked **SQL-fundamentals strand** (candidate Stage 10 extension — see `wiki/source-map.md`).
- **Prerequisites**: [[stages/stage-10-application-thinking]]'s databases intro ([[concepts/databases-and-sqlite]]).
- **Caution**: this book's examples are PostgreSQL; the vault's Stage 10 path uses SQLite. Core syntax overlaps, but PostgreSQL-specific pieces (`ILIKE`, `percentile_cont`, `crosstab()`, serial types, pgAdmin workflow) do not transfer 1:1.
- **Status**: parked per [[parking-lot]]. Not part of the active Stage 0-10 path — wait for Chris's go-ahead to build the strand.
