---
type: error-log
stage: 10
status: draft
tags: [errors, cli, testing, databases]
timeline: reference
---

# Stage 10 Common Errors

## 1. `argparse` "missing required argument" usage error

```bash
python greet.py
```

```text
usage: greet.py [-h] [--shout] name
greet.py: error: the following arguments are required: name
```

**Why it happens:** `name` was declared as a required positional argument, and the script was run without it.

**Fix:** this is `argparse` working correctly, not a bug — supply the argument: `python greet.py Chris`.

## 2. `AssertionError` from a failing test

```python
def test_add():
    assert add(2, 3) == 6   # wrong expected value
```

```text
AssertionError: assert 5 == 6
```

**Why it happens:** the test's expected value was wrong (or the function genuinely has a bug) — `pytest` reports exactly which assertion failed and what the actual value was.

**Fix:** check whether the test's expected value is correct, or whether the function itself has the bug — don't assume it's always the function.

## 3. `sqlite3.OperationalError` from a missing table

```python
cursor.execute("SELECT * FROM notes")
```

```text
sqlite3.OperationalError: no such table: notes
```

**Why it happens:** the table was never created (missing `CREATE TABLE`), or the database file path doesn't match what was used before.

**Fix:** make sure `CREATE TABLE IF NOT EXISTS ...` runs before any query against that table.

## 4. Tightly coupled code that can't be tested

```python
def run():
    name = input("Name? ")     # mixed together: getting input...
    print(f"Hello, {name}!")     # ...and producing output, in one function
```

**No traceback** — but this can't be unit tested without manually typing input during the test.

**Why it happens:** the input-gathering and the actual logic are mixed into one function, instead of separated.

**Fix:** pull the testable logic into its own function that takes plain arguments and returns a value, then have a separate, thin function handle the actual `input()`/`print()`:

```python
def greeting(name):          # testable — no input()/print() inside
    return f"Hello, {name}!"

def run():                     # not tested directly, just wires things together
    name = input("Name? ")
    print(greeting(name))
```

## How to Read Any of These

1. `argparse` usage errors → expected behavior when a required argument is missing; just supply it.
2. `AssertionError` → check both the test's expected value and the function itself.
3. `sqlite3.OperationalError` → check the table was actually created before querying it.
4. No error, but can't test something → suspect tightly coupled input/output and logic; separate them.

## Related

- [[concepts/cli-programs-and-argparse]]
- [[concepts/automated-testing-with-pytest]]
- [[concepts/databases-and-sqlite]]
