---
type: tool-capability
status: active
stage: 10
python_tools: [requests, json]
prerequisites: [dictionaries, functions, errors, json]
tags: [reference, programming, capability]
---

# Capability: Pull Data from the Internet (APIs)

## Real-World Problem

Weather for a dashboard, current prices, a list of GitHub repos — data that lives on someone else's server and updates constantly, so copying it by hand is pointless.

## Beginner Version

A script that calls one free, no-key API with `requests.get()`, converts the JSON response to a Python dictionary, and prints two or three fields from it.

## Python Tools Involved

- `requests.get(url)` — make the web request (third-party package, `pip install requests`).
- `response.json()` — JSON → Python dictionaries/lists.
- Dictionary access (`data["main"]["temp"]`) — dig out the fields.
- `response.status_code` / `try`/`except` — handle failures.

## Prerequisites

[[stages/stage-05-data-shapes]] (dictionaries), [[stages/stage-09-automation-bridge]] (JSON — [[concepts/csv-and-json]]), [[stages/stage-10-application-thinking]] — home concept: [[concepts/apis-and-web-requests]].

## Tiny Example

```python
import requests

r = requests.get("https://api.github.com/repos/python/cpython")
data = r.json()
print(data["full_name"], "-", data["stargazers_count"], "stars")
```

## Mini-Project Idea

API snapshot tool: call one public API, save the interesting fields to a CSV with a timestamp, and re-run it a few days in a row to build a tiny dataset.

## School Relevance

Low-medium — beyond the CSE syllabus, but dictionaries-in-practice reinforcement is strong.

## Future Business Relevance

High — supplier prices, review feeds, and public records all arrive via APIs; PCC Ch. 17 detail is pre-ingested in [[working-with-apis-python]].

## Advanced Version — Parked

API keys/authentication, rate limits, web *scraping* of HTML pages (ATBS Ch. 13, `bs4`), and charting API data (Plotly — [[data-visualization-python]]). All Stage 10+ per [[parking-lot]].
