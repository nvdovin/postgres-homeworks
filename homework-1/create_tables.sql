-- SQL-команды для создания таблиц

CREATE TABLE customers
(
	customers_id varchar(5) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

CREATE TABLE employees
(
	first_name varchar(100) PRIMARY KEY,
	last_name varchar(100),
	title varchar(100),
	birth_date varchar(10),
	notes text
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(10) UNIQUE REFERENCES customers(customers_id) NOT NULL,
	employee_id int,
	order_date varchar(10),
	ship_city varchar(50)
);
