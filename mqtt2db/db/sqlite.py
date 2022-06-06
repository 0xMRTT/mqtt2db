import sqlite3

from . import BaseConnector


class SqliteConnector(BaseConnector):
    def connect(self) -> None:
        self.connexion = sqlite3.connect(self.config["database"]["filename"])
        self.cursor = self.connexion.cursor()
