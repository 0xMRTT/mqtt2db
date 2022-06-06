import logging

class BaseConnector:
    """ Basic CRUD methods """
    def __init__(self, config) -> None:
        self.config = config
        self.connexion = None

    def debug(self, msg, *args, **kwargs) -> None:
        """ Debug the database """
        logging.getLogger('mqtt2db').debug(msg, *args, **kwargs)

    def connect(self) -> None:
        """ Connect to the database

        Raises:
            NotImplementedError: if the method isn't overridden
        """
        raise NotImplementedError

    def disconnect(self) -> None:
        """ Disconnect from the database"""
        if self.is_connected():
            self.debug('Disconnecting from the database')
            self.connexion.close()
            self.connexion = None

    def is_connected(self) -> bool:
        """ Check if the database is connected

        Return:
            bool: True if the database is connected, False otherwise"""
        self.debug('Checking if the database is connected')
        if self.connexion is None:
            self.debug('Database is not connected. Use connect() to connect to the database')
            return False
        else:
            self.debug('Database is connected')
            return True

    def commit(self) -> None:
        """ Commit the current transaction """
        if self.is_connected():
            self.connexion.commit()
            self.debug('Commit transaction')
