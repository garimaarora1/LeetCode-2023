# Write your MySQL query statement below
select E.name, EU.unique_id from Employees E
left join EmployeeUNI EU
on E.id = EU.id