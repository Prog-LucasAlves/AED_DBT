with
    categoria as (
        select
            id_categoria,
            descricao_categoria
        from public_data.tb_categoria
    )

select *
from categoria
