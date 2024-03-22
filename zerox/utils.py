from abc import ABC, abstractmethod
from loguru import logger


class BaseTool(ABC):
    def __init__(self):
        # Initialize the logger in the constructor
        # Configure loguru logger if necessary, e.g., log file, log level
        logger.info("BaseTool initialized")

    @abstractmethod
    def connect(self):
        # Abstract method to connect the tool
        pass

    @abstractmethod
    def add(self, item):
        # Abstract method to add an item
        pass

    @abstractmethod
    def close_connection(self):
        # Abstract method to close the tool connection
        pass

    @abstractmethod
    def cache(self, data):
        # Abstract method for caching data
        pass

    # Example of a non-abstract method that subclasses can use or override
    def log_info(self, message):
        logger.info(message)

    def log_error(self, message):
        logger.error(message)
