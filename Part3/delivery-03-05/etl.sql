CREATE OR REPLACE FUNCTION load_product_dim()
    RETURNS VOID AS
$$
DECLARE
    product_id INTEGER;
    DECLARE
    current_p_ean VARCHAR(20);
    DECLARE
    current_p_category VARCHAR(80);
BEGIN
    product_id := 0;
    FOR current_p_ean, current_p_category IN
        SELECT P.ean, P.associated_to_name FROM product P
        LOOP
            INSERT INTO d_product(id_product,
                                  ean,
                                  category)
            VALUES (product_id,
                    current_p_ean, current_p_category);
            product_id := product_id + 1;
        END LOOP;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION load_date_dim()
    RETURNS VOID AS
$$
DECLARE
    date_value TIMESTAMP;
BEGIN
    date_value := '2013-01-01	00:00:00';
    WHILE date_value < '2030-01-01	00:00:00'
        LOOP
            INSERT INTO d_date(date_id,
                                day,
                                week_day,
                                week,
                                month,
                                year )
            VALUES (EXTRACT(YEAR FROM date_value) * 10000
                        + EXTRACT(MONTH FROM date_value) * 100
                        + EXTRACT(DAY FROM date_value),
                    EXTRACT(DAY FROM date_value),
                    TO_CHAR(date_value,'Day'),
                    EXTRACT(WEEK FROM date_value),
                    EXTRACT(MONTH  FROM date_value),
                    EXTRACT(YEAR FROM date_value));
            date_value := date_value + INTERVAL '1	DAY';
        END LOOP;
END;
$$ LANGUAGE plpgsql;

select load_date_dim();
select load_product_dim();

insert into replenishments
select id_product, date_id, units
from replenish_event re
    left outer join d_date dt on make_date(year,month,day) = DATE(re.instant)
    left outer join d_product dp on dp.ean = re.product_ean;