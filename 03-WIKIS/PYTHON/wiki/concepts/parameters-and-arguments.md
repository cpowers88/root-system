---
type: concept
stage: 04
status: draft
source_refs: ["Think Python Ch.3 (Parameters and Arguments, Variables and Parameters Are Local, Stack Diagrams)", "Python Crash Course Ch.8 (Passing Information to a Function)"]
prerequisites: ["defining-and-calling-functions"]
tags: [stage-04, parameters, arguments, scope]
---

# Concept: Parameters, Arguments, and Scope

## Plain-English Meaning

A **parameter** is a name listed in a function's definition — a placeholder for a value the function expects to receive. An **argument** is the actual value you pass in when you call the function. **Scope** describes where a variable can be seen and used — a variable created inside a function is **local** to it and disappears once the function finishes.

## What Problem This Solves

Without parameters, a function could only ever work with hardcoded values or variables from outside it. Parameters let a function be generic and reusable — the same function can act on different data each time it's called.

## When To Use It

Any time a function's behavior should depend on data that varies from call to call: a name to greet, a number to square, a price to discount.

## When Not To Use It

If a function never needs different input — it always does the exact same thing — it doesn't need parameters.

## Code Shape

```python
def function_name(parameter_name):
    # parameter_name acts like a variable, but only inside this function
    print(parameter_name)

function_name(argument_value)   # argument_value is assigned to parameter_name
```

## Tiny Working Example

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Chris")   # "Chris" is the argument; name is the parameter
greet("Alex")    # same function, different argument
```

## Beginner Mistakes

- Confusing the *name* in the function definition (parameter) with the *value* passed at the call site (argument) — they're related but not the same thing.
- Expecting a variable created inside a function to still exist or have changed outside it — local variables vanish when the function ends.
- Calling a function without the arguments it requires, causing a `TypeError` ("missing required positional argument").

## Physical-World Anchor

A parameter is a blank on a form ("Name: ____"). An argument is what you actually write in that blank. The blank itself is reusable — different people fill in different names on the same form.

## Required Vocabulary

- [[glossary/parameter]]
- [[glossary/argument]]
- [[glossary/scope]]

## Related Code Patterns

- [[code-patterns/function-with-parameter]]

## Drill

- [[drills/stage-04-function-writing]]

## Explain-Back Questions

1. What's the difference between a parameter and an argument?
2. If a function creates a variable inside its body, can code outside the function see or use that variable? Why or why not?
3. What error do you get if you call a function without enough arguments, and why?

## Source Notes

- (source: Think Python, 2nd Ed., Ch.3, "Parameters and Arguments," "Variables and Parameters Are Local," "Stack Diagrams")
- (source: Python Crash Course, 3rd Ed., Ch.8, "Passing Information to a Function," "Arguments and Parameters")
