
    

    

    EXEC('create view 
      dbo.testview_5813
     as 
    
    

with all_values as (

    select
        status as value_field,
        count(*) as n_records

    from "fabric-database"."dbo"."orders"
    group by status

)

select *
from all_values
where value_field not in (
    ''placed'',''shipped'',''completed'',''return_pending'',''returned''
)


;')
    select
      
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      select * from 
      dbo.testview_5813
    
    ) dbt_internal_test;

    EXEC('drop view 
      dbo.testview_5813
    ;')

  