WITH clientes AS (
    SELECT
        id_cliente,
        primeiro_nome,
        email,
        estado,
        data_cadastro::DATE AS data_cadastro
    FROM public.clientes
)
SELECT * FROM clientes
