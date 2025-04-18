# Write your MySQL query statement below
SELECT name
FROM Employee 
WHERE id IN (
    -- Get managerIds that appear 5 times or more
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING count(managerId) >= 5
)