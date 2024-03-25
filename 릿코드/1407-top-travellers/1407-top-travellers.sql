# Write your MySQL query statement below
-- 사용자의 distance의 총합으로 컬럼을 뽑아내기
select name, sum(coalesce(distance, 0)) as travelled_distance
from users
left join rides on users.id = rides.user_id
group by user_id
order by travelled_distance desc, name asc