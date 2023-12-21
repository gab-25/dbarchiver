import subprocess
from dbarchiver.abstract_database_client import AbstractDatabseClient
from dbarchiver.database_connection import DatabaseConnection


class MongodbClient(AbstractDatabseClient):
    def __init__(self, connection: DatabaseConnection, archive: str):
        super().__init__("mongodbdump", "mongorestore")
        self.dbname = connection.dbname
        self.host = connection.host
        self.port = connection.port
        self.username = connection.username
        self.password = connection.password
        self.archive = archive

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
        if self.archive is None:
            raise Exception("file archive not found!")
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
