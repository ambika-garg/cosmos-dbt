with new_york_taxis as (
    select * from nyctlc
),

final as (

    SELECT 
        vendorID,
        sum(passengerCount) as totalPassengers,
        paymentType
    FROM 
        dbo.nyctlc 
    GROUP BY 
        vendorID,
        paymentType
)

select * from final
