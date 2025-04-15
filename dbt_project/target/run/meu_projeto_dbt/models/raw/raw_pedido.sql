  create  table "dbtvendas_82ea"."public_raw"."raw_pedido__dbt_tmp"


    as

  (
    with pedido as (select * from "dbtvendas_82ea"."public_staging"."stg_pedido" where total > 0)
select *
from pedido
  );
