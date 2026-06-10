---
name: python-study-state
description: Persistent learning state for the Python track (zero to job-ready) — read this to resume
type: project
last-updated: 2026-06-10
session_number: 5
started: 2026-06-07
pace: ~2 hrs/day, ~5 days/week; sequence Phases 0→9; job-ready target ~3-4 months
---

# Python — Study State

> Fresh start. This file is the mentor's memory — it gets updated live during sessions so every restart is a warm continuation, not a cold start.

---

## ⚡ RESUME POINT
*(Read this first)*

**Last active:** 2026-06-10 (Session #5)
**Was working on:** Phase 6 OOP from zero — built `oops/bankacc.py`: BankAccount + SavingAccount (inheritance, super, methods, state). Passed checkpoint after vocab patch. Phase 6 = PRACTISED.
**Mid-concept:** No
**Next step:** 30-sec warm-up re-ask of OOP vocab (class vs object, __init__/self, inheritance — was shaky verbally). Then either (a) reach OOP MASTERED by refactoring part of the expense tracker into classes, or (b) start Phase 8 (venv, pip, requirements.txt, git, VS Code debugger, tests).
**Instant resume line:** "Welcome back Nikita — last time you nailed OOP and built an inherited BankAccount. Quick 30-sec vocab refresh, then we either turn the expense tracker into classes (to master OOP) or jump into Phase 8 tooling (venvs + the debugger). Which sounds good?"

---

## Phase Status

| Phase | Status | Last touched | Next step |
|---|---|---|---|
| 0 · Setup & Why Python | Mastered | 2026-06-07 | — |
| 1 · Foundations | Mastered | 2026-06-07 | — |
| 2 · Control flow | Mastered | 2026-06-07 | while/if/elif/break/continue used in expense tracker |
| 3 · Data structures | Mastered | 2026-06-07 | lists, dicts, list-of-dicts, groupby-with-dict |
| 4 · Functions & modules | Mastered | 2026-06-07 | 4 function types, params, return, docstrings |
| 5 · Files, errors & formats | Mastered | 2026-06-08 | csv.DictReader/Writer, os.path |
| 6 · OOP | Practised | 2026-06-10 | classes/objects/__init__/self/methods/inheritance done; master by using in a real project |
| 7 · Data analysis (pandas/SQL) | Mastered | 2026-06-09 | pandas + SQL JOINs (incl. 3-table chain on real Olist data + chart) done |
| 8 · Automation & tooling | Learning | 2026-06-08 | git used (repo pushed); next venv, debugger, tests |
| 9 · Choose your quest | Not started | — | portfolio project (Sales_Analysis.ipynb is a start) |

Phases: **Not started → Learning → Practised (passed checkpoint) → Mastered (used in a real build).**

---

## Skills Learned (running log)
*(Concepts the learner can do unaided — add as checkpoints pass)*
- Core Python: variables, types, f-strings, while/if/elif, break/continue
- Data structures: lists, dicts, list-of-dicts, manual groupby
- Functions: 4 types (action/transform/validate/orchestrate), params, return, docstrings
- File I/O: csv.DictWriter/DictReader, os.path.exists
- Pandas: read_csv, info/describe, fillna, str methods, filtering, groupby+agg, sort, value_counts
- Matplotlib: bar/pie charts, savefig
- SQL: SELECT/WHERE/GROUP BY/HAVING/ORDER BY/LIMIT
- SQL JOINs: INNER, LEFT, aggregate-across-join, COALESCE; reading syntax errors
- 3-table CHAIN JOIN on real data (items→orders→customers); COUNT(DISTINCT); WHERE vs HAVING
- Loading multiple real CSVs into SQLite (to_sql); capturing query into a DataFrame variable to chart it
- Debugging: current working directory / FileNotFound, ambiguous column (accidental self-join), reserved-word typos (order/group/select)
- OOP: classes & objects, `__init__`, `self`, methods, object state; inheritance with `super().__init__()`; debugging structural (indentation), value, and logic bugs

## Wins log (the payoff)
*(When the learner builds something real or uses Python for real — log date + what)*
- 2026-06-08 — Built full Expense Tracker project (CLI → Pandas → Matplotlib → SQLite → Jupyter notebook), pushed to GitHub
- 2026-06-08 — Self-debugged two SQL errors by reading the traceback (stray paren + GROUPBY typo)
- 2026-06-09 — Shipped a full real-data pipeline on Olist Kaggle set: 3-table chain JOIN → revenue by state → Matplotlib chart (`revenue_by_state.png`). Self-debugged 4 errors.
- 2026-06-10 — Learned OOP from zero and built a working inherited bank system (`oops/bankacc.py`: BankAccount + SavingAccount). Debugged 3 bug types in one session.

## Checkpoint Scores
*(Phase | date | score | gaps patched)*
- SQL JOINs | 2026-06-08 | 5/6 | aggregate+plain col ⇒ GROUP BY; COALESCE(SUM,0) for NULL→0
- Chain JOINs + chart | 2026-06-09 | core nailed (proven by build) | re-taught reserved-word typos + "assign-to-keep vs print"

## Open Questions
- [ ] Reinforce next time: aggregate (SUM/COUNT/AVG) + plain column ⇒ needs GROUP BY (missed once in checkpoint)
- [ ] Which Kaggle dataset for JOIN practice? (need one with 2+ linkable tables)
- [ ] Which "quest" appeals for Phase 9 — web scraping, an API client, a Streamlit dashboard, or a bot?

## Session Log Index
*(dated files in `sessions/`)*
- 2026-06-08 — `sessions/2026-06-08-sql-joins.md` — Session #3: SQL JOINs (INNER/LEFT/aggregate), checkpoint 5/6
- 2026-06-09 — `sessions/2026-06-08-kaggle-joins.md` — Session #4: 3-table chain JOIN on Olist + revenue chart; JOINs mastered
- 2026-06-10 — `sessions/2026-06-09-oop-basics.md` — Session #5: OOP from zero, BankAccount+SavingAccount inheritance; Phase 6 practised
