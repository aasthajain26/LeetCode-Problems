# Write your MySQL query statement below
with cte as (
select salary, dense_Rank() over( partition by departmentId order by salary desc )  as rn,
e.name as Employee , d.name as Department 
from  employee e
left join 
Department d on e.departmentId = d.id
)
select Department,  Employee , salary from cte where rn = 1