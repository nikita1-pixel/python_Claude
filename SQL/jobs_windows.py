import sqlite3
import pandas as pd

df = pd.read_csv("jobs.csv")
conn = sqlite3.connect(":memory:")
df.to_sql("jobs", conn, index=False)

query = """
SELECT categor
y, title, company_name, publication_date
FROM(
    SELECT 
        category, title, company_name, publication_date,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY publication_date DESC) AS rn
    FROM jobs
)
WHERE rn = 1
ORDER BY category
"""
for row in conn.execute(query):
    print(row)
conn.close()