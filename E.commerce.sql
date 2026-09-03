

USE edb;

-- =========================================
-- 1. BUSINESS KPIs
-- =========================================

-- Total Revenue
SELECT SUM(total_amount) AS total_revenue
FROM ecommerce_sales;

-- Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM ecommerce_sales;

-- Total Customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM ecommerce_sales;

-- Total Profit
SELECT SUM(profit_margin) AS total_profit
FROM ecommerce_sales;

-- Average Profit per Order
SELECT AVG(profit_margin) AS avg_profit_per_order
FROM ecommerce_sales;


-- =========================================
-- 2. SALES BY CATEGORY
-- =========================================

SELECT
    category,
    SUM(total_amount) AS revenue
FROM ecommerce_sales
GROUP BY category
ORDER BY revenue DESC;


-- =========================================
-- 3. PROFIT BY CATEGORY
-- =========================================

SELECT
    category,
    SUM(profit_margin) AS profit
FROM ecommerce_sales
GROUP BY category
ORDER BY profit DESC;


-- =========================================
-- 4. SALES BY REGION
-- =========================================

SELECT
    region,
    SUM(total_amount) AS revenue
FROM ecommerce_sales
GROUP BY region
ORDER BY revenue DESC;


-- =========================================
-- 5. MONTHLY REVENUE
-- =========================================

SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(total_amount) AS revenue
FROM ecommerce_sales
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;


-- =========================================
-- 6. RETURN ANALYSIS
-- =========================================

-- Total returned orders
SELECT
    COUNT(DISTINCT order_id) AS returned_orders
FROM ecommerce_sales
WHERE returned = 'Yes';

-- Return rate
SELECT
    ROUND(
        SUM(returned = 'Yes') / COUNT(*) * 100,
        2
    ) AS return_rate_percentage
FROM ecommerce_sales;


-- =========================================
-- 7. RETURN RATE BY CATEGORY
-- =========================================

SELECT
    category,
    COUNT(*) AS total_orders,
    SUM(returned = 'Yes') AS returned_orders,
    ROUND(
        SUM(returned = 'Yes') / COUNT(*) * 100,
        2
    ) AS return_rate_percentage
FROM ecommerce_sales
GROUP BY category
ORDER BY return_rate_percentage DESC;


-- =========================================
-- 8. RETURN RATE BY REGION
-- =========================================

SELECT
    region,
    COUNT(*) AS total_orders,
    SUM(returned = 'Yes') AS returned_orders,
    ROUND(
        SUM(returned = 'Yes') / COUNT(*) * 100,
        2
    ) AS return_rate_percentage
FROM ecommerce_sales
GROUP BY region
ORDER BY return_rate_percentage DESC;


-- =========================================
-- 9. CUSTOMER RETENTION
-- =========================================

SELECT
    customer_id,
    COUNT(DISTINCT order_id) AS order_count
FROM ecommerce_sales
GROUP BY customer_id
ORDER BY order_count DESC;


-- Repeat customers
SELECT COUNT(*) AS repeat_customers
FROM (
    SELECT customer_id
    FROM ecommerce_sales
    GROUP BY customer_id
    HAVING COUNT(DISTINCT order_id) > 1
) AS repeat_customer_table;


-- One-time customers
SELECT COUNT(*) AS one_time_customers
FROM (
    SELECT customer_id
    FROM ecommerce_sales
    GROUP BY customer_id
    HAVING COUNT(DISTINCT order_id) = 1
) AS one_time_customer_table;


-- =========================================
-- 10. DISCOUNT VS PROFIT
-- =========================================

SELECT
    discount,
    COUNT(DISTINCT order_id) AS orders,
    SUM(total_amount) AS revenue,
    SUM(profit_margin) AS profit,
    AVG(profit_margin) AS avg_profit
FROM ecommerce_sales
GROUP BY discount
ORDER BY discount;


-- =========================================
-- 11. LOSS-MAKING ORDERS
-- =========================================

SELECT
    COUNT(DISTINCT order_id) AS loss_making_orders
FROM ecommerce_sales
WHERE profit_margin < 0;


-- Loss-making orders by discount
SELECT
    discount,
    COUNT(DISTINCT order_id) AS loss_making_orders
FROM ecommerce_sales
WHERE profit_margin < 0
GROUP BY discount
ORDER BY discount;


-- =========================================
-- 12. TOP 10 PRODUCTS BY REVENUE
-- =========================================

SELECT
    product_id,
    SUM(total_amount) AS revenue
FROM ecommerce_sales
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;


-- =========================================
-- 13. TOP 10 PRODUCTS BY PROFIT
-- =========================================

SELECT
    product_id,
    SUM(profit_margin) AS profit
FROM ecommerce_sales
GROUP BY product_id
ORDER BY profit DESC
LIMIT 10;


-- =========================================
-- 14. TOP 10 PRODUCTS BY QUANTITY
-- =========================================

SELECT
    product_id,
    SUM(quantity) AS total_quantity
FROM ecommerce_sales
GROUP BY product_id
ORDER BY total_quantity DESC
LIMIT 10;


-- =========================================
-- 15. TOP 10 CUSTOMERS BY REVENUE
-- =========================================

SELECT
    customer_id,
    SUM(total_amount) AS revenue
FROM ecommerce_sales
GROUP BY customer_id
ORDER BY revenue DESC
LIMIT 10;


-- =========================================
-- 16. SHIPPING COST BY CATEGORY
-- =========================================

SELECT
    category,
    AVG(shipping_cost) AS avg_shipping_cost,
    SUM(shipping_cost) AS total_shipping_cost,
    AVG(profit_margin) AS avg_profit
FROM ecommerce_sales
GROUP BY category
ORDER BY avg_shipping_cost DESC;


-- =========================================
-- 17. CATEGORY PERFORMANCE SUMMARY
-- =========================================

SELECT
    category,
    COUNT(DISTINCT order_id) AS orders,
    SUM(total_amount) AS revenue,
    SUM(profit_margin) AS profit,
    SUM(quantity) AS quantity
FROM ecommerce_sales
GROUP BY category
ORDER BY revenue DESC;