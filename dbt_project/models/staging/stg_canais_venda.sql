with canais_venda as (SELECT id_canal_venda,
                             descricao_canal_venda
                      FROM   public.tb_canais_venda)
SELECT *
FROM   canais_venda;
