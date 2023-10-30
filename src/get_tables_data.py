
class GetTablesData():

    def get_current_accounts(self, cursor):
        cursor.execute("SELECT * FROM account")
        print("\n", "All accounts data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("username: ", row[1])
            print("password: ", row[2], "\n")


    def get_current_roles(self, cursor):
        cursor.execute("SELECT * FROM roles")
        print("\n", "All roles data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("name: ", row[1])
            print("permission: ", row[2], "\n")


    def get_current_users(self, cursor):
        cursor.execute("SELECT * FROM users")
        print("\n", "All users data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("role_id: ", row[1])
            print("account_id: ", row[2])
            print("email: ", row[3])
            print("telephone: ", row[4])
            print("date_of_birth: ", row[5])
            print("rent_status: ", row[6], "\n")


    def get_current_landlords(self, cursor):
        cursor.execute("SELECT * FROM landlords")
        print("\n", "All landlords data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("user_id: ", row[1])
            print("special_key: ", row[2], "\n")


    def get_current_user_logs(self, cursor):
        cursor.execute("SELECT * FROM user_logs")
        print("\n", "All user_logs data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("user_id: ", row[1])
            print("message: ", row[2], "\n")


    def get_current_brands(self, cursor):
        cursor.execute("SELECT * FROM brand")
        print("\n", "All brands data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("name: ", row[1])
            print("model: ", row[2], "\n")


    def get_current_car_types(self, cursor):
        cursor.execute("SELECT * FROM car_type")
        print("\n", "All car_types data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("type_name: ", row[1], "\n")


    def get_current_cars(self, cursor):
        cursor.execute("SELECT * FROM car")
        print("\n", "All cars data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("landlord_id: ", row[1])
            print("car_type_id: ", row[2])
            print("brand_id: ", row[3])
            print("fuel_type: ", row[4])
            print("seats_count: ", row[5])
            print("color: ", row[6])
            print("registration_plate: ", row[7])
            print("price_per_day: ", row[8], "\n")


    def get_current_car_images(self, cursor):
        cursor.execute("SELECT * FROM car_images")
        print("\n", "All car_images data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("car_id: ", row[1])
            print("url: ", row[2], "\n")


    def get_current_pick_up_points(self, cursor):
        cursor.execute("SELECT * FROM pick_up_point")
        print("\n", "All pick_up_points data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("reception_point: ", row[1])
            print("issue_point: ", row[2], "\n")


    def get_current_rental_deals(self, cursor):
        cursor.execute("SELECT * FROM rental_deal")
        print("\n", "All rental_deals data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("user_id: ", row[1])
            print("car_id: ", row[2])
            print("pick_up_id: ", row[3])
            print("start_date: ", row[4])
            print("end_date: ", row[5])
            print("total_price: ", row[6], "\n")


    def get_current_taxes(self, cursor):
        cursor.execute("SELECT * FROM tax")
        print("\n", "All taxes data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("tax_name: ", row[1])
            print("price: ", row[2], "\n")


    def get_current_tax_fillings(self, cursor):
        cursor.execute("SELECT * FROM tax_filling")
        print("\n", "All tax_filling data:", "\n")

        for row in cursor.fetchall():
            print("id: ", row[0])
            print("tax_id: ", row[1])
            print("rental_deal_id: ", row[2], "\n")


    def get_all_tables(self, cursor):
        print("Show all tables data: ", "\n")

        self.get_current_accounts(cursor)
        self.get_current_roles(cursor)
        self.get_current_users(cursor)
        self.get_current_landlords(cursor)
        self.get_current_user_logs(cursor)
        self.get_current_brands(cursor)
        self.get_current_car_types(cursor)
        self.get_current_cars(cursor)
        self.get_current_car_images(cursor)
        self.get_current_pick_up_points(cursor)
        self.get_current_rental_deals(cursor)
        self.get_current_taxes(cursor)
        self.get_current_tax_fillings(cursor)


    def get_current_tables(self, cursor):
        print("Accounts: 1\nRoles: 2\nUsers: 3\nLandlords: 4\nUser logs: 5\nBrands: 6\nCar types: 7\nCars: 8\n" +
            "Car images: 9\nPick up points: 10\nRental deals: 11\nTaxes: 12\nTax fillings: 13")

        print("\nChoose the index of the table you want to see:")

        table_index = int(input())

        match table_index:
            case 1:
                self.get_current_accounts(cursor)
            case 2:
                self.get_current_roles(cursor)
            case 3:
                self.get_current_users(cursor)
            case 4:
                self.get_current_landlords(cursor)
            case 5:
                self.get_current_user_logs(cursor)
            case 6:
                self.get_current_brands(cursor)
            case 7:
                self.get_current_car_types(cursor)
            case 8:
                self.get_current_cars(cursor)
            case 9:
                self.get_current_car_images(cursor)
            case 10:
                self.get_current_pick_up_points(cursor)
            case 11:
                self.get_current_rental_deals(cursor)
            case 12:
                self.get_current_taxes(cursor)
            case 13:
                self.get_current_tax_fillings(cursor)
            case _:
                print("Nothing to get")

