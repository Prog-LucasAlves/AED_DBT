CREATE VIEW "dbtvendas_82ea"."public_staging"."stg_categoria__dbt_tmp" as (with categoria AS (SELECT id_categoria,
                                                                                                     descricao_categoria
                                                                                              FROM   public.tb_categoria)
SELECT *
FROM   categoria);
