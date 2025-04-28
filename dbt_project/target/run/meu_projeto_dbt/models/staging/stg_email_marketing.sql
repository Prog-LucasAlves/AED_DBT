
  create view "dbt_q4iu"."public_staging"."stg_email_marketing__dbt_tmp"


  as (
    with
    email_marketing as (
        select
            id_email_marketing,
            descricao_email_marketing
        from public_data.tb_email_marketing
    )

select *
from email_marketing
  );
