with status as (SELECT id_status,
                       descricao_status
                FROM   public.tb_status)
SELECT *
FROM   status
