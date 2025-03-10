WITH pedidos AS (
    SELECT * FROM {{ ref('stg_pedidos') }}
),
clientes AS (
    SELECT * FROM {{ ref('stg_clientes') }}
),
vendas AS (
    SELECT
        c.id_cliente AS id_cliente,
        c.primeiro_nome AS cliente,
        COUNT(p.id_cliente) AS total_pedidos,
        SUM(CASE WHEN p.status = 'aprovado' THEN p.total ELSE 0 END) AS total_vendido
    FROM pedidos p
    JOIN clientes c ON p.id_cliente = c.id_cliente
    GROUP BY c.id_cliente, c.primeiro_nome
)
SELECT * FROM vendas
