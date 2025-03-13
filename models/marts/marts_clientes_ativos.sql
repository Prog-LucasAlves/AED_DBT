SELECT
    cliente_id,
    COUNT(id) AS total_pedidos
FROM {{ ref('stg_pedidos') }}
WHERE data_pedido >= CURRENT_DATE - INTERVAL '2 months'
GROUP BY cliente_id DESC
