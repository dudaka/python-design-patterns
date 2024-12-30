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

#3. creator (factory)
class DatabaseFactory:
    def __init__(self):
        self.factory = dict(mysql=MySqlConnection, postgresql=PostgreSqlConnection, oracle=OracleConnection)

    def create_connection(self, connection_type):
        if connection_type in self.factory:
            connection = self.factory.get(connection_type)
            return connection()

#5. client code
if __name__ == "__main__":
    factory = DatabaseFactory()
    
    mysql_connection = factory.create_connection('mysql')
    print(mysql_connection.connect())
    
    postgresql_connection = factory.create_connection('postgresql')
    print(postgresql_connection.connect())
    
    oracle_connection = factory.create_connection('oracle')
    print(oracle_connection.connect())