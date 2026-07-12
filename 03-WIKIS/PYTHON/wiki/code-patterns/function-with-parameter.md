---
type: code-pattern
stage: 04
status: draft
concepts: ["function", "def", "parameter", "argument", "scope"]
tags: [stage-04, functions, parameters]
---

# Code Pattern: Function With a Parameter

## Purpose

Write a function that does something different depending on the value it's given, instead of always acting on the exact same hardcoded data.

## Use This When

The same logic needs to run on different input each time it's used.

## Do Not Use This When

The function never needs to vary — it always does the exact same thing with no outside data. In that case, skip the parameter.

## Skeleton

```python
def function_name(parameter_name):
    # use parameter_name inside the body
    print(parameter_name)

function_name(some_value)
```

## Filled Example

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Chris")
greet("Alex")
```

## Step-by-Step Trace

1. `def greet(name):` creates the function and declares it expects one parameter, `name`.
2. `greet("Chris")` calls it, assigning `"Chris"` to `name` for this call only.
3. Inside the function, `name` behaves like a normal local variable holding `"Chris"`.
4. The next call, `greet("Alex")`, runs the same body again with `name` now holding `"Alex"` — completely independent of the previous call.

## Beginner Mistakes

- Calling the function without an argument when it requires one — `TypeError: missing 1 required positional argument`.
- Trying to use the parameter name outside the function — it doesn't exist there (see [[glossary/scope]]).
- Confusing the parameter name with the argument value when explaining the code out loud.

## Related Terms

- [[glossary/parameter]]
- [[glossary/argument]]
- [[glossary/scope]]

## Drill Link

- [[drills/stage-04-function-writing]]

## Flashcards To Create

- Already covered in [[flashcards/stage-04-functions]].
