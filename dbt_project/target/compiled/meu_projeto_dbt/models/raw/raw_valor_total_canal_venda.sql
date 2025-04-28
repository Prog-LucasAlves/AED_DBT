-- Modelo para calcular o valor total por canal de venda
WITH
    total_por_canal_venda AS (
        SELECT
            cv.descricao_canal_venda,
            SUM(p.total) AS total -- Total por canal de venda
        FROM "dbt_q4iu"."public_raw"."raw_pedido" p
        JOIN "dbt_q4iu"."public_staging"."stg_canais_venda" cv ON p.id_canal_venda = cv.id_canal_venda
        GROUP BY cv.descricao_canal_venda
    )

SELECT
    descricao_canal_venda,
    to_char(total, 'L999G999G999D99') AS total_formatado, -- Formata o total com símbolo de moeda
    ROUND((total * 100.0 / nullif(
        (SELECT SUM(total)
        FROM total_por_canal_venda), 0))::numeric, 2) AS percentual -- Percentual do total
FROM total_por_canal_venda
ORDER BY total DESC -- Ordenar por total decrescente
