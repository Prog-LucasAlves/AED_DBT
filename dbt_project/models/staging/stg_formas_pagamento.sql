with
    formas_pagamento as (
        select id_forma_pagamento, descricao_metodo_pagamento
        from public.tb_formas_pagamento
    )

select *
from formas_pagamento
