
  create view "dbt_q4iu"."public_staging"."stg_status__dbt_tmp"


  as (
    with
    status as (
        select
            id_status,
            descricao_status
        from public_data.tb_status
    )

select *
from status
  );
