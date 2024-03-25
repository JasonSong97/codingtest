-- 1
-- 애초에 join을 하는 순간부터 2019년에 해당하는 것만 가져온다
-- select u.user_id as buyer_id, u.join_date, count(o.order_id) as orders_in_2019 
-- from users as u
-- left join orders as o 
--     on u.user_id = o.buyer_id and year(o.order_date) = '2019'
-- group by u.user_id;

-- 2
SELECT u.user_id as buyer_id, u.join_date, COUNT(o.order_id) as orders_in_2019
FROM users AS u
LEFT JOIN orders AS o ON u.user_id = o.buyer_id
WHERE YEAR(o.order_date) = 2019 OR o.order_date IS NULL
GROUP BY u.user_id;
