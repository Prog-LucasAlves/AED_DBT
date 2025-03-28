CREATE VIEW DBTVENDAS_82EA.PUBLIC_STAGING.STG_PEDIDO__DBT_TMP


AS (
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
);
