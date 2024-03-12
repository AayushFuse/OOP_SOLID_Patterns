"""
[Factory Design Pattern] Build a logging system using the Factory Design Pattern.
Create a LoggerFactory class that generates different types of loggers (e.g., FileLogger, ConsoleLogger, DatabaseLogger).
Implement methods in each logger to write logs to their respective destinations.
Show how the Factory Design Pattern helps to decouple the logging system from the application and allows for flexible log handling.
"""

from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):
    def log(self, message):
        with open("filelog.txt", "a",encoding='utf-8') as f:
            f.write(message + "\n")


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)


class DatabaseLogger(Logger):
    def log(self, message):
        pass


class LoggerFactory:
    @staticmethod
    def get_logger(l_type):
        if l_type == "file":
            return FileLogger()
        if l_type == "console":
            return ConsoleLogger()
        if l_type == "database":
            return DatabaseLogger()
        
        raise ValueError("Enter valid logger type")


if __name__ == "__main__":
    LoggerFactory().get_logger("file").log("Hello!! This is Aayush")
