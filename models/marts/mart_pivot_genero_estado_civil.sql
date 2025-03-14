SELECT
  genero,
  {{ dbt_utils.pivot(
      'estado_civil',
      dbt_utils.get_column_values(ref('stg_cliente_genero_estado_civil'), 'estado_civil')
  ) }}
FROM {{ ref('stg_cliente_genero_estado_civil') }}
group by genero
