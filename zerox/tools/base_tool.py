from abc import ABC, abstractmethod
from loguru import logger
from typing import Any


class AbstractBaseTool(ABC):
    def __init__(
        self,
        credentials: Any = None,
        headers: Any = None,
        verbose: bool = False,
        base_url: str = None,
        verison: str = None,
        name: str = None,
        description: str = None,
        *args,
        **kwargs,
    ):
        # Initialize the logger in the constructor
        # Configure loguru logger if necessary, e.g., log file, log level
        logger.info("Tool initialized")

    @abstractmethod
    def connect(self):
        logger.info("Connecting to the tool")
        # Abstract method to connect the tool
        pass

    @abstractmethod
    def add(self, item):
        # Abstract method to add an item
        pass

    @abstractmethod
    def close_connection(self):
        logger.info("Closing the tool connection")
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
