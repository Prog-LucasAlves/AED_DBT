with estado as (SELECT id_estado,
                       descricao_estado,
                       sigla_estado
                FROM   public.tb_estado)
SELECT *
FROM   estado;
