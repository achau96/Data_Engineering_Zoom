{{ config(materialized='view') }}

with tripdata as 
(
  select *,

  from {{ source('staging','fhv_tripdata_local') }}
 
)
select
    -- identifiers
    cast(dispatching_base_num as string) as dispatching_base_num,
    cast(Affiliated_base_number as string) as affiliated_base_number,
    cast(PUlocationID as integer) as  pickup_locationid,
    cast(DOlocationID as integer) as dropoff_locationid,
    
    -- timestamps
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,
    

    
from tripdata
-- dbt build --m <model.sql> --var 'is_test_run: false'
-- {% if var('is_test_run', default=true) %}

--   limit 100

-- {% endif %}