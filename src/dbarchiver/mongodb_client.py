import subprocess
from dbarchiver.abstract_database_client import AbstractDatabseClient
from dbarchiver.database_connection import DatabaseConnection


class MongodbClient(AbstractDatabseClient):
    def __init__(self, connection: DatabaseConnection, archive: str):
        super().__init__("mongodbdump", "mongorestore", archive)
        self.connectionString = (
            f"mongodb://{connection.username@connection.password}:{connection.host}:{connection.port}/?AuthSource=admin"
        )
        self.dbname = connection.dbname

    def dump(self):
        file_archive = f"{self.out_directory}/{self.generate_archive_filename(self.dbname)}" if not self.file_archive else self.file_archive
        result = subprocess.run([self.get_dump_tool(), self.connectionString, f"--db={self.dbname}", 
                                 f"--archive={file_archive}"])

    def restore(self):
        result = subprocess.run([self.get_restore_tool(), self.connectionString, f"--db={self.dbname}", self.file_archive])
