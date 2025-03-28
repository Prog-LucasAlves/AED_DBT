with email_marketing as(SELECT id_email_marketing,
                               descricao_email_marketing
                        FROM   public.tb_email_marketing)
SELECT *
FROM   email_marketing;
