  create view "dbtvendas_82ea"."public_staging"."stg_categoria__dbt_tmp"


  as (
    with categoria as (select id_categoria, descricao_categoria from public.tb_categoria)


select *

from categoria
  );
