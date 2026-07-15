#!/usr/bin/env python3
"""YT Outlier Scanner — Lane A research tool (REVENUE_LAB).

Finds breakout videos: a video's views divided by its own channel's median
views for the same format (Shorts and long-form are always analyzed
separately — Shorts view counts include starts/replays since March 2025 and
would poison a combined median).

Approved: July 14, 2026 (Chris; CASTLE gate conditional pass — research only,
no channel/posting decisions come from this tool, only a niche shortlist).

Stdlib only. YouTube's June 2026 granular quota model gives search.list a
separate default bucket of 100 calls/day; ordinary read requests use the
general default bucket of 10,000 units/day.

Usage:
  python scanner.py discover [--keywords "a,b,c"] [--days 180]
  python scanner.py topic-report "Claude Code tutorial" --rank views
  python scanner.py discover --market [--days 180]
  python scanner.py market-report --top 100 --rank views
  python scanner.py add-channel @SomeHandle --niche trades
  python scanner.py add-channel UCxxxxxxxxxxxxxxxxxxxxxx --niche family
  python scanner.py harvest [--max-videos 200]
  python scanner.py report [--niche trades] [--top 20] [--min-videos 8]
  python scanner.py selftest        # offline check of DB + math, no network

Discover = wide-net niche scan: recent winners per keyword + views/subscriber
breakouts from small channels. It nominates niches and channel candidates;
adding a channel for deep harvest stays a human (Chris) decision.

Setup: set the YOUTUBE_API_KEY environment variable or store it in
~/.root-secrets/YT_Outlier_Scanner.env (outside the .ROOT vault).
"""

import argparse
import json
import os
import re
import sqlite3
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SECRET_FILE = Path.home() / ".root-secrets" / "YT_Outlier_Scanner.env"
DB_PATH = HERE / "scanner.db"
API_BASE = "https://www.googleapis.com/youtube/v3"
SHORT_MAX_SECONDS = 180  # heuristic; Shorts may be up to 3 minutes
OUTLIER_THRESHOLD = 3.0  # views >= 3x channel-format median = breakout

SEARCH_CALLS_USED = 0
OTHER_READ_UNITS_USED = 0

# Wide-net discovery seeds. RPM notes are Tier 2 evidence (published
# creator-economy ranges, not measurements) — the scorecard, not this tool,
# owns the revenue judgment. Spans Chris's asset lanes + high-RPM lanes.
DEFAULT_DISCOVER_KEYWORDS = [
    ("construction estimating", "trades/DIY est. $5-12 RPM"),
    ("contractor business",     "business est. $10-25 RPM"),
    ("home renovation",         "home/DIY est. $5-12 RPM"),
    ("carpentry tips",          "trades/DIY est. $5-12 RPM"),
    ("woodworking projects",    "trades/DIY est. $5-12 RPM"),
    ("AI tools for business",   "tech/business est. $10-25 RPM"),
    ("AI automation",           "tech est. $8-20 RPM"),
    ("learn to code",           "tech/education est. $8-20 RPM"),
    ("excel tutorial",          "education/business est. $8-20 RPM"),
    ("notion templates",        "productivity est. $8-15 RPM"),
    ("personal finance",        "finance est. $15-40 RPM"),
    ("large family vlog",       "lifestyle est. $2-5 RPM"),
]
SMALL_CHANNEL_SUBS = 200_000  # 'reachable' ceiling for breakout ranking
TOPIC_REPORT_DEFAULT = 100

# Defined desk-based research universe. This is broad enough to compare the
# paths Chris can produce from current learning/work, while excluding unrelated
# entertainment, physical-product access, and child-directed content.
MARKET_TOPIC_GROUPS = {
    "practical_ai": (
        "AI automation tutorial",
        "AI tools for beginners",
        "AI tools for business",
        "ChatGPT tutorial",
        "Claude Code tutorial",
        "Codex tutorial",
        "Claude Code workflow",
        "ChatGPT automation tutorial",
        "AI coding tools",
        "best AI tools",
        "AI tools review",
        "ChatGPT vs Claude",
    ),
    "software_tutorials": (
        "excel tutorial",
        "learn to code",
        "notion templates",
        "VS Code tutorial",
        "Python tutorial",
        "GitHub tutorial",
        "Canva tutorial",
        "Google Workspace tutorial",
        "Microsoft 365 tutorial",
        "Power Automate tutorial",
        "Zapier tutorial",
        "n8n tutorial",
        "Obsidian tutorial",
    ),
    "software_reviews": (
        "productivity apps review",
        "best note taking apps",
        "CRM software review",
    ),
    "small_business_ai": (
        "AI for small business",
        "ChatGPT for small business",
        "small business automation",
        "AI CRM small business",
    ),
    "family_technology": (
        "Google Family Link tutorial",
        "screen time app for parents",
        "parental control apps review",
        "family calendar app tutorial",
    ),
}

