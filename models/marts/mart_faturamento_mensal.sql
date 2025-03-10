SELECT
    TO_CHAR(DATE_TRUNC('month', data_pedido), 'YYYY-MM') AS mes,
    'R$' || TO_CHAR(SUM(total), 'FM999G999G999D99') AS faturamento
FROM {{ ref('stg_pedidos') }}
GROUP BY mes
