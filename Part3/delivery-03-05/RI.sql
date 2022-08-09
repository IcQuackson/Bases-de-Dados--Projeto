
CREATE OR REPLACE FUNCTION chk_max_secondary_suppliers()
RETURNS TRIGGER AS
$$
BEGIN
    IF EXISTS(SELECT ean FROM supplies_sec GROUP BY ean HAVING count(*) > 3)
     THEN
        RAISE EXCEPTION
        USING HINT = 'A product can only have at most 3 secondary suppliers';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_max_sec_suppliers AFTER INSERT ON supplies_sec
FOR STATEMENT EXECUTE PROCEDURE chk_max_secondary_suppliers();



CREATE OR REPLACE FUNCTION chk_sup_not_prim_and_sec()
RETURNS TRIGGER AS
$$
BEGIN
    IF EXISTS (select nif from supplier where nif in (select nif from supplies_prim sp where sp.ean = NEW.ean)
and nif in (select nif from supplies_sec sc where sc.ean = new.ean))
    THEN
        RAISE EXCEPTION
        USING HINT = 'For a given product, a supplier cannot be simultaneously a primary and secondary supplier';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER chk_sup_not_prim_and_sec AFTER INSERT ON supplies_sec
FOR ROW EXECUTE PROCEDURE chk_sup_not_prim_and_sec();

CREATE TRIGGER chk_sup_not_prim_and_sec AFTER INSERT ON supplies_prim
FOR ROW EXECUTE PROCEDURE chk_sup_not_prim_and_sec();






















