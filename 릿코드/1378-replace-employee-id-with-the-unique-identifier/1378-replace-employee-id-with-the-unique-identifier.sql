# Write your MySQL query statement below
select unique_id, name from Employees as e
left outer join EmployeeUNI as eu on e.id = eu.id;
# left outer join
# left: driving table(결과값)
# right: driven table(서포터)