# Python — from zero to job-ready, mentored by Claude

A self-contained **learn-Python system** you run inside [Claude Code](https://claude.com/claude-code) (VS Code). It turns Claude into a patient mentor with memory: persistent resume point, dated **verbatim** session logs, a reference shelf, and a knowledge checkpoint at the end of every phase.

**Who it's for:** anyone starting from zero who wants to *master Python to be hireable*. General-purpose Python — plain language, one concept at a time, build something every phase.

**Environment:** VS Code + Claude Code + Python 3.
**Pace that works:** ~2 hrs/day, ~5 days/week → realistically job-ready in **3–4 months**. Consistency beats marathons.

👉 **New here? Read [`APPLYING-THIS-YOURSELF.md`](APPLYING-THIS-YOURSELF.md) for setup, then [`VISION.md`](VISION.md) for the philosophy.**

---

## Why Python (the hook)

Python is the most-used language on Earth for a reason: it reads almost like English, so you spend your brain on *the problem*, not the punctuation. And it's the lingua franca of the things shaping the next decade:

- **Data & analytics** — pandas, the tool that turns a 50,000-row spreadsheet into three lines of code.
- **AI / ML** — every major model is trained and served with Python.
- **Automation** — the boring 2-hour task becomes a 2-second script you run forever.
- **Web & APIs** — backends, scrapers, bots, dashboards.

The possibilities are endless — the point of this track is to make you *dangerous*: able to sit down with a blank file and build the thing.

---

## Roadmap — 10 phases (each: why → learn → build → test)

| Phase | Focus | The build | Checkpoint |
|---|---|---|---|
| **0 · Setup & Why** | VS Code, the REPL, first script | "Hello, world" + a script that talks back | run a `.py` file unaided |
| **1 · Foundations** | variables, types, strings, numbers, I/O | a tiny interactive CLI tool | explain types & f-strings |
| **2 · Control flow** | if/elif/else, loops, break/continue | **number-guessing game** | trace a loop on paper |
| **3 · Data structures** | lists, dicts, tuples, sets, comprehensions | a contact book / word-counter | pick the right structure |
| **4 · Functions & modules** | `def`, args/kwargs, scope, imports, stdlib | a reusable toolkit module | write a clean function |
| **5 · Files, errors & formats** | open/read/write, `csv`, `json`, try/except | read a CSV → summarise it | handle a crashing file |
| **6 · OOP** | classes, objects, methods, inheritance | model a `BankAccount` / deck of cards | when to use a class |
| **7 · Data analysis (pandas)** | DataFrames, filter, groupby, merge, plot | analyse a real public dataset | answer 3 questions in pandas |
| **8 · Automation & tooling** | venv, pip, git, the debugger, tests, logging | a script that does a real chore | set up a clean project |
| **9 · Choose your quest** | scraping · API client · Streamlit app · bot | **a portfolio project** | ship something you'd show |

Phases 0+1 can run as **one fast-recap session** with a checkpoint — if it lands, move to Phase 2 at normal pace. The foundation is never skipped, just compressed.

---

## How to operate

1. Open this folder in VS Code and launch Claude Code. It auto-loads `CLAUDE.md` and tells you exactly where you left off.
2. Say **"start session"** (or "learn phase N") to begin. A dated file is created in `sessions/` and every explanation is logged **verbatim** — you re-read these to learn.
3. Say **"test me"** anytime for a checkpoint quiz on the current phase.
4. Say **"I built X"** → it goes in the **Wins log** in `memory/study-state.md`. That's the motivation engine.
5. Say **"wrap up"** to end — the resume point gets a full update so next time is a warm start.

## Folder map

```
.
├─ CLAUDE.md          — coaching brain (Claude reads this first)
├─ README.md          — this file
├─ VISION.md          — the philosophy / why this works
├─ APPLYING-THIS-YOURSELF.md — setup guide
├─ memory/
│  └─ study-state.md  — resume point, phase status, skills learned, wins log
├─ curriculum/        — phase guides (reference shelf; written as you reach each phase)
├─ sessions/          — dated verbatim session logs
├─ exercises/         — practice problems + solutions
├─ projects/          — the .py files you build
├─ reference/         — cheat sheets per topic
├─ resources.md       — curated external learning links
└─ glossary.md        — running term list
```
