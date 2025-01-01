from abc import ABC, abstractmethod

class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass
    
class MySQLConnection(Connection):
    def connect(self):
        print("Connected to MySQL database")

class PostgreSQLConnection(Connection):
    def connect(self):
        print("Connected to PostgreSQL database")
    
class Cursor(ABC):
    @abstractmethod
    def execute(self, query: str):
        pass
    
class MySQLCursor(Cursor):
    def execute(self, query: str):
        print(f"Executing MySQL query: {query}")

class PostgreSQLCursor(Cursor):
    def execute(self, query: str):
        print(f"Executing PostgreSQL query: {query}")
    
class AbstractDBFactory(ABC):
    @abstractmethod
    def create_connection(self) -> Connection:
        pass
    
    @abstractmethod
    def create_cursor(self) -> Cursor:
        pass
    
class MySQLFactory(AbstractDBFactory):
    def create_connection(self) -> Connection:
        return MySQLConnection()
    
    def create_cursor(self) -> Cursor:
        return MySQLCursor()
    
class PostgreSQLFactory(AbstractDBFactory):
    def create_connection(self) -> Connection:
        return PostgreSQLConnection()
    
    def create_cursor(self) -> Cursor:
        return PostgreSQLCursor()
    
def client():
    factories = dict(mysql=MySQLFactory, postgresql=PostgreSQLFactory)

    fact_list = ', '.join(factories)

    while True:
        db = input(f"Choose a database from {fact_list}: ")
        if db in factories:
            break
        print("Invalid database. Try again.")

    print("=" * 30)
    return factories.get(db)()

if __name__ == "__main__":
    db_factory = client()
    db_connection = db_factory.create_connection()
    cursor = db_factory.create_cursor()

    db_connection.connect()
    cursor.execute("SELECT * FROM users")