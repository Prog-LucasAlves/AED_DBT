  create  table "dbtvendas_82ea"."public_raw"."raw_faturamento_mensal__dbt_tmp"


    as

  (
    WITH faturamento_mensal AS (
    SELECT
        to_char(date_trunc('month', data_pedido), 'YYYY-MM') AS mes,
        'R$ ' || to_char(SUM(total), 'FM999G999G999D99') AS total_faturado,
        'R$ ' || to_char(SUM(SUM(total)) OVER (ORDER BY date_trunc('month', data_pedido)), 'FM999G999G999D99') AS total_faturado_acumulado
    FROM "dbtvendas_82ea"."public_raw"."raw_pedido"
    GROUP BY date_trunc('month', data_pedido)
    ORDER BY mes
)
SELECT *
FROM faturamento_mensal
  );
