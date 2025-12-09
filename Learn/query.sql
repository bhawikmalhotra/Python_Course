SHOW databases;

use test;

select * from customers;

SELECT *
FROM customers
WHERE `First Name` = 'Linda';

-- remove duplicate first names
SELECT DISTINCT `First Name`
FROM customers;

-- modify rollno by adding 10 to each value
SELECT `First Name`, `Phone 2` + 10 AS new_rollno
FROM customers;

-- oracle
SELECT `First Name` || `Last Name` AS Full_Name
FROM customers;

SELECT concat(`First Name`, ' ' ,`Last Name` ) AS Full_Name
FROM customers;