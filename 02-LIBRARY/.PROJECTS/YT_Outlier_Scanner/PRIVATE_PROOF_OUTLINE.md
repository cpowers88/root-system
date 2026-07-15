---
type: private-proof-outline
status: internal-only
tags: [revenue, youtube, scanner, tutorial]
created: 2026-07-14
---

# Private Proof — Free YouTube Topic Research Scanner

## Audience and Promise

**Audience:** A beginner who wants to research a YouTube topic without paid
tools.

**Promise:** Show how to build and use a free local scanner to find the exact
top videos for a topic and identify reachable small-channel breakouts.

## 8–12 Minute Structure

1. **Problem (0:00–1:00):** YouTube search shows recommendations, but it does
   not directly answer which stored topic results have the most views or which
   videos reached far beyond a channel's subscriber base.
2. **Free stack (1:00–2:00):** Claude Code for assisted development, Python's
   standard library, local SQLite storage, and the default free YouTube Data
   API quota. State that public view data measures attention, not revenue.
3. **One command (2:00–3:30):** Run
   `python scanner.py market-report --top 100 --rank views`. Explain that it is
   offline, does not load the API key, combines the defined market topics, and
   deduplicates the same video across searches.
4. **Exact result (3:30–5:30):** Show the combined market header and leading
   rows. Explain that Claude Code is one topic inside the market, not the entire
   report. Point out the title, channel, publish date, format, views,
   views/subscriber, category, and matched topics. Do not scroll through all 100
   on camera.
5. **What the metrics mean (5:30–8:30):** Compare total views with `breakout`
   ranking. Explain that velocity requires two real snapshots at least 24 hours
   apart and remains `n/a` until then.
6. **Limitations (8:30–10:00):** Search is a recent public-data sample, not a
   complete market census. Views are not earnings. Shorts and long-form behave
   differently. Results need human review, and no title/script should be copied.
7. **Close (10:00–12:00):** Recap the repeatable loop: discover a precise topic,
   save results, rank offline, return after 24+ hours for measured velocity, and
   make only original material based on work actually completed.

## Screen List

- Clean terminal working directory showing the single `topic-report` command.
- Exact topic-report output, including views and breakout metrics.
- SQLite file location: `YT_Outlier_Scanner\scanner.db` (do not open the external secret file).
- Review artifact:
  `03-WIKIS\REVENUE_LAB\wiki\yt-outlier-scanner-first-findings-2026-07-14.md`.

## Privacy Checklist

- [ ] Use a clean terminal working directory and clear command history first.
- [ ] Keep `C:\Users\chris\.root-secrets\YT_Outlier_Scanner.env` out of the file explorer, terminal, editor tabs, and recording.
- [ ] Never display, read aloud, paste, or record the API key.
- [ ] Show no private vault content beyond the approved report artifact.
- [ ] Show no family information or protected academic/submission material.
- [ ] Review every visible window, notification, path, and browser tab before
      recording.
- [ ] Demonstrate only behavior verified in the live tool.

## Production Timer

| Stage | Minutes |
|---|---:|
| Preparation | ____ |
| Recording | ____ |
| Editing | ____ |
| **Total added minutes** | **____ / 90 maximum** |

## Original Working Titles — Internal Only

1. **Internal only:** I Built a Free YouTube Topic Scanner with Python and SQLite
2. **Internal only:** Find YouTube Breakout Videos Without Paid Research Tools
3. **Internal only:** Claude Code + Python: My Local YouTube Research Workflow

These are working labels for the private proof, not approved public titles or
thumbnail directions.
