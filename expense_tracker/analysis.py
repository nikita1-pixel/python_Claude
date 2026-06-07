# import pandas as pd
# # LOAD
# df = pd.read_csv('expenses.csv')
# # EXPLORE
# print(df)
# print(df.shape)
# print(df.info())
# print(df.describe())
# # SELECT
# print(df['amount'])
# print(df[['description', 'category']])
# # filter
# expensive = df[df['amount'] > 50]
# drinks    = df[df['category'] == 'drinks']
# print(expensive)
# print(drinks)
# # groupby
# by_category = df.groupby('category')['amount'].sum()
# print(by_category)
# # more groupby
# print(df.groupby("category")['amount'].mean())
# print(df.groupby("category")['amount'].max())
# print(df.groupby("category")['amount'].min())
# print(df.groupby("category")['amount'].count())

# # sort
# print(df.sort_values('amount', ascending=False))

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')

print(df)
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
# HANDLING MISSING DATA 
print(df.isnull().sum())
df["region"] = df["region"].fillna("Unknown") 
df["salesperson"] = df["salesperson"].fillna("Unknown")
print(df.isnull().sum())

# # CLEANING INCONSIDTENT  DATA
print(df["product"].value_counts()) #spot duplicates
df["produt"] = df["product"].str.strip().str.title()
df["category"] = df["category"].str.strip().str.title()
print(df["product"].value_counts())

# NEW COLUMN
df["revenue"] = df["total"] * (1 - df["returned"])
print(df[["total","returned", "revenue"]].head(10))

# MULTIPLE FILTER CONDITONS 
high_value = df[(df["total"] > 5000) & (df["returned"] == 0)]
print(f"High value, not returned : {len(high_value)} rows")

north_electronics = df[(df["region"] =="North") & (df["category"] =="Electronics")]
print(north_electronics[["product", "total", "salesperson"]])

# GROUPBY -=== THE ANALYST CORE 
print(df.groupby("region")["revenue"].sum().sort_values(ascending=False))

# MULTIPLE AGGREGATIONS AT ONCE 
summary = df.groupby('category').agg(
    total_revenue = ('revenue', 'sum'),
    avg_price = ('price', 'mean'),
    num_sales = ('product', 'count'),
    returns = ('returned', 'sum')
)
print(summary)

# GROUP BY TWO COLUMNS  
print(df.groupby(['region', 'category'])['revenue'].sum())

# TOP PERFOMERS 
print(df.groupby("salesperson")["revenue"].sum().sort_values(ascending=False))

# VALUE COUNTS 
print(df['month'].value_counts())
print(df['returned'].value_counts())

# CHART 1 REVENUE BY REGION
print("--CHART 1 :REVENUE BY REGION-------------------------------")
region_revenue = df.groupby('region')['revenue'].sum().sort_values(ascending=False)

plt.figure(figsize= (8, 5))
plt.bar(region_revenue.index, region_revenue.values, color='blue') # type: ignore
plt.title("Revenue by Region")
plt.xlabel('Revenue')
plt.ylabel('Revenue $')
plt.tight_layout()
plt.savefig("region_revenue.png")
plt.show()


# CHART 2 TOP SALESPERSON
print("--CHART 2 : TOP SALESPERSON-------------------------------")
sales_rev = df.groupby("salesperson")["revenue"].sum().sort_values(ascending=False)

plt.figure(figsize= (8, 5))
plt.bar(sales_rev.index, sales_rev.values, color='blue') # type: ignore
plt.title("Top Salesperson")
plt.xlabel('Salesperson')
plt.ylabel('Revenue $')
plt.tight_layout()
plt.savefig("top_salesperson.png")
plt.show()

# CHART 3 CATEGPRY SPPLIT
print("--CHART 3 : CATEGORY SPPLIT-------------------------------")
category_revenue = df.groupby('category')['revenue'].sum().sort_values(ascending=False)

plt.figure(figsize= (8, 5))
plt.pie(category_revenue.values, labels=category_revenue.index, autopct='%1.1f%%', startangle=90) # pyright: ignore[reportArgumentType]
plt.title("Category Split")
plt.tight_layout()
plt.savefig("category_split.png")
plt.show()