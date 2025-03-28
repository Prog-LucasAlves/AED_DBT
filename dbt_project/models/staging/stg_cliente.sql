with cliente as (SELECT id_cliente,
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
                 FROM   public.tb_cliente)
SELECT *
FROM   cliente;
