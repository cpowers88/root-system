---
type: source-summary
status: parked
source_role: reference
difficulty: optional
source_file: raw/books/PythonforDataAnalysis.pdf
tags: [reference, programming, parked, tooling]
---

# IPython and Jupyter Basics

**Summary**: How to run Python interactively via the standard interpreter, IPython shell, and Jupyter notebook, plus IPython's productivity features (tab completion, object introspection with `?`).

**Sources**: PythonforDataAnalysis.pdf, Chapter 2 ("Python Language Basics, IPython, and Jupyter Notebooks")

**Last updated**: 2026-06-23

---

## Three ways to run Python

- **`python`** — the standard interpreter, invoked on the command line. Runs one statement at a time at the `>>>` prompt, or executes a `.py` file passed as its first argument (`python hello_world.py`).
- **`ipython`** — an enhanced interactive interpreter. Same idea, numbered `In [n]:` / `Out[n]:` prompts instead of `>>>`. Encourages an *execute-explore* workflow (run, look at the result, adjust) instead of *edit-compile-run*. The `%run somefile.py` magic command executes a file's code in the current IPython process, so all its variables and functions stay available afterward for live inspection.
- **Jupyter notebook** — a browser-based, cell-based document for code, Markdown text, and inline output, saved as a `.ipynb` file. Started with `jupyter notebook` in a terminal; works through *kernels* (language-specific backends — the Python kernel is built on IPython). Run a cell with Shift-Enter. Closing the browser tab does **not** stop the underlying Python process — use File → "Close and Halt" to actually end it.

Most data analysis code in this book (and in practice) is written and tested in IPython or Jupyter rather than run as standalone scripts, because of the next two features.

## Tab completion

Pressing Tab in IPython searches the current namespace for anything matching what's typed so far and shows matches in a dropdown — variables, built-in functions, object methods/attributes after a `.`, module contents after `import x; x.<Tab>`, even filesystem paths inside a string. It also completes function keyword argument names (with `=`). IPython hides underscore-prefixed (dunder/private) names from the default completion list to avoid clutter; type the leading underscore to see them.

## Object introspection (`?`)

Putting `?` before or after any variable, function, or module shows type, value, length, and docstring — this is *object introspection*, distinct from `print()`. For example, `b?` on a list shows its type and contents; `add_numbers?` on a user-defined function shows its docstring. `??` (not shown above but standard IPython behavior) goes further and shows source code when available. Combined with the wildcard `*`, `?` can search the whole namespace: `np.*load*?` lists every NumPy name containing "load" (`np.load`, `np.loads`, `np.loadtxt`).

## Key Ideas

- IPython/Jupyter are not separate languages — they're enhanced execution environments for the same Python. Nearly everything that works in one works in the other.
- `%run` plus tab completion is the core IPython loop: run a script, then explore its results interactively without restarting.
- `?` is the fastest way to check what a function actually does or what an object actually contains, without leaving the shell to look up documentation.

## Operational Use

This is the baseline environment for every Python task in an audit: pulling a client's CSV, testing a transformation, checking a function's behavior before trusting it in a script. `?` and tab completion specifically remove the need to context-switch to documentation mid-task, which matters when working live with a client or on a deadline.

## Connects to

- [[reading-writing-csv-with-pandas]] — every pandas workflow in this wiki assumes a live IPython/Jupyter session like the one described here.
- [[stages/stage-01-python-atoms]] — the language fundamentals exercised inside this same interactive environment (the book's own language-semantics page was archived as a duplicate of this vault's curriculum).

## Pathway Placement

- **Role**: optional tooling reference — interactive shell/notebook workflow. Nothing in Stages 0-10 requires Jupyter or IPython; the active path runs on VS Code + terminal per Stage 0.
- **Prerequisites**: none beyond [[stages/stage-00-setup-and-orientation]]; becomes genuinely useful only with the parked data-analysis strand.
- **Status**: parked per [[parking-lot]] alongside the pandas/NumPy material.
