# Write your MySQL query statement below
SELECT
    e.employee_id,
    e.name,
    COUNT(reports.employee_id) AS reports_count,
    ROUND(AVG(reports.age)) AS average_age
FROM Employees e
JOIN Employees reports ON e.employee_id = reports.reports_to
GROUP BY e.employee_id;