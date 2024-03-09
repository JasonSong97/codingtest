# Write your MySQL query statement below
select 
    c.name 
from 
    Customer as c
where
    c.referee_id != 2
or
    c.referee_id is null;

# using COALESCE
-- select name from Customer where coalesce(referee_id, 0) <> 2;