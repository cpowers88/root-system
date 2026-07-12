---
type: error-log
stage: 09
status: draft
tags: [stage-09, errors, automation]
---

# Stage 9 Common Errors

## 1. `ModuleNotFoundError` from a missing package

```python
import pygame
```

```text
ModuleNotFoundError: No module named 'pygame'
```

**Why it happens:** `pygame` is a third-party package that wasn't installed — standard library modules like `os` or `csv` never need this step, but third-party ones do.

**Fix:** run `pip install pygame` in a terminal first.

## 2. `ValueError` from forgetting to skip a CSV header

```python
import csv
with open("scores.csv") as f:
    reader = csv.reader(f)
    total = 0
    for row in reader:
        total += float(row[1])   # crashes on the header row: "score" isn't a number
```

```text
ValueError: could not convert string to float: 'score'
```

**Why it happens:** the first row of most CSV files is a header (column names), not data — trying to convert `"score"` to a number fails.

**Fix:** call `next(reader)` once before the loop to skip the header row.

## 3. `FileNotFoundError` when moving into a folder that doesn't exist

```python
import shutil
shutil.move("file.txt", "new_folder/file.txt")
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'new_folder/file.txt'
```

**Why it happens:** `shutil.move()` doesn't create missing destination folders automatically.

**Fix:** create the folder first with `os.makedirs("new_folder", exist_ok=True)`.

## 4. `json.decoder.JSONDecodeError` from malformed JSON

```python
import json
with open("data.json") as f:
    data = json.load(f)
```

```text
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

**Why it happens:** the file is empty, isn't valid JSON, or has a syntax mistake (like a trailing comma) — JSON has stricter syntax rules than Python itself.

**Fix:** check the file actually contains valid JSON; an empty file or a typo from manual editing is a common cause.

## How to Read Any of These

1. `ModuleNotFoundError` → check whether the module is standard library (no install needed) or third-party (needs `pip install`).
2. `ValueError` from a CSV conversion → check whether the header row was skipped.
3. `FileNotFoundError` while moving/saving → check the destination folder actually exists first.
4. `JSONDecodeError` → check the file's contents are valid, complete JSON.

## Related

- [[concepts/modules-and-packages]]
- [[concepts/organizing-files-at-scale]]
- [[concepts/csv-and-json]]
