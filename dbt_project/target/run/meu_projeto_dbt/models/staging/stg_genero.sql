CREATE VIEW DBTVENDAS_82EA.PUBLIC_STAGING.STG_GENERO__DBT_TMP


AS (
    WITH GENERO AS (

        SELECT

            ID_GENERO,

            DESCRICAO_GENERO

        FROM PUBLIC.TB_GENERO

    )


    SELECT *

    FROM GENERO
);
