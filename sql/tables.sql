CREATE TABLE account (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
);


CREATE TABLE roles (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    permission VARCHAR(100) NOT NULL
);


CREATE TABLE users (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    role_id INT REFERENCES roles(id),
    account_id INT REFERENCES account(id) UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    telephone VARCHAR(13) UNIQUE,
    date_of_birth date NOT NULL,
    rent_status boolean NOT NULL default(false)
);


CREATE TABLE landlords (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    user_id INT REFERENCES users(id) UNIQUE,
    special_key VARCHAR(10) NOT NULL UNIQUE
);


CREATE TABLE user_logs (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    user_id INT REFERENCES users(id),
    message VARCHAR(500) NOT NULL
);


CREATE TABLE brand (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    name VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL
);


CREATE TABLE car_type (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    type_name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE car (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    landlord_id INT REFERENCES landlords(id) NOT NULL,
    car_type_id INT REFERENCES car_type(id) NOT NULL,
    brand_id INT REFERENCES brand(id) NOT NULL,
    fuel_type VARCHAR(20),
    seats_count INT,
    color VARCHAR(50),
    registration_plate VARCHAR(10) NOT NULL UNIQUE,
    price_per_day NUMERIC NOT NULL
);


CREATE TABLE car_images (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    car_id INT REFERENCES car(id) NOT NULL UNIQUE,
    url VARCHAR(200) NOT NULL UNIQUE
);


CREATE TABLE pick_up_point (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    reception_point VARCHAR(100) NOT NULL,
    issue_point VARCHAR(100)
);


CREATE TABLE rental_deal (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    user_id INT REFERENCES users(id) NOT NULL,
    car_id INT REFERENCES car(id) NOT NULL UNIQUE,
    pick_up_id INT REFERENCES pick_up_point(id) NOT NULL,
    start_date DATE NOT NULL DEFAULT(NOW()),
    end_date DATE NOT NULL,
    total_price NUMERIC default(NULL)
);


CREATE TABLE tax (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    tax_name VARCHAR(50) NOT NULL,
    price NUMERIC NOT NULL
);


CREATE TABLE tax_filling (
    id SERIAL PRIMARY KEY NOT NULL UNIQUE,
    tax_id INT REFERENCES tax(id) NOT NULL,
    rental_deal_id INT REFERENCES rental_deal(id) NOT NULL
);






