import subprocess
from dbarchiver.__main__ import DatabaseConnection
from dbarchiver.abstract_database_client import AbstractDatabseClient


class MongodbClient(AbstractDatabseClient):
    def __init__(self, connection: DatabaseConnection):
        super().__init__("mongodbdump", "mongorestore")
        self.connectionString = (
            f"mongodb://{connection.username@connection.password}:{connection.host}:{connection.port}/?AuthSource=admin"
        )
        self.dbname = connection.dbname

    def dump(self):
        result = subprocess.run([self.get_dump_tool(), self.connectionString, self.dbname])

    def restore(self):
        pass
