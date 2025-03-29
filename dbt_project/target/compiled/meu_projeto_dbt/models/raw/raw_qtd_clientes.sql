with
    total_por_canal_venda as (
        select cv.descricao_canal_venda, sum(p.total) as total  -- Mantém como número para cálculos
        from dbtvendas_82ea.public_staging.stg_pedido p
        inner join
            dbtvendas_82ea.public_staging.stg_canais_venda cv
            on p.id_canal_venda = cv.id_canal_venda
        group by cv.descricao_canal_venda
    )

select
    descricao_canal_venda,
    -- Conversão para string só aqui
    'R$' || to_char(total, 'FM999G999G999D99') as total_formatado,
    round(
        (total * 100.0 / (select sum(total) from total_por_canal_venda))::numeric, 2
    ) as percentual
from total_por_canal_venda
order by total desc
