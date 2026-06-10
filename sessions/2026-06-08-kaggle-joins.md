---
session_number: 4
date: 2026-06-08
phase: 7
topic: Applying JOINs to a real Kaggle dataset (2+ linkable tables)
duration_min:
---

# Session 4 — Phase 7: JOINs on a real Kaggle dataset

**Goal of today:** Load 2+ real CSVs into SQLite, find their shared key, and answer real business questions by joining them — the portfolio-grade version of last session's skills.
**Files built:** (TBD — e.g. `kaggle_joins.py`)

---

## Live Log
> RULE: paste the FULL explanation verbatim — never summarise.

### Setup: choosing & downloading the dataset
> Why it matters: a JOIN dataset must have 2+ tables sharing a key column (e.g. customer_id in both orders and customers).

Recommended picks: Olist Brazilian E-Commerce (gold standard), Northwind, Chinook.
Dataset chosen: Olist Brazilian E-Commerce
Files: olist_customers_dataset.csv, olist_orders_dataset.csv, olist_order_items_dataset.csv (all in expense_tracker/, loaded into olist.db)

### What we did
- Loaded 2 then 3 real CSVs (99,441 rows each for customers/orders) into olist.db via to_sql
- Shared key found by Nikita: customer_id (customers↔orders), order_id (order_items↔orders)
- Queries written by Nikita (with blanks filled): orders per state, delivered orders per state (JOIN+WHERE), COUNT(DISTINCT unique_people)+HAVING, and the big one ↓

### Concept: 3-table CHAIN JOIN (revenue by state)
> Why: the price lives in order_items, the state in customers — must chain items→orders→customers to connect money to place.
`SELECT customers.customer_state, ROUND(SUM(order_items.price),2) AS revenue FROM order_items INNER JOIN orders ON order_items.order_id = orders.order_id INNER JOIN customers ON orders.customer_id = customers.customer_id GROUP BY customers.customer_state ORDER BY revenue DESC LIMIT 10`
**Output:** SP R$5.2M (>RJ+MG combined), RJ 1.82M, MG 1.58M... steep concentration.

### Bugs debugged this session (all read from the error by Nikita)
- FileNotFoundError → taught current working directory (bare filename = relative to where you RUN, not where the .py lives); fix: cd into folder
- ambiguous column → had written `INNER JOIN orders` (self-join by accident); fix: join to customers
- no such column: customer.x → typo, table is `customers` (plural)

### Concept clarified: separate files/databases
joins_practice.py↔joins_demo.db and kaggle_joins.py↔olist.db are independent. CSV→load(to_sql)→table-in-db→query. "CSV = ingredients on counter, load = into fridge(db), SQL = cooking."

---

## Mini-Checkpoint — chain JOINs + chart
| # | Question | Answer | ✓/✗ |
|---|---|---|---|
| 1 | Why 3 tables for revenue-by-state? | Correct: items→orders→customers chain; items has price, customers has state, orders is the bridge | ✓ |
| 2 | Cause of `near "order"` error | Didn't recall — re-taught: `order` is reserved keyword, typo of `orders`; lesson: weird error on order/group/select ⇒ suspect reserved-word typo | patched |
| 3 | Why `revenue = pd.read_sql` vs run() | Didn't know — re-taught: run() prints & discards; assigning to a variable KEEPS data so matplotlib/savefig can use it. "print = look, assign = keep" | patched |

**Score:** Core skill (chain JOIN) nailed + proven by full pipeline build. Q2/Q3 supporting details patched. **JOINs: MASTERED** (used in a real build).

---

## What I can now do unaided
- Load multiple real CSVs into a SQLite db (to_sql) and query them
- Find shared keys to link tables (customer_id, order_id)
- Write a 3-table CHAIN JOIN (items→orders→customers) + GROUP BY + SUM for revenue
- Capture a query into a DataFrame variable and plot/save it with Matplotlib
- Debug: CWD/FileNotFound, ambiguous column (accidental self-join), reserved-word typos

## Stuck on / open questions
- Reserved keywords (order/group/select) — recognise when an error means a typo'd table name
- "print vs keep": use `var = pd.read_sql(...)` when you need the data again (chart/save/calc)

## Next session starts with
Optional: RIGHT/FULL JOIN + self-JOIN concept; OR start Phase 6 (OOP) — the only foundational gap left before Phase 8 tooling. Recommend a quick chart-polish recap then OOP.

