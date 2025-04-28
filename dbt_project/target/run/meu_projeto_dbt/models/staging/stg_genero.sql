
  create view "dbt_q4iu"."public_staging"."stg_genero__dbt_tmp"


  as (
    with
    genero as (
        select
            id_genero,
            descricao_genero
        from public_data.tb_genero
    )

select *
from genero
  );
