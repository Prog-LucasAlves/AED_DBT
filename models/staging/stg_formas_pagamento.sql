WITH formas_pagamento AS (
    SELECT
        id,
        metodo
    from public.formas_pagamento
)
SELECT * FROM formas_pagamento
