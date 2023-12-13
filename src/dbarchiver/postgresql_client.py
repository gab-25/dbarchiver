from dbarchiver.__main__ import DatabaseConnection
from dbarchiver.abstract_database_client import AbstractDatabseClient


class PostgresqlClient(AbstractDatabseClient):
    def __init__(self, connection: DatabaseConnection):
        super().__init__("pg_dump", "pg_restore")

    def dump(self):
        pass

    def restore(self):
        pass
