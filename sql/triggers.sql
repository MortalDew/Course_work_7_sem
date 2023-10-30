CREATE OR REPLACE FUNCTION add_user_logs() 
    RETURNS trigger AS
$$
    BEGIN
        -- Добавление строки в emp_audit, которая отражает операцию, выполняемую в emp;
        -- для определения типа операции применяется специальная переменная TG_OP.
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO user_logs (user_id, message)
            VALUES
                (OLD.id, CONCAT(
                    'User with id = ',
                    OLD.id,
                    ' and account id = ',
                    OLD.account_id,
                    ' was deleted successfully'
                ));
            RETURN OLD;
        ELSIF (TG_OP = 'UPDATE') 
        THEN
            INSERT INTO user_logs (user_id, message)
            VALUES
                (NEW.id, CONCAT(
                    'User with id = ',
                    NEW.id,
                    ' and account id = ',
                    NEW.account_id,
                    ' was updated successfully'
                ));
            RETURN NEW;
        ELSIF (TG_OP = 'INSERT') 
        THEN
            INSERT INTO user_logs (user_id, message)
            VALUES
                (NEW.id, CONCAT(
                    'User with id = ',
                    NEW.id,
                    ' and account id = ',
                    NEW.account_id,
                    ' was inserted successfully'
                ));
            RETURN NEW; 
        END IF;
        RETURN NULL; -- возвращаемое значение для триггера AFTER игнорируется
    END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER add_logs
AFTER INSERT OR UPDATE OR DELETE 
ON users
    FOR EACH ROW 
    EXECUTE PROCEDURE add_user_logs();


-- test user_logs trigger
INSERT INTO account (username, password) 
VALUES ('batva_suhaya', 'lolchick');

INSERT INTO users (role_id, account_id, email, telephone, date_of_birth) 
VALUES (2, 5, 'batvaaaaa@gmail.com', '+375765434567', '2004-02-06');


CREATE OR REPLACE FUNCTION hour_diff_price() 
    RETURNS trigger AS 
$$
    DECLARE
        date_difference INT = 0;
        car_price INT = 0;
        rented_car_id INT = 0;
        user_id INT = 0;
    BEGIN
        SELECT id
            INTO user_id
            FROM users
            WHERE id = NEW.user_id;
        
        SELECT end_date - start_date + 1 
            INTO date_difference
            FROM rental_deal;

        SELECT id, price_per_day 
            INTO rented_car_id, car_price
            FROM car 
            WHERE car.id = NEW.car_id;

        IF rented_car_id IS NOT NULL THEN
            UPDATE rental_deal
                SET total_price = car_price * date_difference
                WHERE car_id = rented_car_id;

            CALL set_user_rent_status(user_id, true);

            RETURN NEW;
        END IF;
        RETURN NULL;
    END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE trigger get_rental_price
AFTER INSERT
ON rental_deal
    FOR EACH ROW 
    EXECUTE PROCEDURE hour_diff_price();


INSERT INTO rental_deal (user_id, car_id, pick_up_id, start_date, end_date, total_price) 
VALUES (2, 1, 4, '2022-11-11', '2022-12-12', 0);

INSERT INTO rental_deal (user_id, car_id, pick_up_id, start_date, end_date, total_price) 
VALUES (4, 5, 2, '2022-11-11', '2022-11-17', 0);


CREATE OR REPLACE FUNCTION tax_price()
    RETURNS trigger AS
$$
    DECLARE
        price_for_tax INT = 0;
    BEGIN 

        IF NEW.tax_id IS NOT NULL
        AND NEW.rental_deal_id IS NOT NULL 
        THEN
            SELECT price
                INTO price_for_tax
                FROM tax
                WHERE id = NEW.tax_id;

            UPDATE rental_deal
                SET total_price = total_price + price_for_tax
                WHERE id = NEW.rental_deal_id;
            RETURN NEW;
        ELSE
            RETURN NULL;
        END IF;
    END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE trigger get_tax_price
AFTER INSERT
ON tax_filling
    FOR EACH ROW
    EXECUTE PROCEDURE tax_price();


INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (1, 3);
INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (4, 3);
INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (2, 3);
INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (3, 4);


CREATE OR REPLACE PROCEDURE set_user_rent_status(user_id INT, isRented BOOLEAN)
AS $$
    BEGIN   
        UPDATE users
            SET rent_status = CASE
                WHEN isRented = true THEN true
                WHEN isRented = false THEN false
                END
                WHERE id = user_id;
    END;
$$
LANGUAGE plpgsql;

-- for delete rental_deal values
--CALL set_user_rent_status(user_id, false)
