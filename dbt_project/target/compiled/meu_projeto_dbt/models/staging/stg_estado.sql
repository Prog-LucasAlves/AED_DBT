WITH ESTADO AS (
    SELECT
        ID_ESTADO,

        DESCRICAO_ESTADO,

        SIGLA_ESTADO

    FROM PUBLIC.TB_ESTADO

)

SELECT * FROM ESTADO
