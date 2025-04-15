with
    total_por_forma_pagamento as (
        select fp.descricao_metodo_pagamento, sum(p.total) as total
        from "dbtvendas_82ea"."public_raw"."raw_pedido" p
        join
            "dbtvendas_82ea"."public_staging"."stg_formas_pagamento" fp
            on p.id_forma_pagamento = fp.id_forma_pagamento
        group by fp.descricao_metodo_pagamento
    )
select
    descricao_metodo_pagamento,
    'R$' || to_char(total, 'FM999G999G999D99') as total_formatado,
    round(
        (total * 100.0 / (select sum(total) from total_por_forma_pagamento))::numeric, 2
    ) as percentual
from total_por_forma_pagamento
order by total desc
