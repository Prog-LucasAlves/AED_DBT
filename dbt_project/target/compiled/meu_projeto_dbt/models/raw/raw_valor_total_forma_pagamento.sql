-- Modelo para calcular o valor total por forma de pagamento
WITH
    total_por_forma_pagamento AS(
        SELECT
            fp.descricao_metodo_pagamento,
            sum(p.total) AS total -- Calcula o total por forma de pagamento
        FROM "dbt_q4iu"."public_raw"."raw_pedido" p
        JOIN "dbt_q4iu"."public_staging"."stg_formas_pagamento" fp ON p.id_forma_pagamento = fp.id_forma_pagamento
        GROUP BY fp.descricao_metodo_pagamento
    )
SELECT
    descricao_metodo_pagamento,
    'R$' || to_char(total, 'FM999G999G999D99') AS total_formatado, -- Formata o total para moeda brasileira
    round((total * 100.0 /
                (SELECT sum(total)
                 FROM total_por_forma_pagamento))::numeric, 2) AS percentual -- Calcula o percentual de cada forma de pagamento
FROM total_por_forma_pagamento
ORDER BY total DESC -- Ordena os resultados por total decrescente
