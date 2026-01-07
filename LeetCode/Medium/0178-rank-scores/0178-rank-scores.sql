# Write your MySQL query statement below

with cte as (
SELECT *, DENSE_RANK() OVER( ORDER BY SCORE DESC) as rn
FROM Scores
)
select score, rn as 'rank' from cte order by rn ;