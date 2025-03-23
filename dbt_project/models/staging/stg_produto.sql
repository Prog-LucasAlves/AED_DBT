with produto as (SELECT id_produto,
                        descricao_produto,
                        id_categoria,
                        preco_unitario,
                        quantidade_estoque
                 FROM   public.tb_produto)
SELECT *
FROM   produto;
