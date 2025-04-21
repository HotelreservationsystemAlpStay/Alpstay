import os
import sqlite3

class DataBaseController:
    def __init__(self):
        """
        Initializes the database connection with a project-internal, relative database path.
        """
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_file = os.path.join(base_dir, "database", "db.sql")
        self.connection = sqlite3.connect(db_file)
        self.connection.row_factory = sqlite3.Row

    def initialize_database(self) -> None:
        """
        Initializes the database using an SQL schema.

        Reads a predefined SQL file and executes the contained SQL statements.
        """
        schema_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database", "db.sql")
        with open(schema_file, "r", encoding="utf-8") as f:
            schema = f.read()
        self.connection.executescript(schema)
        self.connection.commit()

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """
        Executes a generic SQL command (INSERT, UPDATE, DELETE).

        Args:
            query (str): The SQL command to be executed.
            params (tuple): Parameters for the SQL command (default: empty tuple).

        Returns:
            sqlite3.Cursor: Cursor object after executing the command.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def fetchall(self, query: str, params: tuple = ()) -> list:
        """
        Executes an SQL query and returns all rows of the result.

        Args:
            query (str): The SQL query.
            params (tuple): Parameters for the query (default: empty tuple).

        Returns:
            list: A list of rows corresponding to the query result.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def fetchone(self, query: str, params: tuple = ()) -> sqlite3.Row:
        """
        Executes an SQL query and returns the first row of the result.

        Args:
            query (str): The SQL query.
            params (tuple): Parameters for the query (default: empty tuple).

        Returns:
            sqlite3.Row: The first row of the query result.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def close(self) -> None:
        """
        Closes the database connection.
        """
        self.connection.close()
