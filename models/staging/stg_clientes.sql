WITH clientes AS (
    SELECT
        id,
        primeiro_nome,
        segundo_nome,
        genero_id,
        estado_civil_id,
        cpf,
        rg,
        email,
        telefone,
        endereco,
        estado_id
    FROM public.clientes
)
SELECT * FROM clientes
