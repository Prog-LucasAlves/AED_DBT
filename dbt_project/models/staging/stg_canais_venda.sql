with
    canais_venda as (
        select id_canal_venda, descricao_canal_venda from public.tb_canais_venda
    )

select *
from canais_venda
