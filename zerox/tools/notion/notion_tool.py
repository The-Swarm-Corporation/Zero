import os
import requests
from dotenv import load_dotenv
from pydantic import BaseModel
from loguru import logger
from typing import List, Any

# Load environment variables
load_dotenv()


# Define API header model
class APIHeaderModel(BaseModel):
    Authorization: str = f"Bearer {os.environ.get('NOTION_API_KEY')}"
    NotionVersion: dict = {"Notion-Version": "2021-05-13"}
    ContentType: str = "application/json"


class NotionCredentials(BaseModel):
    api_key: str = os.environ.get("NOTION_API_KEY")
    database_id: str = os.environ.get("NOTION_DATABASE_ID")
    notion_url: str = os.environ.get("NOTION_URL")


class NotionEntry(BaseModel):
    parent: dict
    properties: dict


class NotionUpdate(BaseModel):
    properties: dict


class QueryFilter(BaseModel):
    # Example structure for a simple filter.
    # Adapt according to your query needs.
    property: str
    text: dict


class NotionQuery(BaseModel):
    filter: QueryFilter
    sorts: List[Any] = []


class NotionUpdate(BaseModel):
    properties: dict
    page_id: str


class NotionTool:
    """
    A class representing a tool for interacting with Notion API.

    Attributes:
        base_url (str): The base URL for the Notion API.
        credentials (NotionCredentials): The credentials for accessing the Notion database.
        headers (APIHeaderModel): The headers for making API requests.
    """

    def __init__(
        self,
        base_url: str = "https://api.notion.com/v1/",
        credentials: NotionCredentials = None,
        headers: APIHeaderModel = None,
        *args,
        **kwargs,
    ):
        self.base_url = base_url
        self.credentials = credentials
        self.headers = headers
        logger.info(
            f"Initializing NotionTool with base_url: {base_url}"
        )
        logger.info(f"Using credentials: {credentials}")
        logger.info(f"Using headers: {headers}")

    def connect(self):
        """
        Connects to the Notion API.

        Returns:
            bool: True if the connection is successful, False otherwise.
        """
        try:
            logger.info("Connecting to Notion...")
            url = f"{self.base_url}databases/{self.credentials.database_id}"
            response = requests.get(url, headers=self.headers.dict())
            logger.info(
                f"Connected to Notion: {response.status_code}"
            )
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Error connecting to Notion: {e}")
            return False

    def add(self, item: NotionEntry):
        """
        Adds an item to the Notion database.

        Args:
            item (NotionEntry): The item to be added.

        Returns:
            bool: True if the item is successfully added, False otherwise.
        """
        try:
            logger.info("Adding item to Notion...")
            url = f"{self.base_url}pages"
            response = requests.post(
                url,
                headers=self.headers.dict(),
                json=item.model_json_schema(),
            )
            logger.info(
                f"Item added to Notion: {response.status_code}"
            )
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Error adding item to Notion: {e}")
            return False

    def query(self, query: NotionQuery):
        """
        Queries the Notion database.

        Args:
            query (NotionQuery): The query to be executed.

        Returns:
            Union[dict, None]: The query result if successful, None otherwise.
        """
        try:
            logger.info("Querying Notion...")
            url = f"{self.base_url}databases/{self.credentials.database_id}/query"
            response = requests.post(
                url,
                headers=self.headers.dict(),
                json=query.dict(),
            )
            logger.info(f"Query result: {response.status_code}")
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            logger.error(f"Error querying Notion: {e}")
            return None

    def update(self, update: NotionUpdate):
        try:
            logger.info("Updating Notion...")
            url = f"{self.base_url}pages/{update.page_id}"
            response = requests.patch(
                url,
                headers=self.headers.dict(),
                json=update.dict(),
            )
            logger.info(f"Update result: {response.status_code}")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Error updating Notion: {e}")
            return False

    def close_connection(self):
        """
        Closes the connection to the Notion API.
        """
        logger.info("Closing connection to Notion...")
        # Perform any necessary cleanup or closing operations
        logger.info("Connection to Notion closed")

    def cache(self, data):
        """
        Caches data for future use.
        """
        logger.info("Caching data...")
        # Implement caching logic here
        logger.info("Data cached")
