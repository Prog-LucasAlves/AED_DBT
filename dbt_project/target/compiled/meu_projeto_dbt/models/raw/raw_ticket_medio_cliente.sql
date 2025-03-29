-- Total de pedidos e ticket medio por cliente com status de entrega como ENTREGUE
with
    ticket_medio_por_cliente as (
        select
            c.id_cliente,
            c.primeiro_nome,
            c.email,
            c.telefone,
            count(p.id_pedido) as qtd_pedidos,
            round(cast(avg(p.total) as numeric), 2) as ticket_medio
        from dbtvendas_82ea.public_staging.stg_cliente c
        left join dbtvendas_82ea.public_raw.raw_pedido p on c.id_cliente = p.id_cliente
        where p.id_status = 4
        group by c.id_cliente, c.primeiro_nome, c.email, c.telefone
    )

select *
from ticket_medio_por_cliente
where ticket_medio is not null
order by ticket_medio desc
