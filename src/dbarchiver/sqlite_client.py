from dbarchiver.abstract_database_client import AbstractDatabseClient


class SqliteClient(AbstractDatabseClient):
    def __init__(self):
        super().__init__("sqlite3", "sqlite3")

    def dump(self):
        pass

    def restore(self):
        pass
