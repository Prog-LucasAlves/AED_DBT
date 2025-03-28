WITH total_por_forma_pagamento AS (SELECT
fp.descricao_metodo_pagamento,
sum(p.total) as total
FROM {{ ref('stg_pedido') }} p join {{ ref('stg_formas_pagamento') }} fp
ON p.id_forma_pagamento = fp.id_forma_pagamento
GROUP BY fp.descricao_metodo_pagamento)
SELECT
descricao_metodo_pagamento,
'R$' || to_char(total, 'FM999G999G999D99') as total_formatado,
round((total * 100.0 / (SELECT sum(total)
FROM   total_por_forma_pagamento))::numeric, 2) as percentual
FROM   total_por_forma_pagamento
ORDER BY total desc
