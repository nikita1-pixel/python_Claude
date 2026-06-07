import csv

import random

products =["laptop", "Phone", "Headphones", "monitor", "keyboard", "mouse","Charger"]
categories ={"laptop": "Electronics", "Phone": "Electronics", "Headphones": "Audio", "monitor": "Electronics", "keyboard": "Accessories", "mouse": "Accessories","Charger": "Accessories"}
regions =['North', 'South', 'East', 'West']
reps =['Aisha', 'Rahul', 'Nikita', 'Sofia', 'Liam']
months =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

rows =[]
for _ in range(120):
    product = random.choice(products)
    quantity = random.randint(1, 10)
    price = round(random.uniform(500, 1000), 2)
    rows.append({
        "month" : random.choice(months),
        "product": product,
        "category": categories[product],
        "quantity": quantity,
        "price": price,
        "total": round(quantity * price, 2),
        "region": random.choice(regions),
        "salesperson": random.choice(reps),
        "returned" : random.choice([0, 0, 0, 1])
    })
rows[10]['region'] = ""
rows[25]['salesperson'] = ""
rows[60]['region'] = ""

with open("sales.csv", 'w', newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated {len(rows)} rows -> sales.csv")