CREATE TABLE DBTVENDAS_82EA.PUBLIC_RAW.RAW_TICKET_MEDIO_CLIENTE__DBT_TMP


AS

(
-- Total de pedidos e ticket medio por cliente com status de entrega como ENTREGUE
    WITH TICKET_MEDIO_POR_CLIENTE AS (
        SELECT
            C.ID_CLIENTE,
            C.PRIMEIRO_NOME,
            C.EMAIL,
            C.TELEFONE,
            COUNT(P.ID_PEDIDO) AS QTD_PEDIDOS,
            ROUND(CAST(AVG(P.TOTAL) AS NUMERIC), 2) AS TICKET_MEDIO
        FROM
            DBTVENDAS_82EA.PUBLIC_STAGING.STG_CLIENTE C
        LEFT JOIN
            DBTVENDAS_82EA.PUBLIC_RAW.RAW_PEDIDO P
            ON C.ID_CLIENTE = P.ID_CLIENTE
        WHERE
            P.ID_STATUS = 4
        GROUP BY
            C.ID_CLIENTE, C.PRIMEIRO_NOME, C.EMAIL, C.TELEFONE
    )

    SELECT * FROM TICKET_MEDIO_POR_CLIENTE
    WHERE TICKET_MEDIO IS NOT NULL
    ORDER BY TICKET_MEDIO DESC
);
