with pedido as (select * from {{ ref("stg_pedido") }} where total > 0)
select *
from pedido
