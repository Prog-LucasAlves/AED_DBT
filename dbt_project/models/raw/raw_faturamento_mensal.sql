-- Faturamento mensal com formatação de moeda e total acumulado
WITH
    faturamento_mensal AS(
        SELECT
            to_char(date_trunc('month', data_pedido), 'YYYY-MM') AS mes, -- Formatação para o mês e ano
            'R$ ' || to_char(sum(total), 'FM999G999G999D99') AS total_faturado, -- Formatação para o total do mês
            'R$ ' || to_char(sum(sum(total)) OVER (
                                        ORDER BY date_trunc('month', data_pedido)), 'FM999G999G999D99') AS total_faturado_acumulado
        FROM {{ ref("raw_pedido") }}
        GROUP BY date_trunc('month', data_pedido) -- Agrupamento por mês
        ORDER BY mes
    )

SELECT *
FROM faturamento_mensal
