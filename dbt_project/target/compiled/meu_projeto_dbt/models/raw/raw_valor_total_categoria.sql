with
    total_por_categoria as (
        select ct.descricao_categoria, sum(p.total) as total
        from dbtvendas_82ea.public_staging.stg_pedido p
        inner join
            dbtvendas_82ea.public_staging.stg_categoria ct
            on p.id_categoria = ct.id_categoria
        group by ct.descricao_categoria
    )

select
    descricao_categoria,
    'R$' || to_char(total, 'FM999G999G999D99') as total_formatado,
    round(
        (total * 100.0 / (select sum(total) from total_por_categoria))::numeric, 2
    ) as percentual
from total_por_categoria
order by total desc
