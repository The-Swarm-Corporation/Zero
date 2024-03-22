from abc import ABC, abstractmethod
from loguru import logger
from typing import Any


class AbstractBaseTool(ABC):
    """
    Abstract base class for tools.

    This class defines the common interface and behavior for tools.
    Subclasses should implement the abstract methods to provide specific functionality.

    Args:
        credentials (Any, optional): The credentials for the tool. Defaults to None.
        headers (Any, optional): The headers for the tool. Defaults to None.
        verbose (bool, optional): Whether to enable verbose mode. Defaults to False.
        base_url (str, optional): The base URL for the tool. Defaults to None.
        version (str, optional): The version of the tool. Defaults to None.
        name (str, optional): The name of the tool. Defaults to None.
        description (str, optional): The description of the tool. Defaults to None.

    Attributes:
        credentials (Any): The credentials for the tool.
        headers (Any): The headers for the tool.
        verbose (bool): Whether verbose mode is enabled.
        base_url (str): The base URL for the tool.
        version (str): The version of the tool.
        name (str): The name of the tool.
        description (str): The description of the tool.
    """

    def __init__(
        self,
        credentials: Any = None,
        headers: Any = None,
        verbose: bool = False,
        base_url: str = None,
        version: str = None,
        name: str = None,
        description: str = None,
        *args,
        **kwargs,
    ):
        # Initialize the logger in the constructor
        # Configure loguru logger if necessary, e.g., log file, log level
        self.credentials = credentials
        self.headers = headers
        self.verbose = verbose
        self.base_url = base_url
        self.version = version
        self.name = name
        self.description = description

        # Log the initialization
        logger.info("Tool initialized")

    @abstractmethod
    def connect(self):
        """
        Connect to the tool.

        This method should be implemented by subclasses to establish a connection to the tool.
        """
        logger.info("Connecting to the tool")
        pass

    def add(self, item):
        """
        Add an item to the tool.

        This method should be implemented by subclasses to add an item to the tool.
        """
        pass

    def close_connection(self):
        """
        Close the tool connection.

        This method should be implemented by subclasses to close the connection to the tool.
        """
        logger.info("Closing the tool connection")
        pass

    def cache(self, data):
        """
        Cache data.

        This method should be implemented by subclasses to cache data.
        """
        pass

    def log_info(self, message):
        """
        Log an informational message.

        This method can be used or overridden by subclasses to log an informational message.

        Args:
            message (str): The message to log.
        """
        logger.info(message)

    def log_error(self, message):
        """
        Log an error message.

        This method can be used or overridden by subclasses to log an error message.

        Args:
            message (str): The error message to log.
        """
        logger.error(message)
