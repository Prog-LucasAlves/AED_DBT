WITH clientes_gold AS (
    SELECT
        c.id AS cliente_id,
        g.descricao AS genero,
        e.descricao AS estado_civil
    FROM {{ ref('stg_clientes') }} c
    JOIN {{ ref('stg_generos') }} g ON c.genero_id = g.id
    JOIN {{ ref('stg_estados_civis') }} e ON c.estado_civil_id = e.id
)
SELECT * FROM clientes_gold
