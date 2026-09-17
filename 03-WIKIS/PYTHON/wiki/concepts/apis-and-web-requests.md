---
type: concept
stage: 10
status: draft
source_refs: ["Automate the Boring Stuff Ch.13 (Web Scraping, light intro)"]
prerequisites: ["dictionaries", "csv-and-json"]
tags: [apis, web-requests]
timeline: reference
---

# Concept: APIs and Web Requests (Introductory Only)

## Plain-English Meaning

A **web request** is a program asking a server on the internet for data (or asking it to do something). An **API** (application programming interface) is a defined, structured way a website or service lets programs request its data — usually returning JSON (Stage 9's format) rather than a full web page.

## What Problem This Solves

Lots of useful data lives on the internet — weather, prices, public datasets. APIs let a program request exactly the data it needs in a structured format, instead of needing a human to browse a website.

## When To Use It

When a program needs current or external data that only exists on the internet, and a service offers an API for it.

## When Not To Use It

This vault keeps this topic introductory-only — actually building API-dependent programs (handling authentication, rate limits, error responses) is parked beyond Stage 10's current depth. Don't build a real project around this without more focused study first.

## Code Shape

```python
import requests   # third-party package — needs pip install requests

response = requests.get("https://api.example.com/data")
data = response.json()   # most APIs return JSON — ties directly to Stage 9
```

## Tiny Working Example

```text
(Conceptual only at this stage — making real requests requires
 a live API endpoint, which varies by service and often needs
 an account/API key. The shape above is what it looks like;
 actual hands-on use is parked until Chris wants to pursue it.)
```

## Beginner Mistakes

- Assuming every website offers an API — many don't, and "web scraping" (reading the raw page directly) is a different, more fragile technique covered lightly in Automate the Boring Stuff Ch.13.
- Forgetting that most APIs return JSON, which then uses everything from Stage 9's `json` concept directly.
- Not checking `response.status_code` to confirm the request actually succeeded before trying to use `.json()` on a failed response.

## Physical-World Anchor

An API is like a restaurant menu — a defined, structured list of what you can order (request) and in what format, rather than walking into the kitchen and taking whatever you find (scraping the raw page).

## Required Vocabulary

- [[glossary/api]]
- [[glossary/web-request]]

## Related Code Patterns

- (none — this concept is intentionally kept conceptual/introductory; see Parked Until Later)

## Drill

- [[drills/stage-10-application-practice]]

## Explain-Back Questions

1. What's the difference between an API and web scraping?
2. Why does an API response usually need `.json()` to be useful, connecting back to Stage 9?
3. Why does this vault keep this topic introductory rather than building a full project around it yet?

## Source Notes

- (source: Automate the Boring Stuff, 3rd Ed., Ch.13, "Web Scraping" — light conceptual mention only, full chapter remains parked per `wiki/parking-lot.md`)
