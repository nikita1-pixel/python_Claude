# Modern BI Pipeline — NovaMart (end-to-end enterprise BI project)

Goal: build the **entire modern BI architecture** from `curriculum/modern-bi-architecture.md`, layer by layer,
using free tools — so Nikita can say "I built this whole stack" in interviews.

Company (fictional): **NovaMart** — a retailer selling electronics/home/fashion across Indian + a few
international stores. International orders arrive in foreign currency → gives us real "business logic".

## The stack (enterprise equivalent in brackets)
| Layer | Our tool | Enterprise equivalent |
|-------|----------|----------------------|
| Source systems | messy CSV exports | SAP / Salesforce / ERP |
| ETL / ELT | Python + pandas | Azure Data Factory |
| Staging + Warehouse | **DuckDB** | Azure Synapse / Databricks / Snowflake |
| Transforms + business logic | **dbt** (dbt-duckdb) | stored procedures + transformation framework |
| Star schema + data tests | dbt models (facts + dims + views) + dbt tests | facts + dimensions + views + data quality |
| Semantic layer | Power BI model | Azure Analysis Services / Fabric |
| KPIs / security | DAX + RLS in Power BI | DAX + RLS in semantic layer |
| Dashboard | Power BI Desktop | Power BI |
| AI consumption | "Ask Your Data" (Python + Groq) | conversational BI (emerging) |
| Version control / CI/CD | Git + branches + README story | Azure DevOps CI/CD |

## The phases (one per session, each a working deliverable)
- [x] **Phase 0 — Source systems.** Generate messy raw ERP exports (orders, customers, products, stores).
- [ ] **Phase 1 — ETL/ELT → Staging.** Python loads raw files *untouched* into a DuckDB `staging` schema.
- [ ] **Phase 2 — Warehouse transforms with dbt.** Install dbt + dbt-duckdb; write dbt models that clean +
      apply business logic (currency → INR, dedupe, standardize) from `staging`. (dbt = the modern
      stand-in for stored procedures.)
- [ ] **Phase 3 — Star schema + data tests in dbt.** Build `dim_customer`, `dim_product`, `dim_store`,
      `dim_date`, `fact_sales` as dbt models; add dbt **tests** (not_null, unique, relationships) =
      data quality. Expose final **views**.
- [ ] **Phase 4 — Semantic layer.** Connect Power BI to the views, build relationships, DAX KPIs, RLS.
- [ ] **Phase 5 — Dashboard.** Build the visuals on the model.
- [ ] **Phase 6 — AI consumption layer.** "Ask Your Data" conversational analyst on top of the warehouse.
- [ ] **Phase 7 — Scale demo ("Too Big for Excel").** Load a millions-of-rows dataset (NYC Taxi / Olist)
      as Parquet and show DuckDB aggregating it in ~1 second — DuckDB's real superpower. Interview soundbite.
- [ ] **Phase 8 — CI/CD story + README.** Git structure, branches, architecture diagram, Dev→QA→Prod narrative.
- [ ] **Phase 9 (optional) — Cloud edition.** Lift the pipeline into Snowflake or query public data from S3.

## Why this stack wins (portfolio pitch)
Full BI architecture (interview gold) + **dbt** (trendy "modern data stack" keyword) + a **scale story**
(DuckDB's superpower) + an **AI layer** (differentiator) — all in ONE finished flagship. Most freshers
have none of this. FINISHING the spine beats starting five new ideas.

## Folder map
```
modern-bi-pipeline/
├── PROJECT-PLAN.md
├── source_systems/     raw ERP/CRM exports (Phase 0)
├── pipeline/           ETL scripts        (Phase 1)
├── warehouse/          SQL transforms + star schema (Phase 2-3)
├── semantic_and_bi/    Power BI + DAX + RLS notes  (Phase 4-5)
├── ai_layer/           Ask Your Data       (Phase 6)
└── novamart.duckdb     the warehouse file (created in Phase 1)
```
