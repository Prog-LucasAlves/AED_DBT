with
    genero as (
        select
            id_genero,
            descricao_genero
        from public_data.tb_genero
    )

select *
from genero
