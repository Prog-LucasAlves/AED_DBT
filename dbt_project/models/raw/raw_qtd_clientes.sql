with total_por_canal_venda as (SELECT cv.descricao_canal_venda,
                                      sum(p.total) as total -- Mantém como número para cálculos
                               FROM   {{ ref('stg_pedido') }} p join {{ ref('stg_canais_venda') }} cv
                                       ON p.id_canal_venda = cv.id_canal_venda
                               GROUP BY cv.descricao_canal_venda)
SELECT descricao_canal_venda,
       'R$' || to_char(total, 'FM999G999G999D99') as total_formatado, -- Conversão para string só aqui
       round((total * 100.0 / (SELECT sum(total)
                        FROM   total_por_canal_venda))::numeric, 2) as percentual
FROM   total_por_canal_venda
ORDER BY total desc;