# Conservative title checks for ambiguous searches. The strict market report
# applies these rules; --relevance raw preserves every API result for audit.
TOPIC_TITLE_TERMS = {
    "AI automation tutorial": (
        "ai", "automation", "workflow", "agent", "n8n", "zapier",
    ),
    "AI tools for beginners": ("ai", "chatgpt", "claude", "gemini"),
    "AI tools for business": ("ai", "chatgpt", "claude", "automation"),
    "AI coding tools": (
        "ai", "coding", "programming", "cursor", "copilot", "claude",
        "codex",
    ),
    "best AI tools": ("ai", "chatgpt", "claude", "gemini"),
    "AI tools review": ("ai", "chatgpt", "claude", "gemini"),
    "VS Code tutorial": ("vs code", "vscode", "visual studio code"),
    "Google Workspace tutorial": (
        "google workspace", "gmail", "google drive", "google docs",
        "google sheets", "google slides", "google calendar",
    ),
    "Microsoft 365 tutorial": (
        "microsoft 365", "office 365", "m365", "microsoft office",
        "excel", "word", "powerpoint", "outlook", "teams", "onedrive",
        "sharepoint",
    ),
    "Power Automate tutorial": ("power automate", "power platform"),
    "Obsidian tutorial": (
        "obsidian md", "obsidian app", "obsidian notes", "obsidian note",
        "obsidian vault", "obsidian plugin", "obsidian canvas",
        "obsidian tutorial", "obsidian setup", "obsidian workflow",
    ),
    "learn to code": (
        "code", "coding", "programming", "developer", "python",
        "javascript",
    ),
    "notion templates": ("notion",),
    "productivity apps review": (
        "productivity", "task manager", "calendar app", "note taking",
        "notion", "todo",
    ),
    "best note taking apps": (
        "note taking", "notes app", "notion", "obsidian", "onenote",
        "evernote", "notebook",
    ),
    "CRM software review": (
        "crm", "customer relationship", "salesforce", "hubspot", "zoho",
        "gohighlevel",
    ),
    "Google Family Link tutorial": (
        "family link", "parental control", "screen time",
    ),
    "screen time app for parents": (
        "screen time", "parental control", "parents", "family",
    ),
    "parental control apps review": (
        "parental control", "parents", "family", "screen time",
    ),
    "family calendar app tutorial": (
        "family calendar", "calendar app", "digital calendar",
    ),
}

TOPIC_TITLE_EXCLUDES = {
    "Codex tutorial": ("call of duty", "warhammer", "minecraft"),
    "Python tutorial": ("python snake", "reptile"),
    "Obsidian tutorial": (
        "minecraft", "obsidian trap", "obi trap", "pvp", "nether",
        "dagger", "knife", "blade", "sword",
    ),
}

TITLE_TERM_STOPWORDS = {
    "tutorial", "best", "review", "for", "beginners", "small",
    "business", "apps", "app", "software", "tools", "tool", "vs",
    "workflow", "templates",
}


# ---------------------------------------------------------------- utilities

def load_api_key() -> str:
    key = os.environ.get("YOUTUBE_API_KEY", "").strip()
    if not key and SECRET_FILE.exists():
        for line in SECRET_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("YOUTUBE_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
                break
    if not key:
        sys.exit(
            "No API key found. Set YOUTUBE_API_KEY or put "
            f"YOUTUBE_API_KEY=<key> in {SECRET_FILE}."
        )
    return key


def api_get(endpoint: str, key: str, cost: int = 1, **params) -> dict:
    """Make one API request and account for the two June 2026 read buckets."""
    global SEARCH_CALLS_USED, OTHER_READ_UNITS_USED
    params["key"] = key
    url = f"{API_BASE}/{endpoint}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            if endpoint == "search":
                SEARCH_CALLS_USED += 1
            else:
                OTHER_READ_UNITS_USED += cost
            return json.load(resp)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.exit(f"API error {e.code} on {endpoint}: {body[:400]}")
    except urllib.error.URLError as e:
        sys.exit(f"Network error on {endpoint}: {e.reason}")


def parse_iso8601_duration(s: str) -> int:
    """PT#H#M#S -> seconds."""
    m = re.fullmatch(
        r"P(?:\d+D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or ""
    )
    if not m:
        return 0
    h, mi, se = (int(g) if g else 0 for g in m.groups())
    return h * 3600 + mi * 60 + se


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")


def print_quota_summary() -> None:
    print(f"Search calls this run: {SEARCH_CALLS_USED} / 100 daily default")
    print(
        f"Other read units this run: {OTHER_READ_UNITS_USED} "
        "/ 10,000 daily default"
    )


# ---------------------------------------------------------------- database

SCHEMA = """
CREATE TABLE IF NOT EXISTS channels (
    id TEXT PRIMARY KEY,          -- UC... channel id
    handle TEXT,
    title TEXT,
    niche TEXT NOT NULL,
    uploads_playlist TEXT,
    subscriber_count INTEGER,
    added_at TEXT
);
CREATE TABLE IF NOT EXISTS videos (
    id TEXT PRIMARY KEY,
    channel_id TEXT NOT NULL REFERENCES channels(id),
    title TEXT,
    published_at TEXT,
    duration_s INTEGER,
    is_short INTEGER,             -- 1 if duration <= 180s
    views INTEGER,
    likes INTEGER,
    comments INTEGER,
    fetched_at TEXT
);
CREATE INDEX IF NOT EXISTS idx_videos_channel ON videos(channel_id);
CREATE TABLE IF NOT EXISTS discoveries (
    video_id TEXT,
    keyword TEXT,
    channel_id TEXT,
    channel_title TEXT,
    subscriber_count INTEGER,
    video_title TEXT,
    published_at TEXT,
    duration_s INTEGER,
    is_short INTEGER,
    views INTEGER,
    views_per_sub REAL,           -- NULL if subscriber count hidden
    discovered_at TEXT,
    PRIMARY KEY (video_id, keyword)
);
CREATE TABLE IF NOT EXISTS discovery_snapshots (
    video_id TEXT NOT NULL,
    keyword TEXT NOT NULL,
    observed_at TEXT NOT NULL,
    views INTEGER NOT NULL,
    subscriber_count INTEGER,
    PRIMARY KEY (video_id, keyword, observed_at)
);
CREATE INDEX IF NOT EXISTS idx_discovery_snapshots_topic
    ON discovery_snapshots(keyword, video_id, observed_at);
"""


def db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)
    return conn


