SELECT id_status as unique_field,
       count(*) as n_records
FROM   "dbtvendas_82ea"."public_staging"."stg_status"
WHERE  id_status is not null
GROUP BY id_status having count(*) > 1;
