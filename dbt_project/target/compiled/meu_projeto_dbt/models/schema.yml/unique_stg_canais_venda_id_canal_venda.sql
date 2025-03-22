SELECT id_canal_venda as unique_field,
       count(*) as n_records
FROM   "dbtvendas_82ea"."public_staging"."stg_canais_venda"
WHERE  id_canal_venda is not null
GROUP BY id_canal_venda having count(*) > 1;
