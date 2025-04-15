-- Total de pedidos e ticket medio por cliente com status de entrega como ENTREGUE
WITH ticket_medio_por_cliente AS
  (SELECT c.id_cliente,
          c.primeiro_nome,
          c.email,
          c.telefone,
          count(p.id_pedido) AS qtd_pedidos, -- Total de pedidos
 round(cast(avg(p.total) AS numeric), 2) AS ticket_medio -- Ticket mésio

   FROM "dbtvendas_82ea"."public_staging"."stg_cliente" c
   LEFT JOIN "dbtvendas_82ea"."public_raw"."raw_pedido" p ON c.id_cliente = p.id_cliente
   WHERE p.id_status = 4 -- Filtrando por status de entrega como ENTREGUE

   GROUP BY c.id_cliente,
            c.primeiro_nome,
            c.email,
            c.telefone -- Agrupando por id_cliente, primeiro_nome, email, telefone
)
SELECT
  id_cliente,
  primeiro_nome,
  email,
  telefone,
  qtd_pedidos,
  'R$' || TO_CHAR(ticket_medio, 'FM999G999G999D99') AS ticket_medio -- Formata o total para moeda brasileira
FROM ticket_medio_por_cliente
WHERE ticket_medio IS NOT NULL -- Filtrando por ticket_medio não nulo
ORDER BY id_cliente ASC -- Ordenando por ticket_medio em ordem decrescente