# ---------------------------------------------------------------- commands

def cmd_add_channel(args) -> None:
    key = load_api_key()
    ident = args.channel.strip()
    params = {"part": "snippet,contentDetails,statistics"}
    if re.fullmatch(r"UC[\w-]{22}", ident):
        params["id"] = ident
    else:
        params["forHandle"] = ident.lstrip("@")
    data = api_get("channels", key, **params)
    items = data.get("items", [])
    if not items:
        sys.exit(f"Channel not found: {ident}")
    ch = items[0]
    row = (
        ch["id"],
        ident if ident.startswith("@") else ch["snippet"].get("customUrl", ""),
        ch["snippet"]["title"],
        args.niche,
        ch["contentDetails"]["relatedPlaylists"]["uploads"],
        int(ch["statistics"].get("subscriberCount", 0)),
        now_utc(),
    )
    conn = db()
    conn.execute(
        "INSERT OR REPLACE INTO channels VALUES (?,?,?,?,?,?,?)", row
    )
    conn.commit()
    print(f"Added [{args.niche}] {row[2]} ({row[0]}), "
          f"{row[5]:,} subscribers.")


def cmd_harvest(args) -> None:
    key = load_api_key()
    conn = db()
    channels = conn.execute(
        "SELECT id, title, uploads_playlist FROM channels"
    ).fetchall()
    if not channels:
        sys.exit("No channels yet. Use add-channel first.")
    for ch_id, title, playlist in channels:
        video_ids = []
        page_token = None
        while len(video_ids) < args.max_videos:
            params = {
                "part": "contentDetails",
                "playlistId": playlist,
                "maxResults": 50,
            }
            if page_token:
                params["pageToken"] = page_token
            data = api_get("playlistItems", key, **params)
            video_ids += [
                it["contentDetails"]["videoId"] for it in data.get("items", [])
            ]
            page_token = data.get("nextPageToken")
            if not page_token:
                break
        video_ids = video_ids[: args.max_videos]

        fetched = 0
        for i in range(0, len(video_ids), 50):
            batch = video_ids[i : i + 50]
            data = api_get(
                "videos", key,
                part="snippet,contentDetails,statistics",
                id=",".join(batch), maxResults=50,
            )
            rows = []
            for v in data.get("items", []):
                dur = parse_iso8601_duration(
                    v["contentDetails"].get("duration", "")
                )
                stats = v.get("statistics", {})
                rows.append((
                    v["id"], ch_id, v["snippet"]["title"],
                    v["snippet"]["publishedAt"], dur,
                    1 if dur <= SHORT_MAX_SECONDS else 0,
                    int(stats.get("viewCount", 0)),
                    int(stats.get("likeCount", 0)),
                    int(stats.get("commentCount", 0)),
                    now_utc(),
                ))
            conn.executemany(
                "INSERT OR REPLACE INTO videos VALUES (?,?,?,?,?,?,?,?,?,?)",
                rows,
            )
            fetched += len(rows)
        conn.commit()
        print(f"Harvested {fetched:>4} videos from {title}")
    print("\nDone.")
    print_quota_summary()


def _report_rows(conn, niche=None, min_videos=8):
    """Yield (niche, channel, format, median, video_title, views, ratio)."""
    q = "SELECT id, title, niche FROM channels"
    params = ()
    if niche:
        q += " WHERE niche = ?"
        params = (niche,)
    for ch_id, ch_title, ch_niche in conn.execute(q, params):
        for is_short, label in ((0, "long-form"), (1, "short")):
            vids = conn.execute(
                "SELECT title, views FROM videos "
                "WHERE channel_id=? AND is_short=? AND views>0",
                (ch_id, is_short),
            ).fetchall()
            if len(vids) < min_videos:
                continue
            med = statistics.median(v for _, v in vids)
            if med <= 0:
                continue
            for v_title, views in vids:
                yield (ch_niche, ch_title, label, med, v_title, views,
                       views / med)


