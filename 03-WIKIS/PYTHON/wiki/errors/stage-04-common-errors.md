---
type: error-log
stage: 04
status: draft
tags: [errors, debugging-preview]
timeline: reference
---

# Stage 4 Common Errors

## 1. `TypeError` from missing arguments

```python
def greet(name):
    print(f"Hello, {name}!")

greet()
```

```text
TypeError: greet() missing 1 required positional argument: 'name'
```

**Why it happens:** the function defines a parameter (`name`) that must be supplied, but the call didn't provide one.

**Fix:** supply the argument: `greet("Chris")`.

## 2. `NameError` from using a parameter outside its function

```python
def square(n):
    return n * n

print(n)
```

```text
NameError: name 'n' is not defined
```

**Why it happens:** `n` is a local variable, scoped only to inside `square()`. It doesn't exist outside the function at all.

**Fix:** if you need the value outside, capture the *return value* in a variable at the call site: `result = square(4)`, then use `result`.

## 3. Using a void function's "result"

```python
def shout(message):
    print(message.upper() + "!!!")

result = shout("hello")
print(result + " more text")
```

```text
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```

**Why it happens:** `shout()` never uses `return`, so it returns `None` by default. `result` ends up holding `None`, which can't be combined with a string.

**Fix:** add `return` to the function if you actually need to use its result afterward, or don't try to use the result of a void function.

## 4. Code after `return` never running

```python
def check(n):
    if n > 0:
        return "positive"
        print("this never prints")
    return "not positive"
```

**No error** — but the `print()` line is unreachable and will never run.

**Why it happens:** `return` exits the function immediately — anything after it in the same block is dead code.

**Fix:** move any code that must run before the `return`, above the `return` line.

## How to Read Any of These

1. `TypeError: missing ... argument` → check the function call has all the arguments the definition requires.
2. `NameError` involving a name that looks like a parameter → that variable is local to a function and isn't visible where you're trying to use it.
3. Unexpected `None` showing up → check whether the function you called actually has a `return` statement.

## Related

- [[concepts/defining-and-calling-functions]]
- [[concepts/parameters-and-arguments]]
- [[concepts/return-values]]
