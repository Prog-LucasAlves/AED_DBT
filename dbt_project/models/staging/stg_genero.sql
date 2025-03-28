with genero as (SELECT id_genero,
                       descricao_genero
                FROM   public.tb_genero)
SELECT *
FROM   genero;
