CREATE VIEW "dbtvendas_82ea"."public_staging"."stg_canais_venda__dbt_tmp" as (with canais_venda AS (SELECT id_canal_venda,
                                                                                                           nome_canal_venda
                                                                                                    FROM   public.tb_canais_venda)
SELECT *
FROM   canais_venda);
