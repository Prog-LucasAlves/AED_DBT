-- Quantidade de pedidos 'Pendentes' por cliente ->> ultimos 7 dias
-- Sugestão aplicar um desconto de acordo com o valor total do pedido, conforme a regra abaixo:
-- Se o valor total do pedido for maior que R$ 1.000,00, aplicar um desconto de 15%
-- Se o valor total do pedido for maior que R$ 500,00, aplicar um desconto de 10%
-- Se o valor total do pedido for menor ou igual a R$ 500,00, não aplicar desconto

-- Enviar email para o cliente com os pedidos pendentes ->> ultimos 7 dias
-- Sugestão enviar email com os dados do pedido, incluindo o valor total com desconto e o percentual de desconto aplicado

WITH cliente_pedido_pendente AS (
    SELECT
        c.id_cliente,
        FIRST_VALUE(c.primeiro_nome) OVER (PARTITION BY c.id_cliente) AS primeiro_nome,
        c.email,
        p.id_pedido,
        p.data_pedido,
        p.total,
        cv.descricao_canal_venda,
        COUNT(it.id_produto) AS qtd_itens_pedido,
        STRING_AGG(pr.descricao_produto, ',') AS produtos,

        -- Aplica o desconto
        CASE
            WHEN p.total > 1000 THEN p.total * 0.85  -- Desconto de 15%
            WHEN p.total > 500 THEN p.total * 0.9   -- Desconto de 10%
            ELSE p.total
        END AS total_com_desconto,

        -- Indica qual desconto foi aplicado
        CASE
            WHEN p.total > 1000 THEN 15
            WHEN p.total > 500 THEN 10
            ELSE 0
        END AS percentual_desconto,

        -- Contagem de pedidos pendentes por cliente
        COUNT(*) OVER (PARTITION BY c.id_cliente) AS qtd_pedidos_pendentes,

        -- Soma total de descontos aplicados por cliente
        SUM(
            CASE
                WHEN p.total > 1000 THEN p.total * 0.15
                WHEN p.total > 500 THEN p.total * 0.10
                ELSE 0
            END
        ) OVER (PARTITION BY c.id_cliente) AS valor_desconto

    FROM "dbtvendas_82ea"."public_staging"."stg_cliente" c
    INNER JOIN "dbtvendas_82ea"."public_raw"."raw_pedido" p
        ON c.id_cliente = p.id_cliente
    INNER JOIN "dbtvendas_82ea"."public_staging"."stg_canais_venda" cv
        ON p.id_canal_venda = cv.id_canal_venda
    INNER JOIN "dbtvendas_82ea"."public_staging"."stg_itens_pedido" it
        ON p.id_pedido = it.id_pedido
    INNER JOIN "dbtvendas_82ea"."public_staging"."stg_produto" pr
        ON it.id_produto = pr.id_produto
    WHERE p.id_status = 1
    AND p.data_pedido >= CURRENT_DATE - INTERVAL '7 days'
    GROUP BY
        c.id_cliente, c.primeiro_nome, c.email,
        p.id_pedido, p.data_pedido, p.total,
        cv.descricao_canal_venda
)
SELECT
    id_cliente,
    primeiro_nome,
    email,
    data_pedido,
    id_pedido,
    qtd_itens_pedido,
    produtos,
    'R$' || TO_CHAR(total, 'FM999G999G999D99') AS total,
    percentual_desconto || '%' AS desconto,
    'R$' || TO_CHAR(valor_desconto, 'FM999G999G999D99') AS valor_desconto,
    'R$' || TO_CHAR(total_com_desconto, 'FM999G999G999D99') AS total_com_desconto,
    'R$' || TO_CHAR(SUM(total_com_desconto) OVER (ORDER BY id_cliente), 'FM999G999G999D99') AS soma_acumulada,
    descricao_canal_venda,
    qtd_pedidos_pendentes
FROM cliente_pedido_pendente
ORDER BY id_cliente, id_pedido
