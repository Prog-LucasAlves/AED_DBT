with
    produto as (
        select
            id_produto,
            descricao_produto,
            id_categoria,
            preco_unitario,
            quantidade_estoque
        from public_data.tb_produto
    )

select *
from produto
