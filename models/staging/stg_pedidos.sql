WITH pedidos AS (
    SELECT
        id,
        cliente_id,
        produto_id,
        forma_pagamento_id,
        canal_venda_id,
        status_id,
        quantidade,
        data_pedido,
        subtotal,
        frete,
        total,
        data_entrega
    FROM public.pedidos
)
SELECT * FROM pedidos