def cmd_report(args) -> None:
    conn = db()
    rows = list(_report_rows(conn, args.niche, args.min_videos))
    if not rows:
        sys.exit("No data (or not enough videos per channel). Harvest first.")

    # Niche summary: outlier rate per niche+format
    print("\n== NICHE SUMMARY (share of videos >= "
          f"{OUTLIER_THRESHOLD}x channel median) ==")
    summary = {}
    for n, _, fmt, _, _, _, ratio in rows:
        k = (n, fmt)
        total, hits = summary.get(k, (0, 0))
        summary[k] = (total + 1, hits + (1 if ratio >= OUTLIER_THRESHOLD else 0))
    for (n, fmt), (total, hits) in sorted(summary.items()):
        print(f"  {n:<20} {fmt:<10} {hits:>4}/{total:<5} "
              f"({100 * hits / total:.1f}%) breakout rate")

    # Top outliers
    print(f"\n== TOP {args.top} BREAKOUT VIDEOS (views / channel median) ==")
    rows.sort(key=lambda r: r[6], reverse=True)
    for n, ch, fmt, med, title, views, ratio in rows[: args.top]:
        print(f"  {ratio:>6.1f}x  [{n}/{fmt}] {ch} — "
              f"{title[:60]}  ({views:,} views vs median {int(med):,})")


