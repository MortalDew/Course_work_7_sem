
class CreateTables():

    def get_sql_tables(self):
        """ Create tables for the PostgreSQL database"""
        commands = (
            """
            CREATE TABLE IF NOT EXISTS account (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                username VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS roles (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                name VARCHAR(50) NOT NULL,
                permission VARCHAR(100) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                role_id INT REFERENCES roles(id) ON DELETE CASCADE,
                account_id INT REFERENCES account(id) ON DELETE CASCADE UNIQUE,
                email VARCHAR(100) NOT NULL UNIQUE,
                telephone VARCHAR(13) UNIQUE,
                date_of_birth date NOT NULL,
                rent_status boolean NOT NULL default(false)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS landlords (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                user_id INT REFERENCES users(id) ON DELETE CASCADE UNIQUE,
                special_key VARCHAR(10) NOT NULL UNIQUE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS user_logs (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                user_id INT REFERENCES users(id) ON DELETE CASCADE,
                message VARCHAR(500) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS brand (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                name VARCHAR(50) NOT NULL,
                model VARCHAR(50) NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS car_type (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                type_name VARCHAR(50) NOT NULL UNIQUE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS car (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                landlord_id INT REFERENCES landlords(id) ON DELETE CASCADE NOT NULL,
                car_type_id INT REFERENCES car_type(id) ON DELETE CASCADE NOT NULL,
                brand_id INT REFERENCES brand(id) ON DELETE CASCADE NOT NULL,
                fuel_type VARCHAR(20),
                seats_count INT,
                color VARCHAR(50),
                registration_plate VARCHAR(10) NOT NULL UNIQUE,
                price_per_day NUMERIC NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS car_images (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                car_id INT REFERENCES car(id) ON DELETE CASCADE NOT NULL UNIQUE,
                url VARCHAR(200) NOT NULL UNIQUE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS pick_up_point (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                reception_point VARCHAR(100) NOT NULL,
                issue_point VARCHAR(100)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS rental_deal (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                user_id INT REFERENCES users(id) ON DELETE CASCADE NOT NULL,
                car_id INT REFERENCES car(id) ON DELETE CASCADE NOT NULL UNIQUE,
                pick_up_id INT REFERENCES pick_up_point(id) ON DELETE CASCADE NOT NULL,
                start_date DATE NOT NULL DEFAULT(NOW()),
                end_date DATE NOT NULL,
                total_price NUMERIC NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS tax (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                tax_name VARCHAR(50) NOT NULL,
                price NUMERIC NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS tax_filling (
                id SERIAL PRIMARY KEY NOT NULL UNIQUE,
                tax_id INT REFERENCES tax(id) ON DELETE CASCADE NOT NULL,
                rental_deal_id INT REFERENCES rental_deal(id) ON DELETE CASCADE NOT NULL
            );
            """
        )
        return commands
        
