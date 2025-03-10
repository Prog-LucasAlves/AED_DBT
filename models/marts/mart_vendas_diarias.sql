SELECT
    data_pedido,
    'R$' || TO_CHAR(SUM(total), 'FM999G999G999D99') AS total_vendas,
    COUNT(DISTINCT id_pedido) AS total_pedidos
FROM {{ ref('stg_pedidos') }}
GROUP BY data_pedido
