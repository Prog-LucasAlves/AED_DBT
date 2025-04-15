with
    status as (
        select
            id_status,
            descricao_status
        from public_data.tb_status
    )

select *
from status
