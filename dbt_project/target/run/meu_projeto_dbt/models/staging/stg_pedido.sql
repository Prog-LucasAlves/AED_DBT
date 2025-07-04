
  create view "dbt_q4iu"."public_staging"."stg_pedido__dbt_tmp"


  as (
    with
    pedido as (
        select
            id_pedido,
            id_cliente,
            id_forma_pagamento,
            id_canal_venda,
            id_status,
            data_pedido,
            subtotal,
            frete,
            total,
            data_entrega
        from public_data.tb_pedido
    )

select *
from pedido
  );
