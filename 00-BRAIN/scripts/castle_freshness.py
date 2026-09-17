"""castle_freshness.py — deterministic staleness gate for the CASTLE cockpit.

Written 2026-08-19 (flag #103, Chris-approved). CASTLE's slow layer — the
capability register, opportunity queue, phase pages, and decision log — rotted
for a month because the only thing that read it was a review cadence that
stopped running, and nothing mechanical noticed. root_health.py passed with
0 blockers over a register three weeks wrong. This script is the instrument
the 2026-08-11 Council said was missing: it measures freshness and function,
not presence.

Five checks, all read-only:

  1. current-position.md's "### Reconciled:" date is <= MAX_RECONCILED_AGE days old.
  2. No opportunity-queue Active Queue row has a review date in the past or missing.
  3. No phase page is `status: active` more than PHASE_GRACE days past its window,
     and no `status: planned` phase has an already-open window.
  4. CASTLE's wiki/log.md has an entry within LOG_WINDOW days whenever git shows
     commits touching 00-BRAIN/CASTLE in that window (the return-to-cockpit
     detector: a review sequence that displaces CASTLE goes silent here first).
  5. No live `timeline: now` page carries a `review_trigger` date in the past.

Exit 0 = fresh. Exit 1 = findings (printed one per line). Exit 2 = script error.
--brief prints a single compact line for MORNING_BRIEF.md generation.

Wired into root_health.py on Aug 22 after fail-closed Git behavior and focused
negative tests were added. run_morning_brief.ps1 also calls it.
"""

from __future__ import annotations

import argparse
import calendar
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

MAX_RECONCILED_AGE = 35  # days; monthly cadence plus grace
PHASE_GRACE = 14         # days an active phase may outlive its window
LOG_WINDOW = 14          # days; log silence tolerated against CASTLE commits

MONTHS = {m.lower(): i for i, m in enumerate(calendar.month_name) if m}
MONTHS.update({m.lower(): i for i, m in enumerate(calendar.month_abbr) if m})

DATE_LONG = re.compile(r"([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})")
MONTH_YEAR = re.compile(r"([A-Za-z]+)\.?\s+(\d{4})")
MONTH_ONLY = re.compile(r"^([A-Za-z]+)\.?$")
YEAR_ONLY = re.compile(r"(\d{4})")
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
REVIEW_EXCLUDED = {"99-ARCHIVE", "raw", ".git", ".obsidian", "Report Archive",
                   "Session_Logs", "88-JOURNAL", ".claude", ".agents",
                   "node_modules", ".venv", "venv", "oracleJdk-26"}


def parse_part(part: str, borrow_year: int | None, end: bool):
    """Parse one side of a window expression into a date, or None."""
    part = part.strip().rstrip(".")
    m = DATE_LONG.search(part)
    if m and m.group(1).lower() in MONTHS:
        return dt.date(int(m.group(3)), MONTHS[m.group(1).lower()], int(m.group(2)))
    m = MONTH_YEAR.search(part)
    if m and m.group(1).lower() in MONTHS:
        month, year = MONTHS[m.group(1).lower()], int(m.group(2))
        day = calendar.monthrange(year, month)[1] if end else 1
        return dt.date(year, month, day)
    m = MONTH_ONLY.match(part)
    if m and m.group(1).lower() in MONTHS and borrow_year:
        month = MONTHS[m.group(1).lower()]
        day = calendar.monthrange(borrow_year, month)[1] if end else 1
        return dt.date(borrow_year, month, day)
    m = YEAR_ONLY.search(part)
    if m:
        year = int(m.group(1))
        return dt.date(year, 12, 31) if end else dt.date(year, 1, 1)
    return None


def parse_window(text: str):
    """'Aug 2026 – May 2027' / 'July 2026' / 'Feb – Mar 2027' -> (start, end)."""
    text = re.sub(r"\(.*?\)", "", text)  # drop parentheticals
    parts = re.split(r"\s*[–—]\s*|\s+-\s+", text, maxsplit=1)
    if len(parts) == 2:
        end = parse_part(parts[1], None, end=True)
        start = parse_part(parts[0], end.year if end else None, end=False)
    else:
        start = parse_part(parts[0], None, end=False)
        end = parse_part(parts[0], None, end=True)
    return start, end


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_current_position(wiki: Path, today: dt.date) -> list[str]:
    path = wiki / "current-position.md"
    if not path.exists():
        return [f"current-position.md missing at {path}"]
    m = re.search(r"^### Reconciled:\s*(.+)$", read(path), re.MULTILINE)
    if not m:
        return ["current-position.md has no '### Reconciled:' line to measure"]
    d = DATE_LONG.search(m.group(1))
    if not d or d.group(1).lower() not in MONTHS:
        return [f"current-position.md Reconciled date unparseable: {m.group(1)!r}"]
    when = dt.date(int(d.group(3)), MONTHS[d.group(1).lower()], int(d.group(2)))
    age = (today - when).days
    if age > MAX_RECONCILED_AGE:
        return [f"current-position.md reconciled {when} — {age} days old "
                f"(limit {MAX_RECONCILED_AGE}); the monthly reconciliation is overdue"]
    return []


