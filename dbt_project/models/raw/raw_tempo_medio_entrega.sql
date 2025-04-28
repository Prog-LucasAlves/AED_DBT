-- Modelo para calcular o tempo médio de entrega dos pedidos
WITH tempo_medio_entrega AS (
    SELECT
        p.id_pedido,
        p.data_pedido,
        p.data_entrega,
        (p.data_entrega - p.data_pedido)::INT AS tempo_entrega_dias
    FROM {{ ref("stg_pedido") }} p
    WHERE p.data_entrega IS NOT NULL
)

SELECT * FROM tempo_medio_entrega
