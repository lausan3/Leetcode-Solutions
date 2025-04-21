# Write your MySQL query statement below
SELECT
    ROUND(AVG(IF(customer_pref_delivery_date = order_date, 100, 0)), 2) AS immediate_percentage
FROM Delivery 
WHERE (customer_id, order_date) IN (
    SELECT customer_id, min(order_date)
    FROM Delivery
    GROUP BY customer_id
)
ORDER BY delivery_id ASC;