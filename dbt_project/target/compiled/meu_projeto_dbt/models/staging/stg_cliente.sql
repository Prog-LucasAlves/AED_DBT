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

SELECT * FROM CLIENTE
