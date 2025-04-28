
  create view "dbt_q4iu"."public_staging"."stg_estado__dbt_tmp"


  as (
    with
    estado as (
        select
            id_estado,
            descricao_estado,
            sigla_estado
        from public_data.tb_estado
    )

select *
from estado
  );
