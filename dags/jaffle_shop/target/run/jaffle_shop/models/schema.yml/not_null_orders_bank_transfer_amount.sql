select
      
      count(*) as failures,
      case when count(*) != 0
        then 'true' else 'false' end as should_warn,
      case when count(*) != 0
        then 'true' else 'false' end as should_error
    from (
      
    
    



select bank_transfer_amount
from "fabric-database"."dbo"."orders"
where bank_transfer_amount is null



    ) dbt_internal_test