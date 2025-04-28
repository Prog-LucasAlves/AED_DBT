
  create view "dbt_q4iu"."public_staging"."stg_categoria__dbt_tmp"


  as (
    with
    categoria as (
        select
            id_categoria,
            descricao_categoria
        from public_data.tb_categoria
    )

select *
from categoria
  );
