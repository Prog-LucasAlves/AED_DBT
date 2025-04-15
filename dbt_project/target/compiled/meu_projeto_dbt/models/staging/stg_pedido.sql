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

        from public.tb_pedido

    )

select *

from pedido
