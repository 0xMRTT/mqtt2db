import logging


class BaseConnector:
    """Basic CRUD methods"""

    def __init__(self, config) -> None:
        self.config = config
        self.connexion = None

    def debug(self, msg, *args, **kwargs) -> None:
        """Debug the database"""
        logging.getLogger("mqtt2db").debug(msg, *args, **kwargs)

    def connect(self) -> None:
        """Connect to the database

        Raises:
            NotImplementedError: if the method isn't overridden
        """
        raise NotImplementedError

    def disconnect(self) -> None:
        """Disconnect from the database"""
        if self.is_connected():
            self.debug("Disconnecting from the database")
            self.connexion.close()
            self.connexion = None

    def is_connected(self) -> bool:
        """Check if the database is connected

        Return:
            bool: True if the database is connected, False otherwise"""
        self.debug("Checking if the database is connected")
        if self.connexion is None:
            self.debug(
                "Database is not connected. Use connect() to connect to the database"
            )
            return False
        else:
            self.debug("Database is connected")
            return True

    def commit(self) -> None:
        """Commit the current transaction"""
        if self.is_connected():
            self.connexion.commit()
            self.debug("Commit transaction")

    def create_table(self, table_name:str, **kwargs) -> None:
        """Create a table in the database

        Args:
            table_name (str): name of the table"""
        if self.is_connected():
            self.debug("Creating table %s", table_name)
            query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, "
            for key, value in kwargs.items():
                query += f"{key} {value.upper()},"  # Add the column to the query using the key and the value where the value is the type of the column
            query = query[:-1] + ")"
            self.debug("Execute '%s'", query)
            self.connexion.execute(query)


    def create(self, table_name:str, **kwargs) -> None:
        """Create a new row in the database

        Args:
            table_name (str): name of the table
            **kwargs: key-value pairs of the row to create"""
        if self.is_connected():
            self.debug("Creating row in table %s", table_name)
            query = f"INSERT INTO {table_name} ("
            for key, in kwargs.keys():
                query += f"{key},"
            query = query[:-1] + ") VALUES ("
            for value in kwargs.values():
                query += f"{value},"
            query = query[:-1] + ")"
            self.debug("Execute '%s'", query)
            self.connexion.execute(query)

    def read(self, table_name:str, **kwargs) -> None:
        """Read a row from the database

        Args:
            table_name (str): name of the table
            **kwargs: key-value pairs of the row to read"""
        if self.is_connected():
            self.debug("Reading row from table %s", table_name)
            query = f"SELECT * FROM {table_name}"
            if kwargs is not None:
                query += " WHERE "
                for key, value in kwargs.items():
                    query += f"{key} = {value} AND "
                query = query[:-4]
            self.debug("Execute '%s'", query)
            self.connexion.execute(query)

    def update(self, table_name:str, **kwargs) -> None:
        """Update a row in the database

        Args:
            table_name (str): name of the table
            **kwargs: key-value pairs of the row to update"""
        if self.is_connected():
            self.debug("Updating row in table %s", table_name)
            query = f"UPDATE {table_name} SET "
            for key, value in kwargs.items():
                query += f"{key} = {value},"
            query = query[:-1]
            self.debug("Execute '%s'", query)
            self.connexion.execute(query)

    def delete(self, table_name:str, **kwargs) -> None:
        """Delete a row from the database

        Args:
            table_name (str): name of the table
            **kwargs: key-value pairs of the row to delete"""
        if self.is_connected():
            self.debug("Deleting row from table %s", table_name)
            query = f"DELETE FROM {table_name}"
            if kwargs is not None:
                query += " WHERE "
                for key, value in kwargs.items():
                    query += f"{key} = {value} AND "
                query = query[:-4]
            self.debug("Execute '%s'", query)
            self.connexion.execute(query)

    def delete_table(self, table_name:str) -> None:
        """Delete a table from the database

        Args:
            table_name (str): name of the table"""
        if self.is_connected():
            self.debug("Deleting table %s", table_name)
            query = f"DROP TABLE IF EXISTS {table_name}"
            self.debug("Execute '%s'", query)
            self.connexion.execute(query)
