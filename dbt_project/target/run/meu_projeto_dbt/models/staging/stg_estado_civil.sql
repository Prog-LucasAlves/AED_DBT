
  create view "dbt_q4iu"."public_staging"."stg_estado_civil__dbt_tmp"


  as (
    with
    estado_civil as (
        select
            id_estado_civil,
            descricao_estado_civil
        from public_data.tb_estado_civil
    )

select *
from estado_civil
  );
