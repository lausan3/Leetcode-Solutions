# Write your MySQL query statement below
SELECT
    ROUND(AVG(IF(d.customer_pref_delivery_date = d.order_date, 100, 0)), 2) AS immediate_percentage
FROM (
    SELECT customer_id, min(order_date) AS order_date, customer_pref_delivery_date
    FROM Delivery
    GROUP BY customer_id
) AS d;