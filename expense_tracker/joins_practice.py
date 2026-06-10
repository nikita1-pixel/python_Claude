import sqlite3
import pandas as pd

# Fresh little database just for learning JOINs (kept separate from sales.db)
conn = sqlite3.connect("joins_demo.db")
cursor = conn.cursor()

# Same helper you already know: run a query, print it as a DataFrame
def run(label, query):
    print(f"\n── {label} ──")
    result = pd.read_sql(query, conn)
    print(result)


# ── BUILD TWO TINY TABLES ─────────────────────────────────────────
# Wipe them first so re-running the file doesn't pile up duplicates
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS orders")

# Table 1: customers — WHO they are
cursor.execute("""
    CREATE TABLE customers (
        customer_id INTEGER,
        name        TEXT,
        city        TEXT
    )
""")

cursor.executemany(
    "INSERT INTO customers VALUES (?, ?, ?)",
    [
        (1, "Aarav",  "Mumbai"),
        (2, "Priya",  "Delhi"),
        (3, "Rohan",  "Bengaluru"),
        (4, "Sneha",  "Pune"),     # Sneha exists but places NO orders
    ],
)

# Table 2: orders — WHAT they bought. Linked by customer_id (the shared key)
cursor.execute("""
    CREATE TABLE orders (
        order_id    INTEGER,
        customer_id INTEGER,
        product     TEXT,
        amount      REAL
    )
""")

cursor.executemany(
    "INSERT INTO orders VALUES (?, ?, ?, ?)",
    [
        (101, 1, "Keyboard", 1200.0),
        (102, 1, "Mouse",     500.0),   # Aarav ordered twice
        (103, 2, "Monitor",  9000.0),
        (104, 3, "Laptop",  55000.0),
        (105, 9, "Webcam",   2000.0),   # customer_id 9 has NO matching customer
    ],
)
conn.commit()
print("Two tables built ✓")

# Look at each table on its own first
run("customers table", "SELECT * FROM customers")
run("orders table",    "SELECT * FROM orders")


# ── CONCEPT 1: INNER JOIN ─────────────────────────────────────────
# Stitch the two tables together where customer_id matches in BOTH.
run("INNER JOIN — orders with customer names", """
    SELECT orders.order_id,
           customers.name,
           customers.city,
           orders.product,
           orders.amount
    FROM orders
    INNER JOIN customers
        ON orders.customer_id = customers.customer_id
""")
run("LEFT JOIN - every customer, even with no orders", """ SELECT customers.name, customers.city, orders.product, orders.amount FROM customers LEFT JOIN orders ON customers.customer_id = orders.customer_id """)

run("Total spent per customer", """
    SELECT customers.name, 
        ROUND(SUM(orders.amount), 2 ) AS total_spent
    FROM customers
    LEFT JOIN orders
        ON customers.customer_id = orders.customer_id
    GROUP BY customers.name
    ORDER BY total_spent DESC
""")
