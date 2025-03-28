with itens_pedido as(SELECT id_item_produto,
                            id_pedido,
                            id_produto,
                            quantidade,
                            preco_unitario,
                            valor_subtotal
                     FROM   public.tb_itens_pedido)
SELECT *
FROM   itens_pedido;
