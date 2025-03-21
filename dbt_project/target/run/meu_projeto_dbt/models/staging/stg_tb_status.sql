
  create view "dbtvendas_82ea"."public_staging"."stg_tb_status__dbt_tmp"


  as (
    WITH status AS (
    SELECT
        id_status,
        descricao_status
    FROM public.tb_status
)
SELECT * FROM status
  );
