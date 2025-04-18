# Write your MySQL query statement below
SELECT 
    p.product_id,
    ROUND(SUM(p.price * us.units) / SUM(us.units), 2) AS average_price
FROM UnitsSold us
LEFT JOIN Prices p 
    ON p.product_id = us.product_id
WHERE us.purchase_date 
    BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;