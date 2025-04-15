with
    faturamento_mensal as (
        select
            to_char(date_trunc('month', data_pedido), 'YYYY-MM') as mes,
            'R$ ' || to_char(sum(total), 'FM999G999G999D99') as total_faturado,
            'R$ ' || to_char(
                sum(sum(total)) over (order by date_trunc('month', data_pedido)),
                'FM999G999G999D99'
            ) as total_faturado_acumulado
        from "dbtvendas_82ea"."public_raw"."raw_pedido"
        group by date_trunc('month', data_pedido)
        order by mes
    )
select *
from faturamento_mensal
