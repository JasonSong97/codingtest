# think diagram
select v.customer_id, count(customer_id) as count_no_trans from visits as v
left join transactions as t
    on t.visit_id = v.visit_id
where t.transaction_id is null
group by customer_id;