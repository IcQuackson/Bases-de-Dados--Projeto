
DROP TABLE IF EXISTS 
    consists_of,
    displayed_in,
    planogram,
    supplies_sec,
    supplies_prim,
    replenish_event,
    product,
    super_category,
    simple_category,
    category,
    shelf,
    corridor,
    supermarket,
    supplier,

    CASCADE;


-- ENTITIES

CREATE TABLE supplier (
    nif NUMERIC(9),
    name VARCHAR (200) NOT NULL,
    PRIMARY KEY (nif),
    CHECK (nif BETWEEN 100000000 AND 999999999)
);


CREATE TABLE supermarket(
    NIF NUMERIC(9),
    name VARCHAR(80) not NULL,
    addr VARCHAR(150) not NULL,
    PRIMARY KEY(NIF),
    CHECK (NIF BETWEEN 100000000 AND 999999999)
);

CREATE TABLE corridor(
    nr NUMERIC(9) CHECK (nr >= 0),
    width INTEGER NOT NULL CHECK (width > 0),
    supermarket_NIF NUMERIC(9),

    PRIMARY KEY (nr, supermarket_NIF),
    FOREIGN KEY (supermarket_NIF) REFERENCES  supermarket(NIF)
);

CREATE TABLE shelf (
    supermarket_NIF NUMERIC(9),
    corridor_nr INTEGER,
    side VARCHAR(20),
    height VARCHAR(20),

    PRIMARY KEY (supermarket_NIF, corridor_nr, side, height),
    FOREIGN KEY (supermarket_NIF, corridor_nr) REFERENCES corridor(supermarket_NIF,  nr),
    CHECK (side = 'L'OR side = 'R'),
    CHECK (height = 'UPPER' OR height = 'MIDDLE' OR height = 'FLOOR')
);

CREATE TABLE category(
    name VARCHAR(80),
    PRIMARY KEY (name)

    -- No category can exist at the same time in the table
    -- 'simple_category' and in the table
    -- 'super_category'

    -- Every category must exist either in the table
    -- 'simple_category' or in the table 'super_category'

    -- Categories cannot cyclically consist of one another

    -- Every category must exist in the table 'displayed_in'

);

CREATE TABLE simple_category(
    name VARCHAR(80),
    PRIMARY KEY (name),
    FOREIGN KEY (name) REFERENCES category(name)
);

CREATE TABLE super_category(
    name  VARCHAR(80),
    PRIMARY KEY (name),
    FOREIGN KEY (name) REFERENCES category(name)
    -- A super category must consist of a category
);

CREATE TABLE product (
    ean VARCHAR(20),
    descr TEXT NOT NULL,
    associated_to_name VARCHAR(80) NOT NULL REFERENCES  category(name),

    PRIMARY KEY (ean),
    FOREIGN KEY (associated_to_name) REFERENCES category(name)

    -- A Product can only be exposed in one of the Shelves to which it is associated
);

CREATE TABLE planogram (
    product_ean VARCHAR(20),
    supermarket_NIF NUMERIC(9),
    corridor_nr INTEGER,
    shelf_side VARCHAR(20),
    shelf_height VARCHAR(20),

    facings INTEGER NOT NULL,
    units INTEGER NOT NULL,
    loc INTEGER NOT NULL,

    PRIMARY KEY (product_ean, shelf_side, shelf_height, corridor_nr, supermarket_NIF),
    FOREIGN KEY (product_ean) REFERENCES product(ean),
    FOREIGN KEY (supermarket_NIF, corridor_nr, shelf_side, shelf_height) REFERENCES shelf(supermarket_NIF, corridor_nr, side, height),

    CHECK (facings >= 0),
    CHECK (units >= 0),
    CHECK (loc >= 0)
);

CREATE TABLE replenish_event(
    product_ean VARCHAR(80),
    supermarket_NIF NUMERIC(9),
    corridor_nr INTEGER,
    shelf_side VARCHAR(20),
    shelf_height VARCHAR(20),

    instant TIMESTAMP,
    units INTEGER NOT NULL,

    PRIMARY KEY (product_ean, shelf_side, shelf_height, corridor_nr, supermarket_NIF, instant),
    FOREIGN KEY (supermarket_NIF, corridor_nr, shelf_side, shelf_height, product_ean) REFERENCES planogram(supermarket_NIF, corridor_nr, shelf_side, shelf_height, product_ean),

    CHECK (instant <= NOW()),
    CHECK (units >= 0)
);


--ASSOCIATIONS

CREATE TABLE supplies_prim (
    nif NUMERIC(9),
    ean VARCHAR(20),
    since DATE,

    PRIMARY KEY (nif, ean),
    FOREIGN KEY (nif) REFERENCES supplier (nif),
    FOREIGN KEY (ean) REFERENCES product(ean)

    -- Every product must have a primary supplier
);


CREATE TABLE supplies_sec (
    nif NUMERIC(9),
    ean VARCHAR(20),
    PRIMARY KEY (nif, ean),
    FOREIGN KEY (nif) REFERENCES supplier (nif),
    FOREIGN KEY (ean) REFERENCES product(ean)

    -- For a given Product, a supplier cannot be simultaneously a Primary and Secondary Supplier

    -- A product can only have at most 3 Secondary Suppliers
);


CREATE TABLE displayed_in(
    category_name VARCHAR(80),
    supermarket_NIF NUMERIC(9),
    corridor_nr INTEGER,
    shelf_side VARCHAR(20),
    shelf_height VARCHAR(20),

    PRIMARY KEY (category_name, shelf_side, shelf_height, corridor_nr, supermarket_nif),
    FOREIGN KEY (category_name) REFERENCES category(name),
    FOREIGN KEY (supermarket_NIF, corridor_nr, shelf_side, shelf_height) REFERENCES shelf(supermarket_NIF, corridor_nr, side, height)
);


CREATE TABLE consists_of (
    super_category_name VARCHAR(80),
    category_name VARCHAR(80),

    PRIMARY KEY (category_name),
    FOREIGN KEY (category_name) REFERENCES category(name),
    FOREIGN KEY (super_category_name) REFERENCES category(name),

    CHECK (super_category_name != category_name)
);



