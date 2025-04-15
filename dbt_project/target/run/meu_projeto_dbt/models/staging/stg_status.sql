  create view "dbtvendas_82ea"."public_staging"."stg_status__dbt_tmp"


  as (
    with status as (select id_status, descricao_status from public.tb_status)


select *

from status
  );
