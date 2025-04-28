



  create  table "dbt_q4iu"."public_raw"."raw_pedido__dbt_tmp"


    as

  (
    WITH pedido AS (
    SELECT *
    FROM "dbt_q4iu"."public_staging"."stg_pedido"
    WHERE total > 0) -- Filtra pedidos com valOR maiOR que 0

SELECT * FROM pedido
  );
