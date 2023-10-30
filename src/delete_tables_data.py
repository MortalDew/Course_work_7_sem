from get_tables_data import GetTablesData

class DeleteTables():

    def __delete_current_entities(self, connection, cursor, table_name):
        cursor.execute("SELECT * FROM {0}".format(table_name))
        entities = cursor.fetchall()

        for index, entity in enumerate(entities):
            cursor.execute("DELETE FROM {0} WHERE id = {1}".format(table_name, str(index+1)))

        connection.commit()


    def delete_current_data(self, connection, cursor):
        entity_dict = {
            0: "car_images", 1: "tax_filling",
            2: "tax", 3: "rental_deal",
            4: "pick_up_point", 5: "car",
            6: "car_type", 7: "brand",
            8: "user_logs", 9: "landlords",
            10: "users", 11: "roles", 12: "account"
        }

        for key in entity_dict:
            self.__delete_current_entities(connection, cursor, entity_dict[key])


    def __delete_operation(self, connection, cursor, table_name, id):
        cursor.execute("SELECT * FROM {0}".format(table_name))
        entities = cursor.fetchall()

        for index, entity in enumerate(entities):
            if index == id-1:
                cursor.execute("DELETE FROM {0} WHERE id = {1}".format(table_name, str(id)))
                connection.commit()
                return

        print("No such id in this entity\n")


    def __get_entity_id(self):
        print("\nChoose the id of the entity you want to delete:")
        entity_id = int(input())
        
        return entity_id


    def delete_current_entity(self, connection, cursor):
        print("Accounts: 1\nRoles: 2\nUsers: 3\nLandlords: 4\nBrands: 5\nCar types: 6\nCars: 7\n" +
            "Car images: 8\nPick up points: 9\nRental deals: 10\nTaxes: 11\nTax fillings: 12")

        print("\nChoose the index of the table you want to make delete:")

        table_index = int(input())

        match table_index:
            case 1:
                action = GetTablesData()
                action.get_current_accounts(cursor)
                self.__delete_operation(connection, cursor, "account", self.__get_entity_id())
            case 2:
                action = GetTablesData()
                action.get_current_roles(cursor)
                self.__delete_operation(connection, cursor, "roles", self.__get_entity_id())
            case 3:
                action = GetTablesData()
                action.get_current_users(cursor)
                self.__delete_operation(connection, cursor, "users", self.__get_entity_id())
            case 4:
                action = GetTablesData()
                action.get_current_landlords(cursor)
                self.__delete_operation(connection, cursor, "landlords", self.__get_entity_id())
            case 5:
                action = GetTablesData()
                action.get_current_brands(cursor)
                self.__delete_operation(connection, cursor, "brand", self.__get_entity_id())
            case 6:
                action = GetTablesData()
                action.get_current_car_types(cursor)
                self.__delete_operation(connection, cursor, "car_type", self.__get_entity_id())
            case 7:
                action = GetTablesData()
                action.get_current_cars(cursor)
                self.__delete_operation(connection, cursor, "car", self.__get_entity_id())
            case 8:
                action = GetTablesData()
                action.get_current_car_images(cursor)
                self.__delete_operation(connection, cursor, "car_images", self.__get_entity_id())
            case 9:
                action = GetTablesData()
                action.get_current_pick_up_points(cursor)
                self.__delete_operation(connection, cursor, "pick_up_point", self.__get_entity_id())
            case 10:
                action = GetTablesData()
                action.get_current_rental_deals(cursor)
                self.__delete_operation(connection, cursor, "rental_deal", self.__get_entity_id())
            case 11:
                action = GetTablesData()
                action.get_current_taxes(cursor)
                self.__delete_operation(connection, cursor, "tax", self.__get_entity_id())
            case 12:
                action = GetTablesData()
                action.get_current_tax_fillings(cursor)
                self.__delete_operation(connection, cursor, "tax_filling", self.__get_entity_id())
            case _:
                print("Nothing to fill\n")

