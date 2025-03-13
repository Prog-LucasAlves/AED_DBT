WITH produtos AS (
    SELECT
        id,
        nome,
        categoria_id,
        preco,
        estoque
    FROM produtos
)
SELECT * FROM public.produtos
