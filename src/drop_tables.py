
class DropTables():

    def drop_sql_tables(self):
        """ Create tables for the PostgreSQL database"""
        commands = (
            """
            DROP TABLE IF EXISTS account CASCADE;
            """,
            """
            DROP TABLE IF EXISTS roles CASCADE;
            """,
            """
            DROP TABLE IF EXISTS users CASCADE;
            """,
            """
            DROP TABLE IF EXISTS landlords CASCADE;
            """,
            """
            DROP TABLE IF EXISTS user_logs CASCADE;
            """,
            """
            DROP TABLE IF EXISTS brand CASCADE;
            """,
            """
            DROP TABLE IF EXISTS car_type CASCADE;
            """,
            """
            DROP TABLE IF EXISTS car CASCADE;
            """,
            """
            DROP TABLE IF EXISTS car_images CASCADE;
            """,
            """
            DROP TABLE IF EXISTS pick_up_point CASCADE;
            """,
            """
            DROP TABLE IF EXISTS rental_deal CASCADE;
            """,
            """
            DROP TABLE IF EXISTS tax CASCADE;
            """,
            """
            DROP TABLE IF EXISTS tax_filling CASCADE;
            """
        )
        return commands

