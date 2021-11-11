DROP TABLE IF EXISTS guitars;
DROP TABLE IF EXISTS manufacturers;


CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) ,
    founded VARCHAR(255) ,
    location VARCHAR(255)
);

CREATE TABLE guitars(
    id SERIAL PRIMARY KEY,
    guitar_name VARCHAR(255),
    colour VARCHAR(255),
    manufacturer_id INT REFERENCES manufacturers(id),
    guitar_type VARCHAR(255),
    no_of_strings INT,
    production_date INT,
    stock_price INT,
    selling_price INT,
    quantity int

);
