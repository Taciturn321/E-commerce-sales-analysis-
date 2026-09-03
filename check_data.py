import pandas as pd

df = pd.read_csv("ecommerce_sales.csv")

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATES ---")
print("Duplicate rows:", df.duplicated().sum())

print("\n--- UNIQUE VALUES ---")
print("Unique customers:", df["customer_id"].nunique())
print("Unique products:", df["product_id"].nunique())
print("Unique orders:", df["order_id"].nunique())

print("\n--- CATEGORIES ---")
print(df["category"].unique())

print("\n--- REGIONS ---")
print(df["region"].unique())

print("\n--- PAYMENT METHODS ---")
print(df["payment_method"].unique())

print("\n--- RETURN STATUS ---")
print(df["returned"].value_counts())

print("\n--- DATE RANGE ---")
print("Start:", df["order_date"].min())
print("End:", df["order_date"].max())