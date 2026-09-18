# Modern BI Architecture — Reference & Interview Sheet

> The real pipeline behind enterprise Business Intelligence. Source: Shivam Srivastava (12+ yrs data analytics) + Nikita's mentor notes.
> Revise this before ANY data-analyst interview. The interviewer cares about the **concept**, not the exact tool.

---

## The one-line truth
"Load a dataset → make a Power BI report" is only how *small-scale* BI works.
Real enterprise BI is a **pipeline** with two halves: a **Data Engineer** half and a **Data Analyst** half.
Being able to draw and explain the whole pipeline is what makes a fresher sound experienced.

---

## The pipeline (top to bottom)

```
        SOURCE SYSTEMS   (SAP, Salesforce, other ERP/CRM)   ← data is born here, raw
                │
   ══════════════ DATA ENGINEER's zone ══════════════
        ETL / ELT        (tool: Azure Data Factory / ADF)
                │
        STAGING LAYER    (raw dump, untouched safety copy)
                │
        DATA WAREHOUSE   (Azure Synapse / Databricks)
          ├ stored procedures  = SQL business logic (currency convert, joins, updates)
          ├ FACTS + DIMENSIONS = star schema
          └ final output = VIEWS
                │
   ══════════════ DATA ANALYST's zone (you) ══════════════
        SEMANTIC LAYER   (Azure Analysis Services / Microsoft Fabric)
          ├ import the warehouse views
          ├ DATA MODELING = relationships (1-to-many; bridge tables for many-to-many)
          ├ KPIs written in DAX
          └ ROW-LEVEL SECURITY (RLS)  ← set HERE, not in Power BI
                │  (DirectQuery / live connection — NOT Import; data too huge)
        POWER BI         (build visuals & dashboards only)
                │
        PUBLISH → WORKSPACE → business users (after UAT + docs)

   All changes flow: local repo → push → Pull Request → Dev → QA → Production
   via Azure DevOps CI/CD (platform team approves).
```

---

## Term glossary (define every one in an interview)

| Term | Plain meaning |
|------|--------------|
| **ERP / CRM** | Big business software (SAP = ERP, Salesforce = CRM) that produces data as it runs |
| **ETL** | Extract → Transform → Load: clean the data *before* storing it |
| **ELT** | Extract → Load → Transform: store first, clean later (common with cloud warehouses) |
| **ADF** | Azure Data Factory — the tool that runs the ETL/ELT pipelines |
| **Staging layer** | A landing area holding raw data untouched, before any transformation |
| **Data warehouse** | The big organized analytical store (Synapse, Databricks, Snowflake) |
| **Stored procedure** | Saved reusable SQL (business logic) you call by name inside the DB |
| **Fact table** | The transactions/events — the numbers you measure (amount, qty, order id) |
| **Dimension table** | The descriptive context you slice by (product, customer, date, region) |
| **Star schema** | Fact in the middle, dimensions around it — the standard warehouse model |
| **View** | A saved query that looks like a table; the warehouse's final output |
| **Materialized view** | A view whose result is physically stored (faster reads) |
| **Semantic layer** | Layer between warehouse and Power BI: modeling + KPIs + security, centralized & reused |
| **Data modeling** | Defining relationships between fact and dimension tables |
| **Bridge table** | Extra table that resolves a many-to-many relationship into two one-to-many |
| **DAX** | Data Analysis eXpressions — Power BI's formula language for KPIs |
| **Row-Level Security (RLS)** | Rule that limits which rows a user can see (e.g. a manager sees only their region) |
| **DirectQuery** | Power BI queries the source live instead of importing a copy (used for huge data) |
| **CI/CD** | Continuous Integration / Deployment — automated, reviewed promotion of changes |
| **Dev / QA / Prod** | The three environments changes move through before users see them |

---

## Where Nikita already owns this (real proof)

| Architecture layer | What I've actually done |
|--------------------|-------------------------|
| ETL / ELT | UrbanKart cleaning ticket — extracted a messy CSV, transformed (dedupe/dates/cities), loaded clean |
| Facts + Dimensions (star schema) | Netflix & Starbucks projects modeled fact + dimension tables |
| DAX KPIs | Lending Club Power BI dashboard — 4 DAX measures |
| Row-Level Security | (learning — will build for real in this project) |
| Version control / CI/CD | Git: local commits + push already used |

The only pieces I've *read about* vs *done*: warehouse tooling + the semantic layer. This project fixes that.

---

## The interview script (say this out loud)

> "Data originates in source systems like SAP or Salesforce. A data engineer moves it via ETL/ELT
> — say, Azure Data Factory — into a staging layer, then a data warehouse. In the warehouse, stored
> procedures apply the business logic and structure the data into facts and dimensions, exposed as views.
> On top of that sits a **semantic layer**, where I do the data modeling, define KPIs in DAX, and set
> row-level security — so the logic is centralized and secure. Power BI connects to that via DirectQuery
> and I build the visuals. Every change is version-controlled and promoted Dev → QA → Prod through a
> CI/CD pipeline in Azure DevOps."

Then back it with a real example from your own project.

---

## Honest caveat (don't get caught)
This is the **Microsoft / Azure** version. Other shops swap tools:
- Warehouse: **Snowflake / BigQuery** instead of Synapse
- Transform: **dbt** instead of stored procedures
- BI: **Tableau / Looker** instead of Power BI

The **shape is always the same**: source → ingest → warehouse → model/semantic → consume → govern with CI/CD.
Learn the shape; tool names are interchangeable. If asked about a tool you don't know:
*"I've worked the concept in [X]; the principle transfers."*

---

## Where the AI layer fits (Nikita's edge)
Conversational "Ask Your Data" / AI analyst tools are the **newest consumption layer** — an emerging
alternative to Power BI that sits on top of the same semantic layer / warehouse. Not a replacement for
this architecture; a new floor added on top. Strong interview line:
*"I understand the classic BI stack, and I've also built the AI-native consumption layer coming next."*
