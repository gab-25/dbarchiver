from dbarchiver.abstract_database_client import AbstractDatabseClient


class MongodbClient(AbstractDatabseClient):
    def __init__(self):
        super().__init__("mongodbdump", "mongorestore")

    def dump(self):
        pass

    def restore(self):
        pass
