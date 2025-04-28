
  create view "dbt_q4iu"."public_staging"."stg_cliente__dbt_tmp"


  as (
    with
    cliente as (
        select
            id_cliente,
            primeiro_nome,
            sobrenome,
            id_genero,
            id_estado_civil,
            data_nascimento,
            cpf,
            rg,
            email,
            telefone,
            endereco,
            id_estado,
            id_email_marketing
        from public_data.tb_cliente
    )

select *
from cliente
  );
