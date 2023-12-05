CREATE TABLE countries (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(25) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	gender CHAR(1),
	age INT NOT NULL,
	phone_number CHAR(10) NOT NULL,
	country_id INT NOT NULL,	
	
	CONSTRAINT ck_customers_gender
		CHECK(gender IN ('M', 'F')),
	CONSTRAINT ck_customers_age
		CHECK(age > 0),
	CONSTRAINT fk_customers_countries
		FOREIGN KEY (country_id)
		REFERENCES countries(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE	
);

CREATE TABLE products (
	id SERIAL PRIMARY KEY,
	name VARCHAR(25) NOT NULL,
	description VARCHAR(250),
	recipe TEXT,
	price NUMERIC(10, 2) NOT NULL,
	
	CONSTRAINT ck_products_price
		CHECK(price > 0)
);

CREATE TABLE feedbacks (
	id SERIAL PRIMARY KEY,
	description VARCHAR(255), 
	rate NUMERIC(4, 2),
	product_id INT NOT NULL,
	customer_id INT NOT NULL,
	
	CONSTRAINT ck_feedbacks_rate
		CHECK (rate BETWEEN 0 AND 10),
	CONSTRAINT fk_feedbacks_products
		FOREIGN KEY (product_id)
		REFERENCES products(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_feedbacks_customers
		FOREIGN KEY (customer_id)
		REFERENCES customers(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE distributors (
	id SERIAL PRIMARY KEY,
	name VARCHAR(25) UNIQUE NOT NULL,
	address VARCHAR(30) NOT NULL,
	summary VARCHAR(200) NOT NULL,
	country_id INT NOT NULL,
	
	CONSTRAINT fk_distributors_countries
		FOREIGN KEY (country_id)
		REFERENCES countries(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE ingredients (
	id SERIAL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	description VARCHAR(200),
	country_id INT NOT NULL,
	distributor_id INT NOT NULL,
	
	CONSTRAINT fk_ingredients_countries
		FOREIGN KEY (country_id)
		REFERENCES countries(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_ingredients_distributors
		FOREIGN KEY (distributor_id)
		REFERENCES distributors(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE products_ingredients (
	product_id INT,
	ingredient_id INT,
	
	CONSTRAINT fk_products_ingredients_products
		FOREIGN KEY (product_id)
		REFERENCES products(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT fk_products_ingredients_ingredients
		FOREIGN KEY (ingredient_id)
		REFERENCES ingredients(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);
