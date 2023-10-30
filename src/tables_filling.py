
class FillTables():

    def default_tables_filling(self):
        commands = (
            """
            INSERT INTO roles (name, permission) VALUES ('not logined user', 'watch sale announcements'); 
            INSERT INTO roles (name, permission) VALUES ('logined user', 'not logined user + make rent');
            INSERT INTO roles (name, permission) VALUES ('landlord', 'logined user + add sale announcements');
            INSERT INTO roles (name, permission) VALUES ('moderator', 'delete sale announcements, block users, watch logs');
            INSERT INTO roles (name, permission) VALUES ('admin', 'moderator + users CRUD operations');
            """,
            """
            INSERT INTO account (username, password) VALUES ('machetta', 'qww123wwq');
            INSERT INTO account (username, password) VALUES ('imaksus', 'ya_dadya_mitya');
            INSERT INTO account (username, password) VALUES ('kefir228', 'cheel_horosh');
            INSERT INTO account (username, password) VALUES ('erratic_cyclops', 'from_poland'); 
            """,
            """
            INSERT INTO users (role_id, account_id, email, telephone, date_of_birth) VALUES (2, 1, 'machetta228@gmail.com', '+375291234567', '2002-12-03');
            INSERT INTO users (role_id, account_id, email, telephone, date_of_birth) VALUES (2, 2, 'imaksus@gmail.com', '+375445678901', '2003-02-16');
            INSERT INTO users (role_id, account_id, email, telephone, date_of_birth) VALUES (2, 3, 'badkefir@gmail.com', '+375445673423', '2005-04-06');
            INSERT INTO users (role_id, account_id, email, telephone, date_of_birth) VALUES (2, 4, 'erratic_blin@gmail.com', '+4878882345', '2001-07-23');
            """,
            """
            INSERT INTO landlords (user_id, special_key) VALUES (2, 'Rni7h98Bay');
            INSERT INTO landlords (user_id, special_key) VALUES (4, '45vdeNWE3s');
            """,
            """
            INSERT INTO user_logs (user_id, message) VALUES (1, 'user 1 logined');
            INSERT INTO user_logs (user_id, message) VALUES (2, 'user 2 logined');
            INSERT INTO user_logs (user_id, message) VALUES (2, 'user 2 became landlord');
            INSERT INTO user_logs (user_id, message) VALUES (2, 'user 2 add car to rent');
            INSERT INTO user_logs (user_id, message) VALUES (3, 'user 3 logined');
            INSERT INTO user_logs (user_id, message) VALUES (4, 'user 4 became landlord');
            INSERT INTO user_logs (user_id, message) VALUES (2, 'user 2 add car to rent');
            """,
            """
            INSERT INTO brand (name, model) VALUES ('BMW', '3-series');
            INSERT INTO brand (name, model) VALUES ('Audi', 'A6');
            INSERT INTO brand (name, model) VALUES ('Mercedes-benz', 'S-class');
            INSERT INTO brand (name, model) VALUES ('Nissan', '350Z');
            INSERT INTO brand (name, model) VALUES ('BMW', 'X5');
            INSERT INTO brand (name, model) VALUES ('Subaru', 'Impreza WRX');
            """,
            """
            INSERT INTO car_type (type_name) VALUES ('sedan'), ('wagon'), ('hatchback'), ('pick up'), ('SUV'), ('coupe');
            """,
            """
            INSERT INTO car (landlord_id, car_type_id, brand_id, fuel_type, seats_count, color, registration_plate, price_per_day) VALUES (1, 6, 4, 'petrol', 2, 'yellow', '0350 IT-7', 45);
            INSERT INTO car (landlord_id, car_type_id, brand_id, fuel_type, seats_count, color, registration_plate, price_per_day) VALUES (1, 1, 2, 'diesel', 5, 'dark-blue', '1265 BM-7', 35);
            INSERT INTO car (landlord_id, car_type_id, brand_id, fuel_type, seats_count, color, registration_plate, price_per_day) VALUES (2, 2, 1, 'petrol', 5, 'black', '0340 MM-7', 60);
            INSERT INTO car (landlord_id, car_type_id, brand_id, fuel_type, seats_count, color, registration_plate, price_per_day) VALUES (2, 1, 3, 'diesel', 5, 'grey', '8888 CP-5', 40);
            INSERT INTO car (landlord_id, car_type_id, brand_id, fuel_type, seats_count, color, registration_plate, price_per_day) VALUES (2, 1, 6, 'petrol', 5, 'light blue', '2525 AC-2', 55);
            INSERT INTO car (landlord_id, car_type_id, brand_id, fuel_type, seats_count, color, registration_plate, price_per_day) VALUES (2, 5, 5, 'diesel', 7, 'marakish brown', '5555 XX-7', 65);
            """,
            """
            INSERT INTO car_images (car_id, url) VALUES (3, 'BMW 3-series photo'), (2, 'Audi A6 photo'), (4, 'Mercedes-benz S-class photo');
            INSERT INTO car_images (car_id, url) VALUES (1, 'Nissan 350Z photo'), (6, 'BMW X5 photo'), (5, 'Subaru Impreza WRX photo');
            """,
            """
            INSERT INTO pick_up_point (reception_point, issue_point) VALUES ('Minsk, Kavaleriyskaya street', 'Minsk, Partizanskaya street');
            INSERT INTO pick_up_point (reception_point, issue_point) VALUES ('Vitebsk, Zamkovaya street', 'Grodno, Sovetskaya street');
            INSERT INTO pick_up_point (reception_point, issue_point) VALUES ('Mogilev, Pervomayskaya street', 'Brest, Kosmonavtov street');
            INSERT INTO pick_up_point (reception_point, issue_point) VALUES ('Gomel, Biletskogo street', 'Mogilev, Pervomayskaya street');
            INSERT INTO pick_up_point (reception_point, issue_point) VALUES ('Grodno, Sovetskaya street', 'Minsk, Partizanskaya street');
            INSERT INTO pick_up_point (reception_point, issue_point) VALUES ('Gomel, Biletskogo street', 'Vitebsk, Zamkovaya street');
            """,
            """
            INSERT INTO rental_deal (user_id, car_id, pick_up_id, start_date, end_date, total_price) VALUES (1, 3, 4, '2022-11-11', '2022-12-12', 0);
            INSERT INTO rental_deal (user_id, car_id, pick_up_id, start_date, end_date, total_price) VALUES (1, 4, 2, '2022-09-01', '2022-09-03', 0);
            INSERT INTO rental_deal (user_id, car_id, pick_up_id, start_date, end_date, total_price) VALUES (3, 2, 1, '2022-12-11', '2022-12-12', 0);
            INSERT INTO rental_deal (user_id, car_id, pick_up_id, start_date, end_date, total_price) VALUES (2, 6, 3, '2023-01-23', '2023-01-28', 0);
            """,
            """
            INSERT INTO tax (tax_name, price) VALUES ('main tax', 567.745);
            INSERT INTO tax (tax_name, price) VALUES ('direct tax', 35.5);
            INSERT INTO tax (tax_name, price) VALUES ('luxury tax', 123.4);
            INSERT INTO tax (tax_name, price) VALUES ('excise tax', 76.45);
            INSERT INTO tax (tax_name, price) VALUES ('regressive tax', 34);
            INSERT INTO tax (tax_name, price) VALUES ('eventual tax', 146.7);
            """,
            """
            INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (1, 1);
            INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (2, 1);
            INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (4, 1);
            INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (2, 2);
            INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (3, 2);
            INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (1, 3);
            INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (4, 3);
            INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (2, 3);
            INSERT INTO tax_filling (tax_id, rental_deal_id) VALUES (3, 4);
            """
        )
        return commands


    def __set_current_account(self):
        print("Let's add new account")

        print("Write username: ")
        username = str(input())
        print("Write password: ")
        password = str(input())

        return ("""
            INSERT INTO account 
            (username, password) 
            VALUES ('{}', '{}');
            """.format(username, password), )


    def __set_current_role(self):
        print("Let's add new role")

        print("Write name: ")
        name = str(input())
        print("Write permission: ")
        permission = str(input())

        return ("""
            INSERT INTO roles 
            (name, permission) 
            VALUES ('{}', '{}');
            """.format(name, permission), )


    def __set_current_user(self):
        print("Let's add new user")

        print("Write role_id: ")
        role_id = int(input())
        print("Write account_id: ")
        account_id = int(input())
        print("Write email: ")
        email = str(input())
        print("Write telephone: ")
        telephone = str(input())
        print("Write date_of_birth: ")
        date_of_birth = str(input())

        return ("""
            INSERT INTO users 
            (role_id, account_id, email, telephone, date_of_birth) 
            VALUES ({}, {}, '{}', '{}', '{}');
            """.format(role_id, account_id, email, telephone, date_of_birth), )


    def __set_current_landlord(self):
        print("Let's add new landlord")

        print("Write user_id: ")
        user_id = int(input())
        print("Write special_key: ")
        special_key = str(input())

        return ("""
            INSERT INTO landlords 
            (user_id, special_key) 
            VALUES ({}, '{}');
            """.format(user_id, special_key), )


    def __set_current_user_log(self):
        print("Let's add new user log")

        print("Write ")
        print("Write ")


    def __set_current_brand(self):
        print("Let's add new brand")

        print("Write name: ")
        name = str(input())
        print("Write model: ")
        model = str(input())

        return ("""
            INSERT INTO brand 
            (name, model) 
            VALUES ('{}', '{}');
            """.format(name, model), )


    def __set_current_car_type(self):
        print("Let's add new car type")

        print("Write type_name: ")
        type_name = str(input())

        return ("""
            INSERT INTO car_type 
            (type_name) 
            VALUES ('{}');
            """.format(type_name), )


    def __set_current_car(self):
        print("Let's add new car")

        print("Write landlord_id: ")
        landlord_id = int(input())
        print("Write car_type_id: ")
        car_type_id = int(input())
        print("Write brand_id: ")
        brand_id = int(input())
        print("Write fuel_type: ")
        fuel_type = str(input())
        print("Write seats_count: ")
        seats_count = int(input())
        print("Write color: ")
        color = str(input())
        print("Write registration_plate: ")
        registration_plate = str(input())
        print("Write price_per_day: ")
        price_per_day = int(input())

        return ("""
            INSERT INTO car 
            (landlord_id, car_type_id, brand_id, fuel_type, seats_count, color, registration_plate, price_per_day) 
            VALUES ({}, {}, {}, '{}', {}, '{}', '{}', {});
            """.format(landlord_id, car_type_id, brand_id, fuel_type, seats_count, color, registration_plate, price_per_day), )


    def __set_current_car_image(self):
        print("Let's add new car_image: ")

        print("Write car_id: ")
        car_id = int(input())
        print("Write url: ")
        url = str(input())

        return ("""
            INSERT INTO car_images 
            (car_id, url) 
            VALUES ({}, '{}');
            """.format(car_id, url), )


    def __set_current_pick_up_point(self):
        print("Let's add new pick up point: ")

        print("Write reception_point: ")
        reception_point = str(input())
        print("Write issue_point: ")
        issue_point = str(input())

        return ("""
            INSERT INTO pick_up_point 
            (reception_point, issue_point) 
            VALUES ('{}', '{}');
            """.format(reception_point, issue_point), )


    def __set_current_rental_deal(self):
        print("Let's add new rental deal: ")

        print("Write user_id: ")
        user_id = int(input())
        print("Write car_id: ")
        car_id = int(input())
        print("Write pick_up_id: ")
        pick_up_id = int(input())
        print("Write start_date: ")
        start_date = str(input())
        print("Write end_date: ")
        end_date = str(input())
        total_price = 0

        return ("""
            INSERT INTO rental_deal 
            (user_id, car_id, pick_up_id, start_date, end_date, total_price)
            VALUES ({}, {}, {}, '{}', '{}', {});
            """.format(user_id, car_id, pick_up_id, start_date, end_date, total_price), )


    def __set_current_tax(self):
        print("Let's add new tax: ")

        print("Write tax_name: ")
        tax_name = str(input())
        print("Write price: ")
        price = float(input())

        return ("""
            INSERT INTO tax 
            (tax_name, price) 
            VALUES ('{}', {});
            """.format(tax_name, price), )


    def __set_current_tax_filling(self):
        print("Let's add new tax_filling: ")

        print("Write tax_id: ")
        tax_id = int(input())
        print("Write rental_deal_id: ")
        rental_deal_id = int(input())

        return ("""
            INSERT INTO tax_filling 
            (tax_id, rental_deal_id) 
            VALUES ({}, {});
            """.format(tax_id, rental_deal_id), )


    def current_entity_filling(self):
        print("Accounts: 1\nRoles: 2\nUsers: 3\nLandlords: 4\nBrands: 5\nCar types: 6\nCars: 7\n" +
            "Car images: 8\nPick up points: 9\nRental deals: 10\nTaxes: 11\nTax fillings: 12")

        print("\nChoose the index of the table you want to make fill:")

        table_index = int(input())

        match table_index:
            case 1:
                command = self.__set_current_account()
            case 2:
                command = self.__set_current_role()
            case 3:
                command = self.__set_current_user()
            case 4:
                command = self.__set_current_landlord()
            case 5:
                command = self.__set_current_brand()
            case 6:
                command = self.__set_current_car_type()
            case 7:
                command = self.__set_current_car()
            case 8:
                command = self.__set_current_car_image()
            case 9:
                command = self.__set_current_pick_up_point()
            case 10:
                command = self.__set_current_rental_deal()
            case 11:
                command = self.__set_current_tax()
            case 12:
                command = self.__set_current_tax_filling()
            case _:
                print("Nothing to fill")

        return command