# Write your MySQL query statement below
select users.name, sum(coalesce(distance, 0)) as travelled_distance from rides 
right join users on users.id = rides.user_id
group by user_id order by travelled_distance desc, name asc;