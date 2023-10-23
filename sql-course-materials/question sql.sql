SELECT * FROM sql_store.orders 
WHERE order_date >='2019-01-01' ;
SELECT* FROM orders WHERE shipper_id is null;
SELECT* FROM orders WHERE shipper_id is not null;
SELECT *FROM customers ORDER BY state ,first_name ;
SELECT *FROM customers LIMIT 6;
SELECT *FROM customers ORDER BY points DESC;
SELECT* FROM orders JOIN customers ON orders.customer_id=customer.customer_id
