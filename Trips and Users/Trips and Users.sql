# Write your MySQL query statement below

# Cleaner CTE solution
WITH TripStatus AS (
    SELECT
        request_at AS 'Day',
        t.status != 'completed' AS cancelled
    FROM 
        Trips t
        JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
        JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
    WHERE
        t.request_at BETWEEN
            '2013-10-01' AND '2013-10-03'
)
SELECT
    Day,
    ROUND(SUM(cancelled) / COUNT(cancelled), 2) AS 'Cancellation Rate'
FROM
    TripStatus
GROUP BY Day;


# Normal Join solution
-- SELECT
--     t.request_at AS 'Day',
--     ROUND(SUM(t.status != 'completed') / COUNT(*), 2) AS 'Cancellation Rate'
-- FROM 
--     Trips t
--     JOIN Users d ON d.users_id = t.driver_id
--     JOIN Users c on c.users_id = t.client_id
-- WHERE 
--     t.request_at BETWEEN
--         '2013-10-01' AND '2013-10-03'
--     AND c.banned = 'No'
--     AND d.banned = 'No'
-- GROUP BY t.request_at;