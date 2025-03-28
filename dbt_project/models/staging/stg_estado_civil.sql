with estado_civil as (SELECT id_estado_civil,
                             descricao_estado_civil
                      FROM   public.tb_estado_civil)
SELECT *
FROM   estado_civil;
