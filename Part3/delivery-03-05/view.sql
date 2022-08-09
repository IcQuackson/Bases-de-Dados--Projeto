REATE VIEW supplier_stats AS
SELECT ean, (prim_supplier_count + sec_supplier_count) as total_supplier_count
FROM (SELECT ean, count(*) as prim_supplier_count
	      from supplies_prim
	      group by ean) prim
         natural join (SELECT ean, count(*) as sec_supplier_count
		                       FROM supplies_sec
				                       group by ean) sec;
