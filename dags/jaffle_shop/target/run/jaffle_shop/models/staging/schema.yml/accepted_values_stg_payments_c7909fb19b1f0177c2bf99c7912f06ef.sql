
    

    

    EXEC('create view 
      dbo.testview_18020
     as 
    
    

with all_values as (

    select
        payment_method as value_field,
        count(*) as n_records

    from "fabric-database"."dbo"."stg_payments"
    group by payment_method

)

select *
from all_values
where value_field not in (
    ''credit_card'',''coupon'',''bank_transfer'',''gift_card''
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
      dbo.testview_18020
    
    ) dbt_internal_test;

    EXEC('drop view 
      dbo.testview_18020
    ;')

  