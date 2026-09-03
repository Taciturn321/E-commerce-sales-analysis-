import pandas as pd

# Load the original dataset
df = pd.read_csv("ecommerce_sales.csv")

# Convert order_date from string to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Check the result
print(df.dtypes)
print("\nFirst 5 dates:")
print(df["order_date"].head())

print("\n--- NUMERICAL SUMMARY ---")
print(df[[
    "price",
    "discount",
    "quantity",
    "delivery_time_days",
    "total_amount",
    "shipping_cost",
    "profit_margin",
    "customer_age"
]].describe())

print("\n--- INVALID VALUES CHECK ---")

print("Price <= 0:", (df["price"] <= 0).sum())

print("Quantity <= 0:", (df["quantity"] <= 0).sum())

print("Discount < 0:", (df["discount"] < 0).sum())
print("Discount > 1:", (df["discount"] > 1).sum())

print("Delivery days < 0:", (df["delivery_time_days"] < 0).sum())

print("Customer age < 0:", (df["customer_age"] < 0).sum())
print("Customer age > 100:", (df["customer_age"] > 100).sum())

print("Total amount < 0:", (df["total_amount"] < 0).sum())


print("\n--- CATEGORY VALUES ---")
print(df["category"].value_counts())

print("\n--- PAYMENT METHODS ---")
print(df["payment_method"].value_counts())

print("\n--- REGIONS ---")
print(df["region"].value_counts())

print("\n--- RETURN STATUS ---")
print(df["returned"].value_counts())

print("\n--- GENDER ---")
print(df["customer_gender"].value_counts())

print("\n--- FINANCIAL CONSISTENCY CHECK ---")

# Calculate expected amount after discount
df["calculated_amount"] = (
    df["price"] * df["quantity"] * (1 - df["discount"])
)

# Difference between calculated and dataset amount
df["amount_difference"] = (
    df["total_amount"] - df["calculated_amount"]
)

print("Maximum difference:",
      df["amount_difference"].abs().max())

print("Rows with difference > 0.01:",
      (df["amount_difference"].abs() > 0.01).sum())

print("\n--- HIGHEST PROFIT VALUES ---")
print(
    df[["order_id", "price", "quantity", "discount",
        "total_amount", "profit_margin"]]
    .sort_values("profit_margin", ascending=False)
    .head(10)
)

# Remove temporary columns
df.drop(columns=["calculated_amount", "amount_difference"], inplace=True)

# Save cleaned dataset
df.to_csv("ecommerce_sales_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Final shape:", df.shape)