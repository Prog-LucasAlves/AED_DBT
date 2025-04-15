  create view "dbtvendas_82ea"."public_staging"."stg_produto__dbt_tmp"


  as (
    with

    produto as (

        select

            id_produto,

            descricao_produto,

            id_categoria,

            preco_unitario,

            quantidade_estoque

        from public.tb_produto

    )


select *

from produto
  );
