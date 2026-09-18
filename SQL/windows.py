import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# cur.execute("CREATE TABLE emp (name TEXT, dept TEXT, salary INTEGER)")
# cur.executemany("INSERT INTO emp VALUES (?, ?, ?)",[
#     ("Asha",  "Sales", 50000),
#     ("Bo",    "Sales", 70000),
#     ("Carol", "Sales", 60000),
#     ("Dev",   "Tech",  90000),
#     ("Eli",   "Tech",  90000),
#     ("Finn",  "Tech",  75000),
# ])

# query = """
# SELECT
#     name, 
#     dept, 
#     salary, 
#     ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rank_in_dept,
#     RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rank__,
#     DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dense_rank_ 
#     FROM emp
#     ORDER BY dept DESC, salary DESC
#     """

cur.execute("CREATE TABLE sales (month TEXT , revenue INTEGER)")
cur.executemany("INSERT INTO sales VALUES(?,?)",[
("jan", 100),
("feb", 150),
("mar", 120),
("apr", 200)
])

query = """
SELECT 
    month,
    revenue,
    SUM(revenue) OVER (ORDER BY month) AS Running_total,
    SUM(revenue) OVER () AS Grand_total
    FROM sales
    ORDER BY month
 """

for row in cur.execute(query):
    print(row)
conn.close()