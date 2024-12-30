from abc import ABC, abstractmethod

#################### Factory Method ####################
#1. abstract product
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

#2. concrete products
class MySqlConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to MySQL database ... Established"
    
class PostgreSqlConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to PostgreSQL database ... Established"
    
class OracleConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to Oracle database ... Established"

#3. abstract creator (factory)
class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        pass

#4. concrete creators (factories)
class MySqlConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return MySqlConnection()
    
class PostgreSqlConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSqlConnection()
    
class OracleConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return OracleConnection()

#5. client code
def connect_to_database(factory: DatabaseConnectionFactory):
    connection = factory.create_connection()
    print(connection.connect())

if __name__ == "__main__":
    mysql_factory = MySqlConnectionFactory()
    connect_to_database(mysql_factory)
    
    postgresql_factory = PostgreSqlConnectionFactory()
    connect_to_database(postgresql_factory)
    
    oracle_factory = OracleConnectionFactory()
    connect_to_database(oracle_factory)