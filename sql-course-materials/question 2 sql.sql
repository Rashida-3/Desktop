SELECT* FROM customers WHERE birth_date> '1990-01-01';
-- get order place this year
SELECT * FROM customers  WHERE order_date >= '2019-01-01';
SELECT * FROM customers WHERE birth_date >'1990-01-01' AND points>1000;
SELECT * FROM customers WHERE birth_date >'1990-01-01' OR points>1000 AND state='va';
-- where the total price greater than 30
SELECT* FROM order_items WHERE order_id=6 AND unit_price*quantity>30;
SELECT * FROM customers WHERE state IN ('VA','FL','GA');
SELECT* FROM customers WHERE last_name LIKE '_____y';
SELECT* FROM customers WHERE address LIKE '%trail%' OR
							 address LIKE '%avenue%'	;
SELECT * FROM customers WHERE phone NOT LIKE  '%9'      ;
SELECT * FROM customers WHERE last_name LIKE '%field';
SELECT* FROM customers WHERE last_name REGEXP 'field|mac|rose'  ;
SELECT * FROM customers WHERE last_name REGEXP '[a-h]e'   ;
SELECT* FROM customers WHERE last_name REGEXP 'EY|ON'  ;
SELECT* FROM customers WHERE first_name REGEXP 'ELKA|AMBUR'  ;

                
                             