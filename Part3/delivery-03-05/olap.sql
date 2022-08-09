select category, week_day, month, sum(units) as total_replenishments
from replenishments re
    join d_date dd on re.date_id = dd.date_id
    join d_product dp on re.id_product = dp.id_product
group by cube (category, week_day, month);