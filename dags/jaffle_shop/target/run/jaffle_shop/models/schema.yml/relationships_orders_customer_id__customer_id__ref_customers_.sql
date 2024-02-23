
    

    

    EXEC('create view 
      dbo.testview_13559
     as 
    
    

with child as (
    select customer_id as from_field
    from "fabric-database"."dbo"."orders"
    where customer_id is not null
),

parent as (
    select customer_id as to_field
    from "fabric-database"."dbo"."customers"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


;')
    select
      
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      select * from 
      dbo.testview_13559
    
    ) dbt_internal_test;

    EXEC('drop view 
      dbo.testview_13559
    ;')

  