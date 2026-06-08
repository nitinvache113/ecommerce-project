import pandas as pd

df = pd.read_csv(
    r"C:\Users\HP\Desktop\Ecommerce-Sales-Analytics\Dataset\superstore.csv",
    encoding="latin1"
)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()
df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

df.to_csv(
    r"C:\Users\HP\Desktop\Ecommerce-Sales-Analytics\Dataset\cleaned_superstore.csv",
    index=False
)

print("Cleaned dataset exported successfully!")