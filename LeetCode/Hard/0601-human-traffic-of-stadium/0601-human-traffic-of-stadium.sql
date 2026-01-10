# Write your MySQL query statement below
with cte as(select *,
case when people >= 100 then 1 else 0 end as flag 
from
Stadium
),
cte2 as( 
    select * , row_number() over(partition by flag order by id) as rn ,
     id - row_number() over(partition by flag order by id)  as difference 
     from cte
),
cte3 as (
select flag, difference,count(*) from cte2
group by flag, difference
having count(*)>=3
)
select t.id,t.visit_date,t.people from 
cte3 c 
join cte2 t
on c.flag = t.flag
and c.difference = t.difference 