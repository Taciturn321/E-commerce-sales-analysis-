import pandas as pd

# Load cleaned data
df = pd.read_csv("ecommerce_sales_cleaned.csv")

# Convert date
df["order_date"] = pd.to_datetime(df["order_date"])

# -------------------------------
# 1. BASIC BUSINESS KPIs
# -------------------------------

total_revenue = df["total_amount"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
total_profit = df["profit_margin"].sum()

print("===== BUSINESS KPIs =====")
print("Total Revenue:", round(total_revenue, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Total Profit:", round(total_profit, 2))


# -------------------------------
# 2. SALES BY CATEGORY
# -------------------------------

category_sales = (
    df.groupby("category")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY CATEGORY =====")
print(category_sales)


# -------------------------------
# 3. SALES BY REGION
# -------------------------------

region_sales = (
    df.groupby("region")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY REGION =====")
print(region_sales)

import matplotlib.pyplot as plt

# -------------------------------
# 4. SALES BY CATEGORY - BAR CHART
# -------------------------------

plt.figure(figsize=(10, 6))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# -------------------------------
# 5. SALES BY REGION - BAR CHART
# -------------------------------

plt.figure(figsize=(10, 6))

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()

import matplotlib.pyplot as plt

# -------------------------------
# 4. SALES BY CATEGORY
# -------------------------------

plt.figure(figsize=(10, 6))

category_sales.sort_values().plot(kind="barh")

plt.title("Total Sales by Category")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.tight_layout()

plt.savefig("sales_by_category.png", dpi=150)
plt.show()


# -------------------------------
# 5. SALES BY REGION
# -------------------------------

plt.figure(figsize=(10, 6))

region_sales.sort_values().plot(kind="barh")

plt.title("Total Sales by Region")
plt.xlabel("Total Sales")
plt.ylabel("Region")
plt.tight_layout()

plt.savefig("sales_by_region.png", dpi=150)
plt.show()

# -------------------------------
# 6. MONTHLY REVENUE TREND
# -------------------------------

# Group sales by month
monthly_sales = (
    df.groupby(df["order_date"].dt.to_period("M"))["total_amount"]
    .sum()
)

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

# Convert period to string for plotting
monthly_sales.index = monthly_sales.index.astype(str)

# Create line chart
plt.figure(figsize=(12, 6))

plt.plot(monthly_sales.index, monthly_sales.values, marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("monthly_revenue.png", dpi=150)
plt.show()

# -------------------------------
# 7. CUSTOMER ANALYSIS
# -------------------------------

customer_orders = (
    df.groupby("customer_id")["order_id"]
    .nunique()
)

print("\n===== CUSTOMER ORDER ANALYSIS =====")

print("Average orders per customer:",
      round(customer_orders.mean(), 2))

print("Maximum orders by one customer:",
      customer_orders.max())

print("\nTop 10 customers by number of orders:")
print(customer_orders.sort_values(ascending=False).head(10))


# -------------------------------
# CUSTOMER REVENUE
# -------------------------------

customer_revenue = (
    df.groupby("customer_id")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== CUSTOMER REVENUE =====")

print("Average revenue per customer:",
      round(customer_revenue.mean(), 2))

print("\nTop 10 customers by revenue:")
print(customer_revenue.head(10)) 

# -------------------------------
# 8. ONE-TIME VS REPEAT CUSTOMERS
# -------------------------------

customer_order_counts = (
    df.groupby("customer_id")["order_id"]
    .nunique()
)

one_time_customers = (
    customer_order_counts == 1
).sum()

repeat_customers = (
    customer_order_counts > 1
).sum()

print("\n===== CUSTOMER RETENTION ANALYSIS =====")

print("One-time customers:", one_time_customers)

print("Repeat customers:", repeat_customers)

print(
    "Repeat customer percentage:",
    round((repeat_customers / total_customers) * 100, 2),
    "%"
)

# -------------------------------
# 9. ONE-TIME VS REPEAT CUSTOMERS
# -------------------------------

customer_types = pd.Series({
    "One-time Customers": one_time_customers,
    "Repeat Customers": repeat_customers
})

plt.figure(figsize=(8, 5))

customer_types.plot(kind="bar")

plt.title("One-Time vs Repeat Customers")
plt.xlabel("Customer Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("customer_retention.png", dpi=150)
plt.close()

print("\nCustomer retention chart saved!")



# -------------------------------
# 10. RETURN ANALYSIS
# -------------------------------

# Overall return rate
return_counts = df["returned"].value_counts()

return_rate = (
    (df["returned"] == "Yes").sum() / len(df)
) * 100

print("\n===== RETURN ANALYSIS =====")

print("Total returned orders:",
      (df["returned"] == "Yes").sum())

print("Total non-returned orders:",
      (df["returned"] == "No").sum())

print("Overall return rate:",
      round(return_rate, 2), "%")


# -------------------------------
# RETURNS BY CATEGORY
# -------------------------------

returns_by_category = (
    df.groupby("category")["returned"]
    .apply(lambda x: (x == "Yes").sum())
    .sort_values(ascending=False)
)

print("\n===== RETURNS BY CATEGORY =====")
print(returns_by_category)


# -------------------------------
# RETURN RATE BY CATEGORY
# -------------------------------

return_rate_category = (
    df.groupby("category")["returned"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

print("\n===== RETURN RATE BY CATEGORY =====")
print(return_rate_category.round(2))


# -------------------------------
# RETURNS BY REGION
# -------------------------------

returns_by_region = (
    df.groupby("region")["returned"]
    .apply(lambda x: (x == "Yes").sum())
    .sort_values(ascending=False)
)

print("\n===== RETURNS BY REGION =====")
print(returns_by_region)


# -------------------------------
# RETURN RATE BY REGION
# -------------------------------

return_rate_region = (
    df.groupby("region")["returned"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

print("\n===== RETURN RATE BY REGION =====")
print(return_rate_region.round(2))



# ============================================================
# 11. PROFIT ANALYSIS
# ============================================================

profit_by_category = (
    df.groupby("category")["profit_margin"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PROFIT BY CATEGORY =====")
print(profit_by_category.round(2))


# Profit by region
profit_by_region = (
    df.groupby("region")["profit_margin"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PROFIT BY REGION =====")
print(profit_by_region.round(2))


# Average profit per order
average_profit = df["profit_margin"].mean()

print("\nAverage profit per order:",
      round(average_profit, 2))


# Negative profit orders
loss_orders = (
    df["profit_margin"] < 0
).sum()

print("Orders with negative profit:", loss_orders)


# Profit chart by category
plt.figure(figsize=(10, 6))

profit_by_category.sort_values().plot(kind="barh")

plt.title("Total Profit by Category")
plt.xlabel("Total Profit")
plt.ylabel("Category")

plt.tight_layout()
plt.savefig("profit_by_category.png", dpi=150)
plt.close()


# ============================================================
# 12. PRODUCT ANALYSIS
# ============================================================

product_sales = (
    df.groupby("product_id")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== PRODUCT ANALYSIS =====")

print("Total unique products:",
      df["product_id"].nunique())

print("\nTop 10 products by revenue:")

print(product_sales.head(10))


# Product quantity
product_quantity = (
    df.groupby("product_id")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 products by quantity sold:")

print(product_quantity.head(10))


# Product profit
product_profit = (
    df.groupby("product_id")["profit_margin"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 products by profit:")

print(product_profit.head(10))


# ============================================================
# 13. CATEGORY PERFORMANCE SUMMARY
# ============================================================

category_summary = (
    df.groupby("category")
    .agg(
        orders=("order_id", "nunique"),
        revenue=("total_amount", "sum"),
        profit=("profit_margin", "sum"),
        quantity=("quantity", "sum")
    )
    .sort_values("revenue", ascending=False)
)

print("\n===== CATEGORY PERFORMANCE SUMMARY =====")

print(category_summary.round(2))


# ============================================================
# 14. DISCOUNT VS PROFIT ANALYSIS
# ============================================================

discount_profit = (
    df.groupby("discount")
    .agg(
        orders=("order_id", "nunique"),
        revenue=("total_amount", "sum"),
        profit=("profit_margin", "sum"),
        avg_profit=("profit_margin", "mean")
    )
    .sort_index()
)

print("\n===== DISCOUNT VS PROFIT =====")
print(discount_profit.round(2))


# ============================================================
# 15. LOSS ORDERS BY DISCOUNT
# ============================================================

loss_by_discount = (
    df[df["profit_margin"] < 0]
    .groupby("discount")
    .size()
)

print("\n===== LOSS-MAKING ORDERS BY DISCOUNT =====")
print(loss_by_discount)


# ============================================================
# 16. SHIPPING COST ANALYSIS
# ============================================================

shipping_analysis = (
    df.groupby("category")
    .agg(
        avg_shipping_cost=("shipping_cost", "mean"),
        total_shipping_cost=("shipping_cost", "sum"),
        avg_profit=("profit_margin", "mean")
    )
    .sort_values("avg_profit")
)

print("\n===== SHIPPING COST BY CATEGORY =====")
print(shipping_analysis.round(2))


# ============================================================
# 17. DISCOUNT VS PROFIT CHART
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    discount_profit.index,
    discount_profit["avg_profit"],
    marker="o"
)

plt.title("Average Profit vs Discount")
plt.xlabel("Discount")
plt.ylabel("Average Profit")

plt.tight_layout()

plt.savefig("discount_vs_profit.png", dpi=150)
plt.close()