-- SQL-команды для создания таблиц
createdb -U postgres north

CREATE TABLE customers_name
(
	customer_id varchar(20) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	author varchar(50) NOT NULL
);

CREATE TABLE employees_data
(
	first_name varchar(50) PRIMARY KEY,
	last_name varchar(50) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE orders_data
(
	order_id serial PRIMARY KEY,
	customer_id varchar(20) NOT NULL,
	employee_id varchar(20) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(50) NOT NULL
)