"""
Phase 0 — Source systems simulator.

In real life, data is BORN inside ERP/CRM systems (SAP, Salesforce) and exported as
messy files. We simulate that here: 4 raw exports with realistic mess (mixed date
formats, duplicates, blanks, multiple currencies, inconsistent casing). The rest of the
pipeline's job is to tame this. Run once: python 00_generate_source_data.py
"""
import csv
import os
import random
from datetime import date, timedelta

random.seed(42)  # fixed seed => same "random" data every run (reproducible)

OUT = os.path.join(os.path.dirname(__file__), "source_systems")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- stores (dimension source)
# A few international stores so orders arrive in foreign currency -> real business logic later.
stores = [
    (1, "NovaMart Pune",       "Pune",      "West",  "INR"),
    (2, "NovaMart Mumbai",     "Mumbai",    "West",  "INR"),
    (3, "NovaMart Delhi",      "Delhi",     "North", "INR"),
    (4, "NovaMart Bangalore",  "Bangalore", "South", "INR"),
    (5, "NovaMart Chennai",    "Chennai",   "",      "INR"),   # blank region (fix later)
    (6, "NovaMart Dubai",      "Dubai",     "Intl",  "AED"),
    (7, "NovaMart London",     "London",    "Intl",  "GBP"),
    (8, "NovaMart Singapore",  "Singapore", "Intl",  "SGD"),
]
with open(os.path.join(OUT, "stores_raw.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["store_id", "store_name", "city", "region", "local_currency"])
    w.writerows(stores)

# ---------------------------------------------------------------- products (dimension source)
# product names deliberately inconsistent casing -> standardize later
products = [
    (101, "wireless HEADPHONES", "Electronics", 1200, 3000),
    (102, "Mechanical Keyboard", "Electronics", 2500, 4500),
    (103, "gaming mouse",        "Electronics",  600, 1500),
    (104, "27in MONITOR",        "Electronics", 8000, 12000),
    (105, "USB-C Hub",           "Electronics",  900, 1800),
    (106, "Desk Lamp",           "Home",         300,  800),
    (107, "cushion set",         "Home",         400, 1200),
    (108, "Wall Clock",          "Home",         250,  900),
    (109, "Running SNEAKERS",    "Fashion",     1500, 2500),
    (110, "denim jacket",        "Fashion",     1800, 3000),
    (111, "Leather Wallet",      "Fashion",      500, 1400),
    (112, "Backpack",            "Fashion",      900, 2200),
]
with open(os.path.join(OUT, "products_raw.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["product_id", "product_name", "category", "cost_price", "list_price"])
    w.writerows(products)

# ---------------------------------------------------------------- customers (dimension source)
first = ["Aarav","Diya","Rohan","Isha","Kabir","Ananya","Vivaan","Sara","Arjun","Myra",
         "Reyansh","Aisha","Ved","Kiara","Ayaan","Riya","Dev","Tara","Ishaan","Nisha"]
last  = ["Sharma","Patel","Nair","Gupta","Reddy","Iyer","Singh","Mehta","Bose","Rao"]
cities = ["Pune","Mumbai","Delhi","Bangalore","Chennai","Dubai","London","Singapore"]
customers = []
for cid in range(1001, 1201):  # 200 customers
    name = f"{random.choice(first)} {random.choice(last)}"
    city = random.choice(cities)
    region = ""  # deliberately left blank -> derive from city later
    signup = date(2022, 1, 1) + timedelta(days=random.randint(0, 900))
    customers.append((cid, name, city, region, signup.strftime("%Y-%m-%d")))
with open(os.path.join(OUT, "customers_raw.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["customer_id", "name", "city", "region", "signup_date"])
    w.writerows(customers)

# ---------------------------------------------------------------- orders (FACT source, messy)
currency_of_store = {s[0]: s[4] for s in stores}
date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%d-%b-%Y"]  # mixed formats -> parse later
rows = []
oid = 5000
start = date(2023, 1, 1)
for _ in range(3000):
    oid += 1
    store_id = random.randint(1, 8)
    product_id = random.randint(101, 112)
    customer_id = random.randint(1001, 1200)
    qty = random.choice([1, 1, 2, 2, 3, 4, 5])
    unit_price = dict((p[0], p[4]) for p in products)[product_id]
    # in foreign stores, price is quoted in the local currency (smaller numbers)
    cur = currency_of_store[store_id]
    if cur == "AED":   unit_price = round(unit_price / 22.0, 2)
    elif cur == "GBP": unit_price = round(unit_price / 105.0, 2)
    elif cur == "SGD": unit_price = round(unit_price / 62.0, 2)
    d = start + timedelta(days=random.randint(0, 700))
    date_str = d.strftime(random.choice(date_formats))
    rows.append([oid, date_str, customer_id, store_id, product_id, qty, unit_price, cur])

# inject realistic MESS:
dupes = random.sample(rows, 120)          # 120 duplicate order rows
rows.extend([r[:] for r in dupes])
for r in random.sample(rows, 90):         # 90 rows: blank quantity
    r[5] = ""
for r in random.sample(rows, 60):         # 60 rows: blank price
    r[6] = ""
for r in random.sample(rows, 40):         # 40 rows: zero/negative qty (bad data)
    r[5] = random.choice([0, -1, -2])
random.shuffle(rows)

with open(os.path.join(OUT, "orders_raw.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["order_id","order_date","customer_id","store_id","product_id","quantity","unit_price","currency"])
    w.writerows(rows)

print("Source systems generated in:", OUT)
print(f"  stores_raw.csv     : {len(stores)} rows")
print(f"  products_raw.csv   : {len(products)} rows")
print(f"  customers_raw.csv  : {len(customers)} rows")
print(f"  orders_raw.csv     : {len(rows)} rows (incl. 120 duplicates + blanks + bad qty)")
