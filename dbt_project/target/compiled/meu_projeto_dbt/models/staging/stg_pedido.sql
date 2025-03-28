WITH PEDIDO AS (
    SELECT
        ID_PEDIDO,

        ID_CLIENTE,

        ID_FORMA_PAGAMENTO,

        ID_CANAL_VENDA,

        ID_STATUS,

        DATA_PEDIDO,

        SUBTOTAL,

        FRETE,

        TOTAL,

        DATA_ENTREGA

    FROM PUBLIC.TB_PEDIDO

)

SELECT * FROM PEDIDO
