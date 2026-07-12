---
type: error-log
stage: 06
status: draft
tags: [stage-06, errors, debugging]
---

# Stage 6 Common Errors

This stage is *about* errors, so this page leans more on process than a fixed list — but here are the four shapes Chris will run into most.

## 1. `FileNotFoundError`

```python
with open("missing.txt", "r") as f:
    print(f.read())
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
```

**Why it happens:** the file doesn't exist at the path given — often because of a relative-path mismatch (see [[glossary/file-path]]) or a typo in the filename.

**Fix:** double-check the path, or catch the error with `try`/`except FileNotFoundError:` if a missing file is an expected possibility.

## 2. Losing data by opening in the wrong mode

```python
with open("notes.txt", "w") as f:
    f.write("new note")
# any previous content in notes.txt is now gone
```

**No error** — but silent data loss.

**Why it happens:** `"w"` mode always starts the file fresh, erasing existing content immediately.

**Fix:** use `"a"` (append) mode if you want to add to existing content instead of replacing it.

## 3. Bare `except:` hiding the real bug

```python
try:
    result = some_function(data)
except:
    result = None
```

**No error shown to you** — but a real bug might be silently swallowed.

**Why it happens:** a bare `except:` catches absolutely everything, including bugs unrelated to what you intended to handle.

**Fix:** name the specific exception type you expect (`except ValueError:`, `except FileNotFoundError:`), so unexpected bugs still surface.

## 4. Semantic error — no message, wrong answer

```python
def average(numbers):
    total = sum(numbers)
    return total / len(number)   # typo: "number" instead of "numbers"
```

This actually *would* raise a `NameError` (since `number` doesn't exist) — a good reminder that some "semantic-looking" typos are still caught by Python. A true semantic error has no error at all:

```python
def average(numbers):
    return sum(numbers) / len(numbers) + 1  # off-by-one bug, runs fine, wrong answer
```

**Why it happens:** the code is completely valid Python — it just doesn't compute what was intended.

**Fix:** add `print()` statements at intermediate steps to see actual values, and compare against what you expected by hand.

## How to Read Any of These

1. Check whether you got an error message at all. If yes, read the **last line first**.
2. If no error message but wrong output — that's a semantic error; print intermediate values to investigate.
3. Ask: "Is this failure expected and recoverable?" If yes, consider `try`/`except` with the specific exception type. If you don't fully understand *why* it's failing yet, fix the cause first — don't just wrap it.

## Related

- [[concepts/file-paths-and-reading-writing]]
- [[concepts/exceptions-and-tracebacks]]
- [[concepts/debugging-process]]
