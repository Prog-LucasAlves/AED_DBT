with pedido as (SELECT id_pedido,
                       id_cliente,
                       id_forma_pagamento,
                       id_canal_venda,
                       id_status,
                       data_pedido,
                       subtotal,
                       frete,
                       total,
                       data_entrega
                FROM   public.tb_pedido)
SELECT *
FROM   pedido;
