with pedido as (select * from dbtvendas_82ea.public_staging.stg_pedido where total > 0)

select *
from pedido
