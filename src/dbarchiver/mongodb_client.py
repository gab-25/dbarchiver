import subprocess
from dbarchiver.abstract_database_client import AbstractDatabseClient
from dbarchiver.database_connection import DatabaseConnection


class MongodbClient(AbstractDatabseClient):
    def __init__(self, connection: DatabaseConnection, archive: str):
        super().__init__("mongodbdump", "mongorestore", connection, archive)

    def dump(self):
        file_archive = self.archive if self.archive is not None else self.generate_file_archive(self.dbname)
        result = subprocess.run(
            [
                self.get_dump_tool(),
                "--host={}".format(self.host),
                "--port={}".format(self.port),
                "--username={}".format(self.username),
                "--password={}".format(self.password),
                "--authenticationDatabase=admin",
                "--db={}".format(self.dbname),
                "--out={}".format(file_archive),
            ]
        )

    def restore(self):
        result = subprocess.run(
            [
                self.get_restore_tool(),
                "--host={}".format(self.host),
                "--port={}".format(self.port),
                "--username={}".format(self.username),
                "--password={}".format(self.password),
                "--authenticationDatabase=admin",
                "--db={}".format(self.dbname),
                "{}".format(self.archive),
            ]
        )
