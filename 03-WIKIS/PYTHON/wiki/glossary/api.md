---
type: glossary-entry
stage: 10
status: draft
aliases: ["application programming interface"]
related_terms: ["web-request", "json"]
---

# API

## Plain-English Definition

A defined, structured way a website or service lets programs request its data — usually returning JSON rather than a full web page.

## What Problem It Helps Solve

Lets a program get exactly the data it needs in a predictable format, instead of needing a human to browse a website manually.

## When Chris Will See It

Introductory mention only at this stage — full hands-on API use is parked beyond Stage 10's current depth.

## Code Example

```python
import requests
response = requests.get("https://api.example.com/data")
data = response.json()
```

## Common Confusion

Not every website offers an API — some require web scraping (reading the raw page) instead, which is a different, more fragile technique.

## Physical-World Anchor

A restaurant menu — a defined, structured list of what you can request, in a known format.

## Related Terms

- [[glossary/web-request]]
- [[glossary/json]]

## Flashcard Q/A

**Front:** What format do most APIs return data in?

**Back:** JSON.
