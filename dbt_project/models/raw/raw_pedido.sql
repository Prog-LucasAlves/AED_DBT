
WITH pedido AS
  (SELECT *
   FROM {{ ref("stg_pedido") }}
   WHERE total > 0) -- Filtra pedidos com valOR maiOR que 0

SELECT *
FROM pedido
