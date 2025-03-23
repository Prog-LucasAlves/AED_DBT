with categoria as (SELECT id_categoria,
                          descricao_categoria
                   FROM   public.tb_categoria)
SELECT *
FROM   categoria;
