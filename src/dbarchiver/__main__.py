import argparse
from sshtunnel import SSHTunnelForwarder
from enum import Enum
from dbarchiver.mongodb_client import MongodbClient
from dbarchiver.postgresql_client import PostgresqlClient
from dbarchiver.sqlite_client import SqliteClient


class DatabaseType(Enum):
    POSTGRESQL = "postgresql"
    MONGODB = "mongodb"
    SQLITE = "sqlite"


class DatabaseAction(Enum):
    DUMP = "dump"
    RESTORE = "restore"


class DatabaseConnection:
    def __init__(self, host: str, port: int, username: str, password: str, name: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.name = name


def create_ssh_tunnel(remote_host: str, remote_port: int) -> SSHTunnelForwarder:
    print("init ssh tunnel")
    username = input("username: ")
    password = input("password: ")

    return SSHTunnelForwarder(
        ("localhost", 5432),
        ssh_username=username,
        ssh_password=password,
        remote_bind_address=(remote_host, remote_port),
    )


def __exec_action_database(action: DatabaseAction, type: DatabaseType, connection: DatabaseConnection):
    try:
        database_client = None
        if type == DatabaseType.POSTGRESQL:
            database_client = PostgresqlClient()
        if type == DatabaseType.MONGODB:
            database_client = MongodbClient()
        if type == DatabaseType.SQLITE:
            database_client = SqliteClient()

        database_action = getattr(database_client, action.value)
        database_action()
    except Exception as ex:
        print(ex)


def connect_database(action: DatabaseAction, type: DatabaseType, connection: DatabaseConnection, ssh_tunnel: bool):
    if ssh_tunnel:
        server = create_ssh_tunnel(connection.host, connection.port)
        print("start ssh tunnel")
        server.start()
        print(server.local_bind_port)
        __exec_action_database(action, type, connection)
        print("stop ssh tunnel")
        server.stop()
    else:
        __exec_action_database(action, type, connection)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=[da.value for da in DatabaseAction], help="operation in database")
    parser.add_argument("type", choices=[dt.value for dt in DatabaseType], help="software name database")
    parser.add_argument("--host", default="localhost", help="host connection database")
    parser.add_argument("--port", default=5432, type=int, help="port connection database")
    parser.add_argument("--username", default="default", help="username connection database")
    parser.add_argument("--password", default="default", help="password connection database")
    parser.add_argument("--name", default="default", help="name database")
    parser.add_argument("--ssh", action="store_true", dest="ssh_tunnel", help="use tunnel ssh")
    args = parser.parse_args()

    args.action = DatabaseAction(args.action)
    args.type = DatabaseType(args.type)

    connect_database(**vars(args))


if __name__ == "__main__":
    main()
