-- A    List all products (EAN and description) that have been replenished in more than 15 units, after 25/04/2021 in the “Milk” category

SELECT ean, descr
FROM product
WHERE ean in (SELECT product_ean
              FROM replenish_event
              WHERE product_ean IN (SELECT ean FROM product WHERE associated_to_name = 'Milk')
                AND units > 15
                AND DATE(instant) > '2021-03-25');

-- B    Given the EAN of a product, display the name and NIF of all its suppliers (both primary and secondary).

SELECT name, s.nif
FROM supplier s
         join (SELECT nif
               FROM supplies_prim
               WHERE ean = '27283213588398043725'
               UNION
               SELECT nif
               FROM supplies_sec
               WHERE ean = '27283213588398043725') n
              on n.nif = s.nif;

-- C    Display the number of sub-categories (direct descendants) of the “Milk” category.

SELECT count(*)
FROM consists_of
WHERE super_category_name = 'Milk';

-- D    What is the name and NIF of the supplier who supplied more categories.

select name, nif
from supplier
where nif in
      (select nif
       from (select nif, count(*) as number_categories
             from ((select ean, nif, associated_to_name
                    from supplies_prim sp
                             natural join product)
                   UNION
                   (select ean, nif, associated_to_name
                    from supplies_sec ss
                             natural join product)) a
             group by nif) nc
       where nc.number_categories >= ALL (
           select count(*)
           from ((select ean, nif, associated_to_name
                  from supplies_prim sp
                           natural join product)
                 UNION
                 (select ean, nif, associated_to_name
                  from supplies_sec ss
                           natural join product)) a
           group by nif));

-- E    List the primary suppliers (name and NIF) who supplied products in all simple categories.

select distinct nif, name
from (supplier natural join supplies_prim) sup
where not exists(
        select name
        from simple_category
            except
        select associated_to_name
        from (product join supplies_prim sp on product.ean = sp.ean) ps
        where ps.nif = sup.nif
    );

-- F    List the aisles that contain products from all primary suppliers that are not secondary suppliers of any products.
select distinct corridor_nr, supermarket_nif
from planogram as p
WHERE NOT EXISTS(
        (select distinct nif
         from supplies_prim EXCEPT (select nif from supplies_sec))
        EXCEPT
        (select nif
         from planogram as p2
                  join
              supplies_prim as sp on sp.ean = p2.product_ean
         where p.corridor_nr = corridor_nr
           and p.supermarket_nif = supermarket_nif
        )
    );