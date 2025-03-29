CREATE VIEW DBTVENDAS_82EA.PUBLIC_STAGING.STG_CLIENTE__DBT_TMP


AS (
    WITH CLIENTE AS (

        SELECT

            ID_CLIENTE,

            PRIMEIRO_NOME,

            SOBRENOME,

            ID_GENERO,

            ID_ESTADO_CIVIL,

            DATA_NASCIMENTO,

            CPF,

            RG,

            EMAIL,

            TELEFONE,

            ENDERECO,

            ID_ESTADO,

            ID_EMAIL_MARKETING

        FROM PUBLIC.TB_CLIENTE

    )


    SELECT *

    FROM CLIENTE
);
