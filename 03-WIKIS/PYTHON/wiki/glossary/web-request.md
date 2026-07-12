---
type: glossary-entry
stage: 10
status: draft
aliases: []
related_terms: ["api"]
---

# Web Request

## Plain-English Definition

A program asking a server on the internet for data, or asking it to perform an action.

## What Problem It Helps Solve

Lets a program access information or services that live outside the program itself, on the internet.

## When Chris Will See It

Introductory mention only at this stage — connected directly to APIs (Stage 10) and JSON (Stage 9).

## Code Example

```python
import requests
response = requests.get("https://example.com")
print(response.status_code)   # 200 means success
```

## Common Confusion

Always check `response.status_code` (or equivalent) before assuming a request succeeded — a failed request can still return a "response" object, just not the data you wanted.

## Physical-World Anchor

Mailing a letter and waiting for a reply — the request goes out, and the response (or lack of one) tells you what happened.

## Related Terms

- [[glossary/api]]

## Flashcard Q/A

**Front:** Why should you check a web request's status code before using its data?

**Back:** Because a failed request can still return a response object — the status code tells you whether it actually succeeded.
