class DatabaseConnection:
    def __init__(self, host: str, port: int, username: str, password: str, dbname: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dbname = dbname
