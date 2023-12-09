import argparse
from sshtunnel import SSHTunnelForwarder
from enum import Enum


class DatabaseType(Enum):
    POSTGRESQL = "postgresql"
    MONGODB = "mongodb"
    SQLITE = "sqlite"


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


def __get_database_client(type: DatabaseType, host: str, port: int, name: str):
    # TODO: call databse client
    pass


def connect_database(type: DatabaseType, host: str, port: int, name: str, ssh_tunnel: bool):
    if ssh_tunnel:
        server = create_ssh_tunnel(host, port)
        print("start ssh tunnel")
        server.start()
        print(server.local_bind_port)
        __get_database_client(type, host, port, name)
        print("stop ssh tunnel")
        server.stop()
    else:
        __get_database_client(type, host, port, name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("type", choices=[dt.value for dt in DatabaseType], help="type database")
    parser.add_argument("--host", default="localhost", help="host database")
    parser.add_argument("--port", default=5432, type=int, help="port database")
    parser.add_argument("--name", default="default", help="name database")
    parser.add_argument("--ssh", action="store_true", dest="ssh_tunnel", help="use tunnel ssh")
    args = parser.parse_args()
    args.type = DatabaseType(args.type)

    connect_database(**vars(args))


if __name__ == "__main__":
    main()
