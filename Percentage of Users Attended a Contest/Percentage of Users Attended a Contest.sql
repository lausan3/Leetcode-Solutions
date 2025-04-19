# Write your MySQL query statement below
SELECT
    r.contest_id,
    ROUND(COUNT(r.user_id) * 100 /
        (SELECT COUNT(user_id) from Users)
        , 2) AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id ASC