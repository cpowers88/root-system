---
type: source-summary
status: parked
source_role: project-source
difficulty: stage-10
source_file: raw/books/PythonCrashCourse.pdf
tags: [reference, programming, parked, stage-10-support]
---

# Working with APIs in Python (requests)

**Summary**: The standard pattern for calling a REST API from Python using the `requests` library — making a call, checking status, parsing JSON, handling rate limits, and chaining calls to aggregate data not available in a single response.

**Sources**: python-crash-course.pdf (Chapter 17)

**Last updated**: 2026-06-17

---

## Core call pattern

```python
import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")   # 200 = success

response_dict = r.json()   # parsed JSON -> Python dict
```
(source: python-crash-course.pdf)

This four-line shape — build URL, `requests.get()`, check `status_code`, `.json()` — is the reusable skeleton for **any** integration with a third-party tool's API (CRM, accounting platform, e-commerce backend, etc.). This is the most directly reusable pattern in the book for client integration work.

## Reading the response

API responses are typically a dict with metadata keys plus a list of records:

```python
response_dict['total_count']        # often present for search-style endpoints
response_dict['items']              # the actual list of records
repo_dict['owner']['login']         # nested dicts are common — drill down by key
```
(source: python-crash-course.pdf)

The only reliable way to know what's in a response is to read the API's docs or print/inspect the keys directly (`sorted(repo_dict.keys())`) — there's no shortcut around exploring an unfamiliar API's shape before writing extraction code.

## Rate limits and reliability

- Most APIs cap requests per time window. Check a documented rate-limit endpoint (e.g., GitHub's `/rate_limit`) to see `limit`, `remaining`, and `reset` (Unix timestamp) before assuming a script can run unattended (source: python-crash-course.pdf).
- Many APIs require a registered API key/access token; unauthenticated calls (if allowed at all) usually have much lower limits.
- This matters directly for any unattended automation built for a client — a script that works in testing can silently start failing in production if it outpaces the API's limit.

## Chaining calls to aggregate data

Some APIs return a list of IDs from one endpoint, requiring a separate call per ID to get full details (Hacker News API example: `topstories.json` → list of IDs → `item/{id}.json` per ID):

```python
submission_ids = requests.get(top_url).json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    r = requests.get(f".../item/{submission_id}.json")
    response_dict = r.json()
    submission_dicts.append({
        'title': response_dict['title'],
        'comments': response_dict['descendants'],
    })
```
(source: python-crash-course.pdf)

- Wrap per-item processing in `try/except` for keys that aren't always present (e.g., some post types lack a `comments` field) — same defensive pattern as CSV row errors in [[data-visualization-python]].
- `sorted(list_of_dicts, key=itemgetter('field'), reverse=True)` (from `operator` module) is the standard way to sort a list of dicts by one of their values.

## From API data to deliverable

The same Plotly techniques from [[data-visualization-python]] apply directly to API-sourced data — e.g., turning a list of repos/stars into a bar chart, with `hover_name` for descriptions and HTML anchor tags (`<a href='url'>text</a>`) embedded in axis labels to make bars clickable links back to the source record (source: python-crash-course.pdf). This closes the loop: **pull via API → shape into lists → visualize → present as something a stakeholder can click through**, which is the same shape as a client-facing audit deliverable.

## Connects to

- [[data-visualization-python]] — the visualization half of the same pipeline; API data and downloaded-file data feed the same charting code once it's in plain Python lists.
- [[source-map]] — Python Crash Course's full entry (chapter→stage mapping) lives there; the FORGE-era whole-book hub page was archived 2026-07-07.

## Pathway Placement

- **Role**: support/project-source detail for **Stage 10** — this material is already on the Source Roster as "PCC Part II" in [[learning-path]]; this page is the pre-ingested detail for those chapters.
- **Prerequisites**: [[stages/stage-10-application-thinking]]; the APIs material pairs with [[concepts/apis-and-web-requests]], the visualization material with the Stage 10 capstone options.
- **Status**: parked until Chris reaches Stage 10 (see [[parking-lot]], APIs / web-scraping / image-graphs rows). No change to the mapped path needed — the Source Roster already accounts for these chapters.
