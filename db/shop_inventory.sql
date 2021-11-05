DROP TABLE guitars;
DROP TABLE manufacturers;


CREATE TABLE manufacturers(
    id SERIAL PRIMARY KEY,
    company_name VARCHAR,
    founded VARCHAR,
    location VARCHAR,
)

CREATE TABLE guitars(
    id SERIAL PRIMARY KEY,
    guitar_name VARCHAR(255),
    colour VARCHAR(255),
    manufacturer INT REFERENCES manufacturers(id),
    guitar_type VARCHAR(255),
    no_of_strings VARCHAR(255),
    production_date VARCHAR(255),
    stock_price VARCHAR(255),
    selling_price VARCHAR(255),

);