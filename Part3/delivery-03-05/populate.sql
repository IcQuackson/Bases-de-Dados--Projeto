INSERT INTO "supermarket" (NIF,name,addr) VALUES (382017654,'LIDL','Ap #930-3619 Est Road');
INSERT INTO "supermarket" (NIF,name,addr) VALUES (368277886,'Continente','Ap #303-5235 Nec Rd.');
INSERT INTO "supermarket" (NIF,name,addr) VALUES (884370096,'Pingo Doce','1481 Maecenas Ave');

INSERT INTO "corridor" (nr, width, supermarket_NIF) VALUES (1, 3, 382017654);
INSERT INTO "corridor" (nr, width, supermarket_NIF) VALUES (2, 3, 382017654);
INSERT INTO "corridor" (nr, width, supermarket_NIF) VALUES (4, 2, 382017654);
INSERT INTO "corridor" (nr, width, supermarket_NIF) VALUES (3, 7, 382017654);
INSERT INTO "corridor" (nr, width, supermarket_NIF) VALUES (10, 7, 382017654);
INSERT INTO "corridor" (nr, width, supermarket_NIF) VALUES (5, 11, 382017654);

INSERT INTO "shelf" (supermarket_NIF, corridor_nr, side, height) VALUES (382017654, 1, 'L', 'UPPER');
INSERT INTO "shelf" (supermarket_NIF, corridor_nr, side, height) VALUES (382017654, 1, 'L', 'FLOOR');
INSERT INTO "shelf" (supermarket_NIF, corridor_nr, side, height) VALUES (382017654, 1, 'R', 'UPPER');
INSERT INTO "shelf" (supermarket_NIF, corridor_nr, side, height) VALUES (382017654, 2, 'R', 'UPPER');
INSERT INTO "shelf" (supermarket_NIF, corridor_nr, side, height) VALUES (382017654, 2, 'R', 'MIDDLE');
INSERT INTO "shelf" (supermarket_NIF, corridor_nr, side, height) VALUES (382017654, 3, 'L', 'UPPER');

INSERT INTO "category" (name) VALUES ('cereals');
INSERT INTO "category" (name) VALUES ('sandwiches');
INSERT INTO "category" (name) VALUES ('wines');
INSERT INTO "category" (name) VALUES ('seafood');
INSERT INTO "category" (name) VALUES ('noodles');
INSERT INTO "category" (name) VALUES ('yogurtes');
INSERT INTO "category" (name) VALUES ('greens');
INSERT INTO "category" (name) VALUES ('Breakfast');
INSERT INTO "category" (name) VALUES ('Dinner');
INSERT INTO "category" (name) VALUES ('Lunch');
INSERT INTO "category" (name) VALUES ('fruit');
INSERT INTO "category" (name) VALUES ('Milk');
INSERT INTO "category" (name) VALUES ('Butters');
INSERT INTO "category" (name) VALUES ('cheese');
INSERT INTO "category" (name) VALUES ('demo');
INSERT INTO "category" (name) VALUES ('demo_simple');

INSERT INTO "simple_category" (name) VALUES ('cereals');
INSERT INTO "simple_category" (name) VALUES ('seafood');
INSERT INTO "simple_category" (name) VALUES ('yogurtes');
INSERT INTO "simple_category" (name) VALUES ('demo_simple');

INSERT INTO "super_category" (name) VALUES ('greens');
INSERT INTO "super_category" (name) VALUES ('Breakfast');
INSERT INTO "super_category" (name) VALUES ('Dinner');
INSERT INTO "super_category" (name) VALUES ('Lunch');
INSERT INTO "super_category" (name) VALUES ('fruit');
INSERT INTO "super_category" (name) VALUES ('Milk');
INSERT INTO "super_category" (name) VALUES ('cheese');
INSERT INTO "super_category" (name) VALUES ('demo');
INSERT INTO "super_category" (name) VALUES ('Butters');

INSERT INTO "product" (ean,descr,associated_to_name) VALUES ('88468061281847442320','Chocapic','cereals');
INSERT INTO "product" (ean,descr,associated_to_name) VALUES ('27283213588398043725','Leite Mimosa','Milk');
INSERT INTO "product" (ean,descr,associated_to_name) VALUES ('89000451788816836204','camarão','seafood');
INSERT INTO "product" (ean,descr,associated_to_name) VALUES ('65158055449692428379','Danoninho','yogurtes');

