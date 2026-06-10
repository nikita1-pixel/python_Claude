import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("olist.db")

def run(label, query):
    print(f"\n--{label}--")
    print(pd.read_sql(query, conn))

customers = pd.read_csv("olist_customers_dataset.csv")
orders    = pd.read_csv("olist_orders_dataset.csv")
order_items = pd.read_csv("olist_order_items_dataset.csv")

customers.to_sql("customers", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)
order_items.to_sql("order_items", conn, if_exists="replace", index=False)

print(" dataset loaded")

run("rows counts", """
    SELECT 
        (SELECT COUNT(*) FROM customers) AS num_customers,
        (SELECT COUNT(*) FROM orders) AS num_orders
    """)

run("orders per state", """
    SELECT customers.customer_state,
        COUNT(*) AS num_orders
    FROM orders
    INNER JOIN customers
        ON orders.customer_id = customers.customer_id
    GROUP BY customers.customer_state
    ORDER BY num_orders DESC
    LIMIT 10
    """)

run("delivered orders per state", """
    SELECT customers.customer_state,
        COUNT(*) AS num_orders
    FROM orders
    INNER JOIN customers
        ON orders.customer_id = customers.customer_id
    WHERE orders.order_status ="delivered"
    GROUP BY customers.customer_state
    ORDER BY num_orders DESC
    LIMIT 10
    """)

run("states: orders vs real people(busy state only)", """
    SELECT customers.customer_state,
        COUNT(*)                                      AS num_orders,
        COUNT(DISTINCT customers.customer_unique_id)   AS unique_people
    FROM orders
    INNER JOIN customers
        ON orders.customer_id = customers.customer_id
    GROUP BY customers.customer_state
    HAVING num_orders > 2000
    ORDER BY num_orders DESC
    """)

run("revenue by state", """
    SELECT customers.customer_state,
        ROUND(SUM(order_items.price), 2) AS revenue
    FROM order_items
    INNER JOIN orders
        ON order_items.order_id = orders.order_id
    INNER JOIN customers
        ON orders.customer_id = customers.customer_id
    GROUP BY customers.customer_state
    ORDER BY revenue DESC
    LIMIT 10
""")

revenue = pd.read_sql("""
    SELECT customers.customer_state AS state,
        ROUND(SUM(order_items.price), 2) AS revenue
    FROM order_items
    INNER JOIN orders ON order_items.order_id = orders.order_id
    INNER JOIN customers ON orders.customer_id = customers.customer_id
    GROUP BY customers.customer_state
    ORDER BY revenue DESC
    LIMIT 10
""", conn)

plt.figure(figsize=(10, 6))
plt.bar(revenue["state"], revenue["revenue"], color="coral")
plt.title("Top 10 Brazillian states by revenue(Olist)")
plt.xlabel("state")
plt.ylabel("revenue")

plt.tight_layout()
plt.savefig("revenue_by_state.png")
print("cahrt saved")