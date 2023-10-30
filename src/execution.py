import psycopg2
import argparse
from create_tables import CreateTables
from tables_filling import FillTables
from get_tables_data import GetTablesData
from delete_tables_data import DeleteTables
from drop_tables import DropTables
from triggers_creation import TriggersCreation

def db_connection(database, user, password, host, port):

    connection = psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port
    )
    return connection


def all_tables_interaction(connection, cursor, commands):

    for command in commands:
        cursor.execute(command)

    connection.commit()


def create_tables(connection, cursor, commands):

    all_tables_interaction(connection, cursor, commands)
    print("All tables were created successfully")


def drop_tables(connection, cursor, commands):

    all_tables_interaction(connection, cursor, commands)
    print("All tables were dropped successfully")


def all_tables_filling(connection, cursor, commands):

    all_tables_interaction(connection, cursor, commands)
    print("All tables were filled successfully")


def main():

    database = "car_rental_db"
    user = "matuamod"
    password = "matua335"
    host = "0.0.0.0"
    port = "5432"

    connection = None
    cursor = None

    try:
        """ Connection to an existing database """
        connection = db_connection(database, user, password, host, port)
        print("Connection successfully created")

        """ Open cursor to perfom database operations """
        cursor = connection.cursor()
        print("Cursor successfully created")

        """ Query the database """

        parser = argparse.ArgumentParser(
            description="Executes standart queries on Postgres database")
        parser.add_argument("-c", "--create_all", required=False,
                            help="create all tables", action="store_true")
        parser.add_argument("-ct", "--create_triggers", required=False,
                            help="create all triggers", action="store_true")
        parser.add_argument("-dr", "--drop_all", required=False,
                            help="drop all tables", action="store_true")
        parser.add_argument("-da", "--delete_all", required=False,
                            help="delete all tables", action="store_true")
        parser.add_argument("-dc", "--delete_current", required=False,
                            help="delete current entity by id", action="store_true")
        parser.add_argument("-fa", "--fill_all", required=False,
                            help="fill all tables", action="store_true")
        parser.add_argument("-fc", "--fill_current", required=False,
                            help="fill current entity", action="store_true")
        parser.add_argument("-ga", "--get_all", required=False,
                            help="get all tables data", action="store_true")
        parser.add_argument("-gc", "--get_current", required=False,
                            help="get current tables data", action="store_true")
        args = parser.parse_args()

        if args.create_all:
            action = CreateTables()
            commands = action.get_sql_tables()
            create_tables(connection, cursor, commands)
        if args.create_triggers:
            action = TriggersCreation()
            commands = action.create_triggers()
            create_tables(connection, cursor, commands)
        if args.fill_all:
            action = FillTables()
            commands = action.default_tables_filling()
            all_tables_filling(connection, cursor, commands)
        if args.fill_current:
            action = FillTables()
            commands = action.current_entity_filling()
            all_tables_filling(connection, cursor, commands)
        if args.get_all:
            action = GetTablesData()
            action.get_all_tables(cursor)
        if args.get_current:
            action = GetTablesData()
            action.get_current_tables(cursor)
        if args.drop_all:
            action = DropTables()
            commands = action.drop_sql_tables()
            drop_tables(connection, cursor, commands)
        if args.delete_all:
            action = DeleteTables()
            action.delete_current_data(connection, cursor)
        if args.delete_current:
            action = DeleteTables()
            action.delete_current_entity(connection, cursor)

    except Exception as error:
        print(error)

    finally:
        # Close communication with database
        if cursor is not None:
            cursor.close()
            print("Cursor successfully closed")
        if connection is not None:
            connection.close()
            print("Connection successfully closed")


if __name__ == "__main__":
    print("Execution started")
    main()
    print("Execution finished")
