DROP TABLE refers;
DROP TABLE consists_of;
DROP TABLE exposta;
DROP TABLE planogram;
DROP TABLE supplies_sec;
DROP TABLE supplies_prim;
DROP TABLE replenish_event;
DROP TABLE product;
DROP TABLE super_category;
DROP TABLE simple_category;
DROP TABLE category;
DROP TABLE shelf;
DROP TABLE corridor;
DROP TABLE supermarket;
DROP TABLE supplier;

/*SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;')
FROM information_schema.tables
WHERE table_schema = 'public'*/


-- ENTITIES

CREATE TABLE supplier (
    nif VARCHAR (20),
    name VARCHAR (200) NOT NULL,
    PRIMARY KEY (nif)
);


CREATE TABLE supermarket(
    NIF VARCHAR(20),
    name VARCHAR(80) not NULL,
    addr VARCHAR(150) not NULL,
    PRIMARY KEY(NIF)
);

CREATE TABLE corridor(
    nr INTEGER CHECK (nr >= 0),
    width INTEGER NOT NULL CHECK (width > 0),
    supermarket_NIF VARCHAR(20),

    PRIMARY KEY (nr, supermarket_NIF),
    FOREIGN KEY (supermarket_NIF) REFERENCES  supermarket(NIF)
);

CREATE TABLE shelf (
    supermarket_NIF VARCHAR(20),
    corridor_nr INTEGER,
    side VARCHAR(20),
    height VARCHAR(20),

    PRIMARY KEY (supermarket_NIF, corridor_nr, side, height),
    FOREIGN KEY (supermarket_NIF) REFERENCES supermarket(NIF),
    FOREIGN KEY (supermarket_NIF, corridor_nr) REFERENCES corridor(supermarket_NIF,  nr)
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

    -- Every category must exist in the table 'exposta'

);

CREATE TABLE simple_category(
    name VARCHAR(80),
    PRIMARY KEY (name),
    FOREIGN KEY (name) REFERENCES category(name)
);

CREATE TABLE super_category(
    name  VARCHAR(80),
    --nameOfParent VARCHAR(80) alexandro name  e nameOfParent têm q ser diferentes IC1
    PRIMARY KEY (name),
    FOREIGN KEY (name) REFERENCES category(name)
    -- NEW CODE pedro
    -- A super category must consist of a category
    -- END OF CODE
);

CREATE TABLE product (
    ean VARCHAR(20),
    descr TEXT NOT NULL,
    supplies_sec_nif VARCHAR(20) NOT NULL REFERENCES supplier(nif),
    has_category VARCHAR(80) NOT NULL REFERENCES  category(name),

    PRIMARY KEY (ean),
    FOREIGN KEY (supplies_sec_nif) REFERENCES supplier (nif),
    FOREIGN KEY (has_category) REFERENCES category(name)

    -- A Product can only be exposed in one of the Shelves to which it is associated
);

CREATE TABLE replenish_event(
    product_ean VARCHAR(80),
    supermarket_NIF VARCHAR(20),
    corridor_nr INTEGER,
    shelf_side VARCHAR(20),
    shelf_height VARCHAR(20),
    instant TIMESTAMP,

    PRIMARY KEY (product_ean, shelf_side, shelf_height, corridor_nr, supermarket_NIF, instant),
    FOREIGN KEY (product_ean) REFERENCES product(ean),
    FOREIGN KEY (supermarket_NIF, corridor_nr, shelf_side, shelf_height) REFERENCES shelf(supermarket_NIF, corridor_nr, side, height),

    CHECK (instant <= CURRENT_TIMESTAMP)
);


--ASSOCIATIONS

CREATE TABLE supplies_prim (
    nif VARCHAR(20),
    ean VARCHAR(20),
    since DATE,

    PRIMARY KEY (nif, ean),
    FOREIGN KEY (nif) REFERENCES supplier (nif),
    FOREIGN KEY (ean) REFERENCES product(ean)

    -- Every product must have a primary supplier
);


CREATE TABLE supplies_sec ( --associacao
    nif VARCHAR(20),
    ean VARCHAR(20),
    since DATE,
    PRIMARY KEY (nif, ean),
    FOREIGN KEY (nif) REFERENCES supplier (nif),
    FOREIGN KEY (ean) REFERENCES product(ean)

    -- For a given Product, a supplier cannot be simultaneously a Primary and Secondary Supplier

    -- A product can only have at most 3 Secondary Suppliers
);

CREATE TABLE planogram (
    product_ean VARCHAR(20),
    supermarket_NIF VARCHAR(20),
    corridor_nr INTEGER,
    shelf_side VARCHAR(20),
    shelf_height VARCHAR(20),

    facings INTEGER NOT NULL,
    units INTEGER NOT NULL,
    loc INTEGER NOT NULL,

    PRIMARY KEY (product_ean, shelf_side, shelf_height, corridor_nr, supermarket_NIF),
    FOREIGN KEY (product_ean) REFERENCES product(ean),
    FOREIGN KEY (supermarket_NIF, corridor_nr, shelf_side, shelf_height) REFERENCES shelf(supermarket_NIF, corridor_nr, side, height),


-- NEW CODE: CHECKS ADDED
    CHECK (facings >= 0),
    CHECK (units >= 0),
    CHECK (loc >= 0)
);

CREATE TABLE exposta(
    category_name VARCHAR(80),
    supermarket_NIF VARCHAR(20),
    corridor_nr INTEGER,
    shelf_side VARCHAR(20),
    shelf_height VARCHAR(20),

    PRIMARY KEY (category_name, shelf_side, shelf_height, corridor_nr, supermarket_nif),
    FOREIGN KEY (supermarket_NIF, corridor_nr, shelf_side, shelf_height) REFERENCES shelf(supermarket_NIF, corridor_nr, side, height)
);


CREATE TABLE consists_of (
    super_category_name VARCHAR(80),
    category_name VARCHAR(80),

    PRIMARY KEY (category_name),
    FOREIGN KEY (category_name) REFERENCES category(name),
    FOREIGN KEY (super_category_name) REFERENCES category(name),

    --CHECK (consists_of.super_category_name = category_name AND consists_of.category_name = super_category_name NOT IN (SELECT * FROM consists_of)),
    CHECK (super_category_name != category_name)
    --CHECK (EXISTS(SELECT 1 FROM consists_of WHERE consists_of.super_category_name = category_name AND consists_of.category_name = super_category_name))
);

CREATE TABLE refers (
    product_ean VARCHAR(20),
    supermarket_NIF VARCHAR(20),
    corridor_nr INTEGER,
    shelf_side VARCHAR(20),
    shelf_height VARCHAR(20),
    instant TIMESTAMP,

    PRIMARY KEY (product_ean, shelf_side, shelf_height, corridor_nr, supermarket_NIF, instant),
    FOREIGN KEY (product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height) REFERENCES planogram(product_ean, supermarket_NIF, corridor_nr, shelf_side, shelf_height),
    FOREIGN KEY (product_ean, shelf_side, shelf_height, corridor_nr, supermarket_NIF, instant) REFERENCES replenish_event(product_ean, shelf_side, shelf_height, corridor_nr, supermarket_NIF, instant)
);


/*

*/