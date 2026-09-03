# E-Commerce Sales Analysis

## About the Project

This project is an analysis of e-commerce sales data to understand sales performance, profit, customer behavior, returns, discounts, and regional performance.

The data was cleaned and analyzed using Python, business queries were performed using MySQL, and the results were presented through an interactive Power BI dashboard.

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- MySQL
- Power BI

## Dataset

The dataset contains 34,500 e-commerce orders with information about customers, products, categories, prices, discounts, payment methods, order dates, regions, returns, shipping costs, and profit.

Some important figures from the dataset:

- Revenue: 5,865,293.05
- Profit: 970,019.41
- Orders: 34,500
- Customers: 7,903
- Return Rate: 5.52%

## Analysis Performed

### Python

Used Python and Pandas for data cleaning and exploratory analysis.

The analysis includes:

- Sales by category
- Profit by category
- Sales by region
- Monthly revenue
- Customer retention
- Return analysis
- Discount and profit analysis
- Loss-making orders
- Top products
- Shipping cost analysis

### MySQL

SQL was used to perform business-level analysis on the cleaned dataset.

The queries cover:

- Revenue and profit KPIs
- Category and regional sales
- Return rates
- Customer order frequency
- Discount vs profit
- Loss-making orders
- Top products
- Top customers
- Shipping costs

### Power BI

Created an interactive dashboard to view the main business metrics and analysis.

The dashboard includes:

- Revenue
- Profit
- Orders
- Customers
- Return rate
- Customer retention
- Category performance
- Regional performance
- Discount vs profit
- Shipping costs
- Loss-making orders
- Top customers and products

## Key Findings

- Electronics generated the highest revenue and profit.
- Grocery was the only category with an overall loss.
- Fashion had the highest return rate at 8.28%.
- 93.99% of customers were repeat customers.
- There were 6,104 loss-making orders.
- Average profit per order decreased as the discount increased.
- South had the highest revenue among the regions.
- Electronics had the highest average shipping cost.

## Project Structure

```text
E-commerce/
│
├── data/
│   ├── ecommerce_sales.csv
│   └── ecommerce_sales_cleaned.csv
│
├── python/
│   ├── check_data.py
│   ├── clean_data.py
│   └── eda.py
│
├── sql/
│   └── ecommerce_analysis.sql
│
├── powerbi/
│   └── dash b.pbix
│
├── images/
│   ├── sales_by_category.png
│   ├── profit_by_category.png
│   ├── sales_by_region.png
│   ├── customer_retention.png
│   ├── discount_vs_profit.png
│   └── monthly_revenue.png
│
└── README.md