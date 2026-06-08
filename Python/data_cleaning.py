import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\Ecommerce-Sales-Analytics\Dataset\superstore.csv",
    encoding="latin1"
)

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print(df.dtypes)


# Create new columns

df["Year"] = df["Order Date"].dt.year

df["Month"] = df["Order Date"].dt.month_name()

df["Day"] = df["Order Date"].dt.day_name()

df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

print(df[["Order Date", "Ship Date", "Year", "Month", "Day", "Shipping Days"]].head())


print("\n===== BUSINESS KPIs =====")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
avg_order_value = total_sales / total_orders

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ${avg_order_value:,.2f}")


print("\n===== SALES BY CATEGORY =====")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)


print("\n===== PROFIT BY CATEGORY =====")

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(category_profit)

print("\n===== TOP 10 PRODUCTS =====")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print(monthly_sales.head())

import matplotlib.pyplot as plt

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12,5))
plt.plot(monthly_sales.index, monthly_sales.values)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig(
    r"C:\Users\HP\Desktop\Ecommerce-Sales-Analytics\Dashboard_Screenshots\monthly_sales_trend.png"
)

print("Chart saved successfully!")

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(region_profit)

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)