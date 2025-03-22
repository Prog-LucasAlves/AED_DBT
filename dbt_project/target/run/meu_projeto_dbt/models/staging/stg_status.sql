CREATE VIEW "dbtvendas_82ea"."public_staging"."stg_status__dbt_tmp" as (with status AS (SELECT id_status,
                                                                                               descricao_status
                                                                                        FROM   public.tb_status)
SELECT *
FROM   status);
