with
    estado_civil as (
        select
            id_estado_civil,
            descricao_estado_civil
        from public_data.tb_estado_civil
    )

select *
from estado_civil
