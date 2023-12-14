from dbarchiver.abstract_database_client import AbstractDatabseClient
from dbarchiver.database_connection import DatabaseConnection


class SqliteClient(AbstractDatabseClient):
    def __init__(self, connection: DatabaseConnection):
        super().__init__("sqlite3", "sqlite3")

    def dump(self):
        pass

    def restore(self):
        pass
