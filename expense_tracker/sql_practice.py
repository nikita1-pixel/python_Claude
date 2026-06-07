import sqlite3
import pandas as pd
  
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()


# ── LOAD CSV INTO DATABASE ────────────────────────────────────────
df = pd.read_csv("sales.csv")
df.to_sql("sales", conn, if_exists="replace", index=False)
# "sales" = table name, if_exists="replace" = overwrite if already exists
print("Data loaded into sales.db ✓")
# helper run queris + print results

def run(label, query):
    print(f"\n── {label} ──")
    result = pd.read_sql(query, conn)   # runs SQL, returns a DataFrame
    print(result)


# see all data 
run(" ALL data(first 5)","SELECT * FROM sales LIMIT 5")

# filter 
run("north region only", """ SELECT product, total, salesperson FROM sales WHERE region = "North" """)

# multiple conditions
run("High vales + not required", """ SELECT product, total, region FROM sales WHERE total > 5000 AND returned = 0 ORDER BY total DESC """) 

# groupby
run("revenue by region", """ SELECT region, ROUND(SUM(total * (1 - returned)), 2) AS revenue, COUNT(*) AS num_sales FROM sales GROUP BY region ORDER BY revenue DESC """)

# group by multiple columns
run("Revenue by region + category", """ SELECT region, category, ROUND(SUM(total), 2) AS total_revenue FROM sales GROUP BY region, category ORDER BY region, total_revenue DESC """)


# having filter after grouping
run("categories with revenue > 60000", """ SELECT category, ROUND(SUM(total), 2) AS revenue FROM sales GROUP BY category HAVING revenue > 60000""") 

#  top saleperson
run("salesperson leaderboard", """ SELECT salesperson, ROUND(SUM(total * (1 - returned)), 2) AS revenue FROM sales GROUP BY salesperson ORDER BY revenue DESC  """)