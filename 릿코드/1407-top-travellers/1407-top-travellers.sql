# Write your MySQL query statement below
-- 1
-- select name, sum(coalesce(distance, 0)) as travelled_distance
-- from users
-- left join rides on users.id = rides.user_id
-- group by user_id
-- order by travelled_distance desc, name asc

-- 2
SELECT DISTINCT u.name, 
IFNULL(SUM(distance) OVER (PARTITION BY user_id), 0) as travelled_distance 
FROM Rides r 
RIGHT JOIN Users u 
    ON r.user_id = u.id 
ORDER BY travelled_distance DESC, name