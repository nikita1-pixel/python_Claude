# Curriculum — roadmap & phase outlines

The reference shelf. Each phase's **full guide is written when we reach it** (kept emerging + logged live); this index holds the outline so the path is always visible.

Format per phase: **Why → Concepts → Build → Checkpoint.**

---

## Phase 0 · Setup & Why Python  → `phase-0-1-foundations.md`
- **Why:** can't learn to swim from the shore — get the environment running and feel the loop.
- **Concepts:** VS Code + Python extension, the terminal, `python3`, the REPL vs a `.py` file, comments, `print()`.
- **Build:** "Hello, world" + a script that prints a few lines about you.
- **Checkpoint:** run a `.py` file unaided; explain REPL vs script.

## Phase 1 · Foundations  → `phase-0-1-foundations.md`
- **Why:** every program is just data (values) and what you do to it.
- **Concepts:** variables, types (int/float/str/bool), strings + f-strings, numbers + operators, `input()`, type conversion (`int()`, `str()`).
- **Build:** a tiny interactive CLI tool (asks your name/age, talks back, does a calc).
- **Checkpoint:** explain types & f-strings; predict output of mixed-type expressions.

## Phase 2 · Control flow
- **Why:** programs that make decisions and repeat work.
- **Concepts:** `if/elif/else`, comparison + logical operators, `while`, `for`, `range`, `break`/`continue`.
- **Build:** the classic **number-guessing game** (random number, hints, attempt counter).
- **Checkpoint:** trace a loop by hand; spot an infinite loop.

## Phase 3 · Data structures
- **Why:** real data comes in collections, not single values.
- **Concepts:** lists, tuples, dicts, sets; indexing/slicing; looping over them; list/dict comprehensions; nesting.
- **Build:** a contact book (dict) or a word-frequency counter.
- **Checkpoint:** pick the right structure for a scenario; write a comprehension.

## Phase 4 · Functions & modules
- **Why:** stop repeating yourself; package logic you can reuse.
- **Concepts:** `def`, parameters/arguments, `return`, default + keyword args, `*args/**kwargs`, scope, `import`, a tour of the standard library (`random`, `math`, `datetime`).
- **Build:** a small reusable toolkit module you import into another file.
- **Checkpoint:** write a clean documented function; explain scope.

## Phase 5 · Files, errors & formats
- **Why:** programs that touch the real world read and write files — and don't crash when things go wrong.
- **Concepts:** `open`/`with`, read/write text, the `csv` module, `json`, file paths (`pathlib`), `try/except/finally`, raising errors.
- **Build:** read a CSV → compute a summary → write results to a new file.
- **Checkpoint:** handle a missing/malformed file gracefully.

## Phase 6 · OOP (object-oriented programming)
- **Why:** the model real codebases and job interviews are built on — bundle data + behaviour together.
- **Concepts:** classes vs objects, `__init__`, attributes, methods, `self`, inheritance, `__str__`/dunder basics, when *not* to use a class.
- **Build:** model a `BankAccount` (deposit/withdraw/balance) or a deck of cards.
- **Checkpoint:** decide when a class beats a dict; extend a class via inheritance.

## Phase 7 · Data analysis with pandas
- **Why:** the analyst superpower — 50,000 rows in three lines. Where Python crushes a spreadsheet.
- **Concepts:** `Series`/`DataFrame`, `read_csv`, selecting/filtering, `groupby`, sort, `merge`, missing data, a quick plot. (numpy basics alongside.)
- **Build:** load a real public dataset, answer 3 questions about it.
- **Checkpoint:** answer a fresh question in pandas unaided.

## Phase 8 · Automation & tooling (engineering basics)
- **Why:** turn a script into a real, shareable project — and look like someone who's done this before.
- **Concepts:** virtual environments (`venv`), `pip` + `requirements.txt`, project layout, the **VS Code debugger** (breakpoints), `logging`, intro to tests (`assert`/`pytest`), `git` commit/push.
- **Build:** a script that automates a genuine chore, set up as a clean repo.
- **Checkpoint:** set up a fresh venv + project from scratch.

## Phase 9 · Choose your quest → portfolio project
- **Why:** ship something you'd show an interviewer. This is the proof.
- **Pick one:** web scraping (`requests` + `BeautifulSoup`) · an **API client** (hit a real API, parse JSON) · a **Streamlit** mini-dashboard · a CLI app · a small bot.
- **Build:** the portfolio project, committed to GitHub with a README.
- **Checkpoint:** demo it; explain the code end-to-end.
