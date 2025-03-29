select id_status as unique_field, count(*) as n_records
from dbtvendas_82ea.public_staging.stg_status
where id_status is not null
group by id_status
having count(*) > 1
;
