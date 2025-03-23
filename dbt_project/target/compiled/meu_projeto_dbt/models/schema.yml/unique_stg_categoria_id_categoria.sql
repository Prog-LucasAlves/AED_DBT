SELECT id_categoria as unique_field,
       count(*) as n_records
FROM   "dbtvendas_82ea"."public_staging"."stg_categoria"
WHERE  id_categoria is not null
GROUP BY id_categoria having count(*) > 1;
