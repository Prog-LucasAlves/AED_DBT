  create view "dbtvendas_82ea"."public_staging"."stg_genero__dbt_tmp"


  as (
    with genero as (select id_genero, descricao_genero from public.tb_genero)


select *

from genero
  );
