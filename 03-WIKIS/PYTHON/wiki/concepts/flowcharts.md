---
type: concept
stage: 07
status: draft
source_refs: ["Invent Your Own Computer Games Ch.7 (Designing Hangman with Flowcharts)"]
prerequisites: ["decomposition-and-pseudocode", "if-elif-else"]
tags: [flowcharts, program-design]
timeline: reference
---

# Concept: Flowcharts

## Plain-English Meaning

A **flowchart** is a diagram of a program's logic using shapes: rectangles for actions, diamonds for decisions (branches), and arrows showing the order things happen in. It's a visual alternative to pseudocode for planning, especially useful when there's a lot of branching.

## What Problem This Solves

Some programs have logic that's easier to *see* as a diagram than to read as a list of steps — especially anything with multiple decision points and different paths depending on the outcome (a game, a multi-step form).

## When To Use It

When a problem has several decision points and you're having trouble keeping the branches straight in your head or in plain pseudocode — sketch it as a flowchart instead.

## When Not To Use It

For a simple, mostly-linear sequence of steps, plain pseudocode is faster and just as clear — don't draw a flowchart for something with no real branching.

## Code Shape

```text
[Start] -> (Pick a random word) -> (Ask for a letter)
              |
       <Is the letter in the word?>
        /                      \
     Yes                        No
      |                          |
(Reveal the letter)      (Lose a guess)
      |                          |
       \                        /
      <Word fully revealed, or guesses gone?>
        /                          \
      Yes                           No
       |                             |
  [Show result]              (back to "Ask for a letter")
```

## Tiny Working Example

A flowchart isn't code — but each diamond in it maps directly to an `if`/`elif`/`else` once you start coding:

```python
if letter in secret_word:
    reveal_letter(letter)
else:
    guesses_left -= 1
```

## Beginner Mistakes

- Trying to flowchart every tiny detail instead of just the decision points — this makes the diagram cluttered and less useful.
- Drawing a flowchart that doesn't actually loop back where it should (forgetting an arrow back to "ask for a letter" until the game actually ends).
- Treating the flowchart as a one-time exercise instead of a tool to come back to when the logic gets confusing mid-build.

## Physical-World Anchor

A flowchart is like a "choose your own adventure" map — each diamond is a fork in the path, and the arrows show exactly where each choice leads.

## Required Vocabulary

- [[glossary/flowchart]]

## Related Code Patterns

- [[code-patterns/if-elif-else-decision-chain]] (this is what each flowchart diamond becomes in real code)

## Drill

- [[drills/stage-07-decompose-a-problem]]

## Explain-Back Questions

1. What does a diamond shape represent in a flowchart?
2. When would a flowchart be more useful than plain pseudocode?
3. Sketch a 4-step flowchart (on paper) for "decide what to wear based on the weather."

## Source Notes

- (source: Invent Your Own Computer Games with Python, 4th Ed., Ch.7, "Designing Hangman with Flowcharts")
