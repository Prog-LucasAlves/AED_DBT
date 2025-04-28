
  create view "dbt_q4iu"."public_staging"."stg_itens_pedido__dbt_tmp"


  as (
    with
    itens_pedido as (
        select
            id_item_produto,
            id_pedido,
            id_produto,
            quantidade,
            preco_unitario,
            valor_subtotal
        from public_data.tb_itens_pedido
    )

select *
from itens_pedido
  );
