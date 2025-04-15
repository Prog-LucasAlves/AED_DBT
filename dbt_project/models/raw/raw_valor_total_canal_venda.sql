-- Total fatrurado por canal de venda
WITH
    total_por_canal_venda AS (
        SELECT
            cv.descricao_canal_venda,
            sum(p.total) AS total -- Total por canal de venda
        FROM {{ ref("raw_pedido") }} p
        JOIN {{ ref("stg_canais_venda") }} cv ON p.id_canal_venda = cv.id_canal_venda
        GROUP BY cv.descricao_canal_venda
    )

SELECT
    descricao_canal_venda,
    to_char(total, 'L999G999G999D99') AS total_formatado, -- Formata o total com símbolo de moeda
    round((total * 100.0 / nullif(
                                 (SELECT sum(total)
                                  FROM total_por_canal_venda), 0))::numeric, 2) AS percentual -- Percentual do total
FROM total_por_canal_venda
ORDER BY total DESC -- Ordenar por total decrescente
