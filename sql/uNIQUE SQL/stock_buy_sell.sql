# Write your MySQL query statement below

select stock_name,sum(
    case when
    operation="Buy" then -price
    else
    price
    end
) as capital_gain_loss
from stocks
group by stock_name


# select b.stock_name,(s.sell_price-b.buy_price) as capital_gain_loss
# from
# (select stock_name,operation,sum(price) as buy_price
# from stocks
#  where operation='Buy'
#  group by stock_name,operation
# ) as b
# join
# (select stock_name,operation,sum(price) as sell_price
# from stocks
#  where operation = 'Sell'
#  group by stock_name,operation
# ) as s
# on b.stock_name=s.stock_name