# Write your MySQL query statement below
-- 1
-- select firstName, lastName, city, state from person left join address on person.personId = address.personId;

-- 2
select p.firstName, p.lastName, a.city, a.state from person p left join address a using (personId);