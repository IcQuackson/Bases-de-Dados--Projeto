DROP TABLE IF EXISTS
    d_product,
    d_date,
    replenishments,


    CASCADE;



CREATE TABLE d_product(
    id_product integer NOT NULL,
    ean VARCHAR(20) NOT NULL,
    category VARCHAR(80) NOT NULL
);

CREATE TABLE d_date (
  date_id integer NOT NULL,
  day integer NOT NULL,
  week_day varchar(9) NOT NULL,
  week integer NOT NULL,
  month integer NOT NULL,
  year integer NOT NULL
);

CREATE TABLE replenishments(
  id_product integer NOT NULL,
  date_id integer NOT NULL,
  units integer NOT NULL
);