INSERT INTO "supplier" (nif,name) VALUES (249368934,'Maxi Supplier');
INSERT INTO "supplier" (nif,name) VALUES (280861747,'Eggs Institute');
INSERT INTO "supplier" (nif,name) VALUES (795141672,'Adipiscing Company');
INSERT INTO "supplier" (nif,name) VALUES (826043114,'Ac Nulla Institute');

INSERT INTO "consists_of" (category_name, super_category_name) VALUES ('cheese', 'Milk');
INSERT INTO "consists_of" (category_name, super_category_name) VALUES ('Butters', 'Milk');
INSERT INTO "consists_of" (category_name, super_category_name) VALUES ('yogurtes', 'Milk');
INSERT INTO "consists_of" (category_name, super_category_name) VALUES ('cereals', 'Breakfast');
INSERT INTO "consists_of" (category_name, super_category_name) VALUES ('Milk', 'Breakfast');
INSERT INTO "consists_of" (category_name, super_category_name) VALUES ('demo', 'Butters');
INSERT INTO "consists_of" (category_name, super_category_name) VALUES ('demo_simple', 'Butters');

INSERT INTO "planogram" (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height, facings, units, loc) VALUES ('88468061281847442320', 382017654, 2, 'R', 'UPPER', 10, 5, 3);
INSERT INTO "planogram" (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height, facings, units, loc) VALUES ('27283213588398043725', 382017654, 1, 'L', 'UPPER', 3, 5, 4);
INSERT INTO "planogram" (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height, facings, units, loc) VALUES ('65158055449692428379',382017654, 2, 'R', 'UPPER', 12, 3, 7);
INSERT INTO "planogram" (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height, facings, units, loc) VALUES ('89000451788816836204',382017654, 3, 'L', 'UPPER', 12, 3, 10);

INSERT INTO "replenish_event" (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height, instant, units) VALUES ('88468061281847442320', 382017654, 2, 'R', 'UPPER', '2021-04-14 06:14:00.742000000',30);
INSERT INTO "replenish_event" (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height, instant, units) VALUES ('88468061281847442320', 382017654, 2, 'R', 'UPPER', '2014-07-07 09:17:00.742000000',4);
INSERT INTO "replenish_event" (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height, instant, units) VALUES ('27283213588398043725', 382017654, 1, 'L', 'UPPER', '2014-09-08 00:13:04.000000000',10);
INSERT INTO "replenish_event" (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height, instant, units) VALUES ('27283213588398043725', 382017654, 1, 'L', 'UPPER', '2021-03-26 00:13:04.000000000',21);
INSERT INTO "replenish_event" (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height, instant, units) VALUES ('27283213588398043725', 382017654, 1, 'L', 'UPPER', '2021-03-30 00:13:04.000000000',16);

INSERT INTO "supplies_sec" (nif, ean) VALUES (249368934,'88468061281847442320');
INSERT INTO "supplies_sec" (nif, ean) VALUES (826043114,'88468061281847442320');
INSERT INTO "supplies_sec" (nif, ean) VALUES (795141672,'88468061281847442320');
--INSERT INTO "supplies_sec" (nif, ean) VALUES (280861747,'88468061281847442320');      -- Triggers integrity constraint (max 3 suppliers)

INSERT INTO "supplies_sec" (nif, ean) VALUES (826043114,'27283213588398043725');
INSERT INTO "supplies_sec" (nif, ean) VALUES (249368934,'27283213588398043725');

INSERT INTO "supplies_prim" (nif, ean, since) VALUES (280861747,'65158055449692428379', '2019-08-17');
INSERT INTO "supplies_prim" (nif, ean, since) VALUES (280861747,'88468061281847442320', '2020-04-10');
INSERT INTO "supplies_prim" (nif, ean, since) VALUES (280861747,'89000451788816836204', '2020-04-10');
--INSERT INTO "supplies_prim" (nif, ean, since) VALUES (795141672,'88468061281847442320', '2021-10-10');      -- Triggers integrity constraint (supplier being prim and sec)
INSERT INTO "supplies_prim" (nif, ean, since) VALUES (795141672,'27283213588398043725', '2020-11-23');

INSERT INTO "displayed_in" (category_name, shelf_side, shelf_height, corridor_nr, supermarket_nif) VALUES('Milk', 'L', 'UPPER', 1, 382017654 );
INSERT INTO "displayed_in" (category_name, shelf_side, shelf_height, corridor_nr, supermarket_nif) VALUES('Milk', 'R', 'UPPER', 2, 382017654 );
INSERT INTO "displayed_in" (category_name, shelf_side, shelf_height, corridor_nr, supermarket_nif) VALUES('yogurtes', 'R', 'UPPER', 2, 382017654 );
