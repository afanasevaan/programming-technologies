
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):
    def log(self, message):
        print("Logging to file:", message)


class ConsoleLogger(Logger):
    def log(self, message):
        print("Logging to console:", message)


class LoggerFactory(ABC):
    @abstractmethod
    def createLogger(self):
        pass

    def logMessage(self, message):
        logger = self.createLogger()
        logger.log(message)


class FileLoggerFactory(LoggerFactory):
    def createLogger(self):
        return FileLogger()


class ConsoleLoggerFactory(LoggerFactory):
    def createLogger(self):
        return ConsoleLogger()


file_factory = FileLoggerFactory()
file_factory.logMessage("Hello")

console_factory = ConsoleLoggerFactory()
console_factory.logMessage("Hello")