def check_opportunity_queue(wiki: Path, today: dt.date) -> list[str]:
    path = wiki / "opportunity-queue.md"
    if not path.exists():
        return [f"opportunity-queue.md missing at {path}"]
    findings = []
    for line in read(path).splitlines():
        if not line.startswith("| OPP-"):
            continue
        clean = re.sub(r"\[\[[^\]]*\]\]", "LINK", line)  # wikilink pipes break cells
        cells = [c.strip() for c in clean.split("|")][1:-1]
        opp_id, review = cells[0], (cells[-2] if len(cells) >= 2 else "")
        iso = ISO_DATE.fullmatch(review)
        if not iso:
            findings.append(f"opportunity-queue {opp_id}: review date missing or "
                            f"not a date ({review!r}) — a dated trigger nobody owns "
                            f"does not exist (AGENT.md ED7)")
        elif dt.date.fromisoformat(review) < today:
            findings.append(f"opportunity-queue {opp_id}: review date {review} is past "
                            f"with no disposition")
    return findings


def check_phases(wiki: Path, today: dt.date) -> list[str]:
    findings = []
    for path in sorted((wiki / "phases").glob("phase-*.md")):
        text = read(path)
        status = re.search(r"^status:\s*(\S+)", text, re.MULTILINE)
        window = re.search(r"^\*\*Window\*\*:\s*(.+)$", text, re.MULTILINE)
        if not status or not window:
            continue
        status_v = status.group(1).lower()
        start, end = parse_window(window.group(1))
        if status_v == "active" and end and (today - end).days > PHASE_GRACE:
            findings.append(f"{path.name}: status active but its window closed "
                            f"{end} ({(today - end).days} days ago; grace {PHASE_GRACE})")
        if status_v == "planned" and start and start <= today:
            findings.append(f"{path.name}: status planned but its window opened "
                            f"{start} — flip to active or record why not")
    return findings


def check_log_recency(root: Path, wiki: Path, today: dt.date) -> list[str]:
    path = wiki / "log.md"
    if not path.exists():
        return [f"log.md missing at {path}"]
    headings = re.findall(r"^## (\d{4}-\d{2}-\d{2})", read(path), re.MULTILINE)
    last_entry = max((dt.date.fromisoformat(h) for h in headings), default=None)
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "log", f"--since={LOG_WINDOW}.days",
             "--format=%ad", "--date=short", "--", "00-BRAIN/CASTLE"],
            capture_output=True, text=True, timeout=30, check=True,
        ).stdout.split()
    except (OSError, subprocess.SubprocessError) as exc:
        raise RuntimeError(f"CASTLE git history unavailable: {exc}") from exc
    if not out:
        return []
    if last_entry is None or (today - last_entry).days > LOG_WINDOW:
        newest = max(out)
        return [f"CASTLE commits as recent as {newest} but wiki/log.md's last entry is "
                f"{last_entry or 'unparseable'} — a review sequence may have displaced "
                f"the cockpit without returning control (OPERATIONS.md Session Close 7)"]
    return []


def check_review_triggers(root: Path, today: dt.date) -> list[str]:
    """Find expired or malformed review triggers on live `timeline: now` pages."""
    findings = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if REVIEW_EXCLUDED.intersection(rel.parts) or not path.is_file():
            continue
        text = read(path)
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---", 4)
        if end == -1:
            continue
        fm = text[4:end]
        timeline = re.search(r"^timeline:\s*['\"]?([^'\"#\n]+)", fm, re.MULTILINE)
        if not timeline or timeline.group(1).strip() != "now":
            continue
        trigger = re.search(r"^review_trigger:\s*['\"]?([^'\"#\n]+)",
                            fm, re.MULTILINE)
        if not trigger:
            continue
        value = trigger.group(1).strip()
        if not ISO_DATE.fullmatch(value):
            findings.append(f"{rel}: review_trigger {value!r} is not YYYY-MM-DD")
            continue
        when = dt.date.fromisoformat(value)
        if when < today:
            findings.append(f"{rel}: review_trigger {value} is past — review or re-date it")
    return findings


def run(root: Path, today: dt.date) -> list[str]:
    wiki = root / "00-BRAIN" / "CASTLE" / "wiki"
    findings = []
    findings += check_current_position(wiki, today)
    findings += check_opportunity_queue(wiki, today)
    findings += check_phases(wiki, today)
    findings += check_log_recency(root, wiki, today)
    findings += check_review_triggers(root, today)
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=None, help="vault root (default: two up)")
    parser.add_argument("--today", default=None, help="override date, YYYY-MM-DD (tests)")
    parser.add_argument("--brief", action="store_true",
                        help="one compact line for the morning brief")
    args = parser.parse_args()

    root = Path(args.root) if args.root else Path(__file__).resolve().parents[2]
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()

    try:
        findings = run(root, today)
    except Exception as exc:  # a broken gate must say so, not pass silently
        print(f"castle_freshness ERROR: {exc}")
        return 2

    if args.brief:
        if findings:
            print(f"CASTLE freshness: {len(findings)} finding(s) — "
                  + "; ".join(f.split(" — ")[0] for f in findings))
        else:
            print("CASTLE freshness: PASS")
        return 1 if findings else 0

    if findings:
        print(f"castle_freshness: {len(findings)} finding(s), {today}:")
        for f in findings:
            print(f"  - {f}")
        return 1
    print(f"castle_freshness: PASS ({today})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