def _parse_utc(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _topic_report_rows(conn, keyword, format_filter="all"):
    """Return stored discovery rows with real snapshot velocity when valid."""
    query = (
        "SELECT video_id, video_title, channel_title, published_at, "
        "is_short, views, subscriber_count, views_per_sub "
        "FROM discoveries WHERE keyword=?"
    )
    params = [keyword]
    if format_filter != "all":
        query += " AND is_short=?"
        params.append(1 if format_filter == "short" else 0)

    rows = []
    for result in conn.execute(query, params):
        (video_id, title, channel, published_at, is_short, views,
         subscribers, views_per_sub) = result
        observations = conn.execute(
            "SELECT observed_at, views FROM discovery_snapshots "
            "WHERE video_id=? AND keyword=? ORDER BY observed_at",
            (video_id, keyword),
        ).fetchall()
        velocity = None
        if len(observations) >= 2:
            earliest_at, earliest_views = observations[0]
            latest_at, latest_views = observations[-1]
            elapsed_days = (
                _parse_utc(latest_at) - _parse_utc(earliest_at)
            ).total_seconds() / 86_400
            if elapsed_days >= 1:
                velocity = (latest_views - earliest_views) / elapsed_days
        rows.append({
            "video_id": video_id,
            "title": title,
            "channel": channel,
            "published_at": published_at,
            "format": "short" if is_short else "long",
            "views": views,
            "subscribers": None if subscribers is None or subscribers < 0
            else subscribers,
            "views_per_sub": views_per_sub,
            "velocity": velocity,
        })
    return rows


def _rank_topic_rows(rows, rank):
    metric = {
        "views": "views",
        "breakout": "views_per_sub",
        "velocity": "velocity",
    }[rank]

    def sort_key(row):
        value = row[metric]
        return (value is not None, value if value is not None else 0,
                row["views"])

    return sorted(rows, key=sort_key, reverse=True)


def _market_keywords(category="all"):
    if category == "all":
        return [
            keyword
            for keywords in MARKET_TOPIC_GROUPS.values()
            for keyword in keywords
        ]
    return list(MARKET_TOPIC_GROUPS[category])


def _normalized_text(value):
    return " ".join(re.findall(r"[a-z0-9]+", value.lower()))


def _contains_title_term(normalized_title, term):
    normalized_term = _normalized_text(term)
    if " " in normalized_term:
        return normalized_term in normalized_title
    return normalized_term in normalized_title.split()


def _topic_title_relevant(keyword, title):
    normalized_title = _normalized_text(title)
    excludes = TOPIC_TITLE_EXCLUDES.get(keyword, ())
    if any(_contains_title_term(normalized_title, term) for term in excludes):
        return False
    terms = TOPIC_TITLE_TERMS.get(keyword)
    if terms is None:
        terms = tuple(
            token for token in _normalized_text(keyword).split()
            if token not in TITLE_TERM_STOPWORDS and len(token) >= 2
        )
    return any(_contains_title_term(normalized_title, term) for term in terms)


def _market_report_rows(
    conn, category="all", format_filter="all", relevance="strict"
):
    """Return deduplicated videos across the defined market topic universe."""
    keywords = _market_keywords(category)
    placeholders = ",".join("?" for _ in keywords)
    query = (
        "SELECT video_id, keyword, video_title, channel_title, published_at, "
        "is_short, views, subscriber_count FROM discoveries "
        f"WHERE keyword IN ({placeholders})"
    )
    params = list(keywords)
    if format_filter != "all":
        query += " AND is_short=?"
        params.append(1 if format_filter == "short" else 0)

    category_by_keyword = {
        keyword: group
        for group, group_keywords in MARKET_TOPIC_GROUPS.items()
        for keyword in group_keywords
    }
    videos = {}
    for result in conn.execute(query, params):
        (video_id, keyword, title, channel, published_at, is_short, views,
         subscribers) = result
        if relevance == "strict" and not _topic_title_relevant(keyword, title):
            continue
        row = videos.get(video_id)
        if row is None:
            row = {
                "video_id": video_id,
                "title": title,
                "channel": channel,
                "published_at": published_at,
                "format": "short" if is_short else "long",
                "views": views,
                "subscribers": None,
                "views_per_sub": None,
                "velocity": None,
                "topics": set(),
                "categories": set(),
            }
            videos[video_id] = row
        if views >= row["views"]:
            row.update({
                "title": title,
                "channel": channel,
                "published_at": published_at,
                "format": "short" if is_short else "long",
                "views": views,
                "subscribers": (
                    None if subscribers is None or subscribers < 0
                    else subscribers
                ),
            })
        row["topics"].add(keyword)
        row["categories"].add(category_by_keyword[keyword])

    snapshot_query = (
        "SELECT video_id, observed_at, MAX(views) "
        "FROM discovery_snapshots "
        f"WHERE keyword IN ({placeholders}) "
        "GROUP BY video_id, observed_at ORDER BY observed_at"
    )
    observations = {}
    for video_id, observed_at, views in conn.execute(snapshot_query, keywords):
        if video_id in videos:
            observations.setdefault(video_id, []).append((observed_at, views))

    for video_id, row in videos.items():
        subscribers = row["subscribers"]
        row["views_per_sub"] = (
            row["views"] / subscribers if subscribers else None
        )
        snapshots = observations.get(video_id, [])
        if len(snapshots) >= 2:
            earliest_at, earliest_views = snapshots[0]
            latest_at, latest_views = snapshots[-1]
            elapsed_days = (
                _parse_utc(latest_at) - _parse_utc(earliest_at)
            ).total_seconds() / 86_400
            if elapsed_days >= 1:
                row["velocity"] = (
                    latest_views - earliest_views
                ) / elapsed_days
        row["topics"] = sorted(row["topics"])
        row["categories"] = sorted(row["categories"])
    return list(videos.values())


def cmd_topic_report(args) -> None:
    """Rank one exact stored topic without loading a key or using a network."""
    conn = db()
    keywords = [row[0] for row in conn.execute(
        "SELECT DISTINCT keyword FROM discoveries ORDER BY keyword"
    )]
    if args.keyword not in keywords:
        print(f"No stored discovery keyword exactly matches: {args.keyword}")
        if keywords:
            print("Available stored keywords:")
            for keyword in keywords:
                print(f"  {keyword}")
        else:
            print("No discovery keywords are stored yet. Run discover first.")
        conn.close()
        return

    rows = _topic_report_rows(conn, args.keyword, args.format)
    conn.close()
    rows = _rank_topic_rows(rows, args.rank)[:args.top]
    print(
        f"TOPIC REPORT — exact keyword: {args.keyword} | "
        f"rank: {args.rank} | format: {args.format}"
    )
    if not rows:
        print("No stored videos match that format filter.")
        return
    print(
        "rank | exact video title | channel | publish date | format | "
        "current views | subscribers | views/subscriber | measured views/day"
    )
    for index, row in enumerate(rows, 1):
        subscribers = ("n/a" if row["subscribers"] is None
                       else f'{row["subscribers"]:,}')
        breakout = ("n/a" if row["views_per_sub"] is None
                    else f'{row["views_per_sub"]:.2f}x')
        velocity = ("n/a" if row["velocity"] is None
                    else f'{row["velocity"]:,.1f}')
        publish_date = (row["published_at"] or "n/a")[:10]
        print(
            f'{index} | {row["title"]} | {row["channel"]} | '
            f'{publish_date} | {row["format"]} | {row["views"]:,} | '
            f'{subscribers} | {breakout} | {velocity}'
        )


def cmd_market_report(args) -> None:
    """Rank the deduplicated relevant market without using the network."""
    conn = db()
    expected = _market_keywords(args.category)
    stored = {
        row[0] for row in conn.execute(
            "SELECT DISTINCT keyword FROM discoveries"
        )
    }
    present = [keyword for keyword in expected if keyword in stored]
    missing = [keyword for keyword in expected if keyword not in stored]
    rows = _market_report_rows(
        conn, args.category, args.format, args.relevance
    )
    conn.close()
    total_unique = len(rows)
    rows = _rank_topic_rows(rows, args.rank)[:args.top]

    print(
        f"MARKET REPORT — category: {args.category} | rank: {args.rank} | "
        f"format: {args.format} | relevance: {args.relevance}"
    )
    print(
        f"coverage: {len(present)}/{len(expected)} defined topics stored | "
        f"{total_unique} unique videos available | {len(rows)} shown"
    )
    if missing:
        print("missing topic scans: " + ", ".join(missing))
    if not rows:
        print("No stored videos match this market selection.")
        return
    print(
        "rank | exact video title | channel | publish date | format | "
        "current views | subscribers | views/subscriber | measured views/day "
        "| categories | matched topics"
    )
    for index, row in enumerate(rows, 1):
        subscribers = ("n/a" if row["subscribers"] is None
                       else f'{row["subscribers"]:,}')
        breakout = ("n/a" if row["views_per_sub"] is None
                    else f'{row["views_per_sub"]:.2f}x')
        velocity = ("n/a" if row["velocity"] is None
                    else f'{row["velocity"]:,.1f}')
        publish_date = (row["published_at"] or "n/a")[:10]
        print(
            f'{index} | {row["title"]} | {row["channel"]} | '
            f'{publish_date} | {row["format"]} | {row["views"]:,} | '
            f'{subscribers} | {breakout} | {velocity} | '
            f'{",".join(row["categories"])} | {",".join(row["topics"])}'
        )


def cmd_discover(args) -> None:
    """Wide-net scan: per keyword, pull recent top-viewed + relevant videos,
    join with channel subscriber counts, and rank views/subscriber breakouts
    from small channels. Nominates niches; does NOT add channels."""
    from datetime import timedelta
    key = load_api_key()
    if args.market:
        keywords = [
            (keyword, f"{category} market topic")
            for category, group_keywords in MARKET_TOPIC_GROUPS.items()
            for keyword in group_keywords
        ]
    elif args.keywords:
        keywords = [(k.strip(), "RPM n/a (custom keyword)")
                    for k in args.keywords.split(",") if k.strip()]
    else:
        keywords = DEFAULT_DISCOVER_KEYWORDS
    cutoff = (datetime.now(timezone.utc) - timedelta(days=args.days)
              ).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn = db()
    observed_at = now_utc()
    kw_results = {}  # keyword -> list of video dicts

    for kw, rpm_note in keywords:
        video_ids = []
        for order in ("viewCount", "relevance"):
            data = api_get(
                "search", key,
                part="snippet", q=kw, type="video", order=order,
                publishedAfter=cutoff, maxResults=50,
                relevanceLanguage="en", regionCode="US",
            )
            video_ids += [it["id"]["videoId"] for it in data.get("items", [])
                          if it.get("id", {}).get("videoId")]
        video_ids = list(dict.fromkeys(video_ids))  # dedupe, keep order

        videos = {}
        for i in range(0, len(video_ids), 50):
            data = api_get(
                "videos", key,
                part="snippet,contentDetails,statistics",
                id=",".join(video_ids[i:i + 50]), maxResults=50,
            )
            for v in data.get("items", []):
                dur = parse_iso8601_duration(
                    v["contentDetails"].get("duration", ""))
                videos[v["id"]] = {
                    "channel_id": v["snippet"]["channelId"],
                    "channel_title": v["snippet"]["channelTitle"],
                    "title": v["snippet"]["title"],
                    "published_at": v["snippet"]["publishedAt"],
                    "duration_s": dur,
                    "is_short": 1 if dur <= SHORT_MAX_SECONDS else 0,
                    "views": int(v.get("statistics", {}).get("viewCount", 0)),
                }

        ch_ids = list({v["channel_id"] for v in videos.values()})
        subs = {}
        for i in range(0, len(ch_ids), 50):
            data = api_get(
                "channels", key, part="statistics",
                id=",".join(ch_ids[i:i + 50]), maxResults=50,
            )
            for c in data.get("items", []):
                st = c.get("statistics", {})
                subs[c["id"]] = (None if st.get("hiddenSubscriberCount")
                                 else int(st.get("subscriberCount", 0)))

        rows = []
        for vid, v in videos.items():
            s = subs.get(v["channel_id"])
            vps = (v["views"] / s) if s else None
            v = {**v, "video_id": vid, "subs": s, "views_per_sub": vps}
            rows.append(v)
            conn.execute(
                "INSERT OR REPLACE INTO discoveries VALUES "
                "(?,?,?,?,?,?,?,?,?,?,?,?)",
                (vid, kw, v["channel_id"], v["channel_title"],
                 s if s is not None else -1, v["title"], v["published_at"],
                 v["duration_s"], v["is_short"], v["views"], vps, now_utc()),
            )
            conn.execute(
                "INSERT OR IGNORE INTO discovery_snapshots "
                "(video_id, keyword, observed_at, views, subscriber_count) "
                "VALUES (?,?,?,?,?)",
                (vid, kw, observed_at, v["views"], s),
            )
        conn.commit()
        kw_results[kw] = (rpm_note, rows)
        print(f"scanned '{kw}': {len(rows)} videos, "
              f"{len(ch_ids)} channels")

    # ---- report
    print(f"\n== WIDE-NET NICHE SCAN (uploads from last {args.days} days) ==")
    print(f"{'keyword':<24} {'vids':>4} {'median views':>13} "
          f"{'top views':>12} {'%<200k subs':>11}  rpm note")
    for kw, (rpm_note, rows) in kw_results.items():
        if not rows:
            print(f"{kw:<24} {'0':>4}  (no results)")
            continue
        views = sorted(v["views"] for v in rows)
        med = views[len(views) // 2]
        small = [v for v in rows
                 if v["subs"] is not None and v["subs"] < SMALL_CHANNEL_SUBS]
        print(f"{kw:<24} {len(rows):>4} {med:>13,} {views[-1]:>12,} "
              f"{100 * len(small) / len(rows):>10.0f}%  {rpm_note}")

    print(f"\n== TOP SMALL-CHANNEL BREAKOUTS "
          f"(views/subscriber, channels < {SMALL_CHANNEL_SUBS:,} subs) ==")
    all_small = [
        (v["views_per_sub"], kw, v) for kw, (_, rows) in kw_results.items()
        for v in rows
        if v["views_per_sub"] and v["subs"] and v["subs"] < SMALL_CHANNEL_SUBS
        and v["views"] >= args.min_views
    ]
    all_small.sort(reverse=True, key=lambda t: t[0])
    for vps, kw, v in all_small[:args.top]:
        fmt = "short" if v["is_short"] else "long"
        print(f"  {vps:>7.1f}x  [{kw}/{fmt}] {v['channel_title']} "
              f"({v['subs']:,} subs) — {v['title'][:55]}  "
              f"({v['views']:,} views)")

    print()
    print_quota_summary()


def cmd_selftest(_args) -> None:
    """Offline: exercise schema, ranking, velocity, and outlier math."""
    test_db = HERE / "selftest.db"
    if test_db.exists():
        test_db.unlink()
    conn = sqlite3.connect(test_db)
    conn.executescript(SCHEMA)
    conn.execute(
        "INSERT INTO channels VALUES "
        "('UCtest', '@t', 'TestChannel', 'testniche', 'PLx', 1000, '')"
    )
    # 9 ordinary long-form videos (median 1000) + 1 breakout (10x)
    vids = [(f"v{i}", "UCtest", f"vid {i}", "", 600, 0, 1000, 0, 0, "")
            for i in range(9)]
    vids.append(("vX", "UCtest", "BREAKOUT", "", 600, 0, 10000, 0, 0, ""))
    # shorts cohort, median 500, one 4x outlier
    vids += [(f"s{i}", "UCtest", f"short {i}", "", 45, 1, 500, 0, 0, "")
             for i in range(9)]
    vids.append(("sX", "UCtest", "SHORT-BREAKOUT", "", 45, 1, 2000, 0, 0, ""))
    conn.executemany(
        "INSERT INTO videos VALUES (?,?,?,?,?,?,?,?,?,?)", vids)

    discoveries = [
        ("t1", "test topic", "UCtest", "TestChannel", 100,
         "Breakout first", "2026-01-01T00:00:00Z", 600, 0, 1000,
         10.0, "2026-01-03 00:00:00Z"),
        ("t2", "test topic", "UCtest", "TestChannel", 1000,
         "Views first", "2026-01-02T00:00:00Z", 600, 0, 2000,
         2.0, "2026-01-03 00:00:00Z"),
        ("t3", "test topic", "UCtest", "TestChannel", -1,
         "Hidden subscribers", "2026-01-03T00:00:00Z", 45, 1, 1500,
         None, "2026-01-03 00:00:00Z"),
        ("m1", "Claude Code tutorial", "UCmarket", "MarketChannel", 100,
         "Claude Code and ChatGPT shared AI video",
         "2026-01-01T00:00:00Z", 600, 0, 3000,
         30.0, "2026-01-01 00:00:00Z"),
        ("m1", "ChatGPT tutorial", "UCmarket", "MarketChannel", 100,
         "Claude Code and ChatGPT shared AI video",
         "2026-01-01T00:00:00Z", 600, 0, 3200,
         32.0, "2026-01-03 00:00:00Z"),
        ("m2", "excel tutorial", "UCmarket2", "SoftwareChannel", 1000,
         "Excel spreadsheet tutorial", "2026-01-02T00:00:00Z", 600, 0,
         5000,
         5.0, "2026-01-03 00:00:00Z"),
    ]
    conn.executemany(
        "INSERT INTO discoveries VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        discoveries,
    )
    conn.execute(
        "INSERT INTO discovery_snapshots VALUES (?,?,?,?,?)",
        ("t1", "test topic", "2026-01-01 00:00:00Z", 1000, 100),
    )
    conn.executemany(
        "INSERT INTO discovery_snapshots VALUES (?,?,?,?,?)",
        [
            ("m1", "Claude Code tutorial", "2026-01-01 00:00:00Z",
             3000, 100),
            ("m1", "ChatGPT tutorial", "2026-01-03 00:00:00Z",
             3200, 100),
        ],
    )
    conn.commit()

    rows = list(_report_rows(conn, None, min_videos=5))
    long_break = [r for r in rows if r[4] == "BREAKOUT"]
    short_break = [r for r in rows if r[4] == "SHORT-BREAKOUT"]
    assert long_break and abs(long_break[0][6] - 10.0) < 0.01, "long-form math"
    assert short_break and abs(short_break[0][6] - 4.0) < 0.01, "shorts math"
    assert parse_iso8601_duration("PT1H2M3S") == 3723, "duration parse"
    assert parse_iso8601_duration("PT59S") == 59, "duration parse short"

    topic_rows = _topic_report_rows(conn, "test topic")
    assert len(topic_rows) == 3, "exact topic lookup"
    assert not _topic_report_rows(conn, "TEST TOPIC"), "topic must be exact"
    assert _rank_topic_rows(topic_rows, "views")[0]["video_id"] == "t2", (
        "views ranking"
    )
    assert _rank_topic_rows(topic_rows, "breakout")[0]["video_id"] == "t1", (
        "breakout ranking"
    )
    one_snapshot = next(row for row in topic_rows if row["video_id"] == "t1")
    assert one_snapshot["velocity"] is None, "one snapshot velocity unavailable"

    conn.execute(
        "INSERT INTO discovery_snapshots VALUES (?,?,?,?,?)",
        ("t1", "test topic", "2026-01-03 00:00:00Z", 1400, 100),
    )
    conn.commit()
    topic_rows = _topic_report_rows(conn, "test topic")
    two_snapshots = next(row for row in topic_rows if row["video_id"] == "t1")
    assert abs(two_snapshots["velocity"] - 200.0) < 0.01, (
        "two-snapshot velocity"
    )
    assert _rank_topic_rows(topic_rows, "velocity")[0]["video_id"] == "t1", (
        "velocity ranking"
    )

    market_rows = _market_report_rows(conn)
    assert len(market_rows) == 2, "market deduplicates videos across topics"
    shared = next(row for row in market_rows if row["video_id"] == "m1")
    assert shared["topics"] == ["ChatGPT tutorial", "Claude Code tutorial"], (
        "market preserves matched topics"
    )
    assert shared["categories"] == ["practical_ai"], "market category"
    assert abs(shared["velocity"] - 100.0) < 0.01, "market velocity"
    assert _rank_topic_rows(market_rows, "views")[0]["video_id"] == "m2", (
        "market views ranking"
    )
    assert _rank_topic_rows(market_rows, "breakout")[0]["video_id"] == "m1", (
        "market breakout ranking"
    )
    conn.close()
    test_db.unlink()
    print("SELFTEST PASS — schema, format separation, exact-topic and "
          "deduplicated-market ranking, snapshot velocity, outlier math, "
          "and duration parsing all correct.")


# ---------------------------------------------------------------- main

def main() -> None:
    # Windows consoles default to cp1252, which chokes on emoji in video
    # titles; never let output encoding kill a run.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("discover",
                       help="wide-net niche scan; nominates niches/channels")
    discover_scope = d.add_mutually_exclusive_group()
    discover_scope.add_argument(
        "--keywords",
        help="comma-separated keyword list (default: built-in 12)",
    )
    discover_scope.add_argument(
        "--market",
        action="store_true",
        help="scan all defined desk-based market topics",
    )
    d.add_argument("--days", type=int, default=180,
                   help="only videos published in the last N days (default 180)")
    d.add_argument("--top", type=int, default=25,
                   help="breakout rows to show (default 25)")
    d.add_argument("--min-views", type=int, default=50_000,
                   help="ignore breakouts under N views (default 50,000)")
    d.set_defaults(fn=cmd_discover)

    t = sub.add_parser(
        "topic-report",
        help="offline ranking for one exact stored discovery keyword",
    )
    t.add_argument("keyword", help="exact stored discovery keyword")
    t.add_argument("--top", type=int, default=TOPIC_REPORT_DEFAULT,
                   help="number of rows to show (default 100)")
    t.add_argument("--rank", choices=("views", "breakout", "velocity"),
                   default="views", help="ranking metric (default views)")
    t.add_argument("--format", choices=("all", "long", "short"),
                   default="all", help="format filter (default all)")
    t.set_defaults(fn=cmd_topic_report)

    m = sub.add_parser(
        "market-report",
        help="offline deduplicated ranking across relevant desk-based topics",
    )
    m.add_argument("--top", type=int, default=TOPIC_REPORT_DEFAULT,
                   help="number of rows to show (default 100)")
    m.add_argument("--rank", choices=("views", "breakout", "velocity"),
                   default="views", help="ranking metric (default views)")
    m.add_argument("--format", choices=("all", "long", "short"),
                   default="all", help="format filter (default all)")
    m.add_argument(
        "--category",
        choices=("all",) + tuple(MARKET_TOPIC_GROUPS),
        default="all",
        help="limit to one defined market category (default all)",
    )
    m.add_argument(
        "--relevance",
        choices=("strict", "raw"),
        default="strict",
        help="title relevance gate or unfiltered API results (default strict)",
    )
    m.set_defaults(fn=cmd_market_report)

    a = sub.add_parser("add-channel", help="register a channel to scan")
    a.add_argument("channel", help="@handle or UC... channel id")
    a.add_argument("--niche", required=True,
                   help="niche label, e.g. trades / buildinpublic / family")
    a.set_defaults(fn=cmd_add_channel)

    h = sub.add_parser("harvest", help="fetch uploads + stats for all channels")
    h.add_argument("--max-videos", type=int, default=200,
                   help="most recent N uploads per channel (default 200)")
    h.set_defaults(fn=cmd_harvest)

    r = sub.add_parser("report", help="niche summary + top breakout videos")
    r.add_argument("--niche", help="limit to one niche label")
    r.add_argument("--top", type=int, default=20)
    r.add_argument("--min-videos", type=int, default=8,
                   help="min videos per channel+format to compute a median")
    r.set_defaults(fn=cmd_report)

    s = sub.add_parser("selftest", help="offline logic check, no network")
    s.set_defaults(fn=cmd_selftest)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
