# Write your MySQL query statement below
SELECT
    ROUND(AVG(d.order_date = d.customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM
    Delivery d
INNER JOIN (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM
        Delivery
    GROUP BY
        customer_id
) AS first_orders
-- Join condition ensures we only consider the first order for each customer
ON d.customer_id = first_orders.customer_id
AND d.order_date = first_orders.first_order_date;