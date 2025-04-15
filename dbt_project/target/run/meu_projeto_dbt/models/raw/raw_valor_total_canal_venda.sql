  create  table "dbtvendas_82ea"."public_raw"."raw_valor_total_canal_venda__dbt_tmp"


    as

  (
    with
    total_por_canal_venda as (
        select cv.descricao_canal_venda, sum(p.total) as total
        from "dbtvendas_82ea"."public_raw"."raw_pedido" p
        join "dbtvendas_82ea"."public_staging"."stg_canais_venda" cv on p.id_canal_venda = cv.id_canal_venda
        group by cv.descricao_canal_venda
    )
select
    descricao_canal_venda,
    'R$' || to_char(total, 'FM999G999G999D99') as total_formatado,
    round(
        (total * 100.0 / (select sum(total) from total_por_canal_venda))::numeric, 2
    ) as percentual
from total_por_canal_venda
order by total desc

-- raw_pedido
  );
