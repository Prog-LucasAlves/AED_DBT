CREATE VIEW DBTVENDAS_82EA.PUBLIC_STAGING.STG_ESTADO__DBT_TMP


AS (
    WITH ESTADO AS (

        SELECT

            ID_ESTADO,

            DESCRICAO_ESTADO,

            SIGLA_ESTADO

        FROM PUBLIC.TB_ESTADO

    )


    SELECT *

    FROM ESTADO
);
