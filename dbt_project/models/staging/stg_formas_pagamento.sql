with formas_pagamento as (SELECT id_forma_pagamento,
                                 descricao_metodo_pagamento
                          FROM   public.tb_formas_pagamento)
SELECT *
FROM   formas_pagamento;
