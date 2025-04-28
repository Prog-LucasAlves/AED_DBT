
  create view "dbt_q4iu"."public_staging"."stg_formas_pagamento__dbt_tmp"


  as (
    with
    formas_pagamento as (
        select
            id_forma_pagamento,
            descricao_metodo_pagamento
        from public_data.tb_formas_pagamento
    )

select *
from formas_pagamento
  );
