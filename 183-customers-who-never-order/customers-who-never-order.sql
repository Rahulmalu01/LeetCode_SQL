select name as Customers from customers c
Left outer join orders o
on o.customerID = c.id
where o.customerID IS NULL;