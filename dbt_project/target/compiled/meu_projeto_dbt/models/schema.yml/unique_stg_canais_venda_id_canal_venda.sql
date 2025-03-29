select id_canal_venda as unique_field, count(*) as n_records
from dbtvendas_82ea.public_staging.stg_canais_venda
where id_canal_venda is not null
group by id_canal_venda
having count(*) > 1
;
