WITH pedidos AS (
    SELECT
        {{ dbt_utils.generate_surrogate_key(['id', 'produto_id']) }} AS pedido_sk,
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
