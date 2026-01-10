
select stock_name,
case when operation = 'Buy' then -sum(price)
when operation ='Sell' then sum(price)
 end as capital_gain_loss
from stocks
group by stock_name, operation
