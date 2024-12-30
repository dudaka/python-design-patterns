from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass
    
class ConsoleLogger(Logger):
    def log(self, message):
        print(f'Console Logger: {message}')

class FileLogger(Logger):
    def log(self, message):
        with open('log.txt', 'a') as file:
            file.write(f'File Logger: {message}\n')

class DatabaseLogger(Logger):
    def log(self, message):
        # Database logging implementation
        print(f'Database Logger: {message}')

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass
    
class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()
    
class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()
    
class DatabaseLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return DatabaseLogger()
    
def perform_logging(factory: LoggerFactory, message: str):
    logger = factory.create_logger()
    logger.log(message)


if __name__ == "__main__":
    console_factory = ConsoleLoggerFactory()
    perform_logging(console_factory, 'Log message to console')
    
    file_factory = FileLoggerFactory()
    perform_logging(file_factory, 'Log message to file')
    
    database_factory = DatabaseLoggerFactory()
    perform_logging(database_factory, 'Log message to database')