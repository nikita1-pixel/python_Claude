# Advanced Roadmap — Junior → Pro AI-Augmented Analyst

**Goal:** take Nikita from "advanced fresher" to **pro-level, AI-leveraged data analyst** — deep skills + proof projects that land a job.
**Pace:** ~2 hr/day, 5 days/week → ~10–11 weeks. Started 2026-08-12.
**Rule:** one concept at a time, build something every module, AI woven through, `/log-skill` every win.
**Domain:** mixed real-world (different dataset per module) for portfolio range.

Status key: ⬜ not started · 🔸 in progress · ✅ practised · 🏆 shipped project

---

## Module 1 — Core Python Mastery: AI-Ready Foundation (3 wk) 🔸
**Full working Python an AI developer actually uses** (not every CS corner — skip deep metaprogramming/heavy multiprocessing until needed).
- **1A Data structures deep:** lists/dicts/tuples/sets — when to use which, dict/set methods, nested structures & JSON, slicing, unpacking
- **1B Comprehensions:** list / dict / set / generator comprehensions
- **1C Functions pro:** `*args`/`**kwargs`, default-arg gotchas, lambda, `map`/`filter`, closures, `functools` (`lru_cache`, `partial`), **decorators**
- **1D Iterators & generators:** `yield`, lazy/streaming, memory efficiency
- **1E OOP depth:** classes, inheritance vs composition, **dunder methods**, `@property`, class/static methods, **dataclasses**
- **1F Robust code:** exceptions (custom), `with`/context managers, **type hints**, logging
- **1G Concurrency for AI:** threading vs async, **`asyncio`** (concurrent API/LLM calls), when to reach for multiprocessing
- **1H Tooling & ecosystem:** modules/packages, venv, **pytest**, REST APIs (`requests`/`httpx`), JSON, env vars/secrets
- **Build:** a small real Python package/CLI tool (e.g., an API-backed data fetcher) using OOP + generators + decorators + tests

## Module 2 — Advanced pandas & Data Wrangling (2 wk) ⬜
- `groupby().transform()` — group-level calcs row-aligned (≈ SQL window fn)
- reshaping: pivot / melt / stack / unstack
- method chaining + `.assign()` + `.pipe()`
- `.apply()` vs vectorization (why vectorized wins)
- time series: datetime index, resample, rolling windows
- **Build:** a reusable data-pipeline + automated report generator

## Module 2 — Advanced SQL for Analytics (1.5 wk) ⬜
- advanced window functions: running totals, moving averages, RANK, LAG/LEAD, NTILE
- CTEs incl. recursive; CASE logic; date/time functions
- analytics patterns: **cohort, funnel, retention, RFM segmentation**
- query optimization thinking (indexes, subquery vs CTE vs window)
- **Build:** an analytics SQL project answering real business questions (cohorts/retention)

## Module 3 — Advanced Excel + Power Query (1 wk) ⬜
- Power Query ETL (extract/transform/load in Excel)
- Power Pivot + DAX basics; data model
- dynamic arrays: FILTER, UNIQUE, SORT, SEQUENCE, LAMBDA
- interactive dashboard + advanced conditional formatting
- **Build:** a self-refreshing Excel dashboard from a messy source

## Module 4 — Dashboards + Data Storytelling (2 wk) ⬜
- star-schema data modeling
- advanced DAX: CALCULATE, FILTER context, time intelligence (YoY, MTD, running)
- drill-through, bookmarks, tooltips, Row-Level Security
- **storytelling framework:** audience → question → insight → so-what → action
- chart choice, executive summary, dashboard design principles
- **Build:** a narrative-driven Power BI dashboard + a written insight memo

## Module 5 — Statistics + ML Depth (2 wk) ⬜
- correlation vs causation, distributions, confidence intervals
- **hypothesis testing, A/B testing** (t-test, p-value, significance)
- regression + classification fundamentals, feature engineering
- honest model evaluation (she has some: precision/recall/ROC-AUC)
- **Build:** an A/B-test analysis + an upgraded predictive model with proper eval

## Module 6 — AI Automation & the AI-Augmented Analyst (2.5 wk) ⬜ — THE DIFFERENTIATOR
- LLM APIs deeper (she has Groq basics), prompt-engineering patterns
- structured output / data extraction with LLMs
- **RAG** (retrieval-augmented generation) over documents
- **natural-language-to-SQL**, AI agents that run analysis
- automating insights & reports with LLMs
- **Build → 🏆 FLAGSHIP CAPSTONE**

## 🏆 Flagship Capstone — "AI Analytics Assistant"
One deployed Streamlit app showing every skill:
connect data → auto-clean & profile (Python) → SQL analytics → interactive dashboard →
**AI layer** that answers natural-language questions about the data + auto-writes an insights summary.
→ portfolio centerpiece; the proof of "AI-augmented analyst."

---

### Progress log
- 2026-08-12: Roadmap created. Starting Module 1 (Advanced Python), mixed domains.
