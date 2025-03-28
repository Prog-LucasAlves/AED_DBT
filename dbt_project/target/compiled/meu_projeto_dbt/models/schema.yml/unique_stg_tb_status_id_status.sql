SELECT
    ID_STATUS AS UNIQUE_FIELD,
    count(*) AS N_RECORDS

FROM DBTVENDAS_82EA.PUBLIC_STAGING.STG_TB_STATUS
WHERE ID_STATUS IS NOT NULL
GROUP BY ID_STATUS
HAVING count(*) > 1
