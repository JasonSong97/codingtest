# Write your MySQL query statement below
select 
    name
from salesperson
where sales_id not in (
    select sales_id from orders inner join company using(com_id) where name = 'RED'
)
order by name;