WITH clientes_ativos AS (
    SELECT
        cliente_id,
        COUNT(id) AS total_pedidos
    FROM {{ ref('stg_pedidos') }}
    WHERE data_pedido >= CURRENT_DATE - INTERVAL '2 months'
    GROUP BY cliente_id
    ORDER BY total_pedidos DESC
)
SELECT * FROM clientes_ativos

/*
Adicionar o nome do cliente, email e telefone.
/*
