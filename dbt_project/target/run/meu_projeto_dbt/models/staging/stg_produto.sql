CREATE VIEW "dbtvendas_82ea"."public_staging"."stg_produto__dbt_tmp" as (with produto AS (SELECT id_produto,
                                                                                                 descricao_produto,
                                                                                                 id_categoria,
                                                                                                 preco_unitario,
                                                                                                 quantidade_estoque
                                                                                          FROM   public.tb_produto)
SELECT *
FROM   produto);
