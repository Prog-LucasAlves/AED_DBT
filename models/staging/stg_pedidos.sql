WITH pedidos AS (
    SELECT
        data_pedido::DATE AS data_pedido,
        id_cliente,
        id_pedido,
        forma_pagamento,
        status,
        total
    FROM public.pedidos
)
SELECT * FROM pedidos
